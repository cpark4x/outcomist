from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)


class SessionState(BaseModel):
    intent: Literal["validation", "execution", "unknown"] = "unknown"
    confidence: Literal["high", "medium", "low"] = "low"
    patterns_identified: list[str] = Field(default_factory=list)
    questions_asked: list[str] = Field(default_factory=list)
    current_round: int = 0
    awaiting_summary_confirmation: bool = False
    recommendation_delivered: bool = False
    summary_text: str = ""
    user_answers: list[str] = Field(default_factory=list)


class Session(BaseModel):
    session_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    decision_statement: str
    current_tier: int = 1
    conversation: list[Message] = Field(default_factory=list)
    state: SessionState = Field(default_factory=SessionState)


class StartSessionRequest(BaseModel):
    decision: str = Field(min_length=1)


class RespondRequest(BaseModel):
    message: str = Field(min_length=1)


class IntentRequest(BaseModel):
    intent: Literal["validation", "execution"]


class ConfidenceRequest(BaseModel):
    confidence: Literal["high", "medium", "low"]


class ProceedRequest(BaseModel):
    proceed: bool = True
