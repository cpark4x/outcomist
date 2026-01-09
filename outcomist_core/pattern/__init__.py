"""Pattern recognition module for Outcomist.

This module provides pattern matching capabilities for decision exploration.
"""

from .types import (
    Pattern,
    PatternType,
    PatternMatch,
    Signal,
    Question,
    Pitfall,
)

from .library import (
    get_all_patterns,
    get_pattern_by_id,
    PERSONAL_SANCTUARY,
    EMPLOYABILITY_ANXIETY,
    HEALTH_ANXIETY,
    ADDITIONAL_REVENUE_MISFRAME,
    POPULARITY_CONTEST,
    SCARCITY_MINDSET,
    SOLUTION_LOOKING_FOR_PROBLEM,
    PREMATURE_PRESENTATION,
    STUCK_IN_BUILD_PHASE,
)

from .matcher import PatternMatcher

__all__ = [
    # Types
    "Pattern",
    "PatternType",
    "PatternMatch",
    "Signal",
    "Question",
    "Pitfall",
    # Functions
    "get_all_patterns",
    "get_pattern_by_id",
    # Pattern constants
    "PERSONAL_SANCTUARY",
    "EMPLOYABILITY_ANXIETY",
    "HEALTH_ANXIETY",
    "ADDITIONAL_REVENUE_MISFRAME",
    "POPULARITY_CONTEST",
    "SCARCITY_MINDSET",
    "SOLUTION_LOOKING_FOR_PROBLEM",
    "PREMATURE_PRESENTATION",
    "STUCK_IN_BUILD_PHASE",
    # Matcher
    "PatternMatcher",
]
