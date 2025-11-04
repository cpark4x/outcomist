# Outcomist Must-Have Improvements

**Date**: 2025-11-04 (Updated)
**Status**: Captured from 5 successful test scenarios
**Purpose**: Core improvements to nail advisory excellence before adding execution/companion layers

---

## Context

After testing 5 scenarios (office redesign, passive income, cancer prevention, feature decision, client vs product), we identified 4 critical improvements that will elevate Outcomist's advisory excellence from "good" to "must-have."

**Focus**: Nail the advisory layer first, then add execution/companion features later.

---

## 1. Question Quality

### Current State
- Questions are contextual and one-by-one (✅ working well)
- Pattern: Question 4 consistently reveals breakthrough insight across all 3 tests
- BUT: Question quality is ad-hoc, not systematized

### The Opportunity

**Pattern from tests:**
- **Office test**: Q4 revealed multi-use space → personal sanctuary need
- **Passive income test**: Q4 revealed $500K+ capital → entire recommendation pivot
- **Cancer test**: Q1 revealed friend's stage 4 diagnosis → anxiety trigger
- **Feature decision test**: Q3 revealed product positioning contradiction → values crisis
- **Client vs product test**: Q2 revealed $60K savings/12-14 months runway → false scarcity

**The insight:** ONE question consistently unlocks the real problem. Can we get better at identifying which question to ask when?

### What to Build

**Question framework by domain:**

1. **Trigger questions** (always first for health/anxiety/career decisions):
   - "What happened that's making you think about this RIGHT NOW?"
   - "Why now, not 6 months ago or 6 months from now?"

2. **Constraint questions** (for resource decisions):
   - Capital available? (passive income test - game changer)
   - Time available? (office test - revealed renovation appetite)
   - Risk tolerance? (would apply to business decisions)
   - Financial runway? (client vs product test - revealed false scarcity)

3. **Usage/context questions** (for space/design/product decisions):
   - How will you actually use this? (office test - revealed games + personal storage)
   - Who else is involved? (would apply to family/team decisions)

4. **Pattern questions** (for medical/technical decisions):
   - Family history? (cancer test - revealed hereditary pattern)
   - Past attempts? (would apply to health/productivity scenarios)

### Success Criteria

- [ ] Question library organized by decision domain
- [ ] Clear heuristics for "which question to ask when"
- [ ] Pattern: Breakthrough insight occurs by Question 3-4 (not luck, by design)

---

## 2. Adaptive Questioning

### Current State
- Some adaptive questioning happening (✅ passive income test pivoted after Q4)
- BUT: Adaptation is reactive, not systematic

### The Opportunity

**What worked:**
- Passive income: Q4 capital reveal → entire recommendation changed
- Cancer: Q3 cancer types → recognized hereditary pattern → Q4 focused on current approach

**What could improve:**
- After Q2 in cancer test (family history), could have asked about ethnicity (affects genetic testing)
- After Q1 in passive income test (employability anxiety), could have asked about age/stage (affects strategy)

### What to Build

**Adaptive questioning rules:**

1. **After revealing constraint, probe implications:**
   - User reveals capital → Ask about time horizon, risk tolerance, liquidity needs
   - User reveals family history → Ask about ethnicity, specific types, ages of diagnosis

2. **After revealing anxiety, probe depth:**
   - User mentions friend's diagnosis → Ask about relationship, how recent, what type
   - User mentions career fears → Ask about age, years in field, specific triggers

3. **After revealing multi-use context, probe priorities:**
   - User mentions work + personal use → Ask about time allocation, primary use case
   - User mentions multiple stakeholders → Ask about decision power, alignment

### Success Criteria

- [ ] After each answer, system identifies what NEW questions become critical
- [ ] Questions evolve based on previous answers (not just a fixed sequence)
- [ ] Pattern: Recommendations get sharper as discovery deepens

---

## 3. Confidence Calibration

### Current State
- All 3 tests used "high confidence" recommendations
- BUT: Cancer test should have been "medium-high" with earlier caveats

### The Problem

**Current approach:**
- Confidence stated at end of recommendation
- Caveats come late ("I can't diagnose, BUT...")
- Users don't know scope/limitations until after recommendation

**What's missing:**
- Nuanced confidence levels (not just high/medium/low)
- Explicit reasoning for each confidence level
- Upfront caveats about what recommendation CAN'T do

### What to Build

**Confidence framework:**

**High confidence (80-95%):**
- Clear pattern match (seen this many times)
- Complete context (no major unknowns)
- Recommendation is execution-focused (not judgment call)
- Example: Office test - "Man cave refresh" (clear problem-solution fit)

