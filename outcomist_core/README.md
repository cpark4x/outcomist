# Outcomist Core

**Modular decision exploration library with pattern recognition and adaptive questioning**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What is Outcomist?

Outcomist helps people figure out what they actually want before taking action. It uses pattern recognition and adaptive questioning to surface what matters, turning unclear intentions into clear, executable proposals.

**This library** provides the core components as reusable Python modules that can be integrated into web apps, CLIs, chatbots, APIs, and other tools.

---

## Quick Start

### Installation

```bash
# From local directory
pip install /path/to/outcomist_core

# With Claude API support
pip install "/path/to/outcomist_core[anthropic]"
```

### Basic Usage

```python
from outcomist_core.discovery import DiscoveryFlow
from outcomist_core.llm import AnthropicProvider

# Initialize with Claude
flow = DiscoveryFlow(llm_provider=AnthropicProvider(api_key="your-key"))

# Start a discovery session
session, response = flow.start_session(
    "Should I take this client work or focus on my product?"
)

# Tier 1 pattern recognition delivered
print(response.content)
# → "You're framing this as stable vs risky, but the word 'thankful' 
#    reveals you're operating from scarcity, not strategic growth..."

# Check detected patterns
if response.patterns:
    print(f"Pattern: {response.patterns[0].pattern_name}")
    # → "Scarcity Mindset Hiding Opportunity"

# Continue the conversation
response = flow.continue_session(session, "Yes, let's explore this")
# → Tier 2 Round 1 question

# Complete the flow
# Round 1 → Round 2 → Summary → Recommendation
```

---

## Features

### 🎯 Pattern Recognition (9 Validated Patterns)

```python
from outcomist_core import PatternMatcher

matcher = PatternMatcher()
matches = matcher.match("Should I redesign my office to be more inspiring?")

# Returns: [PatternMatch(Personal Sanctuary Pattern, confidence=0.24)]
```

**9 Patterns Included**:
1. Personal Sanctuary - Creating retreat space, not work optimization
2. Employability Anxiety - Career hedging, not entrepreneurship
3. Health Anxiety - Control over outcomes after trigger event
4. "Additional Revenue" Misframing - High effort framed as "extra"
5. Popularity Contest - Product identity hidden by volume
6. Scarcity Mindset - Fear preventing commitment despite resources
7. Solution Looking for Problem - Building before validating
8. Premature Presentation - Presenting without proof
9. Stuck in Build Phase - Scope issues masking as technical limits

### 📊 Context Analysis

```python
from outcomist_core.context.analyzer import ContextAnalyzer

analyzer = ContextAnalyzer()
context = analyzer.analyze("Why is progesterone causing acne?")

# Returns: QuestionType.INFORMATION (vs DECISION or EXECUTION)
# Extracts: financial signals, emotional language, constraints, etc.
```

### 🔄 Complete Discovery Flow

```python
from outcomist_core.discovery import DiscoveryFlow

flow = DiscoveryFlow(llm_provider=your_llm)

# Tier 1: Pattern Recognition (30 sec)
session, tier1 = flow.start_session(decision)

# Tier 2: Discovery Questions (5-10 min)
round1 = flow.continue_session(session, user_answer)
round2 = flow.continue_session(session, user_answer)
summary = flow.continue_session(session, user_answer)

# Recommendation
recommendation = flow.confirm_summary(session, confirmed=True)
```

### 💾 Session Management

```python
from outcomist_core.state import Session

# Create session
session = Session(session_id="123", decision_statement="My decision")

# Track conversation
session.add_message("user", "My answer")
session.add_message("assistant", "Next question")

# Serialize
data = session.to_dict()
# Store in database, Redis, file system, etc.

# Restore later
restored = Session.from_dict(data)
```

### 🔌 LLM Provider Abstraction

```python
from outcomist_core.llm import AnthropicProvider, MockLLMProvider

# Use Claude
llm = AnthropicProvider(api_key="sk-ant-...")

# Or mock for testing
llm = MockLLMProvider(canned_responses={"pattern": "Mock response"})

# Easy to add OpenAI, local models, etc.
```

---

## Architecture

### Modular Design

```
outcomist_core/
├── pattern/        Pattern recognition (9 patterns, 87.5% accuracy)
├── context/        Context analysis & question type detection
├── state/          Session management with serialization
├── prompts/        Prompt templates with tone guidelines
├── discovery/      Progressive disclosure flow (Tier 1→2→3→4)
└── llm/            LLM provider abstraction
```

Each module is **self-contained** and can be used independently or composed together.

### API Levels

**Level 1: High-Level** (easiest)
```python
from outcomist_core import DiscoveryFlow
flow = DiscoveryFlow(llm_provider=my_llm)
session, response = flow.start_session(decision)
```

**Level 2: Composable** (flexible)
```python
from outcomist_core import PatternMatcher, ContextAnalyzer

matcher = PatternMatcher()
analyzer = ContextAnalyzer()
# Use individual components
```

**Level 3: Programmatic** (full control)
```python
from outcomist_core import Session, get_tier_1_prompt

session = Session(...)
prompt = get_tier_1_prompt(decision)
# Build custom flows
```

---

## Use Cases

