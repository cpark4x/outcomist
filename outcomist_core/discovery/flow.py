"""Discovery flow orchestrator for Outcomist.

This module orchestrates the progressive disclosure flow through tiers,
managing pattern detection, questioning, and recommendations.
"""

from typing import Optional
import uuid

from .types import FlowResponse, FlowStep
from ..state.types import Session, SessionState, Tier, Intent
from ..pattern.matcher import PatternMatcher
from ..context.analyzer import ContextAnalyzer
from ..llm.provider import BaseLLMProvider
from ..prompts import get_tier_1_prompt, TIER_1_SYSTEM_PROMPT


class DiscoveryFlow:
    """Orchestrates the discovery flow through progressive tiers.
    
    This is the main entry point for running a complete discovery session.
    It manages state, pattern detection, and LLM interactions.
    """
    
    def __init__(
        self,
        llm_provider: BaseLLMProvider,
        pattern_matcher: Optional[PatternMatcher] = None,
        context_analyzer: Optional[ContextAnalyzer] = None,
    ):
        """Initialize discovery flow.
        
        Args:
            llm_provider: LLM provider for generating responses
            pattern_matcher: Optional PatternMatcher (creates if None)
            context_analyzer: Optional ContextAnalyzer (creates if None)
        """
        self.llm = llm_provider
        self.pattern_matcher = pattern_matcher or PatternMatcher()
        self.context_analyzer = context_analyzer or ContextAnalyzer()
    
    def start_session(
        self,
        decision_statement: str,
        user_id: Optional[str] = None
    ) -> tuple[Session, FlowResponse]:
        """Start a new discovery session.
        
        Args:
            decision_statement: User's decision statement
            user_id: Optional user identifier
        
        Returns:
            Tuple of (Session, FlowResponse with Tier 1 pattern recognition)
        """
        # Create new session
        session = Session(
            session_id=str(uuid.uuid4()),
            decision_statement=decision_statement,
            user_id=user_id,
        )
        
        # Add user message
        session.add_message("user", decision_statement)
        
        # Analyze context
        context = self.context_analyzer.analyze(decision_statement)
        session.state.metadata['question_type'] = context.question_type.value
        session.state.metadata['user_state'] = context.user_state.value
        
        # Detect patterns
        pattern_matches = self.pattern_matcher.match(decision_statement, context)
        if pattern_matches:
            session.state.pattern_matches = [
                match.pattern_id.value for match in pattern_matches[:3]
            ]
        
        # Run Tier 1 pattern recognition
        response = self._run_tier_1(session, context)
        
        return session, response
    
    def _run_tier_1(self, session: Session, context) -> FlowResponse:
        """Run Tier 1 pattern recognition.
        
        Args:
            session: Current session
            context: DecisionContext from analysis
        
        Returns:
            FlowResponse with pattern recognition insight
        """
        from ..llm.types import LLMRequest, LLMMessage
        
        # Build Tier 1 prompt
        user_prompt = get_tier_1_prompt(session.decision_statement)
        
        # Call LLM
        request = LLMRequest(
            system=TIER_1_SYSTEM_PROMPT,
            messages=[LLMMessage(role="user", content=user_prompt)],
            temperature=0.7,
            max_tokens=500,
        )
        
        llm_response = self.llm.complete(request)
        
        # Store Tier 1 insight
        session.state.tier_1_insight = llm_response.content
        session.add_message("assistant", llm_response.content)
        
        # Get pattern matches
        pattern_matches = self.pattern_matcher.match(
            session.decision_statement, 
            context
        )
        
        return FlowResponse(
            content=llm_response.content,
            step=FlowStep.TIER_1_COMPLETE,
            tier=Tier.TIER_1,
            patterns=pattern_matches[:3] if pattern_matches else None,
            needs_user_response=True,
            next_step=FlowStep.TIER_2_ROUND_1,
            suggested_questions=self._get_suggested_questions(pattern_matches) if pattern_matches else None,
        )
    
    def continue_session(
        self,
        session: Session,
        user_response: str
    ) -> FlowResponse:
        """Continue an existing session with user's response.
        
        Args:
            session: Current session
            user_response: User's response to previous question
        
        Returns:
            FlowResponse with next step in flow
        """
        # Add user message
        session.add_message("user", user_response)
        
        # Determine current state and next action
        if session.state.tier == Tier.TIER_1:
            # User responded to Tier 1, move to Tier 2
            return self._start_tier_2(session)
        
        elif session.state.tier == Tier.TIER_2:
            if session.state.round == 1:
                # User answered Round 1, do analysis and ask Round 2
                return self._tier_2_round_1_complete(session, user_response)
            elif session.state.round == 2:
                # User answered Round 2, create summary
                return self._tier_2_round_2_complete(session, user_response)
            elif session.state.summary_confirmed:
                # User confirmed summary, shouldn't reach here
                # (recommendation happens immediately after confirmation)
                return self._tier_2_deliver_recommendation(session)
        
        # Default: continue current tier
        return FlowResponse(
            content="I'm not sure what to do next. Can you clarify?",
            step=FlowStep.INIT,
            tier=session.state.tier,
            needs_user_response=True,
        )
    
    def _start_tier_2(self, session: Session) -> FlowResponse:
        """Start Tier 2 discovery (Round 1).
        
        Args:
            session: Current session
        
        Returns:
            FlowResponse with Round 1 question
        """
        from ..llm.types import LLMRequest, LLMMessage
        from ..prompts import TIER_2_ROUND_1_SYSTEM_PROMPT
        
        # Update session state
        session.state.advance_to_tier(Tier.TIER_2)
        session.state.round = 1
        
        # Build Round 1 prompt
        context_str = f"Decision: {session.decision_statement}\n"
        if session.state.tier_1_insight:
            context_str += f"Pattern insight: {session.state.tier_1_insight}\n"
        
        # Call LLM for Round 1 question
        request = LLMRequest(
            system=TIER_2_ROUND_1_SYSTEM_PROMPT,
            messages=[LLMMessage(role="user", content=context_str)],
            temperature=0.7,
            max_tokens=300,
        )
        
        llm_response = self.llm.complete(request)
        question = llm_response.content.strip()
        
        # Store question
        session.state.add_question(question)
        session.add_message("assistant", question)
        
        return FlowResponse(
            content=question,
            step=FlowStep.TIER_2_ROUND_1,
            tier=Tier.TIER_2,
            needs_user_response=True,
            next_step=FlowStep.TIER_2_ANALYSIS,
        )
    
    def _tier_2_round_1_complete(
        self,
        session: Session,
        user_answer: str
    ) -> FlowResponse:
        """Process Round 1 answer and ask Round 2 question.
        
        Args:
            session: Current session
            user_answer: User's answer to Round 1
        
        Returns:
            FlowResponse with Round 2 question
        """
        from ..llm.types import LLMRequest, LLMMessage
        from ..prompts import TIER_2_ROUND_2_SYSTEM_PROMPT
        
        # Store answer
        session.state.add_answer(user_answer)
        
        # Update round
        session.state.advance_round()
        
        # Build Round 2 prompt with context
        context_str = f"""Decision: {session.decision_statement}

Round 1:
Q: {session.state.questions_asked[0]}
A: {user_answer}

Ask ONE targeted question based on what you learned."""
        
        # Call LLM for Round 2 question
        request = LLMRequest(
            system=TIER_2_ROUND_2_SYSTEM_PROMPT,
            messages=[LLMMessage(role="user", content=context_str)],
            temperature=0.7,
            max_tokens=300,
        )
        
        llm_response = self.llm.complete(request)
        question = llm_response.content.strip()
        
        # Store question
        session.state.add_question(question)
        session.add_message("assistant", question)
        
        return FlowResponse(
            content=question,
            step=FlowStep.TIER_2_ROUND_2,
            tier=Tier.TIER_2,
            needs_user_response=True,
            next_step=FlowStep.TIER_2_SUMMARY,
        )
    
    def _tier_2_round_2_complete(
        self,
        session: Session,
        user_answer: str
    ) -> FlowResponse:
        """Process Round 2 answer and create summary.
        
        Args:
            session: Current session
            user_answer: User's answer to Round 2
        
        Returns:
            FlowResponse with summary for confirmation
        """
        from ..llm.types import LLMRequest, LLMMessage
        from ..prompts import TIER_2_SUMMARY_SYSTEM_PROMPT
        
        # Store answer
        session.state.add_answer(user_answer)
        
        # Build summary prompt
        context_str = f"""Decision: {session.decision_statement}

Q1: {session.state.questions_asked[0]}
A1: {session.state.user_answers[0]}

Q2: {session.state.questions_asked[1]}
A2: {user_answer}

Summarize what you've heard (3-4 key facts, NO JUDGMENT)."""
        
        # Call LLM for summary
        request = LLMRequest(
            system=TIER_2_SUMMARY_SYSTEM_PROMPT,
            messages=[LLMMessage(role="user", content=context_str)],
            temperature=0.7,
            max_tokens=400,
        )
        
        llm_response = self.llm.complete(request)
        summary = llm_response.content.strip()
        
        # Store summary
        session.state.summary_text = summary
        session.add_message("assistant", summary)
        
        return FlowResponse(
            content=summary,
            step=FlowStep.TIER_2_SUMMARY,
            tier=Tier.TIER_2,
            needs_user_response=True,
            next_step=FlowStep.TIER_2_RECOMMENDATION,
        )
    
    def confirm_summary(
        self,
        session: Session,
        confirmed: bool = True
    ) -> FlowResponse:
        """Confirm summary and deliver recommendation.
        
        Args:
            session: Current session
            confirmed: Whether user confirmed summary
        
        Returns:
            FlowResponse with recommendation
        """
        if not confirmed:
            return FlowResponse(
                content="What did I miss or get wrong? Please clarify.",
                step=FlowStep.TIER_2_SUMMARY,
                tier=Tier.TIER_2,
                needs_user_response=True,
            )
        
        session.state.summary_confirmed = True
        return self._tier_2_deliver_recommendation(session)
    
    def _tier_2_deliver_recommendation(self, session: Session) -> FlowResponse:
        """Deliver Tier 2 recommendation.
        
        Args:
            session: Current session
        
        Returns:
            FlowResponse with recommendation
        """
        from ..llm.types import LLMRequest, LLMMessage
        from ..prompts import TIER_2_RECOMMENDATION_SYSTEM_PROMPT
        
        # Build recommendation prompt
        context_str = f"""Decision: {session.decision_statement}

Summary confirmed: {session.state.summary_text}

Full Q&A:
Q1: {session.state.questions_asked[0]}
A1: {session.state.user_answers[0]}

Q2: {session.state.questions_asked[1]}
A2: {session.state.user_answers[1]}

Provide clear recommendation focused on their situation."""
        
        # Call LLM for recommendation
        request = LLMRequest(
            system=TIER_2_RECOMMENDATION_SYSTEM_PROMPT,
            messages=[LLMMessage(role="user", content=context_str)],
            temperature=0.7,
            max_tokens=800,
        )
        
        llm_response = self.llm.complete(request)
        recommendation = llm_response.content.strip()
        
        # Store recommendation
        session.state.recommendation = recommendation
        session.add_message("assistant", recommendation)
        
        return FlowResponse(
            content=recommendation,
            step=FlowStep.TIER_2_RECOMMENDATION,
            tier=Tier.TIER_2,
            needs_user_response=False,
            is_complete=True,
            next_step=FlowStep.TIER_2_COMPLETE,
        )
    
    def _get_suggested_questions(self, pattern_matches) -> list[str]:
        """Get suggested questions based on detected patterns.
        
        Args:
            pattern_matches: List of PatternMatch objects
        
        Returns:
            List of suggested question strings
        """
        if not pattern_matches:
            return []
        
        # Get questions from top pattern
        top_pattern = pattern_matches[0]
        questions = self.pattern_matcher.get_questions_for_pattern(
            top_pattern.pattern_id
        )
        
        return questions[:3]  # Return top 3 questions
