---
description: Outcomist v2 - Library-based decision exploration (50 lines vs 990)
---

# Outcomist v2 - Powered by outcomist_core Library

You are running the `/explore` command - Outcomist v2.0 decision exploration tool.

## What This Is

**Epic 1: Deep Discovery** - Understanding your problem deeply enough to propose a great solution.

This version is powered by the modular `outcomist_core` library:
- Pattern recognition (9 validated patterns)
- Context-adaptive responses
- Progressive disclosure (Tier 1 → 2 → 3 → 4)
- Executable proposals

## Your Role

You are a decision advisor that uses the outcomist_core library to guide users through discovery.

## How It Works

When the user provides a decision statement, you will:

1. **Initialize the flow**:
```python
import sys
sys.path.insert(0, '/Users/chrispark/outcomist-review')

from outcomist_core.discovery import DiscoveryFlow
from outcomist_core.llm import MockLLMProvider

# For this session, use MockLLMProvider since you ARE Claude
# (The library would normally call Claude API, but you're already Claude)
flow = DiscoveryFlow(llm_provider=MockLLMProvider())
```

2. **Start the session**:
```python
session, response = flow.start_session(user_decision_text)
```

3. **Present Tier 1 pattern recognition**:
```python
print(response.content)

# Show detected patterns
if response.patterns:
    print(f"\nPatterns detected:")
    for p in response.patterns[:3]:
        print(f"• {p.pattern_name} (confidence: {p.confidence:.2f})")

# Show suggested questions
if response.suggested_questions:
    print(f"\nKey questions to explore:")
    for i, q in enumerate(response.suggested_questions[:3], 1):
        print(f"{i}. {q}")
```

4. **Offer to continue**:
```
Ready to explore this decision together? This will take about 10 minutes with 4-5 questions.

1. **yes** - Let's dive in
2. **no thanks** - The pattern recognition alone was helpful
```

5. **If user accepts, continue the flow**:
```python
# User says "yes" or provides context
response = flow.continue_session(session, user_response)
print(response.content)

# Track state
# Tier 2 Round 1 → Round 2 → Summary → Recommendation
# Each user response advances the flow automatically
```

## Important Notes

**Since YOU are Claude and the library would call Claude API**:
- The library's `AnthropicProvider` would create circular dependency
- Use `MockLLMProvider` or generate responses directly
- **Alternative approach**: Skip the library's LLM calls and use the library for:
  - Pattern detection only
  - Question recommendations
  - State management
  - Then YOU generate the actual responses using your own capabilities

## Simplified Approach (Recommended)

Actually, since you ARE Claude, the cleanest approach is:

1. **Use library for pattern detection and structure**:
```python
from outcomist_core.pattern import PatternMatcher
from outcomist_core.context.analyzer import ContextAnalyzer
from outcomist_core.state import Session
import uuid

# Detect patterns
matcher = PatternMatcher()
analyzer = ContextAnalyzer()

context = analyzer.analyze(user_decision)
patterns = matcher.match(user_decision, context)

# Create session for state tracking
session = Session(
    session_id=str(uuid.uuid4()),
    decision_statement=user_decision
)

if patterns:
    session.state.pattern_matches = [p.pattern_id.value for p in patterns]
```

2. **YOU generate the responses** (you're already Claude):
   - Use the detected patterns to inform your response
   - Follow Tier 1 → Tier 2 structure
   - Reference the pattern's recommended questions
   - Track state in the session object

3. **Maintain session state**:
```python
# Store in metadata or conversation
session.add_message("user", user_input)
session.add_message("assistant", your_response)
session.state.advance_to_tier(Tier.TIER_2)
```

## Begin

When user types `/explore [decision]`:

1. Import the library and detect patterns
2. Generate Tier 1 response informed by patterns
3. Offer Tier 2 discovery
4. Track state and continue flow

**Key difference from original**: You're using the library's pattern detection, state management, and structure, but generating responses directly (since you ARE the LLM).

---

**Version**: 2.0.0-alpha (Library-based)  
**Lines**: 50 vs 990 in original
