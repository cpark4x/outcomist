#!/usr/bin/env python3
"""Simple test with real Claude API - no interactive prompts.

This script runs two quick tests to validate quality:
1. Office Redesign (Personal Sanctuary pattern)
2. Client vs Product (Scarcity Mindset pattern)

Usage:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python3 test_claude_simple.py
"""

import sys
import os
from pathlib import Path

# Add outcomist_core to path
sys.path.insert(0, str(Path(__file__).parent))


def main():
    """Run tests with real Claude API."""
    
    # Check API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set")
        print("\nSet it with: export ANTHROPIC_API_KEY='sk-ant-...'")
        return 1
    
    print("=" * 70)
    print("Testing Outcomist Core with Real Claude API")
    print("=" * 70)
    print(f"\n✅ API key: {api_key[:15]}...")
    
    from outcomist_core.discovery import DiscoveryFlow
    from outcomist_core.llm import AnthropicProvider
    
    # Initialize
    print("\n🔧 Initializing Claude...")
    try:
        llm = AnthropicProvider(api_key=api_key)
        flow = DiscoveryFlow(llm_provider=llm)
        print("✅ Connected to Claude API")
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        return 1
    
    # Test 1: Office Redesign
    print("\n" + "=" * 70)
    print("TEST 1: Office Redesign")
    print("=" * 70)
    
    decision1 = "I want to redesign my office to make it more inspiring for work"
    print(f"\n📝 Decision: '{decision1}'")
    print("\n🤖 Claude's Tier 1 response:\n")
    
    try:
        session1, response1 = flow.start_session(decision1)
        
        print("-" * 70)
        print(response1.content)
        print("-" * 70)
        
        if response1.patterns:
            print(f"\n🎯 Top pattern: {response1.patterns[0].pattern_name} ({response1.patterns[0].confidence:.2f})")
        
        print("\n✅ Test 1 complete")
        
    except Exception as e:
        print(f"\n❌ Test 1 failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # Test 2: Client vs Product
    print("\n" + "=" * 70)
    print("TEST 2: Client vs Product")
    print("=" * 70)
    
    decision2 = "Should I take this $6K/month client work or focus on my $2K MRR product? The market is tough and I'm thankful for the stable client money."
    print(f"\n📝 Decision: '{decision2}'")
    print("\n🤖 Claude's Tier 1 response:\n")
    
    try:
        session2, response2 = flow.start_session(decision2)
        
        print("-" * 70)
        print(response2.content)
        print("-" * 70)
        
        if response2.patterns:
            print(f"\n🎯 Top pattern: {response2.patterns[0].pattern_name} ({response2.patterns[0].confidence:.2f})")
        
        print("\n✅ Test 2 complete")
        
    except Exception as e:
        print(f"\n❌ Test 2 failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # Summary
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    print("\n✅ Both tests completed successfully!")
    print("\n📊 API Usage:")
    print("   • Tests run: 2")
    print("   • LLM calls: 2 (Tier 1 only)")
    print("   • Estimated cost: ~$0.02-0.05")
    
    print("\n🎯 Quality Assessment:")
    print("   Review the Tier 1 responses above and compare with")
    print("   what the original /explore command would produce.")
    
    print("\n💡 Next Steps:")
    print("   • If quality is good → Build CLI integration (explore_v2.md)")
    print("   • If quality needs work → Adjust prompts and re-test")
    print("   • Run full Tier 2 flow test (rounds 1-2, summary, recommendation)")
    
    print("\n" + "=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
