# Outcomist Pattern Library

**Last Updated**: 2025-11-05
**Status**: 9 patterns captured from 8 test scenarios
**Goal**: 10+ patterns for robust decision exploration

---

## How to Use This Library

When a user describes their decision, scan these patterns to identify potential matches. Patterns help you:
1. **Recognize deeper issues** beneath surface requests
2. **Ask better questions** specific to the pattern
3. **Avoid common pitfalls** that lead to bad recommendations

**Remember**: Patterns are recognition tools, not rigid rules. Use them to inform discovery, not replace it.

---

## Pattern 1: Personal Sanctuary Pattern

**Surface request**: Home improvement, office redesign, space optimization

**Signals to recognize**:
- Emotional language: "inspiring," "proud," "excited" (not functional benefits)
- Multi-use space mentioned: work + games + personal storage
- "Mine" ownership language: "my space," "where I can..."
- Renovation appetite: Willing to invest time/money in transformation

**Real problem**: Creating retreat/escape space, not optimizing productivity

**Key questions to ask**:
1. How will you actually use this space beyond work?
2. What activities make you feel most yourself?
3. Who else uses or accesses this space?
4. What's your appetite for renovation vs. refresh?

**Common pitfalls**:
- Treating as pure work optimization (ergonomic chair, standing desk)
- Missing the emotional/personal dimension
- Recommending minimal changes when transformation desired

**Example scenario**: [Office redesign test](../../archive/test-logs/TEST_LOG_NOV3_OFFICE.md) - User wanted "inspiring office" but real need was personal sanctuary with games, personal memorabilia, and retreat space.

---

## Pattern 2: Employability Anxiety Pattern

**Surface request**: Side business, passive income, skill development, "additional revenue"

