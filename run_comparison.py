#!/usr/bin/env python3
"""Run library version tests to compare with original explore.md.

This script runs the 3 test scenarios with the library and displays results
for manual comparison with the original /explore command.
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from outcomist_core.discovery import DiscoveryFlow
from outcomist_core.llm import AnthropicProvider


def run_scenario(scenario_name: str, decision: str, expected_pattern: str):
    """Run a scenario and display results."""
    
    print("\n" + "=" * 70)
    print(f"SCENARIO: {scenario_name}")
    print("=" * 70)
    
    print(f"\n📝 Decision:")
    print(f"   \"{decision}\"")
    
    print(f"\n🎯 Expected Pattern: {expected_pattern}")
    
    print("\n🤖 Library Version (explore_v2) Response:\n")
    print("─" * 70)
    
    try:
        llm = AnthropicProvider()
        flow = DiscoveryFlow(llm_provider=llm)
        
        session, response = flow.start_session(decision)
        
        # Display response
        print(response.content)
        print("─" * 70)
        
        # Display pattern info
        if response.patterns:
            print(f"\n✅ Pattern Detected: {response.patterns[0].pattern_name}")
            print(f"   Confidence: {response.patterns[0].confidence:.2f}")
            
            if len(response.patterns) > 1:
                print(f"\n   Other patterns:")
                for p in response.patterns[1:3]:
                    print(f"   • {p.pattern_name} ({p.confidence:.2f})")
        else:
            print(f"\n⚠️  No pattern detected")
        
        # Display suggested questions
        if response.suggested_questions:
            print(f"\n💡 Suggested Questions:")
            for i, q in enumerate(response.suggested_questions[:3], 1):
                print(f"   {i}. {q}")
        
        print(f"\n✅ Test complete")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all 3 comparison scenarios."""
    
    # Check API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY not set")
        print("\nSet it with: export ANTHROPIC_API_KEY='sk-ant-...'")
        return 1
    
    print("=" * 70)
    print("MANUAL COMPARISON: Testing Library Version")
    print("=" * 70)
    print("\nThis will run 3 scenarios with the library version.")
    print("You can then test the same scenarios with /explore to compare.")
    print("\n⚠️  This will make 3 real API calls (~$0.05 total)")
    print("\nContinue? (yes/no)")
    
    confirm = input("> ").strip().lower()
    if confirm not in ["yes", "y"]:
        print("\n👋 Canceled")
        return 0
    
    scenarios = [
        {
            "name": "Test 1: Office Redesign",
            "decision": "I want to redesign my office to make it more inspiring for work",
            "expected": "Personal Sanctuary Pattern"
        },
        {
            "name": "Test 2: Client vs Product",
            "decision": "Should I take this $6K/month client work or focus on my $2K MRR product? The market is tough and I'm thankful for the stable client money.",
            "expected": "Scarcity Mindset Hiding Opportunity"
        },
        {
            "name": "Test 3: Feature Decision",
            "decision": "Should I build Feature X for 10 customers or Feature Y for 2 customers? We position ourselves as employees-first.",
            "expected": "Popularity Contest Hiding Identity Crisis"
        }
    ]
    
    results = []
    for scenario in scenarios:
        success = run_scenario(
            scenario["name"],
            scenario["decision"],
            scenario["expected"]
        )
        results.append(success)
    
    # Summary
    print("\n" + "=" * 70)
    print("LIBRARY VERSION TESTING COMPLETE")
    print("=" * 70)
    
    print(f"\n✅ Tests completed: {sum(results)}/3")
    
    print("\n📋 Now test with ORIGINAL /explore command:")
    print("\nFor each scenario above, run:")
    print("   /explore [same decision text]")
    print("\nThen compare the Tier 1 responses.")
    
    print("\n🔍 Comparison Criteria:")
    print("   1. Pattern detection - Same pattern identified?")
    print("   2. Tone - Conversational vs academic?")
    print("   3. Specificity - Quotes user's exact words/numbers?")
    print("   4. Insight quality - Similar depth and relevance?")
    print("   5. Overall - Would you be equally satisfied with both?")
    
    print("\n💾 Document your findings in:")
    print("   MANUAL_COMPARISON_GUIDE.md")
    
    print("\n" + "=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
