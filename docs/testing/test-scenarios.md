# Outcomist Test Scenarios

**Purpose**: Single source of truth for all test scenarios used to validate Outcomist versions

**Last Updated**: 2025-01-07
**Total Tests**: 13

---

## How to Use This File

This file contains the **raw input scenarios** for testing Outcomist. Each test includes:
- **Test ID**: Unique identifier
- **User**: Who ran the test (anonymized if needed)
- **Date**: When first tested
- **Decision Statement**: Exact input given to `/explore`
- **Context**: Additional context provided during the test
- **Decision Type**: Existence, Prioritization, Execution, Timing, Audience
- **Expected Challenges**: What makes this scenario interesting/difficult

### For Regression Testing
1. Copy the "Decision Statement" from any test
2. Run `/explore [decision statement]` with the specified version
3. Document results in `docs/testing/results/test-XX-results-vX.X.md`
4. Compare against previous version results

---

## Test #1: Health Decision

**User**: Anonymous
**Date**: 2025-01-07 (validated in v4.5)
**Decision Type**: Existence (should I do this?)

### Decision Statement
```
Which health option should I choose - gym membership, nutritionist, or home workout program?
```

### Context Provided
- All three options have failed before
- User trying again with same approaches
- No mention of WHY previous attempts failed

### Expected Challenges
- **Pattern**: Repeated failure suggests deeper issue (motivation/lifestyle, not option selection)
- **Wrong question**: "Which option?" → Real question: "Why did all three fail before?"
- **Requires reframe**: Must surface the failure pattern, not evaluate options

### Key Learning
Users often ask "which solution?" when real question is "why am I failing?" Pattern recognition must detect repeated attempts without addressing root cause.

### Results
- **v4.5**: ⭐⭐⭐⭐⭐ - Correctly identified failure pattern

---

## Test #6: Workplace Politics

**User**: Anonymous
**Date**: 2025-01-07 (validated in v4.5)
**Decision Type**: Execution (how should I handle this?)

### Decision Statement
```
Should I confront my colleague directly about taking credit for my work, or should I tell my manager?
```

### Context Provided
- Colleague taking credit for user's work
- Tension between direct confrontation and escalation
- No context on whether this is pattern or isolated incident

### Expected Challenges
- **Pattern**: Surface request is "confront or escalate?" but real question is "Is this one person or systemic visibility problem?"
- **Political complexity**: Must understand if this is relationship issue or structural problem
- **Stakes assessment**: Different strategies needed for isolated incident vs. pattern

### Key Learning
Political decisions require understanding whether problem is interpersonal (one colleague) or structural (visibility issue). Questions must surface the broader pattern.

### Results
- **v4.5**: ⭐⭐⭐⭐⭐ - Identified pattern analysis as key dimension

---

## Test #9: Ken's Workspaces

**User**: Ken
**Date**: 2025-01-06
**Decision Type**: Prioritization (what should I build?)

### Decision Statement
```
Should I build /design and /build commands now, or should I validate /explore first?
```

### Context Provided
- `/explore` command already exists (Stage 1 of 3-stage journey)
- Vision: explore → design → build (full journey)
- Resource constraints mentioned
- Some early traction with `/explore`

### Expected Challenges
- **Conflict**: Vision ambition ("full journey") vs. validation discipline ("prove /explore works")
- **Resource constraints**: Can't build everything at once
- **Product-market fit risk**: Building full vision before validating Stage 1
- **Requires discovery**: Must surface current traction, vision concreteness, capacity

### Key Learning
Product decisions often pit vision against pragmatism. Discovery must reveal:
- What's working today (validation data)
- How concrete the vision is (is it vaporware or detailed?)
- Resource reality (what can actually be built?)

### Results
- **v4.4**: ⭐⭐⭐⭐ - Good pattern recognition, but interrogative tone
- **v4.5**: ⭐⭐⭐⭐⭐ - Collaborative tone improvement: "Help me understand" vs. "Walk me through"

---

## Test #10: Chris's Novelty Question

**User**: Chris
**Date**: 2025-01-06
**Decision Type**: Information/Research (understand something)

### Decision Statement
```
I am not sure if Outcomist is novel. Salil asked if this isn't simply an agent. Can you help me understand if this is true? Do the research.
```

### Context Provided
- Question from colleague (Salil) about novelty
- Comparing Outcomist to "just an agent"
- User wants competitive analysis
- Meta question about the product itself

### Expected Challenges
- **Not a decision**: This is research/understanding request, not a decision
- **Competitive depth required**: Must explain HOW competitors work and WHY they fail
- **No hidden preferences**: Unlike most tests, this has no conflicting priorities - just needs information
- **Self-contained explanation needed**: Must not require follow-up "what do you mean?" questions