**Signals to recognize**:
- Age concerns: "I'm 45," "been doing this 20 years"
- AI/disruption fears: Mentions automation, AI replacing jobs
- Job security language: "market is tough," "just in case"
- High-effort option framed as "additional" (doesn't match - why work so hard for "extra" money?)
- Innovation/cutting-edge team member feeling vulnerable

**Real problem**: Hedging against career uncertainty, not entrepreneurship

**Key questions to ask**:
1. What triggered you thinking about this RIGHT NOW?
2. How secure does your current job feel? (1-10)
3. If money weren't a concern, would you still want to do this?
4. What's your capital situation? (might reveal better hedging strategies)

**Common pitfalls**:
- Taking "side business" request at face value
- Recommending entrepreneurship when real need is career insurance
- Missing that "additional revenue" framing contradicts high effort required
- Not exploring less-effort hedging options (savings, passive investments)

**Example scenario**: [Passive income test](../../archive/test-logs/TEST_LOG_NOV3_PASSIVE_INCOME.md) - User wanted "fast food franchise for additional revenue" but real issue was employability anxiety. Had $500K+ capital - better hedge was passive income, not high-effort business.

---

## Pattern 3: Health Anxiety Pattern

**Surface request**: Prevention, screening, lifestyle optimization, "catch it early"

**Signals to recognize**:
- Recent diagnosis in social circle: Friend, family member, colleague
- Family history mentioned: Multiple relatives with same condition
- Urgency language: "I feel like I should," "I need to do something"
- "Catch it early" framing: Focus on detection over actual risk reduction
- Trigger timing: Right after someone else's diagnosis

**Real problem**: Control over health outcomes, avoiding being blindsided (not generic prevention)

**Key questions to ask**:
1. What happened that's making you think about this RIGHT NOW?
2. What types of cancer/conditions run in your family?
3. At what ages were family members diagnosed?
4. What's your ethnicity? (affects genetic testing recommendations)
5. What screening are you currently doing?

**Common pitfalls**:
- Generic "eat healthy, exercise" advice
- Missing the anxiety trigger (recent diagnosis)
- Not recognizing hereditary patterns that change risk profile
- Treating all prevention the same (hereditary vs. lifestyle vs. random)

**Example scenario**: [Cancer prevention test](../../archive/test-logs/TEST_LOG_NOV3_CANCER_PREVENTION.md) - User wanted "preventative measures" after friend's stage 4 diagnosis. Family history revealed hereditary pattern (colon, pancreatic, breast cancer early-onset) → genetic counseling recommended, not generic screening.

---

## Pattern 4: "Additional Revenue" Misframing Pattern

**Surface request**: Starting business, side hustle, passive income

**Signals to recognize**:
- High-effort option (franchise, business) framed as "additional" revenue
- Mismatch between effort and "additional" language
- Core revenue already exists and stable
- No clear entrepreneurial passion mentioned
- Defensive/hedging language: "just in case," "to be safe"

**Real problem**: Either security hedge OR wrong solution entirely

**Key questions to ask**:
1. Why do you need additional revenue? (often reveals security fears)
2. How much time/effort are you willing to invest?
3. What's your current financial situation? (capital, savings, runway)
4. If you had $X already, would you still want to do this?

**Common pitfalls**:
- Not catching the effort/framing mismatch
- Assuming entrepreneurial motivation when it's security seeking
- Recommending business when passive investment better fits need
- Missing capital availability that changes recommendation entirely

**Example scenario**: [Passive income test](../../archive/test-logs/TEST_LOG_NOV3_PASSIVE_INCOME.md) - "Fast food franchise for additional revenue" (high-effort) didn't match "additional" framing. Real issue: employability hedge with $500K+ capital available.

---

## Pattern 5: Popularity Contest Hiding Identity Crisis

**Surface request**: Feature prioritization decision (customer count-based)

**Signals to recognize**:
- Framed as COUNT vs VALUE: "10 customers want X, 2 want Y"
- Features serve opposite stakeholders: Employers vs. employees, users vs. admins
- One feature described as "controversial" or "politically loaded"
- Product positioning contradiction: "Employees first" but feature serves employers
- "Nice-to-have" from many vs. "make-or-break" from few

**Real problem**: Product identity crisis - must choose who you're building for

**Key questions to ask**:
1. What's your product positioning? Who do you claim to serve?
2. Who actually requested the popular feature? (Top-down or bottom-up?)
3. What's the political/cultural context? Why is it controversial?
4. Does this feature align with your stated values?
5. What happens if you DON'T build the popular feature? (often: nothing)

**Common pitfalls**:
- Optimizing for customer count instead of values alignment
- Treating feature prioritization as pure ROI calculation
- Missing that "nice-to-have" from many < "make-or-break" from few
- Not recognizing when features lock you into positioning
- Assuming more customers = better decision

**Example scenario**: [Feature decision test](../../archive/test-logs/TEST_LOG_NOV4_FEATURE_DECISION.md) - "10 customers want workplace presence (RTO tool), 2 want exclude list (safety feature)." Real issue: Product identity crisis. Can't serve both employers (surveillance) and employees (privacy/safety).

---

## Pattern 6: Scarcity Mindset Hiding Opportunity

**Surface request**: "Stable money vs risky thing" decision

**Signals to recognize**:
- Fear-based language: "market is tough," "I'm thankful," "playing it safe"
- Strong fundamentals contradicting scarcity narrative: Growth, savings, runway
- Underpriced "stable" option: Below-market rates framed as opportunity
- Inflection point timing: Growth momentum that would be lost if paused
- Framing choice as "safety vs risk" when math shows risk is minimal

**Real problem**: Fear preventing commitment to opportunity despite having resources and validation

**Key questions to ask**:
1. What's your actual financial runway? (reveal false scarcity)
2. What are the fundamentals of what you're "risking"? (reveal strength)
3. What's the hourly rate of the "stable" option? (reveal if underpriced)
4. What happens if you pause momentum? (reveal opportunity cost)

**Common pitfalls**:
- Accepting "market is tough" without challenging with user's own metrics
- Validating fear-based decision when fundamentals are strong
- Treating "stable money" as inherently better than "risky growth"
- Missing that low-rate work can be distraction from inflection point
- Not recognizing scarcity mindset despite substantial runway

**Example scenario**: [Client vs product test](../../archive/test-logs/TEST_LOG_NOV4_CLIENT_VS_PRODUCT.md) - "$6K/month client (stable) vs $2K MRR product (risky)." Reality: $60K savings (12-14 months runway), product 4X growth in 6 months, 97% retention. Client was $40/hour (below market). Scarcity in head, not bank account.

---

## Pattern 7: Solution Looking for Problem

**Surface request**: Build a product/app/feature

**Signals to recognize**:
- "I had an idea... thought it would be cool/useful"
- No research done upfront
- Lists features before identifying who/why
- **Can't articulate core pain point when asked directly**
- First-time builder with limited time
- Excitement-driven, not problem-driven
- Jumps to comprehensive feature list immediately

**Real problem**: Wants to build something, picked an idea that sounds good, hasn't validated it's worth months of work

**Key questions to ask**:
1. What triggered this idea RIGHT NOW? (reveals spontaneous vs researched)
2. What's your track record with side projects? (reveals if serial starter or first-timer)
3. How much time can you realistically commit? (reveals if timeline is feasible)
4. Have you validated this with potential users? (reveals depth of validation)
5. **What's the ONE problem you're solving?** (reveals if they know the core pain point)

**Common pitfalls**:
- Taking feature list at face value (they described WHAT, not WHY)
- Not challenging lack of validation
- Missing that first-time builders underestimate shipping time by 3-5x
- Assuming excitement = validation
- Not asking about core pain point explicitly
- Recommending "just build it" when they haven't validated demand

**Example scenario**: [Meal planning app test](../../archive/test-logs/TEST_LOG_NOV4_MEAL_PLANNING_APP.md) - User wanted to build comprehensive meal planning app (custom plans, recipes, shopping lists, nutrition tracking). First-time builder, 5-10 hrs/week, couldn't answer "What's the ONE problem frustrating you most?" Revealed: solution-first, not problem-first thinking.

---

## Pattern 8: Premature Presentation (Presenting Without Proof)

**Surface request**: Help me prepare a presentation for leadership/stakeholders

**Signals to recognize**:
- Excited about vision/project
- **No measurable results yet** to back up the ask
- **Unclear what they're asking for** ("just a check-in", "not sure")
- Skeptics already exist in the audience
- Top-level support but middle management doubt
- Wants adoption/behavior change without proof
- Timing driven by excitement, not strategy

**Real problem**: Presenting too early out of excitement, not readiness. Will burn credibility on "we might have something" when they could wait and present "we DO have something."

**Key questions to ask**:
1. What does the audience currently know? (reveals awareness vs skepticism)
2. What specific decision are you asking them to make? (reveals if ask is clear)
3. What's the current adoption/results status? (reveals if they have proof)
4. What happens if they say "prove it first"? (reveals if timeline is flexible)
5. **What's driving the timing - why now vs later?** (reveals if it's excitement vs necessity)
6. Are you under threat that requires immediate action? (reveals true urgency)

