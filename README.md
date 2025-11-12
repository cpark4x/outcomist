# Outcomist

**AI drives activity, not outcomes. Outcomist helps you figure out what you actually want before taking action.**

**Current Status**: Epic 1 (Deep Discovery) validated - v4.8 shipped | Epic 2-3 design in progress

---

## The Problem

People ask AI to do things, but they often don't know:
1. What they actually want (the real outcome)
2. How to articulate it clearly enough for AI to help
3. Whether what they're asking for will achieve the outcome

The result? Lots of activity, but not the outcomes they're seeking.

---

## Quick Start

```
/explore [your decision]
```

**Example**:
```
/explore Should I take this $6K/month client work or focus on my product?
```

Outcomist will:
1. **Recognize the pattern** - Reveal what's really being decided (30 sec)
2. **Ask targeted questions** - Build context one question at a time (5-10 min)
3. **Deliver clear recommendation** - Specific to YOUR situation with next actions

---

## What is Outcomist?

A decision exploration tool that helps you understand what you actually want before taking action. It asks the right questions to surface what matters, so you can make decisions that lead to real outcomes.

People frame decisions wrong:
- "Should I redesign my office?" → Really about creating personal sanctuary
- "Should I take stable money or bet on my product?" → Really about scarcity mindset despite strong fundamentals
- "Should I build for 10 customers or 2?" → Really about product identity crisis

**Outcomist reveals the real question through pattern recognition and adaptive discovery.**

---

## The Three-Epic Journey

Outcomist guides users through three progressive epics. See [Product Vision v2](docs/vision/product-vision-v2.md) for complete details.

### **Epic 1: Deep Discovery** (✅ Validated)
One continuous discovery process combining pattern recognition, questions, and optional deep analysis. Validates AI can execute within user's constraints.
**Output**: Executable proposal

### **Epic 2: Proposal Review** (⏳ Proposed)
User reviews tangible, high-quality proposal with working prototypes or complete artifacts. Iterative refinement until validated.
**Output**: "This is exactly what I want"

### **Epic 3: Build & Track** (⏳ Proposed - Optional)
Execute validated proposal, track progress, handle blockers, measure outcomes.
**Output**: Done + learned

**Key insight**: Users want to reach Epic 2 (proposal review) as quickly as possible. Epic 1 exists to make Epic 2 proposals high-quality, executable, and gap-free.

---

## Repository Structure

```
/docs/                    # All documentation
  /architecture/          # System design & technical specs
  /patterns/              # Decision patterns & question framework
  /testing/               # Test scenarios & results (regression tests)
  /design/                # Version improvements & tone refinements
  /vision/                # Product vision & roadmap

/outcomist_web/           # Web implementation (Reflex)
/outcomist_shared/        # Shared prompt library (used by CLI & web)
/archive/                 # Historical artifacts & test logs
/tests/                   # Test scripts
/.claude/                 # CLI commands (/explore)
```

## Documentation

### Core Documentation
- [Product Vision v2](./docs/vision/product-vision-v2.md) - What we're building & why (3-epic model)
- [End-to-End Flow](./docs/vision/end-to-end-flow.md) - Complete user journey through all epics
- [Epic 1: Deep Discovery](./docs/epics/epic-1-deep-discovery.md) - Pattern recognition + discovery process
- [Epic 2: Proposal Review](./docs/epics/epic-2-proposal-review.md) - Proposal validation & refinement
- [Epic 3: Build & Track](./docs/epics/epic-3-build-track.md) - Optional execution support
- [Pattern Library](./docs/patterns/pattern-library.md) - 9 patterns captured from 13 tests
- [Question Framework](./docs/patterns/question-framework.md) - Question quality heuristics

### Testing & Validation
- [Test Scenarios](./docs/testing/test-scenarios.md) - Single source of truth (13 tests)
- [Test Results](./docs/testing/results/) - Version-specific outcomes
- [Test Status](./docs/testing/results/STATUS.md) - Documentation progress

### Archive
- [Test Logs](./archive/test-logs/) - Historical raw test logs
- [Changelogs](./archive/changelogs/) - Version history
- [Work Artifacts](./archive/work-artifacts/) - Implementation attempts

---

## Current Status (Epic 1)

**Shipped**: v4.8 (January 2025)
- ✅ Product Vision v2 alignment - 3-epic model validated
- ✅ Context-adaptive response system (3 response types)
- ✅ Question type detection (information/execution/decision routing)
- ✅ Trade-off discovery mechanism with factual validation
- ✅ Pattern recognition working (9 patterns captured)
- ✅ Discovery questions validated (10 regression tests + 4 sample tests)
- ✅ Progressive disclosure architecture (Tier 1-4)
- ✅ Context inference guidelines
- ✅ Collaborative partnership tone
- ✅ UX improvements: numbered lists, discovery transparency, question pacing

