# Epic 1: Deep Discovery

**Status**: ✅ Validated and shipped (v4.8)
**Duration**: 30 seconds to 30 minutes (adaptive)
**Goal**: Understand deeply enough to propose a really great solution

---

## Overview

Epic 1 is ONE continuous discovery process that adapts to decision complexity. It combines what was previously "Pattern Recognition", "Discovery", and "Deep Analysis" into a seamless flow whose sole purpose is to arrive at a high-quality, executable proposal.

**The principle**: Get to Epic 2 (proposal review) as quickly as possible while ensuring the proposal is tangible, polished, and gap-free enough for confident evaluation.

---

## User Story

"As a decision-maker, I need AI to deeply understand my problem AND validate it can execute a solution, so I get a high-quality, executable proposal to review."

---

## What Deep Discovery Includes

### 1. Pattern Recognition (30 seconds)
- Identify which of 9 documented patterns applies
- Reframe question to reveal deeper issue
- Preview what deeper exploration would uncover
- User chooses: Continue or stop here

### 2. Discovery Questions (5-10 minutes)
- Adaptive questioning based on previous answers
- Evidence gathering ("Show me" questions verify facts)
- Pattern synthesis (analysis showing what system detected)
- Targeted follow-up based on insights
- Summary & confirmation before recommendation

### 3. Deep Analysis (Optional, 20-30 minutes)
- When decision is complex with multiple viable options
- Systematic comparison of alternatives
- Risk assessment and scenario planning
- Trade-off analysis when conflicts detected
- Only when complexity warrants it

### 4. Executability Validation (Throughout)
**Critical**: AI must validate it can execute within user's constraints before proposing.

**Technical constraints**:
- Current tech stack (WordPress? Shopify? Custom?)
- Deployment capabilities (Vercel? Heroku? Shared hosting?)
- Maintenance capabilities (Can edit code? Need no-code?)

**Skill/Resource constraints**:
- Technical comfort level
- Budget for services ($10/month? $100/month? $1000/month?)
- Hiring capabilities (Freelancer? Agency? No one?)

**Access/Permission constraints**:
- Admin access (DNS? Database? APIs?)
- Integration requirements (CRM? Payment processor?)
- Compliance requirements (HIPAA? GDPR? SOC2?)

---

## Core Principles

### Adaptive Depth
- **Quick path** (30 sec - 5 min): Pattern recognition + discovery questions
- **Thorough path** (20-30 min): Includes alternatives comparison and deep analysis
- Depth adapts to decision complexity, not arbitrary stages

### Executability First
- AI only proposes what it can actually deliver
- **No "floating countertops"**: Don't propose cool ideas that can't be executed
- Validate constraints before proposing solutions
- If AI can't execute, either simplify to fit constraints or tell user explicitly

### Constraint Awareness
- Capture technical, resource, skill, and access constraints
- Understand user's context completely before proposing
- Ask "Can I actually build this for them?" before suggesting it

### One Continuous Process
- Not separate stages with hard boundaries
- Seamless flow from pattern → questions → analysis (when needed)
- User doesn't experience "entering Epic 1 Phase 3"
- Just progressively deeper understanding until proposal is ready

---

## Output of Epic 1

**"Here's what I'll build for you"** - AI's executable proposal

The proposal must be:
- **Specific**: Not "a web app with features X, Y, Z" but "here's the working prototype"
- **Executable**: AI has validated it can actually build this within constraints
- **High-quality**: Polished enough to evaluate confidently
- **Gap-free**: Explicitly identifies what's included and what's not
- **Tangible**: User can see/click/read what they'll get at the end

---

## Flow Diagram

```
User inputs decision
    ↓
Pattern Recognition (30 sec)
    ↓
Reframe + Preview
    ↓
User choice: Continue or stop?
    ↓
Discovery Questions (5-10 min)
    ↓
Evidence Gathering
    ↓
Pattern Synthesis
    ↓
Targeted Follow-up
    ↓
Summary & Confirmation
    ↓
[Optional: Deep Analysis if complexity warrants]
    ↓
Executability Validation
    ↓
Executable Proposal → Epic 2
```

---

## Features Implemented (v4.8)

### 1.1: Decision Input
- Natural language decision statement
- No forced format or structure
- User speaks naturally

### 1.2: Pattern Detection
- Identifies which of 9 patterns applies
- Uses signals from pattern library
- Streaming pattern recognition

### 1.3: Reframing & Preview
- Shows real issue (not just stated problem)
- Previews what exploration would uncover
- User sees value before committing time

### 1.4: Adaptive Questioning (Round 1)
- 2-3 high-level questions
- Context-aware based on pattern
- Evidence gathering ("Show me" questions)

### 1.5: Pattern Synthesis
- Analysis showing what system detected
- Transparent reasoning
- User sees how AI is thinking

### 1.6: Targeted Follow-up (Round 2)
- Focused question based on Round 1
- Digs into specific insights
- Clarifies ambiguities