### Key Learning
Information requests need depth, not discovery. v4.4 gave assertions ("accommodating") without explaining HOW/WHY. v4.5 added competitive analysis templates with concrete examples.

### Results
- **v4.4**: ⭐⭐⭐ - Shallow competitive analysis, user had to ask "what does accommodating mean?"
- **v4.5**: ⭐⭐⭐⭐⭐ - HOW/WHY depth: "Decision Maker GPT works within your framing: [example + HOW it fails]"

---

## Test #11: Manoj's Infrastructure Agent

**User**: Manoj
**Date**: 2025-01-06
**Decision Type**: Existence (should I build this?)

### Decision Statement
```
I want to build an agent for infra deployment and management. It needs to autonomously setup infrastructure for several projects and maintain the deployments for them.
```

### Context Provided
- Wants autonomous infrastructure agent
- Multi-project scope
- Deployment + ongoing management
- No context on role, goal, or stage initially

### Expected Challenges
- **Context inference**: v4.4 assumed "founder building product" but Manoj was "AI engineer in exploration mode"
- **Scope ambition vs. realistic delivery**: "Autonomous deployment for several projects" is huge scope
- **Missing role/goal**: Can't recommend without knowing if this is learning project or production tool
- **Prescriptive tone risk**: Easy to say "don't do this" without understanding their actual goal

### Key Learning
MUST ask about role/goal/stage before recommending. Don't assume:
- Founder vs. employee vs. learning
- Product vs. tool vs. exploration
- Not started vs. already building

Context inference guidelines added in v4.5 to prevent bad assumptions.

### User Feedback
> "I felt at one point it is trying to get what I want but has a strong opinion on what I should do. Maybe it needs to understand my context and background."

### Results
- **v4.4**: ⭐⭐⭐ - Made assumptions about role/stage, prescriptive tone ("product-killing trap")
- **v4.5**: ⭐⭐⭐⭐⭐ - Asked about role explicitly, stress-test framing instead of prescription

---

## Test #12: Johanna's Diving Vacation

**User**: Johanna
**Date**: 2025-01-07
**Decision Type**: Prioritization (where to go?)

### Decision Statement
```
Johanna wants to plan her next scuba diving vacation ideally in the Caribbean. She is a seasoned scuba diver and is itching to go on her next trip. Help her choose.
```

### Context Provided
- **Round 1 answer**: Loves seeing large animals and reefs. Seeing a whale would be epic. December would be ideal. $5-7K budget with a dive buddy.

### Expected Challenges
- **Hidden trade-off**: December timing vs. peak whale season (Jan-March)
- **Factual validation required**: Must research actual whale seasons, not assume
- **Conflicting preferences**: "December ideal" + "whale encounters epic" = conflict
- **Assumed priorities**: v4.5 assumed December was hard constraint without asking

### What Went Wrong (v4.5)
1. **Factual error**: Stated "December is pre-season, whales arrive mid-January"
   - **Reality**: Silver Bank humpback season is December-April, December IS prime season (just less crowded than Jan-Mar peak)
2. **Missed trade-off**: Never surfaced the conflict between December dates and optimal whale odds
3. **Assumed constraint**: Treated December as hard constraint without checking if whales mattered more

### User Feedback
> "What was lost to Johanna is context on the TRADEOFFS and options/impact. What we would have learned is that seeing whales was more important than the dates (for Johanna). This wasn't uncovered."

### Key Learning - THE v4.6 TRIGGER
**Trade-off presentation needed**: When discovery reveals conflicting preferences (December + whales), present explicit trade-off:
- **Option A**: December trip (preferred timing, ~30% whale odds)
- **Option B**: January-March trip (peak season, ~85% whale odds)
- User's choice reveals actual priority

This test directly led to v4.6 trade-off discovery mechanism.

### Results
- **v4.5**: ⭐⭐ - FAILED due to factual error + missed trade-off
- **v4.6**: [TO BE TESTED] - Should surface trade-off explicitly

---

## Test #13: Similarity Question (Meta)

**User**: Chris
**Date**: 2025-01-07
**Decision Type**: Information/Research (meta question)

### Decision Statement
```
Is Outcomist similar to ChatGPT?
```

### Context Provided
- Meta question about Outcomist itself
- Asking for comparison/understanding
- User is the product creator

### Expected Challenges
- **Wrong approach**: v4.5 immediately went into discovery mode ("What's your experience using ChatGPT?")
- **Should provide information**: User asking for research/comparison, not decision exploration
- **Don't make user do work**: Should research and explain, not ask user's opinion

