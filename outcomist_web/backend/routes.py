import uuid
import os
from fastapi import APIRouter, HTTPException
from sse_starlette.sse import EventSourceResponse
from .models import (
    StartSessionRequest,
    Session,
    IntentRequest,
)
from .storage import SessionStorage
from .engine import ExplorationEngine

router = APIRouter()
storage = SessionStorage()
_engine = None


def get_engine():
    global _engine
    if _engine is None:
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise HTTPException(
                status_code=503,
                detail="API key not configured. Please set ANTHROPIC_API_KEY environment variable."
            )
        _engine = ExplorationEngine(storage)
    return _engine


@router.post("/sessions/start")
async def start_session(request: StartSessionRequest):
    session_id = str(uuid.uuid4())
    session = Session(session_id=session_id, decision_statement=request.decision)

    storage.save(session)

    return {"session_id": session_id}


@router.get("/sessions/{session_id}/stream")
async def stream_response(session_id: str):
    session = storage.load(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    async def event_generator():
        try:
            engine = get_engine()
            async for chunk in engine.generate_tier_1(session):
                yield {"event": "message", "data": chunk}

            yield {"event": "done", "data": ""}
        except HTTPException:
            raise
        except Exception as e:
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())


@router.get("/sessions/{session_id}")
async def get_session(session_id: str):
    session = storage.load(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return session.model_dump(mode="json")


@router.post("/sessions/{session_id}/intent")
async def set_intent(session_id: str, request: IntentRequest):
    session = storage.load(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session.state.intent = request.intent
    storage.save(session)

    return {"status": "ok", "intent": request.intent}


@router.get("/sessions/{session_id}/proceed")
async def proceed_to_tier_2(session_id: str):
    session = storage.load(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    async def event_generator():
        try:
            engine = get_engine()
            async for chunk in engine.start_tier_2(session):
                yield {"event": "message", "data": chunk}

            yield {"event": "done", "data": ""}
        except HTTPException:
            raise
        except Exception as e:
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())


@router.get("/sessions/{session_id}/respond")
async def respond_to_question(session_id: str, message: str):
    if not message or not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    session = storage.load(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    async def event_generator():
        try:
            engine = get_engine()
            if session.state.awaiting_summary_confirmation:
                async for chunk in engine.confirm_summary_and_recommend(session, message):
                    yield {"event": "message", "data": chunk}
            else:
                async for chunk in engine.handle_answer(session, message):
                    yield {"event": "message", "data": chunk}

            yield {"event": "done", "data": ""}
        except HTTPException:
            raise
        except Exception as e:
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())
