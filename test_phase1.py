#!/usr/bin/env python3
"""Test script to validate Phase 1 pattern extraction.

This script verifies that:
1. All 9 patterns are extracted correctly
2. Pattern structure is intact (signals, questions, pitfalls)
3. Prompts are accessible
4. Types are properly defined
"""

import sys
from pathlib import Path

# Add outcomist_core to path
sys.path.insert(0, str(Path(__file__).parent))

from outcomist_core import (
    get_all_patterns,
    get_pattern_by_id,
    PatternType,
    Session,
    DecisionContext,
    TIER_1_SYSTEM_PROMPT,
    get_tier_1_prompt,
)


def test_patterns():
    """Test pattern library."""
    print("🔍 Testing Pattern Library...")
    
    # Test 1: Get all patterns
    patterns = get_all_patterns()
    assert len(patterns) == 9, f"Expected 9 patterns, got {len(patterns)}"
    print(f"✅ All 9 patterns loaded")
    
    # Test 2: Check each pattern has required fields
    for pattern in patterns:
        assert pattern.name, f"Pattern {pattern.id} missing name"
        assert pattern.surface_request, f"Pattern {pattern.id} missing surface_request"
        assert pattern.real_problem, f"Pattern {pattern.id} missing real_problem"
        assert len(pattern.signals) > 0, f"Pattern {pattern.id} has no signals"
        assert len(pattern.questions) > 0, f"Pattern {pattern.id} has no questions"
        assert len(pattern.pitfalls) > 0, f"Pattern {pattern.id} has no pitfalls"
    print(f"✅ All patterns have required fields")
    
    # Test 3: Pattern lookup by ID
    personal_sanctuary = get_pattern_by_id(PatternType.PERSONAL_SANCTUARY)
    assert personal_sanctuary.name == "Personal Sanctuary Pattern"
    assert len(personal_sanctuary.signals) == 4
    assert len(personal_sanctuary.questions) == 4
    assert len(personal_sanctuary.pitfalls) == 3
    print(f"✅ Pattern lookup by ID works")
    
    # Test 4: Print pattern summary
    print("\n📋 Pattern Summary:")
    for i, pattern in enumerate(patterns, 1):
        print(f"  {i}. {pattern.name}")
        print(f"     - {len(pattern.signals)} signals")
        print(f"     - {len(pattern.questions)} questions")
        print(f"     - {len(pattern.pitfalls)} pitfalls")
    
    return True


def test_prompts():
    """Test prompt library."""
    print("\n🔍 Testing Prompt Library...")
    
    # Test 1: Tier 1 system prompt exists
    assert TIER_1_SYSTEM_PROMPT, "TIER_1_SYSTEM_PROMPT is empty"
    assert "pattern recognition" in TIER_1_SYSTEM_PROMPT.lower()
    print(f"✅ Tier 1 system prompt loaded ({len(TIER_1_SYSTEM_PROMPT)} chars)")
    
    # Test 2: Tier 1 prompt generation
    decision = "Should I redesign my office?"
    prompt = get_tier_1_prompt(decision)
    assert decision in prompt
    assert "pattern recognition" in prompt.lower()
    print(f"✅ Tier 1 prompt generation works")
    
    return True


def test_types():
    """Test type definitions."""
    print("\n🔍 Testing Type Definitions...")
    
    # Test 1: Session creation
    session = Session(
        session_id="test-123",
        decision_statement="Should I take this job?"
    )
    assert session.session_id == "test-123"
    assert session.decision_statement == "Should I take this job?"
    print(f"✅ Session type works")
    
    # Test 2: Session serialization
    session.add_message("user", "I'm deciding between two options")
    session.add_message("assistant", "Tell me more")
    session_dict = session.to_dict()
    assert session_dict["session_id"] == "test-123"
    assert len(session_dict["conversation"]) == 2
    print(f"✅ Session serialization works")
    
    # Test 3: Session deserialization
    restored = Session.from_dict(session_dict)
    assert restored.session_id == session.session_id
    assert len(restored.conversation) == 2
    print(f"✅ Session deserialization works")
    
    # Test 4: DecisionContext
    context = DecisionContext.from_text("Should I redesign my office?")
    assert context.decision_text == "Should I redesign my office?"
    print(f"✅ DecisionContext type works")
    
    return True


def test_real_scenario():
    """Test with a real scenario from the test suite."""
    print("\n🔍 Testing Real Scenario...")
    
    # Test scenario: Office Redesign (should match Personal Sanctuary pattern)
    decision = "I want to redesign my office to make it more inspiring for work"
    
    # Get patterns that might match
    patterns = get_all_patterns()
    personal_sanctuary = get_pattern_by_id(PatternType.PERSONAL_SANCTUARY)
    
    print(f"\n📝 Scenario: '{decision}'")
    print(f"\n🎯 Expected Pattern: {personal_sanctuary.name}")
    print(f"   Surface Request: {personal_sanctuary.surface_request}")
    print(f"   Real Problem: {personal_sanctuary.real_problem}")
    print(f"\n   Key Signals:")
    for signal in personal_sanctuary.signals:
        print(f"   • {signal.description}")
    print(f"\n   Key Questions:")
    for q in personal_sanctuary.questions[:3]:  # Show first 3
        print(f"   • {q.text}")
    
    return True


def main():
    """Run all tests."""
    print("=" * 70)
    print("PHASE 1 VALIDATION: Pattern & Prompt Extraction")
    print("=" * 70)
    
    try:
        test_patterns()
        test_prompts()
        test_types()
        test_real_scenario()
        
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED - Phase 1 Complete!")
        print("=" * 70)
        print("\n📦 Package Structure:")
        print("   outcomist_core/")
        print("   ├── pattern/       ✅ 9 patterns extracted")
        print("   ├── context/       ✅ Types defined")
        print("   ├── state/         ✅ Session management")
        print("   ├── prompts/       ✅ Prompt library")
        print("   ├── discovery/     ⏳ Phase 2")
        print("   └── llm/           ⏳ Phase 5")
        print("\n🎯 Next Steps: Phase 2 - Build PatternMatcher")
        return 0
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