### Web Application
```python
@app.post("/api/explore")
def explore(decision: str):
    flow = DiscoveryFlow(llm_provider=AnthropicProvider())
    session, response = flow.start_session(decision)
    
    db.save_session(session.to_dict())
    
    return {
        "session_id": session.session_id,
        "response": response.content,
        "patterns": [p.pattern_name for p in response.patterns]
    }
```

### Slack Bot
```python
@slack.command("/decide")
def decide_command(decision):
    matcher = PatternMatcher()
    patterns = matcher.match(decision)
    
    if patterns:
        return f"I notice a pattern: {patterns[0].pattern_name}"
```

### Jupyter Notebook
```python
from outcomist_core import DiscoveryFlow

flow = DiscoveryFlow(llm_provider=AnthropicProvider())
session, response = flow.start_session("My decision")

# Interactive exploration
```

### Custom CLI Tool
```python
#!/usr/bin/env python3
from outcomist_core import DiscoveryFlow
import sys

flow = DiscoveryFlow(llm_provider=AnthropicProvider())
session, response = flow.start_session(sys.argv[1])
print(response.content)
```

---

## Testing

### Run Tests

```bash
# Pattern extraction validation
python3 test_phase1.py

# Pattern matching tests  
python3 test_phase2.py

# End-to-end flow tests
python3 test_phase3.py

# Real Claude API tests
python3 test_claude_simple.py
```

### Test Coverage

- ✅ Pattern matching: 87.5% accuracy (7/8 tests passing)
- ✅ Question type detection: 80% accuracy (8/10 tests)
- ✅ Context extraction: Financial, emotional, temporal signals
- ✅ Session serialization: Round-trip tested
- ✅ Discovery flow: Complete Tier 1→2 flow
- ✅ LLM integration: Claude API tested

---

## Development

### Project Structure

```
outcomist_core/
├── pattern/
│   ├── types.py       # Pattern, Signal, Question, Pitfall types
│   ├── library.py     # 9 validated patterns
│   └── matcher.py     # PatternMatcher class
├── context/
│   ├── types.py       # DecisionContext, QuestionType types
│   └── analyzer.py    # ContextAnalyzer, QuestionTypeDetector
├── state/
│   └── types.py       # Session, SessionState, Message types
├── prompts/
│   └── library.py     # All prompt templates
├── discovery/
│   ├── types.py       # FlowResponse, FlowStep types
│   └── flow.py        # DiscoveryFlow orchestrator
└── llm/
    ├── types.py       # LLMRequest, LLMResponse types
    ├── provider.py    # BaseLLMProvider, MockLLMProvider
    └── anthropic.py   # AnthropicProvider
```

### Adding a New LLM Provider

```python
from outcomist_core.llm.provider import BaseLLMProvider
from outcomist_core.llm.types import LLMRequest, LLMResponse

class MyLLMProvider:
    def complete(self, request: LLMRequest) -> LLMResponse:
        # Your implementation
        return LLMResponse(content="...", model="my-model")
```

---

## Quality Metrics

| Metric | Score | Notes |
|--------|-------|-------|
| Pattern detection | 87.5% | 7/8 test scenarios correct |
| Question type detection | 80% | 8/10 scenarios correct |
| Tone quality | 9/10 | Conversational consultant style |
| Code coverage | High | Unit + integration tests |
| Production ready | ✅ | Validated with real Claude API |

---

## Comparison with Original

This library is a modular extraction of the proven Outcomist v4.8 command:

| Aspect | Original (explore.md) | Library (outcomist_core) |
|--------|---------------------|------------------------|
| Lines of code | 990 | 130 (CLI) + 36KB (library) |
| Reusability | ❌ None | ✅ Full |
| Maintainability | ⚠️ Hard | ✅ Easy |
| Testability | ⚠️ Manual | ✅ Automated |
| Tone quality | 10/10 | 9/10 |
| Pattern accuracy | ✅ Proven | ✅ 87.5% tested |

---

## Philosophy

**Progressive Disclosure**: Start simple (Tier 1: 30 sec), go deeper only if needed (Tier 2: 10 min, Tier 3: 30 min, Tier 4: 60 min)

**Pattern Recognition**: 9 validated patterns from real usage that reveal what users actually need vs what they ask for

**Executability First**: Only propose solutions that can actually be built within user's constraints ("No floating countertops")

**Quality Over Speed**: Get to proposals quickly, but make them tangible and gap-free

---

## Version History

- **v2.0.0** (2026-01-08) - Initial modular library release
  - Extracted from Outcomist v4.8 (100% regression test pass rate)
  - 9 validated patterns with 87.5% detection accuracy
  - Complete Tier 1→2 discovery flow
  - Improved conversational tone (9/10)
  - Full test suite

---

## License

MIT License - See LICENSE file for details

---

## Credits

**Original Outcomist**: Chris Park ([@cpark4x](https://github.com/cpark4x))  
**Library Architecture**: Modular rebuild for cross-project reusability  
**Patterns**: Captured from 13 real-world test scenarios

---

## Support

- **Issues**: [GitHub Issues](https://github.com/cpark4x/outcomist/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cpark4x/outcomist/discussions)
- **Documentation**: See [main Outcomist repo](https://github.com/cpark4x/outcomist)