**Common pitfalls**:
- Taking "prepare presentation" request at face value
- Not challenging whether they should present at all
- Missing the credibility gap (big ask, no proof)
- Not questioning unclear ask ("not sure what I want")
- Assuming excitement = readiness to present
- Not asking about strategic timing

**Example scenario**: [Amplifier SLT presentation test](../../archive/test-logs/TEST_LOG_NOV4_AMPLIFIER_PRESENTATION.md) - User wanted to present Amplifier project to SLT for "awareness, air cover, and pivot teams." Reality: No results yet, handful of users, unclear ask ("just a check-in, not sure"), middle management skeptics. Recommendation: DON'T present now, build proof first (3-6 months), then present with clear results and ask.

---

## Pattern 9: Stuck in Build Phase (No-Code/LLM Builders)

**Surface request**: Help me finish/accelerate my product build

**Signals to recognize**:
- Ambitious roadmap (many epics, 100+ user stories)
- **Cannot get ONE flow to reviewable/demo state**
- Mentions "LLM limitations" or tools as blocker
- Has infrastructure but no end-to-end demo
- Non-technical (no-code, uses AI to "vibe code")
- Focuses on features/stories, not working product
- Stuck in build phase, can't reach review phase
- Needs to "fail fast" but building comprehensive solution

**Real problem**: Scope management, not technical limitations. Building 179 things when they need 1 working demo. Wrong prompt strategy for LLM (asking for "features" instead of "demo").

