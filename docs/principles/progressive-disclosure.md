# Progressive Disclosure

**Last Updated**: 2025-11-04
**Status**: Core principle of Outcomist architecture

---

## What is Progressive Disclosure?

Progressive disclosure is a design principle where complexity is revealed gradually based on need, rather than presented all at once.

For Outcomist, this means:
- **Start simple** (30 seconds of pattern recognition)
- **Go deeper only if needed** (5-10 min discovery, 20-30 min analysis, 45-60 min comprehensive)
- **Let stakes drive depth** (simple decisions stay simple, complex decisions get appropriate depth)

---

## The Four-Tier Architecture

### Tier 1: Pattern Recognition (30 seconds)
**Purpose**: Immediate value through pattern recognition

**Structure**:
```
[PARAGRAPH 1: PATTERN + REFRAME]
- Identify deeper pattern (30-50 words)
- Reframe question to reveal real issue
- Reference user's specific words

[PARAGRAPH 2: CREATE HUNGER - OPTIONAL]
- Hint at deeper complexity without solving it
- Show there's more to discover

[CALL TO ACTION]
Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand:
• [Specific question preview]
• [Specific question preview]
• [Specific question preview]
• [Specific question preview]

Ready to explore?

(If you already have a sense of your answer, tell me and I'll validate it)
```

**Maximum**: 150 words total

**Example**:
> You're framing this as "stable money vs bet on product" - but that's not the real question.
>
> The real question is: "Am I choosing safety because I'm afraid to commit to the thing I actually want?"
>
> Your product went from $500 → $2,000 MRR in 6 months (4X growth), 97% retention. That's CRUSHING IT. But you're considering $40/hour client work because "market is tough." The scarcity is in your head, not your bank account.
>
> Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand:
> • Why this client opportunity is happening RIGHT NOW
> • What "$2K MRR growing" actually means (how fast, how sustainable)
> • Your financial runway (can you afford to say no to $6K?)
> • What happens to the product if you pause
>
> Ready to explore?

---

### Tier 2: Discovery (5-10 minutes)
**Purpose**: Build context through structured inquiry, deliver specific recommendation

**Structure**:
```
[ROUND 1: 2-3 HIGH-LEVEL QUESTIONS]
Get the landscape, understand constraints
One question at a time, wait for answer

↓

[QUICK ANALYSIS: 30-50 words]
Show you're listening, surface patterns

↓

[ROUND 2: 2-3 TARGETED QUESTIONS]
Dig into what matters based on Round 1
Adapt questions based on answers

↓

[DELIVER RECOMMENDATION]
Clear stance with reasoning
Specific to THEIR situation
Include next actions
```

**Total**: 4-6 questions across 2 rounds

**After recommendation**, offer Tier 3:
> This recommendation is based on what you've told me so far.
>
> Want to go deeper? I can spend another 20-30 minutes on:
> • Alternative approaches compared side-by-side
> • Risk analysis and mitigation strategies
> • Scenario planning (what if X happens?)
> • Implementation roadmap with decision gates
>
> Need that depth, or is this enough to move forward?

---

### Tier 3: Analysis (20-30 minutes)
**Purpose**: Deep exploration of alternatives, tradeoffs, second-order effects

**When to use**:
- User requests deeper analysis from Tier 2
- Discovery reveals high complexity during Tier 2
- High stakes detected ($50K+, team changes, migrations)

**Structure**:
```
[ROUND 1: 3 HIGH-LEVEL QUESTIONS]
[DEEP ANALYSIS: 50-80 words]

[ROUND 2: 3 TARGETED QUESTIONS]
[DEEP ANALYSIS: 50-80 words]

[ROUND 3: 3 SPECIFIC QUESTIONS]
[COMPREHENSIVE RECOMMENDATION]
```

**Total**: 9 questions across 3 rounds

**After recommendation**, offer Tier 4 if appropriate:
> This covers the major factors and alternatives.
>
> For major organizational decisions, I can go even deeper with:
> • Complete stakeholder mapping
> • Scenario modeling (6-12 month outcomes)
> • Systematic tradeoff matrix
> • Full risk analysis with cascading effects
> • Phased implementation with decision gates
> • Contingency planning
>
> This is Tier 4 - reserved for decisions affecting multiple teams, irreversible choices, or budgets >$50K. Need that level, or is this comprehensive enough?

---

### Tier 4: Comprehensive (45-60+ minutes)
**Purpose**: Exhaustive exploration for high-stakes, irreversible decisions

**When to use**:
- Major organizational change (restructuring, tech stack replacement)
- Significant budget ($50K+)
- Irreversible decisions (data migration, vendor lock-in)
- User explicitly requests "comprehensive" or "exhaustive"
- Tier 3 reveals even deeper complexity

**Structure**: Full analysis with:
- Complete stakeholder mapping
- Scenario modeling (6-12 month outcomes)
- Systematic tradeoff matrix
- Full risk analysis with cascading effects
- Phased implementation with decision gates
- Contingency planning

---

## The Ladder, Not a Fork

**CRITICAL**: Progressive disclosure is a ladder you climb, not a fork in the road.

**Bad approach (fork)**:
```
"Do you want:
1) Quick answer (2 min)
2) Discovery session (10 min)
3) Deep analysis (30 min)"
```

