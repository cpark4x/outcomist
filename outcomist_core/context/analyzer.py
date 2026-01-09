"""Context analysis and question type detection for Outcomist.

This module implements analysis of user's decision text to extract:
- Question type (information, execution, decision)
- User state (confident, exploring, stuck)
- Context clarity
- Mentioned constraints, stakeholders, alternatives
"""

from typing import List, Optional
import re

from .types import (
    DecisionContext,
    QuestionType,
    UserState,
    ContextClarity,
    Constraint,
)


class QuestionTypeDetector:
    """Detects what type of question the user is asking."""
    
    # Patterns for question type detection (from v4.7 of explore.md)
    INFORMATION_PATTERNS = [
        r"\bwhy\b.*\?",
        r"\bwhat causes\b",
        r"\bcan you explain\b",
        r"\bis .* similar to\b",
        r"\bwhat'?s the difference between\b",
        r"\bhow does .* work\b",
    ]
    
    EXECUTION_PATTERNS = [
        r"\bwhat .* should I (make|create|build)\b",
        r"\bhow do I (implement|build|create)\b",
        r"\bwhat are some ideas for\b",
        r"\bcan you help me (create|make|build)\b",
        r"\bgive me suggestions for\b",
        r"\bhelp me (create|make|build)\b",
    ]
    
    DECISION_PATTERNS = [
        r"\bshould I\b",
        r"\bwhich option\b",
        r"\bhelp me decide\b",
        r"\bis it worth\b",
        r"\bwhat should I prioritize\b",
        r"\bshould we\b",
        r"\b(take|accept|choose|pick)\b.*\bor\b",
    ]
    
    @classmethod
    def detect(cls, text: str) -> QuestionType:
        """Detect question type from text.
        
        Args:
            text: User's question or statement
        
        Returns:
            QuestionType (INFORMATION, EXECUTION, or DECISION)
        """
        text_lower = text.lower()
        
        # Check information patterns
        for pattern in cls.INFORMATION_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return QuestionType.INFORMATION
        
        # Check execution patterns
        for pattern in cls.EXECUTION_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return QuestionType.EXECUTION
        
        # Check decision patterns
        for pattern in cls.DECISION_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return QuestionType.DECISION
        
        # Default to decision if ambiguous
        return QuestionType.DECISION