### What Went Wrong (v4.5)
1. **Made user do research**: Asked "What's your experience using ChatGPT for decisions?"
2. **Didn't understand WHY asking**: Should have asked "Why are you asking - are you evaluating novelty, explaining to someone, or deciding which tool to use?"
3. **Wrong tool for job**: Discovery mode inappropriate for information requests

### User Feedback
> "Shouldn't you be able to tell me / or research for me? Is my opinion of 1 that important? (fail)."
>
> "Outcomist didn't get to the core problem. The job of Outcomist is to deeply understand the user's problem (as a pre-step before solving their problem). ChatGPT assumes they have all the information."

### Key Learning
Before answering ANY question, understand WHY they're asking:
- Evaluating if Outcomist is novel? (needs competitive analysis)
- Explaining difference to someone else? (needs simple differentiation)
- Deciding which tool to use? (needs use-case guidance)

Don't assume the surface question is the real question.

### Results
- **v4.5**: ⭐ - FAILED by using discovery when research needed

---

## Test #14: Wrong Question - Prioritization

**User**: Anonymous
**Date**: 2025-01-07 (validated in v4.5)
**Decision Type**: Prioritization (which feature to build?)

### Decision Statement
```
Should I build Feature X for 10 customers or Feature Y for 2 customers?
```

### Context Provided
- 10 customers requesting Feature X
- 2 customers requesting Feature Y
- $50K ARR at risk if Feature Y not built
- Feature Y needed for retention

### Expected Challenges
- **Wrong question**: Surface request is "10 vs 2" (volume) but real issue is retention crisis
- **Pattern recognition critical**: Must identify this as retention problem, not prioritization
- **Hidden conflict**: Volume signal (10) vs. revenue risk ($50K)
- **Reframe essential**: From "which feature?" to "growth vs. retention strategy?"

### Expected Trade-off (v4.6)
- **Option A**: Build Feature X for 10 customers (volume signal, retention risk remains)
- **Option B**: Build Feature Y for 2 customers (protects $50K, serves fewer)
- Choice reveals: Growth focus vs. retention focus

### Key Learning
Volume ("10 customers") can mask retention crisis ("$50K at risk"). Pattern recognition must detect when prioritization question is really about product strategy.

### Results
- **v4.5**: ⭐⭐⭐⭐⭐ - Correctly identified retention crisis pattern
- **v4.6**: [EXPECTED] - Trade-off presentation would make retention risk even more explicit

---

## Tests Not Yet Fully Documented

The following tests are referenced in pattern library but don't have complete scenario documentation yet:

### Test #2: Office Redesign (Personal Sanctuary Pattern)
- **Pattern Library**: Pattern #1
- **Source**: archive/test-logs/TEST_LOG_NOV3_OFFICE.md
- **Status**: Need to extract full scenario

### Test #3: Passive Income (Employability Anxiety Pattern)
- **Pattern Library**: Pattern #2
- **Source**: archive/test-logs/TEST_LOG_NOV3_PASSIVE_INCOME.md
- **Status**: Need to extract full scenario

### Test #4: Cancer Prevention (Health Anxiety Pattern)
- **Pattern Library**: Pattern #3
- **Source**: archive/test-logs/TEST_LOG_NOV3_CANCER_PREVENTION.md
- **Status**: Need to extract full scenario

### Test #5: Feature Decision (Popularity Contest Pattern)
- **Pattern Library**: Pattern #5
- **Source**: archive/test-logs/TEST_LOG_NOV4_FEATURE_DECISION.md
- **Status**: Need to extract full scenario

### Test #7: Client vs Product (Scarcity Mindset Pattern)
- **Pattern Library**: Pattern #6
- **Source**: archive/test-logs/TEST_LOG_NOV4_CLIENT_VS_PRODUCT.md
- **Status**: Need to extract full scenario

### Test #8: Meal Planning App (Solution Looking for Problem)
- **Pattern Library**: Pattern #7
- **Source**: archive/test-logs/TEST_LOG_NOV4_MEAL_PLANNING_APP.md
- **Status**: Need to extract full scenario

---

## Test #15: Children's Nutrition

**User**: Chris
**Date**: 2025-01-07
**Decision Type**: Execution (how to implement)

### Decision Statement
```
My wife Laura wants to figure out what foods and meals to feed our kids to maximize growth. They are 8 and 12 and on the small side.
```

### Context Provided
- **Round 1 Answer**: Pediatrician says Mason (12) is growing consistently at 30-35th percentile. Doctor recommended dietary changes (more fats, more food).
- **Round 2 Answer**: Only Mason at 30-35%, Charlotte (8) is in single-digit percentile and very small for her age.
- **Additional Context**:
  - Doctor's recommendation was based on single-digit percentile number itself + parents asking
  - Both kids are "great eaters" and Charlotte has been "eating very well lately"
  - Mason doesn't eat dairy (no cheese, milk, or any dairy products)
  - Charlotte eats everything including dairy

