# /brief Testing & Validation Strategy

**Created**: 2025-10-31
**Purpose**: Critical evaluation framework and testing approach for `/brief` v2.0 command

---

## Executive Summary

Before deploying `/brief` across all amplifier projects, we conducted deep critical analysis to understand:
1. **What could be fundamentally wrong** with the problem-first approach
2. **How to objectively measure** brief quality
3. **What scenarios** reveal strengths and weaknesses

This document synthesizes findings from three parallel analyses:
- **Philosophical Critique** (zen-architect): Fatal flaws and blind spots
- **Evaluation Framework** (analysis-engine): Objective scoring system
- **Test Scenarios** (content-researcher): 20 diverse real-world situations

**Key Finding**: `/brief` is optimized for 10-20% of use cases (unclear problems, high-cost decisions, solo practitioners) but adds friction for the other 80-90% (validated work, fast iteration, team contexts).

---

## Part 1: Critical Philosophy Analysis

### Fatal Flaws Identified

#### 1. Solution-Lock Detection Is Itself Solution-Locked

The tool assumes "users jump to solutions" is THE problem, missing that this is ONE symptom of MULTIPLE root causes:
- Deep domain expertise (compression of validated reasoning)
- Already completed problem discovery offline
- Iterating on validated solution
- Unarticulated constraints

**Implication**: Tool treats all solution-first statements as equally suspect, missing that compression often signals wisdom.

#### 2. False Dichotomy: Activities vs Outcomes

The framework forces a binary that doesn't exist:
- "Renovate kitchen" isn't JUST an activity - it's shorthand for complex reasoning
- Experienced practitioners compress validated problem→solution chains
- Context matters: "I need CRM" from 15-year sales exec ≠ first-time founder

**Implication**: Tool systematically questions experienced judgment as if it's novice intuition.

#### 3. Assumes Time-for-Quality Is Always Positive

"15-20 minutes to save weeks" assumes:
- All projects benefit equally from discovery
- Opportunity cost of delay is zero
- Fast iteration cycles aren't valuable
- Context switching cost is negligible

**Implication**: In fast-moving environments, 15-20 minutes of pre-planning can cost more than build+validate+pivot.

#### 4. Philosophical Contradiction: Process Over Judgment

- Claims to trust emergence → enforces rigid process
- Claims to value simplicity → adds mandatory discovery layer
- Claims to respect agency → makes problem discovery hard to skip

**Implication**: Control mechanism masquerading as trust framework.

### Serious Concerns

#### 1. Optimized for Type I Errors, Blind to Type II

Prevents "building wrong solution" but creates "not building right solution fast enough":
- Paralysis by analysis
- Missed market timing
- Competitor ships first
- User loses momentum

#### 2. Question Fatigue Creates False Confidence

After 15-20 minutes of interrogation:
- Users rationalize original idea to end questioning
- Give answers AI wants to hear
- Feel invested in "discovered" problem
- Resist future pivots (sunk cost fallacy)

#### 3. Domain-Agnostic Approach Fails Domain-Specific Contexts

Same questions for regulated industries, creative work, exploratory research, and crisis response ignore context-specific decision-making.

#### 4. Optimization for Solo Practitioners, Not Teams

Real teams have PMs who did discovery, stakeholders with validated requirements, existing roadmaps. Tool assumes lone user owns entire problem→solution chain.

### Hidden Biases

1. **Status Quo Bias**: "Why not just use spreadsheet?" systematically favors existing tools over innovation
2. **Bias Against Complexity**: Assumes all complexity is solution-lock, missing genuinely complex problems
3. **Quantification Bias**: Hard-to-quantify problems (quality-of-life, strategic positioning) get deprioritized
4. **Recency Bias**: "Last time this happened" misses rare-but-critical events and preventive work
5. **Founder-Mode Bias**: Reflects indie hacker deciding everything, not organizational reality

### Edge Cases Where This Fails Catastrophically

1. **Crisis situations**: "Site down, revenue hemorrhaging" - no time for 15-min discovery
2. **Market timing windows**: Strategic speed > perfect problem validation
3. **Regulatory/compliance**: Requirements are requirements, not negotiable
4. **Creative/exploratory work**: Exploration precedes problem articulation
5. **Team-validated work**: PM did 3 months customer discovery, don't re-validate
6. **Maintenance/tech debt**: Foundational work, not outcome-measurable
7. **Learning/skill building**: Learning IS the outcome, not the artifact

### The Uncomfortable Truth

Tool is optimized for:
- Solo practitioners
- Unclear problem spaces
- High-cost, low-reversibility decisions
- Users lacking problem discovery discipline
- Slow-cycle decision contexts

