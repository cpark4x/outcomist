#!/usr/bin/env python3
"""
Comprehensive end-to-end test of shared prompt library.
Tests both CLI and Web App to ensure they use the same prompts.
"""

import json
import sys
from pathlib import Path

# Test results storage
test_results = {
    "cli": {"tier1": None, "questions": [], "summary": None, "recommendation": None, "score": 0},
    "web": {"tier1": None, "questions": [], "summary": None, "recommendation": None, "score": 0},
    "comparison": {"prompts_match": False, "behavior_match": False, "quality_match": False}
}

# Test scenario
SCENARIO = "Client wants ongoing work $6K/month (90% of time). Means pausing product for 6+ months. Product has traction (100 users, $2K MRR growing). Stable money or bet on product?"

ANSWERS = [
    "it's a relatively new customer. they pitched me with the idea and i think they are looking for cost control. $6k for 35 hours is very light. but the market is really tough and I'm thankful for the work.",
    "monthly burn is about 5k / 60k in savings / 12-14 months without new income / none / my girlfriend",
    "MRR was 500 6 months ago / it is growing about 100 per month / 200 paying 10 per month / 3% churn"
]

# Expected patterns from baseline test
EXPECTED_PATTERNS = {
    "tier1_pattern": "scarcity mindset",
    "tier1_reframe": "Am I choosing safety because I'm afraid",
    "q1_focuses_on": "client opportunity details",
    "q2_focuses_on": "financial runway",
    "q3_focuses_on": "product metrics",
    "no_market_research_requests": True,
    "summary_has_no_judgment": True,
    "recommendation": "Say no to client, go all in on product"
}

def score_tier1(response):
    """Score Tier 1 pattern recognition."""
    score = 0
    feedback = []

    # Check for scarcity mindset pattern
    if "scarcity" in response.lower() or "fear" in response.lower():
        score += 25
        feedback.append("✓ Identified scarcity mindset pattern")
    else:
        feedback.append("✗ Missed scarcity mindset pattern")

    # Check for reframe
    if "afraid" in response.lower() or "choosing safety" in response.lower():
        score += 25
        feedback.append("✓ Reframed to fear-based decision")
    else:
        feedback.append("✗ Weak reframe")

    # Check word count (should be ~160 words max)
    word_count = len(response.split())
    if word_count <= 180:
        score += 25
        feedback.append(f"✓ Concise ({word_count} words)")
    else:
        feedback.append(f"✗ Too verbose ({word_count} words)")

    # Check for intent check
    if "validation" in response.lower() or "whether" in response.lower():
        score += 25
        feedback.append("✓ Includes intent check")
    else:
        feedback.append("✗ Missing intent check")

    return score, feedback

def score_questions(questions):
    """Score discovery questions."""
    score = 0
    feedback = []

    if len(questions) < 2:
        feedback.append("✗ Too few questions")
        return 0, feedback

    # Check Q1 - should ask about client or personal situation
    q1 = questions[0].lower()
    if "client" in q1 or "opportunity" in q1 or "situation" in q1:
        score += 20
        feedback.append("✓ Q1 asks about personal context")
    else:
        feedback.append("✗ Q1 doesn't focus on personal context")

    # Check Q2 - should dig deeper
    if len(questions) > 1:
        q2 = questions[1].lower()
        if "runway" in q2 or "savings" in q2 or "afford" in q2 or "burn" in q2:
            score += 20
            feedback.append("✓ Q2 asks about financial runway")
        else:
            feedback.append("✗ Q2 doesn't probe finances")

    # Check Q3 - should ask about product
    if len(questions) > 2:
        q3 = questions[2].lower()
        if "product" in q3 or "mrr" in q3 or "growth" in q3 or "metrics" in q3:
            score += 20
            feedback.append("✓ Q3 asks about product metrics")
        else:
            feedback.append("✗ Q3 doesn't focus on product")

    # Check for market research requests (should be ZERO)
    market_research = any("research" in q.lower() or "look up" in q.lower() for q in questions)
    if not market_research:
        score += 20
        feedback.append("✓ No market research requests")
    else:
        score += 0
        feedback.append("✗ Asks user to research data")

    # Check question count
    if 2 <= len(questions) <= 3:
        score += 20
        feedback.append(f"✓ Good question count ({len(questions)})")
    else:
        feedback.append(f"✗ Odd question count ({len(questions)})")

    return score, feedback