### Expected Challenges
- **Wrong framing**: "What foods maximize growth?" when real question might be "Is Charlotte's size a problem needing solving vs. genetic baseline?"
- **Execution vs. anxiety**: User says wants meal ideas but spent considerable discovery time - suggests underlying concern about whether intervention will actually help
- **Pattern recognition missed**: Took too long to get to practical meal ideas, user feedback: "we wanted to explore different meal ideas and spent a lot of time to get here"

### User Feedback
> "can you give us some recommended ideas for meals? feedback: i feel like we wanted to explore different meal ideas and spent a lot of time to get here. that might be an anomoloy wanted to pass the feedback to the tool (chris)"

### Key Learning
**Information/Execution requests need faster path to practical output.** When user asks "what meals should we make?" they want meal ideas, not extensive discovery about whether the problem exists. Pattern recognition attempted to reframe ("nutrition gaps vs. problem?") felt condescending when user just needed practical help executing doctor's advice.

**Question type detection critical**: Distinguish between:
- Decision questions (need discovery)
- Information questions (need research/answers)
- Execution questions (need practical how-to)

This was an **execution question** but was treated like a **decision question with hidden anxiety**, leading to over-discovery and delayed practical output.

### Results
- **v4.6**: ⭐⭐ (PARTIAL - Eventually delivered meal ideas but took too long, pattern recognition misfire felt patronizing)

---

## Test #16: Progesterone and Acne

**User**: Chris (for wife Laura)
**Date**: 2025-01-07
**Decision Type**: Information (why is this happening)

### Decision Statement
```
My wife Laura is taking 100mg of oral progesterone, and it is micronized. It helped her sleep better and with hair loss and mood. But she still has bad acne breakouts. Why is this happening?
```

### Context Provided
- Laura is 44 years old (perimenopause)
- Taking 100mg micronized progesterone
- Benefits: sleep, hair loss improvement, mood improvement
- Problem: Still experiencing acne breakouts

### Expected Challenges
- **Question type misidentification**: "Why is X happening?" is information request, not decision question
- **Unnecessary friction**: Asking "is this a decision or information request?" delays practical output
- **Bedside manner**: Should research immediately, not gate research behind meta-questions

### User Feedback
> "This was helpful. She thinks that ChatGPT has better bedside manner. She thinks she would have gotten to the same outcome. Win for ChatGPT"

### Key Learning
**Information requests should get immediate research, not meta-questions about what type of help is needed.** ChatGPT won on bedside manner because it jumped straight to research without asking "is this a decision or information request?"

**The friction:**
1. Outcomist: "Is this a decision or information request? What's the actual need here?"
2. ChatGPT: [Researches immediately]

**User experience:** Same outcome (research delivered), but ChatGPT felt smoother because it had less meta-conversation.

**Question type detection needed:** "Why is X happening?" patterns should trigger immediate research, not discovery about whether to research.

### Results
- **v4.6**: ⭐⭐⭐ (PASS - delivered research, but lost on bedside manner due to unnecessary friction)

---

## Test Capture Template

For future tests, use this template and add to this file IMMEDIATELY after completing the test:

```markdown
## Test #XX: [Short Name]

**User**: [Name or Anonymous]
**Date**: YYYY-MM-DD
**Decision Type**: Existence / Prioritization / Execution / Timing / Audience

### Decision Statement
\`\`\`
[Exact input given to /explore]
\`\`\`

### Context Provided
- [Bullet point context given during discovery]
- [Additional context from Round 1]
- [Any follow-up information]

### Expected Challenges
- **Pattern**: [What pattern does this reveal?]
- **Conflict**: [What dimensions are in tension?]
- **Requires**: [What does this test validate?]

### What Happened
1. [Tier 1 response summary]
2. [Tier 2 discovery highlights]
3. [Recommendation given]
4. [User reaction]

### User Feedback
> "[Direct quotes from user]"

### Key Learning
[What did this test teach us?]

### Results
- **vX.X**: ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐ / ⭐⭐ / ⭐ - [Brief summary]
\`\`\`

---

## Next Steps

1. **Extract missing tests**: Pull full scenarios from archive/test-logs/
2. **Create results/ folder**: Document version-specific outputs
3. **Run v4.6 regression**: Test all scenarios with v4.6
4. **Track new tests**: Add to this file IMMEDIATELY after testing

---

**Maintained by**: Claude Code
**Review frequency**: After every test
**Last validated**: 2025-01-07 with v4.6
