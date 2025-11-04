# Outcomist

**Decision exploration through pattern recognition and progressive discovery**

**Current Status**: Stage 1 (Explore) complete - v4.0 shipped

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

A decision exploration tool that helps you understand what you're REALLY deciding.

People frame decisions wrong:
- "Should I redesign my office?" → Really about creating personal sanctuary
- "Should I take stable money or bet on my product?" → Really about scarcity mindset despite strong fundamentals
- "Should I build for 10 customers or 2?" → Really about product identity crisis

**Outcomist reveals the real question through pattern recognition and adaptive discovery.**

---

## The Three-Stage Journey

Outcomist is Stage 1 of a three-stage decision journey:

### **Stage 1: Explore** (Current - `/explore`)
Understand the real problem through pattern recognition and discovery
- **Uncover**: When you don't know the core problem
- **Inform**: When context needs synthesis
- **Challenge**: When you think you know but you're wrong

**Output**: Understanding + clear recommendation

### **Stage 2: Design** (Future - `/design`)
Align on what to build before building it
- Show wireframes, designs, specs, prototypes
- Iterate on OUTPUT before execution
- Prevents "building the wrong thing efficiently"

**Output**: Visual representation you sign off on

### **Stage 3: Build** (Future - `/build`)
Execute and track implementation
- Actually build the thing
- Handle blockers
- Measure outcomes

**Output**: Working solution

---

## Documentation

### Vision
- [Product Vision](./docs/vision/product-vision.md) - What we're building & why
- [Three-Stage Journey](./docs/vision/three-stage-journey.md) - explore → design → build (coming soon)
- [User Personas](./docs/vision/user-personas.md) - Who this is for (coming soon)

### Patterns & Principles
- [Pattern Library](./docs/patterns/pattern-library.md) - 6 patterns captured from testing
- [Question Framework](./docs/patterns/question-framework.md) - Question quality heuristics
- [Progressive Disclosure](./docs/principles/progressive-disclosure.md) - Tier 1-4 architecture (coming soon)

### Testing
- [Test Scenarios](./test-scenarios.md) - 20 scenarios for validation
- [MUST_HAVES](./MUST_HAVES.md) - Active implementation roadmap

### Archive
- [Test Logs](./archive/test-logs/) - Historical test documentation
- [Changelogs](./archive/changelogs/) - Version history

---

## Current Status (Stage 1)

**Shipped**: v4.0
- ✅ Pattern recognition working
- ✅ Discovery questions validated
- ✅ 5 test scenarios completed
- ✅ 6 patterns captured
- ✅ User validation consistently positive

**Next**: Complete validation
- ⏳ 5 more test scenarios (50% complete)
- ⏳ Pattern library (60% complete - target 10+)
- ⏳ Question framework implementation
- ⏳ Adaptive questioning systematic

**Then**: Build Stages 2 & 3

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

- [Explore Command](.claude/commands/explore-command.md) - Full command specification
- [Pattern Library](./docs/patterns/pattern-library.md) - Decision patterns
- [Question Framework](./docs/patterns/question-framework.md) - Question heuristics
- [Test Logs](./archive/test-logs/) - Detailed test documentation

---

**Version**: 4.0
**Last Updated**: 2025-11-04
