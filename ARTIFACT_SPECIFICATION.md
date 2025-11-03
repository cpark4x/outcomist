# Outcomist Artifact Specification

**Version**: 1.0
**Date**: 2025-11-03
**Purpose**: Define the output artifact Outcomist generates to enable downstream AI tools to achieve user outcomes

---

## Overview

Outcomist generates a single `Brief.md` file that captures everything discovered during the session:
- **Problem understanding** - What they asked vs what they're really asking
- **Context** - Their world, constraints, and history
- **Success criteria** - What winning looks like
- **Principles** - Decision guardrails
- **Recommendation** - What to build/do and why

The brief scales from minimal (Tier 1) to comprehensive (Tier 4) by expanding sections, not adding files.

---

## The Three Core Insights

Outcomist addresses three fundamental challenges:

1. **Users don't know what problem they want to solve**
   → Captured in "Problem" section (evolution from initial to real question)

2. **Users know but can't easily communicate it**
   → Captured through trust-building pattern documented in "Discovery Journey"

3. **AI knows what user wants, but user doesn't trust it**
   → Captured in "Discovery Journey" section (proves understanding through Mirror Back → Pull Out Real Goal → Demonstrate Understanding)

---

## The Single Artifact: Brief.md

**One file. Sections expand as you go deeper.**

```
Brief.md
├── Problem (all tiers)
├── Discovery Journey (Tier 2+)
├── Context (Tier 2+)
├── Success (Tier 2+)
├── Principles (Tier 2+)
├── Recommendation (Tier 2+)
├── Alternatives (Tier 3+)
├── Scenarios (Tier 3+)
└── Implementation (Tier 4+)
```

---

## Progressive Expansion by Tier

| Tier | Time | Sections in Brief.md | Purpose |
|------|------|---------------------|---------|
| **1** | 30 sec | Problem only | Capture pattern recognition |
| **2** | 5-10 min | +Discovery Journey, Context, Success, Principles, Recommendation | Enable basic execution |
| **3** | 20-30 min | +Alternatives, Scenarios | Enable confident implementation |
| **4** | 45-60+ min | +Implementation (constraints, phases) | Enable complex/high-stakes execution |

---

## Brief.md Template

### Tier 1 Version (30 seconds)

```markdown
---
tier: 1
date: [timestamp]
duration: 30 seconds
---

# Decision Brief

## Problem

### What You Asked
[Original question verbatim]

### What You're Really Asking
[Reframed problem - the deeper pattern]

**Why this matters:**
[The pattern identified - what this is really about]

---

**Next step:** Want to explore deeper? This could be a 5-10 minute discovery (Tier 2) or 20-30 minute deep analysis (Tier 3).
```

### Tier 2 Version (5-10 minutes)

```markdown
---
tier: 2
date: [timestamp]
duration: [actual time]
confidence: high/medium/low
---

# Decision Brief

## Problem

### What You Asked
[Original question verbatim]

### What You're Really Asking
[Reframed problem - validated through trust-building]

### Discovery Journey
**Mirror Back:** [How I restated your problem]
- Your correction: [If any]

**Pull Out Real Goal:** [What you revealed about your true motivation]

**Demonstrate Understanding:** [How I showed I got it]

---

## Context

**Your Situation:**
[Current state - what's happening now]

**Key Constraints:**
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

**What Led Here:**
[History - past attempts, failures, successes if relevant]

**Assumptions:**
[What we're taking as given]

---

## Success

### Primary Goal
[The main thing to achieve - measurable]

### Success Looks Like
- [Concrete indicator 1]
- [Concrete indicator 2]
- [Concrete indicator 3]

### Failure Looks Like
- [Anti-pattern 1]
- [Anti-pattern 2]

### How You'll Know It Worked
[Real signals, not fake metrics]

**Timeline:**
- Short-term (days-weeks): [Quick wins]
- Medium-term (months): [Sustained progress]

---

## Principles

### What Matters Most
[Core values - ranked]

### Trade-off Preferences
[When forced to choose between X and Y, prefer...]

### Non-Negotiables
[Hard boundaries - what you won't compromise]

### Acceptable Risks
[What you're willing to tolerate]

---

## Recommendation

### I Recommend: [Specific option]

**Why for YOUR situation:**
- [Reason 1 from your constraints]
- [Reason 2 from your context]
- [Reason 3 from your goals]

**Evidence basis (honest):**
- Pattern: [What I've seen frequently]
- Your signals: [Your specific indicators]
- Confidence: [High/Med/Low] because [reasoning]

**Next actions:**
1. [Specific action from your context]
2. [Specific action from your context]
3. [Specific action from your context]

**Success check (1-2 weeks):** [How you'll know it's working]
```

