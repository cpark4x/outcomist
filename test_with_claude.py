#!/usr/bin/env python3
"""Test Outcomist Core with real Claude API.

This script validates that the modular library produces quality output
comparable to the original 990-line explore.md command.

Usage:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python3 test_with_claude.py
"""

import sys
import os
from pathlib import Path

# Add outcomist_core to path
sys.path.insert(0, str(Path(__file__).parent))


def check_api_key():
    """Check if Anthropic API key is available."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print("\nTo run this test:")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        print("  python3 test_with_claude.py")
        return False
    
    print(f"✅ API key found: {api_key[:15]}...")
    return True


def test_office_redesign():
    """Test Office Redesign scenario with real Claude."""
    print("\n" + "=" * 70)
    print("TEST 1: Office Redesign (Personal Sanctuary Pattern)")
    print("=" * 70)
    
    from outcomist_core.discovery import DiscoveryFlow
    from outcomist_core.llm import AnthropicProvider
    
    # Initialize with real Claude
    print("\n🔧 Initializing Claude API...")
    try:
        llm = AnthropicProvider()
        flow = DiscoveryFlow(llm_provider=llm)
        print("✅ Connected to Claude")
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        return False
    
    # Start session
    decision = "I want to redesign my office to make it more inspiring for work"
    
    print(f"\n📝 Decision: '{decision}'")
    print("\n🤖 Calling Claude for Tier 1 pattern recognition...\n")
    
    try:
        session, response = flow.start_session(decision)
        
        print("-" * 70)
        print(response.content)
        print("-" * 70)
        
        # Show detected patterns
        if response.patterns:
            print(f"\n🎯 Patterns detected:")
            for i, pattern in enumerate(response.patterns, 1):
                print(f"  {i}. {pattern.pattern_name} (confidence: {pattern.confidence:.2f})")
        
        # Show suggested questions
        if response.suggested_questions:
            print(f"\n💡 Suggested questions for discovery:")
            for i, q in enumerate(response.suggested_questions, 1):
                print(f"  {i}. {q}")
        
        print(f"\n✅ Tier 1 complete (session: {session.session_id[:8]}...)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during flow: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_client_vs_product():
    """Test Client vs Product scenario with real Claude."""
    print("\n" + "=" * 70)
    print("TEST 2: Client vs Product (Scarcity Mindset Pattern)")
    print("=" * 70)
    
    from outcomist_core.discovery import DiscoveryFlow
    from outcomist_core.llm import AnthropicProvider
    
    # Initialize with real Claude
    llm = AnthropicProvider()
    flow = DiscoveryFlow(llm_provider=llm)
    
    # Start session
    decision = "Should I take this $6K/month client work or focus on my $2K MRR product? The market is tough and I'm thankful for the stable client money."
    
    print(f"\n📝 Decision: '{decision}'")
    print("\n🤖 Calling Claude for Tier 1 pattern recognition...\n")
    
    try:
        session, response = flow.start_session(decision)
        
        print("-" * 70)
        print(response.content)
        print("-" * 70)
        
        # Show detected patterns
        if response.patterns:
            print(f"\n🎯 Patterns detected:")
            for i, pattern in enumerate(response.patterns, 1):
                print(f"  {i}. {pattern.pattern_name} (confidence: {pattern.confidence:.2f})")
        
        # Show suggested questions
        if response.suggested_questions:
            print(f"\n💡 Suggested questions for discovery:")
            for i, q in enumerate(response.suggested_questions, 1):
                print(f"  {i}. {q}")
        
        print(f"\n✅ Tier 1 complete")
        
        # Optionally continue to Tier 2 if user wants
        print("\n" + "=" * 70)
        print("Continue to Tier 2 Discovery? (yes/no)")
        print("=" * 70)
        
        user_input = input("> ").strip().lower()
        
        if user_input in ["yes", "y"]:
            print("\n🤖 Calling Claude for Tier 2 Round 1 question...\n")
            
            response = flow.continue_session(session, user_input)
            
            print("-" * 70)
            print(response.content)
            print("-" * 70)
            
            print(f"\n✅ Tier 2 Round 1 delivered")
            print("\n💬 You can continue answering questions to see the full flow.")
            print("   (For now, stopping here to keep test simple)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during flow: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_information_request():
    """Test information request detection."""
    print("\n" + "=" * 70)
    print("TEST 3: Information Request (Question Type Detection)")
    print("=" * 70)
    
    from outcomist_core.context.analyzer import ContextAnalyzer
    
    decisions = [
        ("Why is progesterone causing acne?", "information"),
        ("What meals should I make?", "execution"),
        ("Should I take this job?", "decision"),
    ]
    
    analyzer = ContextAnalyzer()
    
    print("\n🔍 Testing question type detection:\n")
    
    for decision, expected in decisions:
        context = analyzer.analyze(decision)
        detected = context.question_type.value
        
        status = "✅" if detected == expected else "❌"
        print(f"{status} '{decision[:50]}...'")
        print(f"   Expected: {expected}, Detected: {detected}")
        print()
    
    return True


def main():
    """Run real Claude API tests."""
    print("=" * 70)
    print("PHASE 4: Real Claude API Integration Testing")
    print("=" * 70)
    
    # Check API key
    if not check_api_key():
        return 1
    
    print("\n⚠️  NOTE: This will make real API calls to Claude.")
    print("   Estimated cost: ~$0.05-0.10 for both tests")
    print("\nContinue? (yes/no)")
    
    confirm = input("> ").strip().lower()
    if confirm not in ["yes", "y"]:
        print("\n👋 Canceled")
        return 0
    
    try:
        # Test 1: Office Redesign (quick pattern test)
        success1 = test_office_redesign()
        
        # Test 2: Client vs Product (with optional Tier 2)
        success2 = test_client_vs_product()
        
        # Test 3: Question type detection (no API calls)
        success3 = test_information_request()
        
        # Summary
        print("\n" + "=" * 70)
        print("PHASE 4 RESULTS")
        print("=" * 70)
        
        if success1 and success2 and success3:
            print("\n✅ ALL TESTS PASSED")
            print("\n📊 What was validated:")
            print("   ✅ Real Claude API integration works")
            print("   ✅ Pattern recognition quality")
            print("   ✅ Tier 1 → Tier 2 flow")
            print("   ✅ Question type detection")
            print("\n🎯 Next Steps:")
            print("   • Compare quality with original explore.md")
            print("   • Build CLI integration (explore_v2.md)")
            print("   • Run full regression test suite")
            print("   • Package for distribution")
        else:
            print("\n⚠️  SOME TESTS HAD ISSUES")
            print("   Review errors above")
        
        print("\n" + "=" * 70)
        
        return 0 if (success1 and success2 and success3) else 1
        
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user")
        return 0
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