**Test Results**: 100% pass rate (10/10 regression tests)
- See [v4.8 Full Regression Test](docs/testing/results/v4.8-full-regression-test.md) for complete results
- See [v4.8 Prompt Alignment Test](docs/testing/results/v4.8-prompt-alignment-test.md) for Product Vision v2 validation

**Next**: Build Epic 2 & 3
- ⏳ Epic 2: Proposal Review (tangible, high-quality proposals)
- ⏳ Epic 3: Build & Track (optional execution support)

---

## Examples

### Office Redesign
**User**: "I want to redesign my office to make it more inspiring for work"
**Outcomist**: Revealed real need was personal sanctuary with games, memorabilia, retreat space - not work optimization

### Client vs Product
**User**: "Should I take $6K/month client work or focus on my $2K MRR product?"
**Outcomist**: Revealed $60K savings (12-14 months runway), product 4X growth, 97% retention. "Stable client" was $40/hour distraction. Recommended: Say no, go ALL IN on product.

### Feature Decision
**User**: "10 customers want Feature X, 2 customers want Feature Y. Which should I build?"
**Outcomist**: Revealed product identity crisis - Feature X (workplace presence) serves employers for RTO, Feature Y (exclude list) serves employee safety. Can't be both. Recommended: Build Feature Y, clarify who you're building for.

---

## How It Works

### Tier 1: Pattern Recognition (30 seconds)
Identify deeper pattern, reframe the question

**Example**:
> You're framing this as "stable money vs bet on product" - but you have 12-14 months runway and your product grew 4X in 6 months with 97% retention. The scarcity is in your head, not your bank account.

### Tier 2: Discovery (5-10 minutes)
Ask 4-6 targeted questions, deliver specific recommendation

**Questions adapt based on answers** - not a fixed script

### Tier 3 & 4: Deep Analysis (Optional)
For complex/high-stakes decisions, climb the ladder:
- Tier 3: Alternatives, risk analysis, scenarios (20-30 min)
- Tier 4: Comprehensive with stakeholder mapping (45-60 min)

**Key**: Only go deeper if complexity warrants it

---

## Core Principles

1. **Progressive Disclosure**: Start simple (30 sec), go deeper only if needed
2. **Honest Evidence**: Pattern recognition yes, invented statistics no
3. **Adaptive Questioning**: Questions evolve based on answers
4. **Clear Stance**: "I recommend X" not "here are 7 options"
5. **One-by-One**: Ask questions individually, wait for answers

---

## Development Setup

### Local Development

This project lives inside the [amplifier repository](https://github.com/cpark4x/amplifier) and has direct access to amplifier tools.

### GitHub Codespaces

1. Open this repository in GitHub
2. Click "Code" → "Codespaces" → "Create codespace"
3. The devcontainer automatically initializes the amplifier submodule

---

## Links

- [Explore Command](.claude/commands/explore.md) - Full command specification
- [Pattern Library](./docs/patterns/pattern-library.md) - Decision patterns
- [Question Framework](./docs/patterns/question-framework.md) - Question heuristics
- [Test Scenarios](./docs/testing/test-scenarios.md) - All test scenarios
- [Test Results](./docs/testing/results/) - Version-specific test results

---

**Version**: 4.8 (shipped January 2025)
**Last Updated**: 2025-01-10

---

## Recent Improvements (v4.6 - v4.8)

### v4.8 (January 2025)
- **Product Vision v2 Alignment**: Consolidated to 3-epic model (Epic 1: Deep Discovery, Epic 2: Proposal Review, Epic 3: Build & Track)
- **Context-Adaptive Response System**: Three response types based on user needs (Direct Engagement, Gentle Observation, Clarifying Questions)
- **UX Improvements**: Comprehensive numbered lists, discovery structure transparency, question pacing (1-2 questions max per round)
- **100% Test Pass Rate**: All 10 regression tests + 4 sample tests passed

### v4.7 (January 2025)
- **Question Type Detection**: Routes information requests, execution requests, and decision questions appropriately
- **Improved Bedside Manner**: Immediate research for information requests (no meta-questions)
- **Execution Request Handling**: Minimal discovery, fast path to practical output

### v4.6 (January 2025)
- **Trade-off Discovery Mechanism**: Reveals actual priorities through concrete choices
- **Factual Validation**: Research before presenting trade-offs to ensure accuracy
- **Revealed Preference Guidance**: Choice behavior > stated preferences
