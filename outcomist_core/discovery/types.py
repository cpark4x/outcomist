"""Type definitions for discovery flow module."""

from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

from ..state.types import Tier
from ..pattern.types import PatternMatch


class FlowStep(Enum):
    """Steps in the discovery flow."""
    INIT = "init"
    PATTERN_RECOGNITION = "pattern_recognition"
    TIER_1_COMPLETE = "tier_1_complete"
    TIER_2_ROUND_1 = "tier_2_round_1"
    TIER_2_ANALYSIS = "tier_2_analysis"
    TIER_2_ROUND_2 = "tier_2_round_2"
    TIER_2_SUMMARY = "tier_2_summary"
    TIER_2_RECOMMENDATION = "tier_2_recommendation"
    TIER_2_COMPLETE = "tier_2_complete"
    COMPLETE = "complete"


@dataclass
class FlowResponse:
    """Response from a discovery flow step."""
    
    content: str
    step: FlowStep
    tier: Tier
    
    # Pattern information (if detected)
    patterns: Optional[List[PatternMatch]] = None
    
    # State information
    needs_user_response: bool = True
    is_complete: bool = False
    
    # Next step information
    next_step: Optional[FlowStep] = None
    suggested_questions: Optional[List[str]] = None
    
    def __str__(self) -> str:
        """Return the content for display."""
        return self.content