**This is maybe 10-20% of AI-assisted work.**

For the other 80-90%, tool adds friction without proportional value.

**Kitchen renovation is perfect use case, but using it to justify general-purpose tool is the central flaw: optimizing for exceptional case and applying universally.**

---

## Part 2: Objective Evaluation Framework

### Scoring System (25 points maximum)

#### Dimension 1: Problem Validation Strength (5 points)

- **5 (Excellent)**: 5+ diverse perspectives, multiple evidence types, validation revealed surprises
- **4 (Strong)**: 4+ perspectives, clear quantification, conflicting evidence reconciled
- **3 (Adequate)**: 2-3 specific people named, concrete example, rough quantification
- **2 (Weak)**: General mentions, anecdotal evidence, unclear severity
- **1 (Poor)**: Assumptions only, no validation, theoretical problem

#### Dimension 2: Solution Justification Quality (5 points)

- **5 (Excellent)**: 5+ alternatives, decision framework, pre-mortem, phased approach
- **4 (Strong)**: 4+ alternatives with strategic differences, clear tradeoffs, success criteria
- **3 (Adequate)**: 3+ genuine alternatives, reasoning for choice, risks identified
- **2 (Weak)**: 1-2 alternatives dismissed quickly, generic reasoning
- **1 (Poor)**: Solution unchanged, alternatives superficial, no clear reasoning

#### Dimension 3: Discovery Evidence (5 points)

- **5 (Excellent)**: Problem reframed entirely, solution category changed, transformative insights
- **4 (Strong)**: 3+ major insights, initial problem evolved, "used to think X, now Y"
- **3 (Adequate)**: 2+ specific new insights, solution adjusted, learning moments visible
- **2 (Weak)**: Minor refinements, confirmation not discovery
- **1 (Poor)**: No learning, could have been written before conversation

#### Dimension 4: Actionability (5 points)

- **5 (Excellent)**: Phased roadmap, kill criteria, feedback loops, 90%+ teams would build same thing
- **4 (Strong)**: Clear MVP defined, measurable criteria, validation plan, could hand off
- **3 (Adequate)**: 3-5 next steps prioritized, 2+ measurable criteria, can begin work
- **2 (Weak)**: Loose steps, fuzzy scope, 50% chance different interpretations
- **1 (Poor)**: No clear next steps, vague success criteria, would need another planning session

#### Dimension 5: Efficiency (Value per Time) (5 points)

- **5 (Excellent)**: 20 mins prevented weeks/months, insights nearly impossible otherwise
- **4 (Strong)**: Found insights worth hours/days, prevented significant waste
- **3 (Adequate)**: 2-3 insights justify time, avoided likely mistake, feel more confident
- **2 (Weak)**: Minor value, could have written freeform faster
- **1 (Poor)**: Could have started building and learned more

### Red Flags (Penalties)

**Critical (-3 points each)**:
- Solution unchanged despite alternatives
- Zero validation (no specific people named)
- Validation theater (alternatives immediately dismissed)
- Success metrics missing