### 1.7: Summary & Confirmation
- User validates understanding
- Opportunity to correct misconceptions
- Clear before recommendation

### 1.8: Executability Validation
- Technical constraint checking
- Resource availability assessment
- Access/permission verification
- Only propose what can be executed

---

## Technical Implementation

### Current Stack
- **Web interface**: `outcomist_web/` (Reflex framework)
- **Shared prompts**: `outcomist_shared/prompts.py`
- **Pattern library**: 9 documented patterns
- **Streaming**: Server-Sent Events for natural feel
- **LLM**: Claude API via streaming

### Key Components
```python
# Pattern recognition
ExplorationEngine.generate_tier_1()

# Discovery questions
ExplorationEngine.start_tier_2()
ExplorationEngine.handle_answer()

# Session persistence
Session state tracks conversation and insights
```

### Discovery Process
1. User inputs decision statement
2. System detects pattern (streaming response)
3. System reframes + previews exploration
4. User indicates intent (validation vs execution)
5. System asks Round 1 questions (2-3 questions)
6. User answers, system gathers evidence
7. System synthesizes patterns, shows analysis
8. System asks Round 2 targeted follow-up
9. User answers
10. System generates summary, user confirms
11. System validates executability constraints
12. System delivers executable proposal → Epic 2

---

## Quality Standards

### What Makes a Good Discovery

**✅ Good discovery**:
- Reveals the real problem (not just stated problem)
- Captures all relevant constraints
- Validates AI can execute within constraints
- Asks minimum necessary questions (not 20 questions)
- Gets to proposal quickly without sacrificing quality
- User feels understood, not interrogated

**❌ Bad discovery**:
- Takes surface-level question at face value
- Proposes solutions AI can't actually build
- Asks excessive questions for marginal value
- Misses critical constraints
- Forces unnecessary depth
- User feels exhausted, not clarified

### Speed vs Quality Balance

**Too fast**: Proposal has gaps, surprises during execution, "floating countertop" solutions
**Too slow**: User abandons before reaching proposal, feels like interrogation
**Just right**: Minimum questions needed to validate executability and ensure high-quality proposal

**Rule**: Only go deeper if it materially improves the proposal quality. Most decisions resolve with pattern + discovery questions (5-10 min total).

---

## Transition to Epic 2

### When Ready
After Epic 1, user has:
- ✅ Deep understanding of real problem
- ✅ AI validated it can execute within constraints
- ✅ Executable proposal: "Here's what I'll build for you"
- ✅ Ready to review tangible outcome

### What Flows Forward to Epic 2
- All discovery insights (answers to questions)
- Identified constraints and priorities
- Gathered evidence
- Validated executability
- The specific proposal

### User Choice
- **Continue to Epic 2**: Review the detailed proposal
- **Stop here**: Clarity achieved, decision can be made independently
- **Iterate Epic 1**: Need more discovery before proposal

---

## Success Metrics

### Qualitative
- ✅ User feels deeply understood
- ✅ Real problem identified (not just stated)
- ✅ Proposal is executable (not "floating countertop")
- ✅ User confident moving to Epic 2

### Quantitative
- ✅ 80%+ of users reach Epic 2 within 10 minutes
- ✅ <10% proposals need major rework in Epic 2
- ✅ 0% proposals include non-executable solutions
- ✅ Average 4-6 questions asked (not 15-20)

---

## Common Patterns

### Pattern: "Build vs Buy Decision"
**Quick path** (5 min):
- Pattern recognition: Reveals trade-offs
- Discovery: Budget, timeline, maintenance capacity
- Proposal: Specific tool recommendation with rationale

**Thorough path** (20 min):
- Includes: Detailed comparison of 3 options
- Risk assessment per option
- Scenario planning (best/worst case)
- Proposal: Recommendation with full alternatives documented

### Pattern: "Product Strategy"
**Quick path** (5 min):
- Pattern recognition: Reveals real constraint
- Discovery: Current traction, resources, goals
- Proposal: Clear recommendation with next actions

**Thorough path** (30 min):
- Includes: Market analysis, competitive positioning
- Multiple strategic options compared
- Risk/reward analysis
- Proposal: Strategic plan with execution roadmap

---

## Open Questions

### For Future Iterations
- How to better detect when deep analysis is needed vs overkill?
- Can we predict upfront: quick path vs thorough path?
- How to make executability validation more explicit/visible?
- Should we show "confidence score" on executability?

---

## Related Documentation

- [Product Vision v2](../vision/product-vision-v2.md) - Strategic context
- [End-to-End Flow](../vision/end-to-end-flow.md) - Complete journey
- [Pattern Library](../patterns/pattern-library.md) - 9 documented patterns
- [Question Framework](../patterns/question-framework.md) - Question design principles

---

## Document History

**Created**: 2025-01-10
**Replaces**: epic-1-pattern-recognition.md, epic-2-discovery.md, epic-3-deep-analysis.md
**Status**: Aligned with Product Vision v2
**Audience**: Product team, AI assistants, future builders
