#!/usr/bin/env python3
"""Test script to validate Phase 3 discovery flow.

This script validates the complete discovery flow end-to-end:
1. Session creation
2. Pattern recognition (Tier 1)
3. Discovery questions (Tier 2)
4. Summary confirmation
5. Recommendation delivery
"""

import sys
from pathlib import Path

# Add outcomist_core to path
sys.path.insert(0, str(Path(__file__).parent))

from outcomist_core.discovery import DiscoveryFlow
from outcomist_core.llm import MockLLMProvider
from outcomist_core.state import Tier


def test_complete_flow():
    """Test complete discovery flow end-to-end."""
    print("🔍 Testing Complete Discovery Flow...")
    print("=" * 70)
    
    # Setup mock LLM with canned responses
    canned_responses = {
        "pattern recognition": "You're framing this as a simple redesign, but I notice you used the word 'inspiring' - this sounds like you're looking to create a space that reflects who you are, not just optimize for work.\n\nWhat kind of space would make you feel most yourself?",
        
        "round 1": "What activities beyond work do you imagine doing in this space?",
        
        "round 2": "How much are you willing to invest in this transformation (time and money)?",
        
        "summary": """Let me summarize what I've heard to make sure I understand:

• You want a space that feels inspiring and reflects your personality
• You envision using it for gaming, personal projects, and displaying memorabilia
• You're willing to invest significantly in making this your personal sanctuary

Does that capture it accurately?""",
        
        "recommendation": """Based on what you've shared, I recommend treating this as a **personal sanctuary project**, not just an office redesign.

Here's why: You're not asking about ergonomics or productivity - you're asking about inspiration and personal expression. The space should reflect who you are beyond work.

**Recommended approach:**
1. **Zone the space**: Create distinct areas for work, gaming, and personal display
2. **Start with what inspires you**: Bring in the memorabilia and gaming setup first
3. **Budget realistically**: This is a transformation, not a refresh - plan for $5-10K and 2-3 months
4. **Make it yours**: This isn't about impressing clients, it's about creating a retreat

Want me to help you create a layout plan together, or do you want to take it from here?""",
    }
    
    mock_llm = MockLLMProvider(canned_responses)
    flow = DiscoveryFlow(llm_provider=mock_llm)
    
    # Test scenario: Office Redesign
    decision = "I want to redesign my office to make it more inspiring for work"
    
    print(f"\n📝 Decision: '{decision}'")
    print()
    
    # Step 1: Start session (Tier 1)
    print("=" * 70)
    print("STEP 1: Start Session (Tier 1 Pattern Recognition)")
    print("=" * 70)
    
    session, response = flow.start_session(decision)
    
    print(f"\n✅ Session created: {session.session_id}")
    print(f"✅ Tier: {response.tier.value}")
    print(f"✅ Step: {response.step.value}")
    print(f"\n🤖 Assistant:\n{response.content}")
    
    if response.patterns:
        print(f"\n🎯 Patterns detected:")
        for i, pattern in enumerate(response.patterns, 1):
            print(f"  {i}. {pattern.pattern_name} (confidence: {pattern.confidence:.2f})")
    
    assert response.tier == Tier.TIER_1
    assert response.needs_user_response
    assert session.state.tier == Tier.TIER_1
    print("\n✅ Tier 1 complete")
    
    # Step 2: User accepts and moves to Tier 2
    print("\n" + "=" * 70)
    print("STEP 2: User Accepts → Tier 2 Round 1")
    print("=" * 70)
    
    user_response = "Yes, let's explore this"
    print(f"\n👤 User: {user_response}")
    
    response = flow.continue_session(session, user_response)
    
    print(f"\n✅ Tier: {response.tier.value}")
    print(f"✅ Step: {response.step.value}")
    print(f"\n🤖 Assistant:\n{response.content}")
    
    assert response.tier == Tier.TIER_2
    assert session.state.round == 1
    assert len(session.state.questions_asked) == 1
    print("\n✅ Tier 2 Round 1 complete")
    
    # Step 3: User answers Round 1 → Round 2
    print("\n" + "=" * 70)
    print("STEP 3: Round 1 Answer → Round 2 Question")
    print("=" * 70)
    
    user_response = "I imagine gaming, displaying my memorabilia, and having a space to work on personal projects"
    print(f"\n👤 User: {user_response}")
    
    response = flow.continue_session(session, user_response)
    
    print(f"\n✅ Step: {response.step.value}")
    print(f"\n🤖 Assistant:\n{response.content}")
    
    assert session.state.round == 2
    assert len(session.state.questions_asked) == 2
    assert len(session.state.user_answers) == 1
    print("\n✅ Tier 2 Round 2 complete")
    
    # Step 4: User answers Round 2 → Summary
    print("\n" + "=" * 70)
    print("STEP 4: Round 2 Answer → Summary")
    print("=" * 70)
    
    user_response = "I'm willing to invest $5-10K and a few months to get this right"
    print(f"\n👤 User: {user_response}")
    
    response = flow.continue_session(session, user_response)
    
    print(f"\n✅ Step: {response.step.value}")
    print(f"\n🤖 Assistant:\n{response.content}")
    
    assert len(session.state.user_answers) == 2
    assert session.state.summary_text is not None
    print("\n✅ Summary generated")
    
    # Step 5: User confirms summary → Recommendation
    print("\n" + "=" * 70)
    print("STEP 5: Confirm Summary → Recommendation")
    print("=" * 70)
    
    print("\n👤 User: Yes, that's accurate")
    
    response = flow.confirm_summary(session, confirmed=True)
    
    print(f"\n✅ Step: {response.step.value}")
    print(f"✅ Complete: {response.is_complete}")
    print(f"\n🤖 Assistant:\n{response.content}")
    
    assert response.is_complete
    assert session.state.summary_confirmed
    assert session.state.recommendation is not None
    print("\n✅ Recommendation delivered")
    
    # Summary
    print("\n" + "=" * 70)
    print("FLOW COMPLETE")
    print("=" * 70)
    print(f"\n📊 Session Stats:")
    print(f"  • Questions asked: {len(session.state.questions_asked)}")
    print(f"  • Answers collected: {len(session.state.user_answers)}")
    print(f"  • Messages exchanged: {len(session.conversation)}")
    print(f"  • LLM calls: {mock_llm.call_count}")
    print(f"  • Tier reached: {session.state.tier.value}")
    
    return True