**Key questions to ask**:
1. **"Do you have something reviewable right now (demo, video, screenshot, prototype) or is it all in-progress?"** (reveals if stuck in build phase)
2. **"Show me the docs that need scrubbing"** (reveals scope - often 100+ stories)
3. **"Walk me through your typical workflow when you [build with AI]. Where does it usually break down?"** (reveals LLM is building infrastructure, not demos)
4. "What does 'complete' look like for ONE feature?" (reveals definition is too comprehensive)
5. "What currently EXISTS vs what's BROKEN?" (reveals if problem is scope vs bugs)

**Common pitfalls**:
- Taking "LLM limitations" at face value (it's usually scope, not AI capability)
- Recommending better prompts when real issue is ruthless scope cut
- Not probing for reviewable artifacts early
- Treating as technical problem when it's product strategy problem
- Missing that no-code users need demo-first, not architecture-first approach
- Not recognizing that LLMs are GREAT at demos, TERRIBLE at comprehensive systems

**What they need**:
1. **Scope reality check** - "You're building 179 things when you need 1 thing"
2. **Concrete 'done' definition** - "Demo-ready = 2-min screencast", not "production-ready"
3. **Permission to fake it** - "Hardcode everything not in hero flow"
4. **Executable artifact** - Not just advice, but DEMO_V1.md they can hand to LLM
5. **Co-creation support** - Help them create the scoped spec together

**Why this pattern emerges with LLM builders**:
- Users who don't code rely on LLM for everything
- LLMs are GREAT at: copying patterns, hardcoding demos, vertical slices
- LLMs are TERRIBLE at: architecture, anticipating edge cases, knowing "done"
- Users ask for "features" → LLM builds infrastructure → never reaches reviewable state
- Users need to ask for "demo" → LLM builds visible UI → can actually review

**Example scenario**: [Stuck in Build Phase test - Test #9](../../TEST_SCENARIO_9_REPORT.md) - User had 179 stories across 4 epics, couldn't get ONE to reviewable state. Blamed "LLM limitations" but real issue was scope. Needed demo-first strategy: 7-step hero flow, hardcode everything else, success = 2-min screencast. Co-created DEMO_V1.md together.

---

## Pattern Analysis

### Common Themes Across Patterns

1. **Surface vs. Depth**: All patterns show surface requests hiding deeper issues
2. **Emotional Triggers**: Recent events (diagnosis, job fears, friend's situation) drive decisions
3. **Framing Mismatch**: How user frames decision often contradicts actual situation
4. **Constraint Revelation**: Key question unlocks pattern (Q2 runway, Q4 capital, Q3 cancer types)
5. **Values Alignment**: Decisions often about identity, not optimization

### When to Apply Multiple Patterns

Some decisions match multiple patterns:
- **Employability anxiety** + **"Additional revenue" misframing**: Passive income test
- **Health anxiety** + **Control seeking**: Cancer prevention test
- **Scarcity mindset** + **Underpricing work**: Client vs product test
- **Solution looking for problem** + **First-time builder**: Meal planning app test
- **Premature presentation** + **Unclear ask**: Amplifier SLT presentation test
- **Stuck in build phase** + **Solution looking for problem**: No-code builders with ambitious scope

Use pattern combinations to deepen understanding, not confuse the issue.

---

## Adding New Patterns

As you test more scenarios, capture new patterns using this template:

```markdown
## Pattern N: [Name]

**Surface request**: [What user asks for]

**Signals to recognize**:
- [Signal 1]
- [Signal 2]
- [Signal 3]

**Real problem**: [What they're actually trying to solve]

**Key questions to ask**:
1. [Question that reveals this pattern]
2. [Question that deepens understanding]
3. [Question that challenges assumptions]

**Common pitfalls**:
- [What NOT to recommend]
- [What assumptions to challenge]
- [What to watch out for]

**Example scenario**: [Link to test log]
```

---

## Next Patterns to Capture

**Target**: 10+ patterns total

**Remaining test scenarios that might reveal new patterns**:
- Lose-lose scenarios (RTO policy #8, Pivot decision #16)
- Time pressure decisions (Job offer #7, Competitive feature #17)
- Ethical dilemmas (Manipulate metrics #19)
- Systemic problems (Meeting overload #18)
- Post-success regret (Sold company #15)

---

## Links

- [Question Framework](./question-framework.md) - Question quality heuristics
- [Test Scenarios](../testing/test-scenarios.md) - Full list of 20 scenarios
- [Test Logs](../../archive/test-logs/) - Detailed test documentation