### Tier 3 Version (20-30 minutes)

Adds these sections:

```markdown
## Trade-offs

### [Tension Name]
**Competing forces:** [Force A] ↔ [Force B]

**Why both matter:** [Explanation]

**Your balance:** [Where you want to be]

---

## Alternatives

### Option 1: [Name]
**What it is:** [Description]

**Strengths:**
- [Pro 1]
- [Pro 2]

**Weaknesses:**
- [Con 1]
- [Con 2]

**Principle alignment:**
- [Principle 1]: ✓ Strong / ~ Partial / ✗ Weak

**Best for:** [Scenarios where this excels]

**Risk:** Low/Medium/High
**Effort:** Low/Medium/High

### Option 2: [Name]
[Same structure]

### Why I Recommend Option X
[Specific reasoning for THEIR case]

### Why NOT the Others
- [Option Y]: [Why it loses for THEIR situation]

---

## Scenarios

### Scenario 1: [Name]

**When this happens:**
[Context]

**Current experience:**
1. [Step 1 - with pain points]
2. [Step 2]
3. [Step 3]

**Desired experience:**
1. [Step 1 - solving the pain]
2. [Step 2]
3. [Step 3]

**Success indicators:**
- [Observable 1]
- [Observable 2]

**Failure modes:**
- [What could go wrong]

### Scenario 2: [Name]
[Same structure]

### Critical Path
[The most important scenarios to nail first]
```

### Tier 4 Version (45-60+ minutes)

Adds this section:

```markdown
## Implementation

### Constraints

**Technical:**
- [Platform limitations, integration requirements, performance]

**Resources:**
- Budget: [Financial boundaries]
- Time: [Timeline boundaries]
- People: [Team capacity]
- Skills: [Capability gaps]

**Organizational:**
- Policies: [Rules to follow]
- Politics: [Sensitivities to navigate]
- Culture: [How things are done here]

**What's negotiable:**
- Hard (cannot change): [List]
- Soft (could change with effort): [List]
- Assumed (could challenge): [List]

### Phased Approach

**Phase 1: [Name]**
- Goal: [What this phase achieves]
- Actions: [Specific steps]
- Success: [Observable outcomes]
- Timeline: [Realistic estimate]
- Decision gate: [What to evaluate before Phase 2]

**Phase 2: [Name]**
[Same structure]

### Risk Analysis

**High-likelihood, medium-impact:**
- [Risk]: Mitigation [Action], Early warning [How you'll detect]

**Medium-likelihood, high-impact:**
[Same structure]

**Low-likelihood, catastrophic:**
[Same structure]

### Evaluation Timeline
- Week 1: [What to check]
- Week 4: [What to check]
- Week 12: [What to check]
```

## Example: Live Test Case (Tier 2)

**Tier:** [1/2/3/4]
**Date:** [timestamp]
**Duration:** [actual time spent]