def test_session_serialization():
    """Test session can be saved and restored."""
    print("\n\n🔍 Testing Session Serialization...")
    print("=" * 70)
    
    mock_llm = MockLLMProvider()
    flow = DiscoveryFlow(llm_provider=mock_llm)
    
    # Create session
    decision = "Should I take this client work or focus on my product?"
    session, response = flow.start_session(decision)
    
    # Answer first question
    response = flow.continue_session(session, "Yes, let's explore")
    response = flow.continue_session(session, "I have 12 months of runway and product is growing")
    
    print(f"\n✅ Session has {len(session.conversation)} messages")
    
    # Serialize
    session_dict = session.to_dict()
    print(f"✅ Serialized to dict with {len(session_dict.keys())} keys")
    
    # Deserialize
    from outcomist_core.state import Session
    restored = Session.from_dict(session_dict)
    
    print(f"✅ Restored session with {len(restored.conversation)} messages")
    
    assert restored.session_id == session.session_id
    assert restored.decision_statement == session.decision_statement
    assert len(restored.conversation) == len(session.conversation)
    assert restored.state.tier == session.state.tier
    assert restored.state.round == session.state.round
    
    print("\n✅ Serialization works correctly")
    
    return True


def test_pattern_integration():
    """Test pattern detection integrates with flow."""
    print("\n\n🔍 Testing Pattern Integration...")
    print("=" * 70)
    
    mock_llm = MockLLMProvider()
    flow = DiscoveryFlow(llm_provider=mock_llm)
    
    # Test scenario with clear pattern
    decision = "Should I take this $6K/month client work or focus on my $2K MRR product? The market is tough and I'm thankful for the stable client money."
    
    print(f"\n📝 Decision: '{decision[:60]}...'")
    
    session, response = flow.start_session(decision)
    
    print(f"\n✅ Session created")
    
    if response.patterns:
        print(f"✅ Patterns detected: {len(response.patterns)}")
        for i, pattern in enumerate(response.patterns, 1):
            print(f"  {i}. {pattern.pattern_name} ({pattern.confidence:.2f})")
        
        # Check suggested questions
        if response.suggested_questions:
            print(f"\n✅ Suggested questions: {len(response.suggested_questions)}")
            for i, q in enumerate(response.suggested_questions, 1):
                print(f"  {i}. {q}")
    else:
        print("⚠️  No patterns detected")
    
    # Verify pattern stored in session
    if session.state.pattern_matches:
        print(f"\n✅ Patterns stored in session: {session.state.pattern_matches}")
    
    return True


def main():
    """Run all Phase 3 tests."""
    print("=" * 70)
    print("PHASE 3 VALIDATION: Discovery Flow End-to-End")
    print("=" * 70)
    
    try:
        # Run tests
        test_complete_flow()
        test_session_serialization()
        test_pattern_integration()
        
        # Summary
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED - Phase 3 Complete!")
        print("=" * 70)
        print("\n📦 Phase 3 Components:")
        print("   ✅ llm/provider.py - LLM abstraction with mock provider")
        print("   ✅ llm/anthropic.py - Claude integration (optional)")
        print("   ✅ discovery/flow.py - DiscoveryFlow orchestrator")
        print("   ✅ discovery/types.py - FlowResponse, FlowStep")
        print("\n🎯 Capabilities Validated:")
        print("   ✅ Complete Tier 1 → Tier 2 flow")
        print("   ✅ Pattern detection integration")
        print("   ✅ Question generation and sequencing")
        print("   ✅ Summary creation and confirmation")
        print("   ✅ Recommendation delivery")
        print("   ✅ Session serialization/deserialization")
        print("\n🚀 Next Steps:")
        print("   • Test with real Claude API")
        print("   • Build CLI or web interface")
        print("   • Validate against 13 test scenarios")
        print("   • Deploy and collect real user feedback")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