**Good approach (ladder)**:
```
[Always start with Tier 1 - 30 seconds]
↓
[Offer Tier 2 as default next step]
↓
[After Tier 2, offer Tier 3 if complexity warrants]
↓
[After Tier 3, offer Tier 4 if stakes justify]
```

**Why ladder beats fork**:
- No decision paralysis at the start
- Every user gets immediate value (Tier 1)
- Depth emerges naturally based on need
- Time investment matches stakes
- Users climb as far as they need, then stop

---

## Time Investment Matches Stakes

### Simple decisions stay simple
**Example**: "Should I use React or Vue for this side project?"
- Tier 1: Pattern recognition (30 sec) - "You're asking about frameworks, but real question is time-to-ship vs learning investment"
- Tier 2: 4-5 questions, recommendation (5-10 min)
- Done. ✅

### Complex decisions get appropriate depth
**Example**: "Should we migrate our monolith to microservices?"
- Tier 1: Pattern recognition (30 sec)
- Tier 2: Discovery (10 min)
- Tier 3: Deep analysis (30 min) - alternatives, tradeoffs, risks
- Tier 4: Comprehensive (60 min) - stakeholder mapping, phased implementation, contingency plans
- Done. ✅

**Key**: You don't MAKE decisions complex by forcing them through all tiers. The decision's inherent complexity determines how far up the ladder you go.

---

## How Tiers Connect

### Tier 1 → Tier 2 (default)
**Always offer Tier 2** after Tier 1 unless user declines

**Transition**:
> Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand:
> • [Preview actual questions]
> • [Preview actual questions]
>
> Ready to explore?

### Tier 2 → Tier 3 (if complexity warrants)
**Offer Tier 3** after delivering Tier 2 recommendation if:
- High stakes detected during discovery
- Multiple valid alternatives emerged
- User requests deeper analysis

**Transition**:
> This recommendation is based on what you've told me so far.
>
> Want to go deeper? I can spend another 20-30 minutes on:
> • [Specific value of Tier 3]
>
> Need that depth, or is this enough to move forward?

### Tier 3 → Tier 4 (if stakes justify)
**Offer Tier 4** after Tier 3 only if:
- Major organizational change
- Significant budget ($50K+)
- Irreversible decisions
- User explicitly requests exhaustive analysis

**Transition**:
> This covers the major factors and alternatives.
>
> For major organizational decisions, I can go even deeper with:
> • [Specific value of Tier 4]
>
> This is Tier 4 - reserved for decisions affecting multiple teams, irreversible choices, or budgets >$50K. Need that level, or is this comprehensive enough?

---

## Exit Points

Users can exit at any tier:

**From Tier 1**:
- User says "no thanks" → Done (Tier 1 delivered value)
- User validates their thinking → Quick validation, offer Tier 2, done if they decline
- User asks specific question → Answer, offer Tier 2, done if they decline

**From Tier 2**:
- Recommendation accepted → Done
- User wants deeper analysis → Proceed to Tier 3
- User explores specific alternative within Tier 2 scope → Answer, done

**From Tier 3**:
- Comprehensive recommendation accepted → Done
- User needs exhaustive analysis → Proceed to Tier 4
- User satisfied with depth → Done

**From Tier 4**:
- Exhaustive analysis complete → Done

**Key**: Every tier delivers value. Exiting at any tier is success, not failure.

---

## Benefits of Progressive Disclosure

### For Simple Decisions
- **Fast**: 30 seconds to insight
- **Low commitment**: Can exit after Tier 1
- **No overhead**: Don't pay for depth you don't need

### For Complex Decisions
- **Graduated investment**: Build understanding progressively
- **Natural depth**: Complexity emerges, isn't imposed
- **Appropriate rigor**: Stakes determine depth

### For All Users
- **Immediate value**: Tier 1 always delivers
- **No decision paralysis**: Don't choose depth upfront
- **Time matches stakes**: Simple stays simple, complex gets depth
- **Clear exit points**: Stop when you have what you need

---

## Anti-Patterns to Avoid

### ❌ Forcing every decision through all tiers
Simple decisions don't need 60 minutes of analysis.

### ❌ Offering Tier 3 from Tier 1
Too premature. User doesn't know if they need depth yet.

### ❌ Skipping Tier 1
Every user gets pattern recognition first. No exceptions.

### ❌ Making it a fork instead of a ladder
Don't ask "Which tier do you want?" Start Tier 1, climb as needed.

### ❌ Creating tier paralysis
If you're unsure whether to offer next tier, err toward NOT offering unless clear signals.

---

## Design Inspiration

Progressive disclosure is inspired by:

**Zen philosophy**: Start simple, reveal complexity only when needed

**Wabi-sabi**: Embrace the essential, discard the unnecessary

**Information architecture**: Don't overwhelm users with everything at once

**Game design**: Tutorial → basic → intermediate → advanced (natural progression)

**Teaching**: Start with intuition, add rigor progressively

---

## Links

- [Product Vision](../vision/product-vision.md) - How progressive disclosure fits into Outcomist
- [Pattern Library](../patterns/pattern-library.md) - Patterns inform Tier 1 recognition
- [Question Framework](../patterns/question-framework.md) - Questions drive Tier 2+ discovery
- [Explore Command](.claude/commands/explore-command.md) - Implementation of progressive disclosure

---

**Version**: 4.0
**Last Updated**: 2025-11-04