class ContextAnalyzer:
    """Analyzes decision text to extract structured context."""
    
    # Confidence signals
    CONFIDENT_SIGNALS = [
        "I've already decided",
        "just need a sanity check",
        "pretty sure",
        "I will",
        "I'm going to",
    ]
    
    HESITATION_SIGNALS = [
        "something feels off",
        "am I missing something",
        "not 100% sure",
        "leaning toward",
        "but...",
    ]
    
    STUCK_SIGNALS = [
        "stuck",
        "confused",
        "can't decide",
        "going in circles",
        "don't know",
    ]
    
    def __init__(self):
        """Initialize the context analyzer."""
        self.question_detector = QuestionTypeDetector()
    
    def analyze(self, decision_text: str) -> DecisionContext:
        """Analyze decision text and extract structured context.
        
        Args:
            decision_text: User's decision statement
        
        Returns:
            DecisionContext with extracted information
        """
        question_type = self.question_detector.detect(decision_text)
        user_state = self._detect_user_state(decision_text)
        clarity = self._assess_clarity(decision_text)
        
        context = DecisionContext(
            decision_text=decision_text,
            question_type=question_type,
            user_state=user_state,
            clarity=clarity,
        )
        
        # Extract additional signals
        context.emotional_language = self._extract_emotional_language(decision_text)
        context.temporal_signals = self._extract_temporal_signals(decision_text)
        context.financial_signals = self._extract_financial_signals(decision_text)
        context.constraints = self._extract_constraints(decision_text)
        context.mentioned_stakeholders = self._extract_stakeholders(decision_text)
        context.mentioned_alternatives = self._extract_alternatives(decision_text)
        
        return context
    
    def _detect_user_state(self, text: str) -> UserState:
        """Detect user's state of mind."""
        text_lower = text.lower()
        
        # Check for confident signals
        confident_count = sum(
            1 for signal in self.CONFIDENT_SIGNALS
            if signal.lower() in text_lower
        )
        
        # Check for hesitation signals
        hesitation_count = sum(
            1 for signal in self.HESITATION_SIGNALS
            if signal.lower() in text_lower
        )
        
        # Check for stuck signals
        stuck_count = sum(
            1 for signal in self.STUCK_SIGNALS
            if signal.lower() in text_lower
        )
        
        if stuck_count > 0:
            return UserState.STUCK
        elif confident_count > hesitation_count:
            return UserState.CONFIDENT
        else:
            return UserState.EXPLORING
    
    def _assess_clarity(self, text: str) -> ContextClarity:
        """Assess how clear the question is."""
        # Simple heuristics for now
        
        # Check if question is very short
        if len(text.split()) < 5:
            return ContextClarity.AMBIGUOUS
        
        # Check for confusion markers
        confusion_markers = ["not sure", "don't know", "confused", "unclear"]
        if any(marker in text.lower() for marker in confusion_markers):
            return ContextClarity.CONFUSED
        
        # Check if it has structure (sentences, punctuation)
        has_question = "?" in text
        has_context = len(text.split()) > 15
        
        if has_question or has_context:
            return ContextClarity.CLEAR
        
        return ContextClarity.AMBIGUOUS
    
    def _extract_emotional_language(self, text: str) -> List[str]:
        """Extract emotional words from text."""
        emotional_words = [
            "inspiring", "proud", "excited", "frustrated", "anxious",
            "worried", "scared", "hopeful", "confident", "uncertain",
            "overwhelmed", "passionate", "love", "hate", "fear",
        ]
        
        found = []
        text_lower = text.lower()
        for word in emotional_words:
            if word in text_lower:
                found.append(word)
        
        return found
    
    def _extract_temporal_signals(self, text: str) -> List[str]:
        """Extract time-related signals."""
        temporal_patterns = [
            r"\bright now\b",
            r"\bimmediately\b",
            r"\btoday\b",
            r"\bthis week\b",
            r"\burgent\b",
            r"\bdeadline\b",
            r"\brecently\b",
            r"\bjust\b",
        ]
        
        found = []
        text_lower = text.lower()
        for pattern in temporal_patterns:
            matches = re.findall(pattern, text_lower)
            found.extend(matches)
        
        return found
    
    def _extract_financial_signals(self, text: str) -> List[str]:
        """Extract money-related mentions."""
        # Look for dollar amounts, revenue, costs
        financial_patterns = [
            r"\$[\d,]+",
            r"\d+K",
            r"\bMRR\b",
            r"\bARR\b",
            r"\brevenue\b",
            r"\bcost\b",
            r"\bbudget\b",
            r"\brunway\b",
            r"\bsavings\b",
        ]
        
        found = []
        for pattern in financial_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            found.extend(matches)
        
        return found
    
    def _extract_constraints(self, text: str) -> List[Constraint]:
        """Extract mentioned constraints."""
        constraints = []
        text_lower = text.lower()
        
        # Time constraints
        if any(word in text_lower for word in ["time", "hours", "weeks", "months"]):
            constraints.append(Constraint(
                type="time",
                description="Time constraint mentioned",
                severity="medium"
            ))
        
        # Budget constraints
        if any(word in text_lower for word in ["budget", "cost", "afford", "expensive"]):
            constraints.append(Constraint(
                type="budget",
                description="Budget constraint mentioned",
                severity="medium"
            ))
        
        # Technical constraints
        if any(word in text_lower for word in ["technical", "code", "programming", "no-code"]):
            constraints.append(Constraint(
                type="technical",
                description="Technical constraint mentioned",
                severity="medium"
            ))
        
        # Skill constraints
        if any(word in text_lower for word in ["don't know how", "not sure how", "learning"]):
            constraints.append(Constraint(
                type="skill",
                description="Skill constraint mentioned",
                severity="medium"
            ))
        
        return constraints
    
    def _extract_stakeholders(self, text: str) -> List[str]:
        """Extract mentioned stakeholders."""
        stakeholder_patterns = [
            r"\b(team|boss|manager|leadership|executive|SLT)\b",
            r"\b(customer|client|user)s?\b",
            r"\b(employee|worker|staff)s?\b",
            r"\b(investor|shareholder|board)s?\b",
            r"\b(partner|vendor|supplier)s?\b",
            r"\b(family|spouse|wife|husband|kids)\b",
        ]
        
        found = []
        text_lower = text.lower()
        for pattern in stakeholder_patterns:
            matches = re.findall(pattern, text_lower)
            found.extend(matches)
        
        return list(set(found))  # Remove duplicates
    
    def _extract_alternatives(self, text: str) -> List[str]:
        """Extract mentioned alternatives (A vs B situations)."""
        alternatives = []
        
        # Look for "X or Y" patterns
        or_pattern = r"([^,\.]+?)\s+or\s+([^,\.]+)"
        matches = re.findall(or_pattern, text, re.IGNORECASE)
        
        for match in matches:
            alternatives.append(match[0].strip())
            alternatives.append(match[1].strip())
        
        # Look for "X vs Y" patterns
        vs_pattern = r"([^,\.]+?)\s+vs\.?\s+([^,\.]+)"
        matches = re.findall(vs_pattern, text, re.IGNORECASE)
        
        for match in matches:
            alternatives.append(match[0].strip())
            alternatives.append(match[1].strip())
        
        return alternatives
