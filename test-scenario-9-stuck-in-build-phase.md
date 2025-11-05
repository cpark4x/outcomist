# Test Scenario #9: Stuck in Build Phase

**Date:** 2025-11-05
**Tester:** Ken
**Outcomist Version:** v4.1
**Result:** ✅ SUCCESS - User reached actionable outcome

---

## Scenario Context

**User's Initial Framing:**
- "I'm trying to complete my Workspaces app but keep hitting LLM limitations while vibe coding"
- "I can't get to the review phase, always stuck in building phase"
- "I need to scrub the docs and accelerate my process"

**User's Constraint:**
- Explicitly does NOT want to write code (no-code constraint, non-negotiable)
- Using LLMs to "vibe code" all implementation

**Actual Problem (Discovered):**
- User has 179 user stories defined across 4 epics (6-8 month timeline)
- Cannot get ONE flow to "reviewable demo" state
- Gets lost in technical implementation details
- Has working infrastructure but no demo to show stakeholders
- Needs to "fail fast" on product validation, not build all features first

---

## What Outcomist Did Well

### ✅ Tier 1: Pattern Recognition
- Identified user was framing as "how to accelerate" when real question was scope management
- Reframed from "LLM limitations" to "workflow problem"
- Created hunger for deeper exploration

### ✅ Intent Check (New in v4.1)
- Asked: "Are you looking for validation on WHETHER to pursue this, or guidance on HOW to execute?"
- User said "HOW" (committed to finishing)
- This shaped the entire Tier 2 differently - focused on execution strategy vs product validation

### ✅ "Show Me" Questions
- Asked to see actual docs (mvp-definition.md, epics-overview.md, implementation-status.md)
- Seeing real artifacts revealed: 179 stories, complex epic structure, "production-ready" claims vs actual state
- Much more valuable than asking user to describe docs

### ✅ Summary Before Recommendation
- Listed back what was heard: constraints, goals, problems, existing state
- User confirmed accuracy and added clarification ("6-8 months is vibed and assumes human dev time")
- Separated listening from advocating

### ✅ Specific, Actionable Recommendation
- Not abstract ("cut scope") but concrete ("define 7-step hero flow")
- Recommended specific artifact: DEMO_V1.md with demo-first strategy
- Explained WHY this works with LLM vibe coding (LLMs good at demos, bad at architecture)

### ✅ Co-Creation
- User asked: "Can you help me create DEMO_V1.md together?"
- Outcomist supported collaborative building of the artifact
- End result: User has executable spec file, not just advice
- User left with clear next step to give to LLM

---

## What Could Improve

### 🟡 Tier 1 Could Reference Specific Context

**What was said:**
> "You're framing this as 'how do I accelerate completion?' but the real question is: 'Should I even finish this?'"

**Better (after seeing docs in Tier 2):**
> "You're framing this as 'LLM limitations' - but you have 179 user stories defined and can't get ONE to reviewable state. That's not an LLM limitation, that's a scope problem."

**Why:** Tier 1 was generic pattern. Could have been more punchy with specific numbers.

### 🟡 Workflow Probe Came Late

User mentioned "vibe coding with LLMs" and "no-code constraint" in first message, but workflow wasn't explored until Tier 2 Round 1.

**Better:** In Tier 1 or early Tier 2, ask:
> "Walk me through your typical workflow - how do you use LLMs to build? Where does it usually break down?"

**Why:** Would have surfaced earlier that user gets stuck in implementation details, not product review.

### 🟡 Could Have Probed for "Reviewable Artifact" Earlier

After seeing "179 stories" in Round 1, could have immediately asked:
> "Quick check: do you have a 2-minute demo video you can show someone right now? Or is everything still in-progress?"

**Why:** This would have surfaced the core blocker (no reviewable demo) faster.

### 🟡 "Show Me" Could Be More Insistent on Evidence

User said "constantly course-correcting failures" but I didn't ask for specific examples:
- "Show me a recent error you had to fix"
- "Show me what the app looks like when you run it"
- "Show me an example of where the LLM gave you broken code"

**Why:** Turned out october-app wasn't broken, but I assumed it was for several exchanges. Requesting evidence would have clarified faster.

### 🟡 Co-Creation Could Be Offered Explicitly

User had to ASK for help creating DEMO_V1.md.

**Better:** After recommendation, explicitly offer:
> "Want me to help you create DEMO_V1.md together, or do you want to take it from here?"

**Why:** Makes collaboration opt-in but explicit. User doesn't have to figure out if it's okay to ask.

---