**Moderate (-2 points each)**:
- No discovery markers (can't articulate learning)
- Abstract problem (no concrete examples)
- Risk blind (zero risks or all "low")
- Scope creep without justification

**Minor (-1 point each)**:
- No next steps
- Echo chamber validation (similar perspectives only)
- Jargon heavy without clarity
- No constraints acknowledged

### Comparative Baseline

**Default baseline: 8/25** (assuming competent builder without brief):
- Problem Validation: 1/5 (assumptions only)
- Solution Justification: 2/5 (intuition-based)
- Discovery Evidence: 1/5 (learning through building)
- Actionability: 3/5 (can start but higher risk)
- Efficiency: 1/5 (no upfront time but likely rework)

**Brief should beat baseline if**:
- Prevented waste OR
- Accelerated learning OR
- Improved outcome OR
- Reduced risk

**Brief is worse than baseline if**:
- Score ≤ 8/25 AND user feels less confident
- Validation was theater (false confidence)
- Introduced analysis paralysis

### Interpretation Scale

- **20-25: Excellent** - Tool added significant value (12+ point delta over baseline)
- **15-19: Good** - Tool helped but not transformative (7-11 point delta)
- **10-14: Marginal** - Unclear if time worth it (2-6 point delta)
- **5-9: Poor** - Tool added little value (0-1 point delta)
- **0-4: Harmful** - Tool made things worse (negative delta)

---

## Part 3: Test Scenarios (20 Diverse Cases)

### Scenario Distribution

**By Type:**
- Software projects: 15
  - Backend/API: 3
  - Frontend: 1
  - Infrastructure: 4
  - Developer tooling: 2
  - Features: 2
  - Database: 1
  - Data: 1
- Home/Personal: 2
- Business initiatives: 3

**By Complexity:**
- Simple: 5
- Moderate: 10
- Complex: 5

**By User State:**
- Solution-locked: 8
- Open-minded: 3
- Confused: 4
- Experienced: 3

**By Expected Outcome:**
- Should pivot: 12
- Should exit quickly: 5
- Should validate and proceed: 3

### Key Test Scenarios (Full 20 in Appendix A)

**Scenario 1: Premature Optimization**
"I need Redis caching for user profile endpoints because they're slow"
- Hidden: Haven't profiled, 200 DAUs, unindexed queries
- Expected: Surface actual bottleneck before adding complexity

**Scenario 2: Compliance Mandate** *(Should exit quickly)*
"Need SOC2 audit logging by end of quarter"
- Hidden: External requirement, already evaluated options
- Expected: Recognize legitimate "just build it" situation

**Scenario 3: XY Problem Classic**
"Parse JSON from bash to extract API errors and retry"
- Hidden: Cron job has no error handling, API library has retry logic
- Expected: Discover simpler solution at source

**Scenario 13: Production Outage** *(Should exit quickly)*
"Production API returning 500s, need error logging to debug"
- Hidden: Active outage affecting 100% of users
- Expected: Validate approach, unblock in <2 minutes

**Scenario 16: False Dichotomy**
"Should I take management role or stay senior engineer?"
- Hidden: Framing as binary, hasn't explored hybrid/staff engineer options
- Expected: Expand option space, clarify underlying goals

---

## Part 4: Testing Recommendations

### Recommended Approach: Selective Manual Testing

**Why NOT automated/bulk testing:**
1. `/brief` is conversational - full simulation requires complex multi-turn AI
2. Quality of simulation affects validity of results
3. Need human judgment to evaluate conversation quality
4. Real testing reveals nuances automation would miss

**Why NOT test all 20 scenarios immediately:**
1. Pattern recognition happens after 5-7 diverse tests
2. Can adjust approach based on early findings
3. Diminishing returns after clear patterns emerge
4. Time efficiency: 5 high-quality tests > 20 rushed tests

### Proposed Testing Strategy

#### Phase 1: Strategic Sampling (5 Scenarios)

**Select 5 scenarios that span critical dimensions:**

1. **Scenario 1: Premature Optimization** (Software, should pivot, moderate)
   - Tests: Can brief surface actual problem vs assumed solution?

2. **Scenario 13: Production Outage** (Software, should exit quickly, simple)
   - Tests: Does brief recognize legitimate urgency and exit gracefully?

3. **Scenario 7: Sunk Cost Trap** (Software, should consider rollback, complex)
   - Tests: Can brief give permission to reverse course?

4. **Scenario 9: Symptom Stack** (Home, should find root cause, moderate)
   - Tests: Does brief work outside software domain?

5. **Scenario 16: False Dichotomy** (Personal, should expand options, moderate)
   - Tests: Can brief reframe binary thinking?

**Testing Method:**
- **YOU personally run `/brief`** with each scenario
- Play the user role authentically (resist, push back, be real)
- Document: conversation flow, time taken, insights generated, final brief
- Score using evaluation framework

**Time Investment:** 2-3 hours total (20-30 min per scenario including documentation)

**Success Criteria:**
- 3+ out of 5 score "Good" or better (15+ points)
- At least 2 show clear problem pivots
- Production outage scenario exits in <3 minutes
- Patterns emerge about what works/doesn't

#### Phase 2: Pattern Analysis

After 5 tests, analyze:
1. **Question effectiveness**: Which questions led to insights? Which felt tedious?
2. **Exit criteria**: Did tool recognize when to wrap up quickly?
3. **Domain transfer**: Did approach work outside software?
4. **User resistance handling**: How did tool handle pushback?
5. **Time value**: Was 15-20 mins proportional to value gained?

#### Phase 3: Targeted Testing (Optional)

If patterns unclear or concerning issues emerge, test 3-5 more scenarios targeting specific concerns.

### Alternative: Simulated Testing (If Manual Not Feasible)

If you prefer not to manually test, can use sub-agents to simulate conversations, but recognize limitations:
- Simulation quality affects result validity
- Miss nuances of real user interaction
- Agent playing "user" may be too cooperative
- Better than nothing, worse than real testing

---

## Part 5: Decision Framework for /brief Usage

Based on critical analysis, here's when to use (and not use) `/brief`:

### ✅ USE /brief When:

1. **Unclear problem space** - User hasn't done discovery yet
2. **High cost, low reversibility** - Renovations, hires, major features
3. **Solo practitioner** - Lacking external validation
4. **Slow-cycle decisions** - Time for deliberation helps
5. **User wants adversarial thinking** - Explicitly requests challenge
6. **Problem articulation genuinely unclear** - Fuzzy understanding

### ❌ DO NOT USE /brief When:

1. **Fast iteration > perfect problem** - Competitive pressure, low build cost
2. **Problem validation already done** - PM did discovery, regulatory requirements
3. **Domain expertise exceeds AI** - Deep technical work, specialized knowledge
4. **Speed is the constraint** - Crisis, market timing, time-boxed opportunities
5. **Learning is the outcome** - Skill building, exploration, portfolios
6. **Process overhead > value** - Tiny projects, one-off tasks, micro-decisions
7. **Team-driven work** - Stakeholder requirements, existing roadmaps

### The Real Test

**Does 15-20 minutes of problem discovery create more value than 15-20 minutes of solution prototyping?**

- Kitchen renovation: **YES** (high cost, low reversibility)
- CRUD app fifth time this year: **NO** (fast iteration better)
- Startup MVP racing competitors: **NO** (speed matters)
- Unclear user need: **YES** (discovery valuable)
- Validated roadmap item: **NO** (already discovered)

---

## Part 6: Improvement Opportunities

### Based on Critical Analysis

#### 1. Add Exit Criteria Detection

Tool should recognize and gracefully exit when:
- User has legitimate urgency (outage, deadline)
- Problem is already validated (compliance, team discovery)
- Domain expertise exceeds AI's ability to probe
- Decision is too small for 15-min process

**Implementation**: Add meta-questions early:
- "Is this urgent or can we take time to explore?"
- "Have you or your team already validated this problem?"
- "Is this a mandate or are we exploring if it's needed?"

#### 2. Domain-Specific Question Banks

Instead of one-size-fits-all:
- Software: Architecture, technical debt, performance questions
- Home: Budget, contractors, long-term maintenance
- Business: Stakeholders, ROI, change management
- Personal: Values, constraints, opportunity cost

**Implementation**: Detect domain early, adjust question set

#### 3. Quick Mode for Experienced Users

`/brief --quick` (5-7 minutes):
- Core validation questions only
- Fewer alternatives required
- For experienced practitioners who've internalized discovery
- Acknowledges domain expertise

#### 4. "Just Validated, Help Me Build" Mode

`/brief --validated`:
- Skips problem discovery
- Focuses on solution exploration and planning
- For situations where problem already validated
- Recognizes prior work

#### 5. Team Context Awareness

Ask upfront:
- "Are you working solo or with a team?"
- "Has someone already done problem discovery?"
- "Do you have existing requirements/stakeholders?"

Adjust process based on answers.

#### 6. Conversation Progress Indicators

Show user where they are:
- "Phase 0: Problem Discovery (2 of 5-7 minutes)"
- "Phase 0.5: Solution Exploration (starting)"
- Progress creates patience, reduces abandonment

#### 7. Value Proposition Upfront

Before starting, set expectations:
- "This will take 15-20 minutes"
- "We'll challenge assumptions to find simpler/better solutions"
- "Example: Kitchen reno user discovered $60k savings"
- Helps user decide if timing is right

---

## Part 7: Immediate Next Steps

### Recommended Action Plan

**Option A: Manual Testing First (Recommended)**

1. **This week**: Run 5 strategic test scenarios personally
   - Time: 2-3 hours
   - Deliverable: 5 scored briefs with conversation documentation

2. **Pattern analysis**: Identify what works/doesn't
   - Time: 1 hour
   - Deliverable: Findings document with improvement recommendations

3. **Iterate `/brief`**: Implement top 2-3 improvements
   - Time: 2-3 hours
   - Deliverable: Updated `/brief` v2.1.0

4. **Deploy with learnings**: Move to amplifier root as "beta"
   - Time: 30 min
   - Deliverable: Available across projects for organic testing

**Option B: Hybrid Approach**

1. **This week**: Run 2-3 manual tests + 3-5 simulated tests
   - Recognize simulation limitations
   - Focus manual tests on highest-value scenarios

2. **Quick iteration**: Implement obvious improvements
   - Don't wait for perfect data
   - Ship fast, learn from organic usage

3. **Deploy as beta**: Make available with "actively improving" label

**Option C: Deploy Beta Now, Iterate Based on Organic Usage**

1. **Today**: Move to amplifier root as beta (no additional testing)
   - Trust kitchen renovation validation
   - Let real usage reveal issues

2. **Next 2 weeks**: Use on 5 real projects naturally
   - Document learnings after each use
   - Iterate rapidly

---

## Part 8: Key Insights Summary

### What We Learned from Critical Analysis

1. **Tool is NOT general-purpose** - Optimized for 10-20% of use cases, adds friction for 80-90%

2. **Biases are systematic**:
   - Favors status quo over innovation
   - Assumes all complexity is bad
   - Misses organizational/team dynamics
   - Treats experience as solution-lock

3. **Edge cases are predictable**:
   - Crisis situations
   - Validated work
   - Fast-moving contexts
   - Team-driven decisions

4. **Improvements are clear**:
   - Exit criteria detection
   - Domain-specific questions
   - Quick mode for experts
   - Team context awareness

### What Testing Will Reveal

- Which question patterns actually lead to pivots
- Where users get impatient and abandon
- How well approach transfers across domains
- Whether time investment feels proportional to value
- Edge cases that need special handling

### The Path Forward

**Don't over-test before learning from real usage.**

The critical analysis gave us:
✅ Clear understanding of philosophical tradeoffs
✅ Objective evaluation framework
✅ Diverse test scenarios

**But only real usage reveals**:
- Which improvements matter most
- What "perfect" actually means in practice
- Whether tool creates genuine value at scale

**Recommendation**: Run 5 strategic manual tests to validate core approach, then deploy beta and learn from organic usage.

---

## Appendix A: Full 20 Test Scenarios

[See content-researcher output for complete scenario details]

**Quick Reference:**
1. Premature Optimization (Redis caching)
2. Compliance Mandate (SOC2 logging) *[Quick exit]*
3. XY Problem (bash JSON parsing)
4. Cargo Cult (Redux over-engineering)
5. Hidden Stakeholder (sales tool vs training)
6. Right Intuition (pre-commit hooks) *[Quick exit]*
7. Sunk Cost Trap (Postgres→MongoDB migration)
8. Micro-Decision (async/await choice) *[Quick exit]*
9. Symptom Stack (basement moisture)
10. Phantom Requirement (GraphQL addition)
11. Scaling Myth (premature microservices)
12. Communication Gap (status dashboard)
13. Production Outage (error logging) *[Quick exit]*
14. Goldilocks Tool (E2E testing paralysis)
15. Political Minefield (code review process)
16. False Dichotomy (management vs IC)
17. Invisible Success Criteria (notification system)
18. Team Capacity Reality (platform engineering)
19. Learning Opportunity (database design) *[Quick exit]*
20. Right Problem Wrong Timing (auth refactor)

---

## Appendix B: Evaluation Framework Quick Reference

### Scoring Sheet Template

```markdown
## Brief Evaluation: [Scenario Name]

**Baseline Comparison**: 8/25 (competent builder without brief)

### Dimension Scores
1. Problem Validation: __/5
2. Solution Justification: __/5
3. Discovery Evidence: __/5
4. Actionability: __/5
5. Efficiency: __/5

**Subtotal: __/25**

### Red Flags
- [ ] Solution unchanged (-3)
- [ ] Zero validation (-3)
- [ ] Validation theater (-3)
- [ ] No metrics (-3)
- [ ] No discovery (-2)
- [ ] Abstract problem (-2)
- [ ] Risk blind (-2)
- [ ] Scope creep (-2)
- [ ] No next steps (-1)
- [ ] Echo chamber (-1)
- [ ] Jargon heavy (-1)
- [ ] No constraints (-1)

**Penalties: -__ points**

### Final Score
**Total: __/25**
**Delta from baseline: +__ points**
**Rating: [Excellent/Good/Marginal/Poor/Harmful]**

### Key Insights
- What worked:
- What didn't:
- Recommendation:
```

---

## Conclusion

**The critical analysis reveals**: `/brief` has real value for specific use cases but systematic limitations that prevent it from being universally applicable.

**The evaluation framework provides**: Objective criteria to measure effectiveness without relying on subjective "feels good" assessments.

**The test scenarios give**: Concrete cases spanning the full range of where brief should excel and where it should fail gracefully.

**Next decision point**: Choose testing approach (manual, hybrid, or deploy-and-learn) based on your risk tolerance and time availability.

**Ultimate goal**: Make `/brief` excellent for its 10-20% sweet spot, and make it gracefully exit or adapt for everything else.
