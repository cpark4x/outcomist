"""Type definitions for context analysis module."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class QuestionType(Enum):
    """Types of questions users ask."""
    INFORMATION = "information"  # "Why is X happening?", "What causes Y?"
    EXECUTION = "execution"      # "What meals should I make?", "How do I implement?"
    DECISION = "decision"        # "Should I?", "Which option?", "Help me decide?"


class UserState(Enum):
    """User's state of mind when asking."""
    CONFIDENT = "confident"      # Clear, decisive language
    EXPLORING = "exploring"      # Open-ended, seeking options
    STUCK = "stuck"             # Confused, cycling through options


class ContextClarity(Enum):
    """How clear the question is."""
    CLEAR = "clear"             # Well-formed question with context
    CONFUSED = "confused"       # Unclear what they're asking
    AMBIGUOUS = "ambiguous"     # Multiple interpretations possible


@dataclass
class Constraint:
    """A constraint mentioned by the user."""
    type: str  # e.g., "time", "budget", "technical", "skill"
    description: str
    severity: str = "medium"  # "low", "medium", "high", "critical"


@dataclass
class DecisionContext:
    """Structured context extracted from user's decision statement."""
    
    decision_text: str
    question_type: QuestionType
    user_state: UserState
    clarity: ContextClarity
    
    # Extracted information
    constraints: List[Constraint] = field(default_factory=list)
    mentioned_stakeholders: List[str] = field(default_factory=list)
    mentioned_alternatives: List[str] = field(default_factory=list)
    
    # Signals detected
    emotional_language: List[str] = field(default_factory=list)
    temporal_signals: List[str] = field(default_factory=list)  # "RIGHT NOW", "urgent"
    financial_signals: List[str] = field(default_factory=list)  # "$6K/month", "stable money"
    
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_text(cls, text: str) -> "DecisionContext":
        """Parse decision text into structured context.
        
        This is a placeholder - actual implementation would use LLM
        or pattern matching to extract context.
        """
        # TODO: Implement context extraction
        return cls(
            decision_text=text,
            question_type=QuestionType.DECISION,  # Default assumption
            user_state=UserState.EXPLORING,
            clarity=ContextClarity.CLEAR,
        )
    
    def has_constraint_type(self, constraint_type: str) -> bool:
        """Check if a specific constraint type is mentioned."""
        return any(c.type == constraint_type for c in self.constraints)
    
    def get_constraints_by_type(self, constraint_type: str) -> List[Constraint]:
        """Get all constraints of a specific type."""
        return [c for c in self.constraints if c.type == constraint_type]
