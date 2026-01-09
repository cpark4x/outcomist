"""Outcomist Core - Modular decision exploration library.

This is the core library for the Outcomist decision exploration tool.
It provides composable modules for pattern recognition, context analysis,
discovery flows, and state management.

Version: 1.0.0-alpha (Phase 1: Pattern Extraction)
"""

from .pattern import (
    Pattern,
    PatternType,
    PatternMatch,
    get_all_patterns,
    get_pattern_by_id,
)

from .context import (
    QuestionType,
    UserState,
    DecisionContext,
)

from .state import (
    Tier,
    Intent,
    Session,
    SessionState,
)

from .prompts import (
    TIER_1_SYSTEM_PROMPT,
    TIER_2_ROUND_1_SYSTEM_PROMPT,
    get_tier_1_prompt,
)

__version__ = "1.0.0-alpha"

__all__ = [
    # Pattern module
    "Pattern",
    "PatternType",
    "PatternMatch",
    "get_all_patterns",
    "get_pattern_by_id",
    # Context module
    "QuestionType",
    "UserState",
    "DecisionContext",
    # State module
    "Tier",
    "Intent",
    "Session",
    "SessionState",
    # Prompts module
    "TIER_1_SYSTEM_PROMPT",
    "TIER_2_ROUND_1_SYSTEM_PROMPT",
    "get_tier_1_prompt",
]
