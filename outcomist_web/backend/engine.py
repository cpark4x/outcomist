import os
from typing import AsyncGenerator
from anthropic import Anthropic
from .models import Session, Message
from .prompts import (
    TIER_1_SYSTEM_PROMPT,
    TIER_2_ROUND_1_SYSTEM_PROMPT,
    TIER_2_ANALYSIS_SYSTEM_PROMPT,
    TIER_2_ROUND_2_SYSTEM_PROMPT,
    TIER_2_SUMMARY_SYSTEM_PROMPT,
    TIER_2_RECOMMENDATION_SYSTEM_PROMPT,
    get_tier_1_prompt,
    get_tier_2_round_1_prompt,
    get_tier_2_analysis_prompt,
    get_tier_2_round_2_prompt,
    get_tier_2_summary_prompt,
    get_tier_2_recommendation_prompt,
)
from .storage import SessionStorage


class ExplorationEngine:
    def __init__(self, storage: SessionStorage):
        self.storage = storage
        api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=api_key)

    async def generate_tier_1(self, session: Session) -> AsyncGenerator[str, None]:
        user_message = Message(role="user", content=session.decision_statement)
        session.conversation.append(user_message)

        prompt = get_tier_1_prompt(session.decision_statement)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            temperature=1.0,
            system=TIER_1_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)

    async def start_tier_2(self, session: Session) -> AsyncGenerator[str, None]:
        session.current_tier = 2
        session.state.current_round = 1

        prompt = get_tier_2_round_1_prompt(session)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            temperature=1.0,
            system=TIER_2_ROUND_1_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        session.state.questions_asked.append(full_response)

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)

    async def handle_answer(self, session: Session, answer: str) -> AsyncGenerator[str, None]:
        user_message = Message(role="user", content=answer)
        session.conversation.append(user_message)
        session.state.user_answers.append(answer)

        current_round = session.state.current_round
        questions_count = len(session.state.questions_asked)

        if current_round == 1 and questions_count == 1:
            async for chunk in self._generate_analysis(session):
                yield chunk

            async for chunk in self._ask_round_2_question(session):
                yield chunk

        elif current_round == 2 and questions_count >= 2:
            async for chunk in self._generate_summary(session):
                yield chunk
        else:
            self.storage.save(session)

    async def _generate_analysis(self, session: Session) -> AsyncGenerator[str, None]:
        prompt = get_tier_2_analysis_prompt(session)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=256,
            temperature=1.0,
            system=TIER_2_ANALYSIS_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)

    async def _ask_round_2_question(self, session: Session) -> AsyncGenerator[str, None]:
        session.state.current_round = 2

        prompt = get_tier_2_round_2_prompt(session)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            temperature=1.0,
            system=TIER_2_ROUND_2_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        session.state.questions_asked.append(full_response)

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)

    async def _generate_summary(self, session: Session) -> AsyncGenerator[str, None]:
        prompt = get_tier_2_summary_prompt(session)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            temperature=1.0,
            system=TIER_2_SUMMARY_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        session.state.summary_text = full_response
        session.state.awaiting_summary_confirmation = True

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)

    async def confirm_summary_and_recommend(
        self, session: Session, confirmation: str
    ) -> AsyncGenerator[str, None]:
        user_message = Message(role="user", content=confirmation)
        session.conversation.append(user_message)

        session.state.awaiting_summary_confirmation = False

        prompt = get_tier_2_recommendation_prompt(session)

        full_response = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            temperature=1.0,
            system=TIER_2_RECOMMENDATION_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        session.state.recommendation_delivered = True

        assistant_message = Message(role="assistant", content=full_response)
        session.conversation.append(assistant_message)

        self.storage.save(session)
