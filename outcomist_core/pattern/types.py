"""Type definitions for pattern recognition module."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class PatternType(Enum):
    """Types of decision patterns."""
    PERSONAL_SANCTUARY = "personal_sanctuary"
    EMPLOYABILITY_ANXIETY = "employability_anxiety"
    HEALTH_ANXIETY = "health_anxiety"
    ADDITIONAL_REVENUE_MISFRAME = "additional_revenue_misframe"
    POPULARITY_CONTEST = "popularity_contest"
    SCARCITY_MINDSET = "scarcity_mindset"
    SOLUTION_LOOKING_FOR_PROBLEM = "solution_looking_for_problem"
    PREMATURE_PRESENTATION = "premature_presentation"
    STUCK_IN_BUILD_PHASE = "stuck_in_build_phase"


@dataclass
class Signal:
    """A signal that indicates a pattern might be present."""
    description: str
    weight: float = 1.0  # 0.0 to 1.0


@dataclass
class Question:
    """A question to ask to validate or explore a pattern."""
    text: str
    purpose: str  # Why we're asking this question
    priority: int = 1  # 1 = high priority, 2 = medium, 3 = low


@dataclass
class Pitfall:
    """A common mistake when addressing this pattern."""
    description: str
    consequence: str


@dataclass
class Pattern:
    """A decision pattern with signals, questions, and pitfalls."""
    
    id: PatternType
    name: str
    surface_request: str
    real_problem: str
    
    signals: List[Signal]
    questions: List[Question]
    pitfalls: List[Pitfall]
    
    example_scenario: Optional[str] = None
    test_link: Optional[str] = None
    
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PatternMatch:
    """A pattern that matched the user's decision."""
    
    pattern: Pattern
    confidence: float  # 0.0 to 1.0
    matched_signals: List[Signal]
    reasoning: Optional[str] = None
    
    @property
    def pattern_id(self) -> PatternType:
        return self.pattern.id
    
    @property
    def pattern_name(self) -> str:
        return self.pattern.name