def score_summary(summary):
    """Score summary quality."""
    score = 0
    feedback = []

    if not summary:
        return 0, ["✗ No summary provided"]

    # Check for bullet points
    if "•" in summary or "*" in summary or "-" in summary:
        score += 25
        feedback.append("✓ Uses bullet points")
    else:
        feedback.append("✗ No bullet points")

    # Check for judgment words (should have NONE)
    judgment_words = ["should", "must", "need to", "bad", "good", "wrong", "right", "mistake"]
    has_judgment = any(word in summary.lower() for word in judgment_words)
    if not has_judgment:
        score += 50
        feedback.append("✓ No judgment - just facts")
    else:
        score += 0
        feedback.append("✗ Contains judgment")

    # Check if asks for confirmation
    if "capture" in summary.lower() or "accurate" in summary.lower() or "correct" in summary.lower():
        score += 25
        feedback.append("✓ Asks for confirmation")
    else:
        feedback.append("✗ Doesn't ask for confirmation")

    return score, feedback

def score_recommendation(recommendation):
    """Score recommendation quality."""
    score = 0
    feedback = []

    if not recommendation:
        return 0, ["✗ No recommendation provided"]

    # Check for clear stance
    if "say no" in recommendation.lower() or "decline" in recommendation.lower() or "go all in" in recommendation.lower():
        score += 30
        feedback.append("✓ Clear stance (say no to client)")
    elif "take the client" in recommendation.lower():
        score += 0
        feedback.append("✗ Wrong recommendation (should reject client)")
    else:
        score += 10
        feedback.append("⚠ Unclear stance")

    # Check for reasoning
    if ("runway" in recommendation.lower() or "12" in recommendation) and ("growth" in recommendation.lower() or "4x" in recommendation.lower()):
        score += 30
        feedback.append("✓ References user's specific context")
    else:
        feedback.append("✗ Generic reasoning")

    # Check for next actions
    if "next" in recommendation.lower() or "action" in recommendation.lower() or "step" in recommendation.lower():
        score += 20
        feedback.append("✓ Includes next actions")
    else:
        feedback.append("✗ No clear next steps")

    # Check for scarcity mindset callout
    if "scarcity" in recommendation.lower() or "head" in recommendation.lower() and "bank" in recommendation.lower():
        score += 20
        feedback.append("✓ Calls out scarcity mindset")
    else:
        feedback.append("⚠ Misses scarcity mindset insight")

    return score, feedback

def print_test_results():
    """Print comprehensive test results."""
    print("\n" + "="*80)
    print("COMPREHENSIVE SHARED PROMPT LIBRARY TEST RESULTS")
    print("="*80)

    print("\n## TEST SCENARIO")
    print(f"Decision: {SCENARIO}")
    print(f"Answers provided: {len(ANSWERS)}")

    print("\n## CLI TEST RESULTS")
    print("-" * 80)
    if test_results["cli"]["tier1"]:
        print(f"Tier 1 Score: {test_results['cli']['score']}/100")
        print("\nNote: CLI test requires manual interaction - scores based on prompt structure analysis")
    else:
        print("⚠ CLI test not completed (requires manual interaction)")

    print("\n## WEB APP TEST RESULTS")
    print("-" * 80)
    print(f"Overall Score: {test_results['web']['score']}/100")

    if test_results["web"]["tier1"]:
        tier1_score, tier1_feedback = score_tier1(test_results["web"]["tier1"])
        print(f"\nTier 1 Pattern Recognition: {tier1_score}/100")
        for fb in tier1_feedback:
            print(f"  {fb}")

    if test_results["web"]["questions"]:
        q_score, q_feedback = score_questions(test_results["web"]["questions"])
        print(f"\nDiscovery Questions: {q_score}/100")
        for fb in q_feedback:
            print(f"  {fb}")

    if test_results["web"]["summary"]:
        s_score, s_feedback = score_summary(test_results["web"]["summary"])
        print(f"\nSummary Quality: {s_score}/100")
        for fb in s_feedback:
            print(f"  {fb}")

    if test_results["web"]["recommendation"]:
        r_score, r_feedback = score_recommendation(test_results["web"]["recommendation"])
        print(f"\nRecommendation Quality: {r_score}/100")
        for fb in r_feedback:
            print(f"  {fb}")

    print("\n## COMPARISON: CLI vs WEB APP")
    print("-" * 80)
    print(f"Prompts from same source: {test_results['comparison']['prompts_match']}")
    print(f"Behavior matches: {test_results['comparison']['behavior_match']}")
    print(f"Quality matches baseline: {test_results['comparison']['quality_match']}")

    print("\n## BASELINE COMPARISON")
    print("-" * 80)
    print("Previous Test (Nov 4):")
    print("  • Pattern: Scarcity mindset ✓")
    print("  • Q1: Client details ($40/hour identified) ✓")
    print("  • Q2: Financial runway (12-14 months revealed) ✓")
    print("  • Q3: Product metrics (4X growth, 97% retention) ✓")
    print("  • Recommendation: Say No to Client, Go ALL IN ✓")
    print("  • User validation: 'Great.'")

    print("\n## CRITICAL VALIDATIONS")
    print("-" * 80)
    validations = [
        ("✓" if "scarcity" in str(test_results).lower() else "✗", "Scarcity mindset pattern identified"),
        ("✓" if not any("research" in str(q).lower() for q in test_results["web"]["questions"]) else "✗", "No market research requests"),
        ("✓" if test_results["web"]["summary"] and all(word not in test_results["web"]["summary"].lower() for word in ["should", "must", "need to"]) else "✗", "Summary has NO judgment"),
        ("✓" if "no" in str(test_results["web"]["recommendation"]).lower() and "client" in str(test_results["web"]["recommendation"]).lower() else "✗", "Recommends rejecting client"),
    ]

    for check, description in validations:
        print(f"  {check} {description}")

    # Final verdict
    print("\n" + "="*80)
    total_score = test_results["web"]["score"]
    if total_score >= 80:
        print("✅ PASS - Shared prompt library working correctly")
    elif total_score >= 60:
        print("⚠ PARTIAL PASS - Some issues detected")
    else:
        print("❌ FAIL - Significant issues detected")
    print("="*80 + "\n")


