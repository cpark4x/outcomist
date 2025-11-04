# Outcomist Artifact Specification (3-File Structure)

**Version**: 1.0
**Date**: 2025-11-03
**Purpose**: Define output artifacts Outcomist generates to enable downstream AI tools to achieve user outcomes

---

## Overview

Outcomist generates **3 files** that capture everything discovered:

1. **SESSION.md** - Meta (how we got here)
2. **UNDERSTANDING.md** - Discovery insights (problem, context, tensions)
3. **SPECIFICATION.md** - Execution-ready (outcomes, principles, recommendation)

Files expand progressively from Tier 1 (minimal) to Tier 4 (comprehensive).

---

## The Three Core Insights

Outcomist addresses three fundamental challenges:

1. **Users don't know what problem they want to solve**
   → Captured in UNDERSTANDING.md (evolution from initial to real question)

2. **Users know but can't easily communicate it**
   → Captured through trust-building pattern in SESSION.md + UNDERSTANDING.md

3. **AI knows what user wants, but user doesn't trust it**
   → Captured in SESSION.md (documents trust-building journey)

---

## The 3-File Structure

```
outcomist-output/
├── SESSION.md           # Meta: Discovery session log
├── UNDERSTANDING.md     # Why: Problem + context + tensions
└── SPECIFICATION.md     # What + How: Outcomes + principles + recommendation
```

---

## Progressive Generation by Tier

| Tier | Time | Files Generated | What Expands |
|------|------|----------------|--------------|
| **1** | 30 sec | SESSION + UNDERSTANDING (minimal) | Just problem reframe |
| **2** | 5-10 min | All 3 files (core sections) | Context, outcomes, principles, recommendation |
| **3** | 20-30 min | All 3 files (expanded) | Add tensions, alternatives, scenarios |
| **4** | 45-60+ min | All 3 files (comprehensive) | Add constraints, implementation phases |

---

## File Templates

### SESSION.md

**Generated**: Tier 1 (updated at all tiers)
**Purpose**: Track progression and confidence level

```markdown
---
tier: [1/2/3/4]
date: [timestamp]
duration: [actual time spent]
confidence: [high/medium/low] (Tier 2+)
---

# Outcomist Session

## Initial Question
[User's original question verbatim]

## Key Reframe
[The deeper pattern identified]

## Trust-Building Journey (Tier 2+)

**Mirror Back:**
[How I restated their problem]
- User's correction: [If any]

**Pull Out Real Goal:**
[What they revealed about true motivation]

**Demonstrate Understanding:**
[How I showed I got it before asking questions]

## Discovery Questions (Tier 2+)

**Round 1:** [2-3 high-level questions asked]
- Analysis: [30-50 word synthesis]

**Round 2:** [2-3 targeted questions asked]
- Analysis: [30-50 word synthesis]

**Round 3 (Tier 3+):** [3 specific questions asked]

## Outcome
[Recommendation delivered / Tier offered / Session type]
```

---

### UNDERSTANDING.md

**Generated**: Tier 1 (expanded at Tier 2+)
**Purpose**: Preserve discovery insights that build trust

#### Tier 1 Version

```markdown
# Problem Understanding

## What You Asked
[Original question verbatim]

## What You're Really Asking
[Reframed problem - the deeper pattern]

**Why this matters:**
[The pattern identified - what this is really about]

---

**Next step:** Want to explore deeper? (5-10 min Tier 2 or 20-30 min Tier 3)
```

#### Tier 2+ Version (adds these sections)

```markdown
# Problem Understanding

## What You Asked
[Original question verbatim]

## What You're Really Asking
[Reframed problem - validated through trust-building]

**How we got here:**
[Evolution through Mirror Back → Pull Out Real Goal → Demonstrate Understanding]

---

## Your World

**Situation:**
[Current state - what's happening now]

**Key Constraints:**
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

**What Led Here:**
[History - past attempts, failures, successes if relevant]

**Assumptions:**
[What we're taking as given]

**Friction Tolerance:** (if applicable)
[User's willingness to accept complexity/effort]
```

#### Tier 3+ Version (adds this section)

```markdown
## Trade-offs

### [Tension Name]
**Competing forces:** [Force A] ↔ [Force B]

**Why both matter:** [Explanation]

**Your desired balance:** [Where you want to be]

### [Tension Name 2]
[Same structure]

## Emerging Patterns
[Themes across multiple tensions]
```

---

### SPECIFICATION.md

**Generated**: Tier 2
**Purpose**: Everything needed for AI implementation

