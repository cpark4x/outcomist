"""Prompt library module for Outcomist.

Single source of truth for all Outcomist prompts.
"""

from .library import (
    # Tier 1
    TIER_1_SYSTEM_PROMPT,
    get_tier_1_prompt,
    # Tier 2
    TIER_2_ROUND_1_SYSTEM_PROMPT,
    TIER_2_ANALYSIS_SYSTEM_PROMPT,
    TIER_2_ROUND_2_SYSTEM_PROMPT,
    TIER_2_SUMMARY_SYSTEM_PROMPT,
    TIER_2_RECOMMENDATION_SYSTEM_PROMPT,
    TIER_2_OFFER_TIER_3_SYSTEM_PROMPT,
    # Helper functions
    get_tier_2_round_1_prompt,
    get_tier_2_analysis_prompt,
    get_tier_2_round_2_prompt,
    get_tier_2_summary_prompt,
    get_tier_2_recommendation_prompt,
)

__all__ = [
    # Tier 1
    "TIER_1_SYSTEM_PROMPT",
    "get_tier_1_prompt",
    # Tier 2
    "TIER_2_ROUND_1_SYSTEM_PROMPT",
    "TIER_2_ANALYSIS_SYSTEM_PROMPT",
    "TIER_2_ROUND_2_SYSTEM_PROMPT",
    "TIER_2_SUMMARY_SYSTEM_PROMPT",
    "TIER_2_RECOMMENDATION_SYSTEM_PROMPT",
    "TIER_2_OFFER_TIER_3_SYSTEM_PROMPT",
    # Helpers
    "get_tier_2_round_1_prompt",
    "get_tier_2_analysis_prompt",
    "get_tier_2_round_2_prompt",
    "get_tier_2_summary_prompt",
    "get_tier_2_recommendation_prompt",
]