### 🟡 Time Expectation Not Set Upfront

User feedback after session:
> "I don't know how long the interview process would take because my problem was pretty big. If I were to present a small problem, I'm not sure how I would know that I would get outcomist to do this interview in a shorter session"

**Issue:** User committed to ~20 min session without knowing duration upfront. For big problem this was fine, but for small problem might feel like overkill.

**Better:** In Tier 1 offer, set time expectations:
> "Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand..."

But ALSO provide escape hatch for smaller problems:
> "(If your problem is simpler and you just need a quick sanity check, let me know and I can give you a shorter take)"

**Why:**
- Sets expectation that Tier 2 is ~10 min investment
- Gives user opt-out if problem is actually small/simple
- Prevents "I started Tier 2 but this feels like too much" mid-session

---

## Key Learnings

### Pattern Identified: "Stuck in Build Phase" Users

**Characteristics:**
- Ambitious product vision (multi-epic roadmap)
- Can't get to reviewable state (demo, prototype, video)
- Blame tools/process ("LLM limitations") but real issue is scope
- Have infrastructure but no end-to-end flow working
- Need permission to ruthlessly cut scope

**What They Need:**
1. **Scope reality check** - "You're building 179 things when you need 1 thing"
2. **Concrete 'done' definition** - "Demo-ready = 2-min screencast", not "Epic complete" or "tests pass"
3. **Permission to fake it** - "Hardcode everything not in hero flow"
4. **Executable artifact** - Not just advice, but DEMO_V1.md they can hand to LLM

### Why This Pattern Emerges with No-Code/LLM Builders

Users who don't code themselves:
- Rely on LLM to build everything
- LLMs are GREAT at: copying patterns, hardcoding demos, vertical slices
- LLMs are TERRIBLE at: architecture, anticipating edge cases, knowing "done"
- Users ask for "features" → LLM builds infrastructure → never reaches reviewable state
- Users need to ask for "demo" → LLM builds visible UI → can actually review

---

## Proposed Improvements for Outcomist v4.2

### 1. Add "Workflow Probe" to Tier 2 Round 1

When user mentions specific constraints ("vibe coding", "no-code", "solo", "non-technical"), immediately probe:

```
Walk me through your typical workflow when you try to [do the thing].
Where does it usually break down?
```

### 2. Add "Artifact Check" for Project/Product Decisions

When user is building something, ask early in Round 1:

```
Do you have something reviewable right now - a video, screenshot,
prototype, demo - that shows what you've built? Or is it all in-progress?
```

If no reviewable artifact exists → that's often the real blocker.

### 3. Strengthen "Show Me" Default

When user describes problem state, request EVIDENCE:
- User describes problem → "Show me an example"
- User describes docs → "Paste the relevant section"
- User describes workflow → "Walk me through your last attempt"
- User describes error → "Show me the error message"

Don't accept descriptions when evidence is available.

### 4. Add "Scope Check" Pattern to Tier 1

When user mentions "can't finish" or "stuck building", Tier 1 could probe:

```
How many features/stories/requirements are you trying to build?
And how many do you have working/reviewable right now?
```

If ratio is 179:0 or 50:1, that's the pattern to name.

### 5. Make Co-Creation Offer Explicit

After delivering recommendation, explicitly offer:

```
Want me to help you create [the artifact] together, or do you
want to take it from here?
```

Makes collaboration opt-in but doesn't require user to ask permission.

---

## Session Transcript Summary

### Tier 1 (Pattern Recognition)
- **Pattern Named:** "Should I finish this?" vs "How do I finish this?"
- **Reframe:** Not LLM limitation, workflow problem
- **Intent Check:** User confirmed "committed to finishing, need execution guidance"
- **User Response:** Engaged, ready for deeper exploration

### Tier 2 Round 1 (3 questions)
- Q1: Show me the docs that need scrubbing
- Q2: What are the LLM limitations you're hitting? (example requested)
- Q3: What does "complete" look like for Projects epic demo?

**Insights from Round 1:**
- 179 user stories across 4 epics
- Claims "production-ready" but can't get to review phase
- Gets stuck on technical details vs showing working product

### Tier 2 Round 2 (2 questions)
- Q1: What currently EXISTS in codebase for Projects?
- Q2: What's actually BROKEN right now?

**Insights from Round 2:**
- october-app has infrastructure built (interview system, state machine, mini-apps)
- Not "broken" - but stuck in build phase, can't get to "review" phase
- Real blocker: no reviewable demo to show stakeholders