#### Tier 2 Version

```markdown
---
tier: 2
confidence: [high/medium/low]
---

# Solution Specification

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

#### Tier 3 Version (adds these sections)

```markdown
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

## Who's Involved

### [Actor Type]
**Role:** [What they do in this context]
**Goals:** [What they want]
**Pain Points:** [What frustrates them]
**Success Criteria:** [What they need to see]

---

## Key Scenarios

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

#### Tier 4 Version (adds this section)

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

---

### Phased Approach

**Phase 1: [Name]**
- Goal: [What this phase achieves]
- Actions: [Specific steps]
- Success: [Observable outcomes]
- Timeline: [Realistic estimate]
- Decision gate: [What to evaluate before Phase 2]

**Phase 2: [Name]**
[Same structure]

---

### Risk Analysis

**High-likelihood, medium-impact:**
- [Risk]: Mitigation [Action], Early warning [How you'll detect]

**Medium-likelihood, high-impact:**
[Same structure]

**Low-likelihood, catastrophic:**
[Same structure]

---

### Evaluation Timeline
- Week 1: [What to check]
- Week 4: [What to check]
- Week 12: [What to check]
```

---

## Example: Live Test Case (Tier 2)

From `TEST_LOG_NOV3_LIVE.md` - AI knowledge manager request:

### SESSION.md
```markdown
---
tier: 2
date: 2025-11-03
duration: 15 minutes
confidence: high
---

# Outcomist Session

## Initial Question
"i want an AI knowledge manager to keep track of my daily journals. i often read tech blogs and i want to keep them so that i can go back to it when i need to. and is tied to my daily journal. i can look back at my journal and leverage the learnings over time."

## Key Reframe
"Not 'knowledge manager' but 'learning integration layer' - the problem is making reading compound over time through journaling, not storage."

## Trust-Building Journey

**Mirror Back:**
"You want a system that connects your tech reading to your daily practice. Not just 'save articles somewhere' but actually tie what you're learning to what you're doing."

- User's correction: "not just for tech reading. for everything in my life."

**Pull Out Real Goal:**
"What are you *actually* trying to accomplish here?"

- User revealed: "1 and 3 only. 1. reading compounding over time, 3. cross-domain pattern recognition"

**Demonstrate Understanding:**
"Ah! So this is really about learning integration across your entire life, not just tech articles."

## Discovery Questions

**Round 1:**
1. Journaling style? → Daily structured format
2. Article handling? → Save to read-later, rarely revisit
3. Recall problem when? → Designing systems, tech conversations

**Round 2:**
4. What would correlation look like? → Auto-suggest + synthesis
5. Cross-domain example? → (Haven't experienced yet)
6. Friction tolerance? → Seamless or bust

## Outcome
Recommended: AI-powered learning integration layer (12 lines)
Offered: Generate full brief document
```

### UNDERSTANDING.md
```markdown
# Problem Understanding

## What You Asked
"i want an AI knowledge manager to keep track of my daily journals"

## What You're Really Asking
"How do I make everything I read and experience compound over time through my journal?"

**How we got here:**
Initial ask: AI knowledge manager for tech blogs + journals
→ Correction: Not just tech, everything in life
→ Real goal revealed: Reading compounding + cross-domain patterns
→ Core problem: Learning integration, not storage

---

## Your World

**Situation:**
- Journal daily with structured format (mix of work + personal thoughts)
- Save articles to read-later app (Pocket/Instapaper-like)
- Rarely revisit saved articles
- Recall problem hits when designing systems or having tech conversations

**Key Constraints:**
- **Seamless required** - Won't use if clunky
- Must integrate with daily journaling (not separate app)
- Automatic linking preferred over manual tagging

**Assumptions:**
- User journals consistently (daily practice established)
- Articles are saved digitally (can be accessed programmatically)
- Cross-domain reading spans: tech, work, personal
```

### SPECIFICATION.md
```markdown
---
tier: 2
confidence: high
---

# Solution Specification

## Success

### Primary Goal
Make reading compound over time through daily journaling

### Success Looks Like
- User makes connections they wouldn't have made manually
- Articles surface at the right moment (during journaling)
- Journal entries are richer because of article integration

### Failure Looks Like
- Manual tagging required
- User stops journaling due to friction
- System becomes another "save and forget" tool

### How You'll Know It Worked
**Real signals:**
- User engages with suggested articles during journaling
- Cross-domain connections emerge (tech article → personal reflection)
- User can recall relevant reading when needed

**Timeline:**
- Short-term (days): System suggests articles during journaling
- Medium-term (months): User builds richer journal entries, sees patterns

---

## Principles

### What Matters Most
1. Zero friction (seamless integration)
2. Automatic synthesis (no manual work)
3. Cross-domain pattern recognition

### Trade-off Preferences
- Automatic linking > Manual tagging
- Seamless integration > Feature richness
- Retrieval during journaling > Comprehensive knowledge base

### Non-Negotiables
- Must integrate with daily journaling (not separate app)
- Seamless or bust (won't use if clunky)

### Acceptable Risks
- Willing to accept some friction if necessary
- Start minimal (journal + articles only, not full knowledge manager)

---

## Recommendation

### I Recommend: AI-Powered Learning Integration Layer

**Why for YOUR situation:**
- Matches your "seamless or bust" principle
- Focuses on retrieval (your pain point) not storage (already solved)
- Enables cross-domain pattern recognition automatically

**Evidence basis (honest):**
- Pattern: Daily journalers + saved articles = retrieval problem, not storage
- Your signals: "Rarely revisit saved articles" + "Can't remember that perfect article"
- Confidence: High - Clear problem-solution fit

**Next actions:**
1. Choose journal integration point (Obsidian plugin? VS Code? Web app?)
2. Prototype semantic similarity matching (embeddings-based retrieval)
3. Test with current journal entries + saved articles
4. Measure: Do surfaced articles actually get engaged with?

**Success check (1-2 weeks):**
- System surfaces relevant articles during journaling
- User engages with at least 30% of suggestions
- Journal entries reference integrated articles
```

---

## AI Agent Contracts

### For Planning Agents
```
Read:
- SESSION.md → Understand confidence level and discovery depth
- UNDERSTANDING.md → Full context and constraints
- SPECIFICATION.md (Success + Principles) → Target and guardrails

Output:
- Proposed approach aligned with principles
```

### For Implementation Agents
```
Read:
- UNDERSTANDING.md (Your World) → Environmental constraints
- SPECIFICATION.md (Scenarios + Recommendation) → What to build
- SPECIFICATION.md (Constraints - Tier 4) → Boundaries

Output:
- Working solution that handles concrete scenarios
```

### For Evaluation Agents
```
Read:
- SPECIFICATION.md (Success) → What to measure
- SPECIFICATION.md (Principles) → Alignment check
- UNDERSTANDING.md (Trade-offs - Tier 3) → Expected compromises

Output:
- Assessment of whether solution achieves outcomes
```

---

## Design Decisions

### Why 3 Files?

**SESSION.md** = Meta
- AI agents need confidence calibration (Tier 1 vs Tier 4)
- Trust-building journey preservation

**UNDERSTANDING.md** = Discovery
- Proves AI understood the real problem
- Provides environmental context for solutions
- Captures trade-offs that constrain design

**SPECIFICATION.md** = Execution
- Everything AI needs to implement
- Clear success criteria
- Decision guardrails

### Why Not More Files?

**Avoided:**
- Separate files for: Outcomes, Principles, Alternatives, Scenarios, Constraints
- Would create 11 files with high drift risk

**Trade-off made:**
- Slightly less modular (can't update just "outcomes" without touching file)
- But: Much simpler, single source of truth per concern

### Why Not Fewer Files (Single Brief.md)?

**Considered** but rejected because:
- SESSION.md is pure meta (agents might not need it)
- UNDERSTANDING.md is discovery-focused (different consumers than SPECIFICATION.md)
- Clear separation: Why (understanding) vs What (specification)

---

## Success Criteria

These artifacts are successful if:

1. ✅ **Downstream AI can implement** without asking clarifying questions
2. ✅ **Files are independent** - can read SPECIFICATION.md without UNDERSTANDING.md if context known
3. ✅ **Drift is manageable** - updating one concern doesn't require touching multiple files
4. ✅ **Human-reviewable** - can skim SESSION.md → UNDERSTANDING.md → SPECIFICATION.md in 2 minutes
5. ✅ **Scales progressively** - Tier 1 minimal, Tier 4 comprehensive
6. ✅ **Ruthlessly simple** - 3 files with clear purpose

---

## Next Steps

1. Update `brief-command.md` to generate these 3 files
2. Test with one scenario from `test-scenarios.md`
3. Validate: Can implementation agent use SPECIFICATION.md to build solution?
4. Measure: What questions does AI still ask after reading artifacts?
5. Iterate based on gaps found

---

**Status**: Ready for implementation
**Confidence**: High - balances simplicity with utility