## Initial Question
[User's original question verbatim]

## Key Reframe
[The deeper pattern identified]

## Trust-Building Steps (Tier 2+)
- **Mirror Back**: [How problem was restated]
- **Pull Out Real Goal**: [What was revealed]
- **Demonstrate Understanding**: [How understanding was proven]

## Discovery Rounds (Tier 2+)
- **Round 1**: [High-level questions asked]
- **Round 2**: [Targeted questions asked]
- **Round 3** (Tier 3+): [Specific questions asked]

## Next Steps
[Recommendation or tier offer]
```

**Why this exists**: AI agents need to know confidence level (Tier 1 quick glance vs Tier 4 comprehensive) to calibrate their own certainty.

---

### `1-understanding/REFRAMING.md` - How the Problem Evolved

**Generated**: Tier 1 (updated at all tiers)
**Purpose**: Preserve discovery journey that builds trust

```markdown
# Problem Reframing

## What You Asked
[Original question verbatim]

## What You're Really Asking
[Reframed problem statement]

## Why This Matters
[The pattern identified - what this is really about]

## How We Got Here (Tier 2+)
[Evolution through Mirror Back → Pull Out Real Goal → Demonstrate Understanding]

## Open Questions (Tier 1)
[Questions that would clarify further - only if still at Tier 1]
```

**Why this exists**: Proves AI understood the user's real intent. Critical for trust ("AI gets what I meant, not just what I said").

**Example from live test**:
- **What You Asked**: "i want an AI knowledge manager to keep track of my daily journals"
- **What You're Really Asking**: "How do I make everything I read and experience compound over time through my journal?"
- **Why This Matters**: Not about storage (knowledge manager), but retrieval and synthesis (learning integration)

---

### `1-understanding/CONTEXT.md` - The User's World

**Generated**: Tier 2
**Purpose**: Environmental constraints for solution proposals

```markdown
# Decision Context

## Situation
[Current state - what's happening now]

## Stakeholders
[Who's affected - roles, not names yet]

## Constraints
[What's fixed - time, resources, policies, technical]

## History
[What led here - past attempts, failures, successes]

## Assumptions
[What we're taking as given]

## Friction Tolerance (if applicable)
[User's willingness to accept complexity/effort]
```

**Why this exists**: AI can't propose viable solutions without understanding the environment. "Seamless or bust" (live test) is a constraint that eliminates entire classes of solutions.

---

### `1-understanding/TENSIONS.md` - Competing Forces

**Generated**: Tier 3
**Purpose**: Navigate trade-offs intelligently

```markdown
# Core Tensions

## Identified Trade-offs

### [Tension Name]
**Competing forces:**
- [Force A] ↔ [Force B]

**Why both matter:**
[Explanation of the tension]

**Current balance:**
[Where things stand now]

**Desired balance:**
[Where you want to be]

## Unresolvable Conflicts
[Where you must choose, can't have both]

## Emerging Patterns
[Themes across multiple tensions]
```

**Why this exists**: Complex decisions involve trade-offs. AI needs to understand these to propose balanced solutions, not optimize for one dimension only.

**Example from live test**:
- **Tension**: Seamless integration ↔ Feature richness
- **User chose**: Seamless (willing to sacrifice features for zero friction)

---

### `2-specification/OUTCOMES.md` - Success Definition

**Generated**: Tier 2
**Purpose**: Execution target - AI knows what "done" means

```markdown
# Success Outcomes

## Primary Goal
[The main thing to achieve - measurable]

## Success Looks Like
- [Concrete indicator 1]
- [Concrete indicator 2]
- [Concrete indicator 3]

## Failure Looks Like
- [Anti-pattern 1]
- [Anti-pattern 2]

## Measurement Approach
[How to know if this worked - real signals, not fake metrics]

## Timeline
- **Short-term** (days-weeks): [Quick wins]
- **Medium-term** (months): [Sustained progress]
- **Long-term** (quarters-years): [Full realization]
```

**Why this exists**: AI needs concrete success criteria. Not "improve knowledge management" but "user journals about RAG implementation, system surfaces 2 related articles from 2 weeks ago."

**Example from live test**:
- **Primary Goal**: Reading compounding over time
- **Success Looks Like**: User makes connections they wouldn't have made manually, articles surface at the right moment
- **Failure Looks Like**: Manual tagging required, user stops journaling due to friction

---

### `2-specification/PRINCIPLES.md` - Decision Guardrails

**Generated**: Tier 2
**Purpose**: AI evaluates options against these

```markdown
# Guiding Principles

## Core Values
[What matters most in this decision - ranked]

## Trade-off Preferences
[When forced to choose between X and Y, prefer...]

## Non-Negotiables
[Hard boundaries - what we won't compromise]

## Acceptable Risks
[What we're willing to tolerate]

## Decision Criteria
[How to evaluate options - weighted factors]
```

**Why this exists**: AI needs guardrails to filter solutions. "Seamless or bust" eliminates solutions that require manual work, even if technically superior.

**Example from live test**:
- **Core Value**: Zero friction
- **Trade-off Preference**: Prefer automatic linking over manual tagging
- **Non-Negotiable**: Must integrate with daily journaling (not separate app)

---

### `2-specification/ALTERNATIVES.md` - Evaluated Options

**Generated**: Tier 3
**Purpose**: AI understands solution space, not just one path

```markdown
# Solution Alternatives

## Option 1: [Name]

**Description:**
[What this approach entails]

**Strengths:**
- [Pro 1]
- [Pro 2]

**Weaknesses:**
- [Con 1]
- [Con 2]

**Principle Alignment:**
- [Principle 1]: ✓ Strong / ~ Partial / ✗ Weak
- [Principle 2]: ...

**Risk Level:** Low / Medium / High
**Effort Level:** Low / Medium / High
**Best For:** [Scenarios where this excels]

## Option 2: [Name]
[Same structure]

## Recommended Approach
[Which option + rationale from discovery]

## Hybrid Possibilities
[Ways to combine elements of multiple options]
```

**Why this exists**: AI can pivot if recommended approach hits blockers. Knowing why other options were rejected prevents repeating failed paths.

**Example from live test**:
- **Option 1**: Manual tagging with Obsidian (rejected: too much friction)
- **Option 2**: Full knowledge graph construction (rejected: over-engineering)
- **Recommended**: AI-powered retrieval during journaling (matches user's "seamless" principle)

---

### `3-execution/ACTORS.md` - Who's Involved

**Generated**: Tier 3
**Purpose**: User personas drive implementation choices

```markdown
# Actors & Perspectives

## Primary Actors

### [Actor Type]
**Role:** [What they do in this context]
**Goals:** [What they want]
**Pain Points:** [What frustrates them]
**Success Criteria:** [What they need to see]
**Influence Level:** High / Medium / Low

## Supporting Actors
[Secondary stakeholders]

## Power Dynamics (Tier 4)
[Who decides, who influences, who implements]

## Alignment Gaps (Tier 4)
[Where actors' goals conflict]
```

**Why this exists**: Implementation must serve real people with real needs. Generic "user" leads to generic solutions.

**Example from live test**:
- **Primary Actor**: Daily journaler who reads across domains (tech, work, personal)
- **Goal**: Compound learning without manual effort
- **Pain Point**: Saves articles but never revisits them
- **Success**: System surfaces relevant articles during journaling

---

### `3-execution/SCENARIOS.md` - Concrete Use Cases

**Generated**: Tier 3
**Purpose**: Concrete examples enable implementation

```markdown
# Key Scenarios

## Scenario 1: [Name]

**Context:**
[When this happens]

**Actor:** [Who's involved]

**Current Experience:**
1. [Step 1 - current state with pain points]
2. [Step 2]
3. [Step 3]

**Desired Experience:**
1. [Step 1 - future state solving pain]
2. [Step 2]
3. [Step 3]

**Success Indicators:**
- [Observable 1]
- [Observable 2]

**Failure Modes:**
- [What could go wrong]

## Scenario 2: [Name]
[Same structure]

## Critical Path
[The most important scenarios to nail first]
```

**Why this exists**: AI needs concrete examples to implement against. "Knowledge manager" is vague. "User journals about RAG challenges, system surfaces 2 related articles from 2 weeks ago with key excerpts" is specific.

**Example from live test**:
- **Scenario**: User journals about RAG implementation challenges
- **Current**: Vaguely remembers reading relevant articles but can't find them
- **Desired**: System auto-suggests "This connects to those 2 RAG articles from 2 weeks ago" + brief synthesis
- **Success**: User engages with suggested articles, journal entry is richer

---

### `3-execution/CONSTRAINTS.md` - Boundaries

**Generated**: Tier 4
**Purpose**: High-stakes decisions need explicit boundaries

```markdown
# Implementation Constraints

## Technical Constraints
[Platform limitations, integration requirements, performance]

## Resource Constraints
- **Budget:** [Financial boundaries]
- **Time:** [Timeline boundaries]
- **People:** [Team capacity]
- **Skills:** [Capability gaps]

## Organizational Constraints
- **Policies:** [Rules to follow]
- **Politics:** [Sensitivities to navigate]
- **Culture:** [How things are done here]

## External Constraints
- **Regulatory:** [Compliance requirements]
- **Market:** [Competitive pressures]
- **Partner:** [Third-party dependencies]

## Constraint Negotiability
- **Hard:** [Cannot change]
- **Soft:** [Could change with effort]
- **Assumed:** [Could challenge if needed]
```

**Why this exists**: Complex/high-stakes decisions have many constraints. Making them explicit prevents AI from proposing solutions that violate boundaries.

---

### `INTEGRATION_GUIDE.md` - Using These Artifacts

**Generated**: Tier 4
**Purpose**: Make artifacts self-documenting for complex cases

```markdown
# How to Use These Artifacts

## For AI Agents

### Planning Agents
- Start with: `1-understanding/` (full context)
- Reference: `2-specification/PRINCIPLES.md` (guardrails)
- Target: `2-specification/OUTCOMES.md` (success criteria)

### Implementation Agents
- Start with: `3-execution/SCENARIOS.md` (concrete cases)
- Reference: `2-specification/ALTERNATIVES.md` (chosen approach)
- Check: `3-execution/CONSTRAINTS.md` (boundaries)

### Evaluation Agents
- Measure: `2-specification/OUTCOMES.md` (success metrics)
- Verify: `2-specification/PRINCIPLES.md` (alignment)
- Consider: `1-understanding/TENSIONS.md` (trade-offs)

## For Humans

### Quick Review
Read: `SESSION.md` → `1-understanding/REFRAMING.md` → `2-specification/OUTCOMES.md`

### Deep Dive
Follow directory order: 1-understanding → 2-specification → 3-execution

### Decision Making
Compare: `2-specification/ALTERNATIVES.md` against `2-specification/PRINCIPLES.md`

## Artifact Dependencies

```
SESSION.md (meta - how we got here)
    ↓
1-understanding/ (why - discovery insights)
    ↓
2-specification/ (what - execution target)
    ↓
3-execution/ (how - implementation guide)
```

## Update Protocol
- New insights → Update `1-understanding/`
- Changed goals → Update `2-specification/`
- Shifted constraints → Update `3-execution/`
- Always update `SESSION.md` with change log
```

**Why this exists**: Complex projects with 11 artifacts benefit from explicit usage guidance. Simple projects (Tier 2) don't need this.

---

## Artifact Contracts (What AI Agents Need)

### For Planning Agents
```
Inputs:
  - 1-understanding/* (full context)
  - 2-specification/OUTCOMES.md (what to achieve)
  - 2-specification/PRINCIPLES.md (decision guardrails)

Outputs:
  - Proposed approach aligned with principles
  - Reasoning for recommendation
```

### For Implementation Agents
```
Inputs:
  - 3-execution/SCENARIOS.md (concrete use cases)
  - 2-specification/ALTERNATIVES.md (chosen approach)
  - 3-execution/CONSTRAINTS.md (boundaries)

Outputs:
  - Working solution that handles concrete scenarios
  - Tests based on success indicators
```

### For Evaluation Agents
```
Inputs:
  - 2-specification/OUTCOMES.md (success criteria)
  - 2-specification/PRINCIPLES.md (alignment check)
  - 1-understanding/TENSIONS.md (trade-offs navigated)

Outputs:
  - Assessment of whether solution achieves outcomes
  - Identification of principle violations
  - Trade-off analysis
```

---

## Design Principles

### 1. Progressive Materialization
**Don't generate everything at once.** Tier 1 creates minimal artifacts, Tier 4 creates comprehensive set. Respects user's time investment.

### 2. Separation of Concerns
**Three-layer structure:**
- `1-understanding/` = Discovery insights (builds trust)
- `2-specification/` = What to achieve (enables planning)
- `3-execution/` = How to implement (enables action)

Mirrors human decision-making: understand → decide → act.

### 3. Modular Composition
**Each artifact is self-contained with clear contract.** Can be read/updated independently. Enables partial changes (update OUTCOMES without rewriting entire brief).

### 4. Executable Insights
**Every artifact answers "what can AI do with this?"** Not documentation for humans, specifications for AI agents.

### 5. Trust Preservation
**Capture the reasoning that builds confidence.** `SESSION.md` + `REFRAMING.md` document the trust-building journey so user knows "AI got what I meant."

---

## Comparison to User's Original Proposal

| User Proposed | Final Architecture | Rationale for Change |
|---------------|-------------------|---------------------|
| problem statement | `1-understanding/REFRAMING.md` | Captures evolution, not just final statement |
| outcomes / success indicators | `2-specification/OUTCOMES.md` | Same, with added measurement approach |
| principles | `2-specification/PRINCIPLES.md` | Same |
| user personas / user stories | `3-execution/ACTORS.md` + `SCENARIOS.md` | Separated concerns: who (actors) vs how they act (scenarios) |
| *(not proposed)* | `1-understanding/CONTEXT.md` | **Added**: AI needs environmental context to propose viable solutions |
| *(not proposed)* | `1-understanding/TENSIONS.md` | **Added**: Trade-offs are critical for intelligent navigation |
| *(not proposed)* | `2-specification/ALTERNATIVES.md` | **Added**: AI needs solution space, not just one recommended path |
| *(not proposed)* | `3-execution/CONSTRAINTS.md` | **Added**: High-stakes decisions need explicit boundaries |
| *(not proposed)* | `SESSION.md` | **Added**: AI needs confidence calibration (Tier 1 vs 4) |
| *(not proposed)* | `INTEGRATION_GUIDE.md` | **Added**: Complex cases benefit from explicit usage guidance |

---

## Success Criteria

These artifacts are successful if:

1. ✅ **Downstream AI can implement solutions** without asking clarifying questions (all context captured)
2. ✅ **Artifacts scale** (Tier 1 minimal, Tier 4 comprehensive) without redundancy
3. ✅ **Each artifact has clear contract** (AI knows what to do with it)
4. ✅ **Human can review at any level** (quick skim or deep dive)
5. ✅ **Discovery insights are preserved** (`SESSION.md` + `REFRAMING.md` capture the journey)
6. ✅ **Ruthlessly simple** (no artifact without clear purpose)

---

## Example: Live Test Case

From `TEST_LOG_NOV3_LIVE.md` - AI knowledge manager request:

### Generated Artifacts (Tier 2)

**`SESSION.md`:**
```markdown
**Tier:** 2 (Discovery)
**Duration:** ~15 minutes
**Initial Question:** "i want an AI knowledge manager..."
**Key Reframe:** "Not 'knowledge manager' but 'learning integration layer'"
```

**`1-understanding/REFRAMING.md`:**
```markdown
**What You Asked:** "AI knowledge manager to keep track of my daily journals"
**What You're Really Asking:** "How do I make everything I read and experience compound over time through my journal?"
**Why This Matters:** Not about storage, but retrieval and synthesis
```

**`1-understanding/CONTEXT.md`:**
```markdown
**Situation:** User journals daily, saves articles to read-later, rarely revisits
**Constraints:** Seamless required (won't use if clunky)
**Friction Tolerance:** Willing to accept some friction, but prefers automation
```

**`2-specification/OUTCOMES.md`:**
```markdown
**Primary Goal:** Reading compounding over time
**Success Looks Like:**
- Makes connections I wouldn't have made manually
- Articles surface at the right moment
- Journal entries are richer because of article integration
```

**`2-specification/PRINCIPLES.md`:**
```markdown
**Core Values:** Zero friction, automatic synthesis
**Trade-off Preference:** Automatic linking over manual tagging
**Non-Negotiable:** Must integrate with daily journaling (not separate app)
```

### What Implementation Agent Can Do

With these 5 artifacts, an implementation agent can:
- ✅ Understand real problem (learning integration, not knowledge base)
- ✅ Know success criteria (connections surfaced during journaling)
- ✅ Respect constraints (seamless integration required)
- ✅ Build correct solution (AI-powered retrieval, not manual tagging)

**Result**: Engineer can take `DISCOVERY_SESSION_NOV3.md` + these artifacts and implement the right solution.

---

## Next Steps

1. **Update `brief-command.md`** to generate these artifacts instead of monolithic Brief.md
2. **Create artifact templates** for each tier (Tier 1, Tier 2, Tier 3, Tier 4)
3. **Test with real scenarios** from `test-scenarios.md`
4. **Validate AI agent consumption** - can downstream tools actually use these?
5. **Iterate based on usage** - do any artifacts prove unnecessary or insufficient?

---

**Document Status**: Ready for implementation
**Validation**: Passed against Outcomist v3.4 test case and amplifier principles
**Confidence**: High - architecture addresses user's stated goals and preserves Outcomist's trust-building approach