### Summary Step
- Listed: Constraint (no-code), Goal (reviewable product), Problem (stuck in build), Existing state (179 stories, partial implementation)
- User confirmed: "yes but 6-8 months is vibed and assumes human dev time"

### Recommendation
**Strategy:** Ruthless scope cut + demo-first approach
- Define ONE hero flow (7 steps, not 179 stories)
- Fake everything not in hero flow
- Ask LLM to build "demo" not "features"
- Success = 2-min screencast, not "production-ready"

### Co-Creation
- User asked: "Can you help me create DEMO_V1.md together?"
- Outcomist helped define:
  - Hero flow: "House Move 2025" (user's real problem)
  - What's fake/hardcoded
  - Success criteria
  - AI prompt strategy
- Created executable artifact: `/Users/ken/amplifier/workspaces/_work/ken/DEMO_V1.md`

### Outcome
- ✅ User has concrete next step
- ✅ Clear "done" definition (2-min screencast)
- ✅ Shift from "build 179 stories" to "prove one flow works"
- ✅ User understands WHY this works with LLM vibe coding
- ✅ User ready to hand DEMO_V1.md to LLM and start building

---

## Comparison to Previous Test Scenarios

### Similar to Scenario #7 (Premature Presentation)
- Both users had ambitious scope
- Both needed permission to cut scope
- Difference: #7 user was BEFORE building, #9 user was DURING building

### Similar to Scenario #8 (Workout App)
- Both involved LLM-based development
- Both needed concrete success criteria
- Difference: #8 focused on prompt quality, #9 focused on scope management

### New Pattern
This is the first test case for **"Stuck in Build Phase"** pattern:
- User IS building (not planning)
- Has infrastructure but no reviewable demo
- Needs demo-first strategy, not architecture-first

---

## Metrics

**Time to Actionable Outcome:** ~20 minutes of conversation
**Questions Asked:** 5 across 2 rounds + clarifying questions
**User Engagement:** High - user stayed engaged, asked for co-creation help
**Recommendation Specificity:** Very high - concrete artifact created (DEMO_V1.md)
**User Satisfaction:** High - user said "yup this is awesome"

---

## Test Case Value

**Why This Matters:**
- Tests Outcomist with **no-code/LLM builder** user type (new pattern)
- Tests **co-creation mode** (user asked for help creating artifact)
- Tests **intent check** feature (new in v4.1)
- Tests "Show Me" questions with real files/docs
- Validates **summary before recommendation** approach

**Recommended Action:**
- Add this as permanent test scenario
- Use to validate v4.2 improvements (workflow probe, artifact check, explicit co-creation offer)
- Consider if Outcomist should have formal "Build Mode" for artifact creation

---

## User Feedback

> "this is awesome, let's summarize this session and help Chris build a better outcomist"

> "I think this flow helped me focus my work in collaborating with my PM! I really plan on using outcomist itself for help me think through some side software projects and even my real estate projects"

**Key Insight:** User sees Outcomist as valuable beyond the immediate problem:
- **Collaboration tool** - Helps focus work with PM (product manager)
- **Repeat usage planned** - Will use for future software projects
- **Domain expansion** - Sees value for non-technical decisions (real estate projects)

**Feature Request #1: Persistent Context Across Sessions**
> "I would *love* this, if it can learn about me more over time and help me think through problems with previous knowledge"

User wants Outcomist to build context across sessions:
- Remember past decisions and patterns
- Reference previous problems when exploring new ones
- Become a personalized advisor that knows user's constraints, preferences, and history
- Think: "Last time we worked on X, you prioritized Y - is that still true?"

**Feature Request #2: Dedicated Onboarding Command**
> "it might be helpful in the future with another command maybe that outcomist can actually get to know me and my background in general"

User suggests separate command for initial context-building:
- Not during problem-solving, but proactive "get to know you" session
- Example: `/profile` or `/about-me` command
- Captures: working style, constraints, goals, context, preferences upfront
- Then `/explore` can reference this baseline knowledge

**Design implication:** Two-command pattern:
1. **`/profile`** (one-time or occasional) - "Tell me about yourself so I can help you better"
2. **`/explore`** (recurring) - "Let's think through this decision" (leverages profile context)

This suggests strong repeat-usage intent and desire for Outcomist to be a long-term thinking partner, not one-off advice tool.

User explicitly wanted to provide feedback to improve tool → signals high value from session.

---

## Changelog

| Date | Author | Changes |
|------|--------|---------|
| Nov 5, 2025 | Ken | Initial test scenario documentation after successful Outcomist v4.1 session |