**Medium-high confidence (60-80%):**
- Pattern recognized, but missing some context
- Recommendation points to expert (not final answer)
- Some uncertainty in outcomes
- Example: Cancer test - "Get genetic counseling" (right direction, but can't diagnose)

**Medium confidence (40-60%):**
- Multiple viable paths (no clear winner)
- Significant unknowns remain
- Recommendation is "here's what to explore next"
- Example: Would apply to lose-lose scenarios (RTO policy, pivot decisions)

**Low confidence (20-40%):**
- Insufficient context for strong recommendation
- Need Tier 3 discovery before confident recommendation
- Recommendation is "here's what I'd need to know"

**What to communicate:**
- Confidence level + reasoning UPFRONT (not just at end)
- Explicit caveats ("I can't diagnose, BUT...")
- What would increase confidence ("If I knew X, Y, Z, I could be more confident")

### Success Criteria

- [ ] Confidence levels are nuanced (not just high/medium/low)
- [ ] Reasoning for confidence is explicit and early
- [ ] Caveats about scope/limitations stated upfront
- [ ] Users know what recommendation CAN'T do before acting on it

---

## 4. Pattern Library

### Current State
- Pattern recognition happening ad-hoc (✅ working, but not systematized)
- Each test revealed patterns, but they're not captured for reuse

### The Opportunity

**Patterns identified from 3 tests:**

1. **"Office redesign" → Personal sanctuary need**
   - Signal: Mentions "inspiring," "proud," "excited" (emotional, not functional)
   - Signal: Multi-use space (work + games + personal)
   - Real problem: Creating retreat space, not optimizing work

2. **"Fast food chain" → Employability anxiety**
   - Signal: High-effort business framed as "additional revenue stream" (doesn't match)
   - Signal: Age + innovation team + AI disruption fears
   - Real problem: Hedging against job loss, not entrepreneurship

3. **"Cancer prevention" → Anxiety about being blindsided**
   - Signal: Urgency ("I feel like preventative is the best option")
   - Signal: Recent diagnosis in social circle
   - Real problem: Control over health, not generic prevention

**The insight:** These patterns are REUSABLE across similar scenarios.

### What to Build

**Pattern library structure:**

```markdown
## Pattern: [Name]

**Surface request:** [What user asks for]

**Signals to recognize:**
- [Signal 1]
- [Signal 2]
- [Signal 3]

**Real problem:** [What they're actually trying to solve]

**Key questions to ask:**
1. [Question that reveals this pattern]
2. [Question that deepens understanding]

**Common pitfalls:**
- [What NOT to recommend]
- [What assumptions to challenge]

**Example scenarios:** [Links to test logs]
```

**Initial patterns to capture:**

1. **Personal sanctuary pattern**
   - Surface: Home improvement, office redesign, space optimization
   - Signals: Emotional language, multi-use space, "mine" ownership
   - Real: Creating retreat/escape space

2. **Employability anxiety pattern**
   - Surface: Side business, passive income, skill development
   - Signals: Age concerns, AI/disruption fears, job security mentions
   - Real: Hedging against career uncertainty

3. **Health anxiety pattern**
   - Surface: Prevention, screening, lifestyle optimization
   - Signals: Recent diagnosis in social circle, family history, "catch it early"
   - Real: Control over health outcomes, avoiding being blindsided

4. **"Additional revenue" misframing pattern**
   - Surface: Starting business, side hustle, passive income
   - Signals: High-effort option framed as "additional" (doesn't match)
   - Real: Either security hedge OR wrong solution entirely

5. **Popularity contest hiding identity crisis pattern** (Feature Decision test)
   - Surface: Feature prioritization decision (10 customers vs 2 customers)
   - Signals: Framed as count vs value, features serve opposite stakeholders, one "controversial"
   - Real: Product identity crisis - must choose who you're building for

6. **Scarcity mindset hiding opportunity pattern** (Client vs Product test)
   - Surface: "Stable money vs risky thing" decision
   - Signals: Fear language ("market is tough"), strong fundamentals contradicting scarcity
   - Real: Fear preventing commitment despite having resources and validation

### Success Criteria

- [ ] Pattern library with 10+ patterns documented
- [ ] Each pattern has: signals, real problem, key questions, pitfalls
- [ ] Patterns link to test logs (examples of pattern in action)
- [ ] New scenarios can quickly match against pattern library

---

## Implementation Priority

**Phase 1: Question Quality** (1-2 weeks)
- Build question library organized by domain
- Document heuristics for "which question when"
- Test with 5 new scenarios from test-scenarios.md

**Phase 2: Pattern Library** (1-2 weeks)
- Capture patterns from all tests (current + new)
- Document structure: signals, real problem, questions, pitfalls
- Build pattern matching system

**Phase 3: Adaptive Questioning** (2-3 weeks)
- Rules for "after X answer, ask Y next"
- Test adaptation with complex scenarios (lose-lose, incomplete info)
- Measure: Do recommendations get sharper as discovery deepens?

**Phase 4: Confidence Calibration** (1 week)
- Define confidence levels with explicit criteria
- Add upfront caveats/reasoning
- Test with medical/high-stakes scenarios

---

## Future Enhancements (NOT NOW)

**Execution Layer:**
- Draft emails, find providers, pre-fill forms
- Reduce friction from advice → action

**Decision Companion:**
- Track decisions over time
- Connect decisions across domains
- Check in on implementation

**Expert Network Integration:**
- Connect to specialists directly
- Pre-brief experts with discovery context

**These are important, but ONLY after advisory excellence is nailed.**

---

## Success Metrics for Advisory Excellence

**Before adding execution/companion layers, we must hit:**

1. ✅ **5 test scenarios completed** (office, passive income, cancer, feature decision, client vs product)
2. ⏳ **10+ test scenarios validated** (from test-scenarios.md) - 50% complete
3. ⏳ **Question quality framework implemented** (question library + heuristics)
4. ⏳ **Pattern library built** (10+ patterns documented) - 60% complete (6 patterns captured)
5. ⏳ **Adaptive questioning working** (questions evolve based on answers)
6. ⏳ **Confidence calibration refined** (nuanced levels + upfront caveats)
7. ✅ **User validation consistently positive** (every test scenario validated)

**Only then do we add execution/companion layers.**

---

**Status**: ✅ 50% toward pattern library goal (5 of 10+ scenarios tested, 6 patterns captured)
**Next**: Test 5 more scenarios to complete pattern library and validate question framework
