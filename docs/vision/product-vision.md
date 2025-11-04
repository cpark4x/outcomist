# Outcomist Product Vision

**Last Updated**: 2025-11-04

---

## What is Outcomist?

Outcomist is a decision exploration tool that helps people understand what they're really deciding through pattern recognition and progressive discovery.

**Current Status**: Stage 1 (Explore) complete and validated through 5 test scenarios.

---

## The Problem

People frame decisions wrong. They ask:
- "Should I redesign my office?" (when it's really about creating personal sanctuary)
- "Should I take stable client money or bet on my product?" (when fundamentals show the "stable" option is actually risky)
- "Should I build for 10 customers or 2?" (when it's really about product identity crisis)

The surface request hides the real problem. Traditional advice tools either:
1. **Answer the wrong question** - Take the framing at face value and optimize for the wrong thing
2. **Overwhelm with options** - Present endless alternatives without understanding context
3. **Generic platitudes** - "It depends" without actually helping decide

---

## Our Solution

Outcomist uses **progressive disclosure** to:

### 1. **Pattern Recognition** (Tier 1 - 30 seconds)
Identify the deeper pattern beneath the surface request. Reframe the question to reveal the real issue.

**Example**:
- User: "Should I take $6K/month client work or focus on my product?"
- Outcomist: "You're framing this as 'stable money vs bet on product' - but you have $60K savings (12-14 months runway) and your product grew 4X in 6 months with 97% retention. The scarcity is in your head, not your bank account."

### 2. **Discovery Questions** (Tier 2 - 5-10 min)
Ask 4-6 targeted questions that reveal context. One question at a time. Adaptive based on answers.

**Outcome**: Clear recommendation specific to their situation with next actions.

### 3. **Deep Analysis** (Tier 3/4 - Optional)
For complex or high-stakes decisions, offer deeper exploration:
- Tier 3: Alternative approaches, risk analysis, scenario planning (20-30 min)
- Tier 4: Comprehensive analysis with stakeholder mapping, full risk deep dive (45-60 min)

**Key**: Only climb the ladder if complexity warrants it. Don't force every decision through

 all tiers.

---

## The Three-Stage Journey

Outcomist is **Stage 1** of a three-stage journey:

### **Stage 1: Explore** (Current - `/explore`)
**Purpose**: Understand the real problem
**Three scenarios**:
1. **Uncover** - User doesn't know the core problem → Pattern recognition reveals it
2. **Inform** - AI doesn't know the full context → Discovery questions gather it
3. **Challenge** - User thinks they know but wrong → Evidence tests assumptions

**Output**: Understanding + clear recommendation

### **Stage 2: Design** (Future - `/design`)
**Purpose**: Align on what to build before building it
**Process**: Show wireframes, designs, specs, prototypes → Iterate on OUTPUT before execution

**Key insight**: Prevents "building the wrong thing efficiently"

**Output**: Visual/tangible representation of solution that user signs off on

### **Stage 3: Build** (Future - `/build`)
**Purpose**: Execute and track implementation
**Process**: Actually build the thing → Handle blockers → Measure outcomes

**Output**: Working solution

---

## Who Is This For?

### User Types

**1. Confused Decider** (Scenario: Uncover)
- State: "I'm stuck / not sure what to do"
- Need: Pattern recognition to reveal hidden problem
- Example: Office redesign (didn't realize it was about personal sanctuary)

**2. Context-Rich Seeker** (Scenario: Inform)
- State: "I have info but can't synthesize it"
- Need: Discovery to connect the dots
- Example: Cancer prevention (had family history + friend's diagnosis but couldn't see pattern)

**3. Confident but Wrong** (Scenario: Challenge)
- State: "I know what I need: [wrong answer]"
- Need: Evidence-based challenge to false beliefs
- Example: Client vs product (thought needed "stable money" despite strong product fundamentals)

### Decision Domains

- **Personal**: Health, home, relationships, lifestyle
- **Workplace**: Career, job changes, conflict, workload
- **Management**: Team decisions, performance, burnout, advocacy
- **Business**: Features, hiring, revenue, strategy, pivots
- **Product**: Prioritization, positioning, values alignment

---

## Core Principles

### 1. **Progressive Disclosure**
Start simple (30 sec pattern), go deeper only if needed. Ladder, not fork.

### 2. **Honest Evidence**
No invented statistics. Pattern recognition yes, "40% of teams do X" no.

### 3. **Adaptive Questioning**
Questions evolve based on answers. Not a fixed script.

### 4. **One-by-One Discovery**
Ask questions individually, wait for answers. Don't batch.

### 5. **Clear Stance**
"I recommend X" not "here are 7 options, you decide."

---

## Success Metrics (Stage 1)

**Before building Stages 2 & 3, we must hit:**

1. ✅ **5 test scenarios completed** (done)
2. ⏳ **10+ test scenarios validated** (50% complete)
3. ⏳ **Pattern library built** (60% complete - 6 patterns captured)
4. ⏳ **Question quality framework** (documented, needs implementation)
5. ✅ **User validation consistently positive** (every test validated)

**Target**: 10+ scenarios tested, 10+ patterns documented, systematic question framework

---

## What Makes This Different?

**Traditional advice tools**:
- Answer the question as asked (wrong question)
- Present options without understanding context (analysis paralysis)
- Generic advice that could apply to anyone (useless)

**Outcomist**:
- Reveals the real question through pattern recognition
- Builds context through adaptive discovery
- Delivers specific recommendation for YOUR situation
- Honest about evidence basis (no fake stats)
- Time matches stakes (30 sec → 60 min based on complexity)

---

## Current Status

**Shipped**: Stage 1 (Explore) - v4.0
- Command: `/explore`
- Pattern recognition working
- Discovery questions validated
- 5 test scenarios completed
- 6 patterns captured

**Next**: Complete Stage 1 validation
- 5 more test scenarios
- Build out pattern library (10+ patterns)
- Implement question quality framework
- Then ship Stages 2 & 3

---

## Links

- [Three-Stage Journey](./three-stage-journey.md) - Deep dive on explore → design → build
- [User Personas](./user-personas.md) - Who uses Outcomist and for what
- [Pattern Library](../patterns/pattern-library.md) - 6 patterns captured from testing
- [Question Framework](../patterns/question-framework.md) - Question quality heuristics
- [Progressive Disclosure](../principles/progressive-disclosure.md) - Tier 1-4 architecture