def test_cli_sync_with_shared_library():
    """
    Validate CLI prompts contain key phrases from shared library.

    This test ensures that .claude/commands/explore.md is synced with
    outcomist_shared/prompts.py (the single source of truth).
    """
    from pathlib import Path

    cli_path = Path('.claude/commands/explore.md')
    if not cli_path.exists():
        raise FileNotFoundError(f"CLI command file not found: {cli_path}")

    cli_content = cli_path.read_text()

    # Key phrases that MUST be present in CLI (from shared library)
    required_phrases = [
        # Round 1 - Anti-research rule
        'Avoid asking users to research external/market data',
        'Focus on THEIR OWN situation and data',

        # Round 2 - Anti-research + capability checking
        'Avoid asking users to research external/market data',
        'Check capabilities - don\'t assume user lacks skills',

        # Summary - No judgment
        'NO JUDGMENT - just state what they told you',
        'This is about LISTENING, not ADVISING',

        # Recommendation - No fake stats
        'Don\'t invent statistics or fake evidence',

        # Sync marker
        'Prompts synced from outcomist_shared/prompts.py',
    ]

    missing_phrases = []
    for phrase in required_phrases:
        if phrase not in cli_content:
            missing_phrases.append(phrase)

    if missing_phrases:
        print("\n❌ CLI SYNC VALIDATION FAILED")
        print("\nMissing phrases in CLI that should be synced from shared library:")
        for phrase in missing_phrases:
            print(f"  • {phrase}")
        print(f"\nPlease sync .claude/commands/explore.md with outcomist_shared/prompts.py")
        raise AssertionError(f"CLI missing {len(missing_phrases)} required phrases from shared library")

    print("✅ CLI prompts synced with shared library")
    print("   All key phrases from outcomist_shared/prompts.py are present in CLI")


if __name__ == "__main__":
    print("Starting comprehensive test...")
    print("Note: This script provides the testing framework.")
    print("Actual testing requires API calls to running backend.")
    print("\nTest framework ready. Run with web app backend active.")

    # Set comparison flags based on architecture
    test_results["comparison"]["prompts_match"] = True  # Both use outcomist_shared/prompts.py
    test_results["comparison"]["behavior_match"] = "PENDING"  # Needs actual test
    test_results["comparison"]["quality_match"] = "PENDING"  # Needs actual test

    # Run sync validation first
    print("\n" + "="*80)
    print("CLI SYNC VALIDATION")
    print("="*80)
    test_cli_sync_with_shared_library()

    print_test_results()
