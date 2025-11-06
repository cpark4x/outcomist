# Self-Learning Pattern System (Future Design)

**Status**: Parked for future discussion
**Date**: 2025-11-06
**Context**: After shipping v4.3 with adaptive fork patterns, user wants to explore how Outcomist can learn new patterns through usage

---

## The Vision

**Goal**: Outcomist becomes smarter over time by capturing patterns from real usage, not just manual curation.

**How it would work:**
1. User runs `/explore` on a decision
2. Discovery reveals a pattern (surface framing → real problem)
3. System captures: initial framing, questions that worked, breakthrough moment, recommendation
4. Pattern gets added to library
5. Future users with similar decisions benefit from the pattern

**Key question from user**: "Should we make this recursive so that as it learns new patterns through usage, it adds them?"

---

## Potential Additional Fork Patterns

Beyond the 5 current forks (Existence, Prioritization, Execution, Timing, Audience), these could be added:

### 1. Resource Fork (Budget/Time/Energy Allocation)
**When detected:** "How should I spend...", "Where should I invest...", resource allocation language

**Fork options:**
- **Optimize current allocation** → Analyze what's working/not working
- **Explore new allocation** → Identify opportunities not yet invested in

**Use cases:** Time management, budget allocation, energy/focus decisions

### 2. Stakeholder Fork (Who vs What)
**When detected:** "Who should...", mentions of multiple people/groups, political/organizational language

**Fork options:**
- **Understand stakeholder needs** → Map who cares and why
- **Assess organizational dynamics** → Understand power/politics at play

**Use cases:** Office politics, team leadership, already partially in Audience fork

### 3. Risk Fork (Safety vs Opportunity)
**When detected:** "Is it safe to...", "Should I take the risk...", risk/safety language

**Fork options:**
- **Understand downside** → Map what could go wrong
- **Understand upside** → Map what you'd gain if it works

**Use cases:** Investment decisions, career moves, already partially in Existence fork

### 4. Recovery Fork (Fix vs Pivot)
**When detected:** "Something went wrong...", "How do I fix...", failure/problem language

**Fork options:**
- **Fix what's broken** → Understand what failed and how to repair
- **Pivot to new approach** → Explore whether to cut losses and try different

**Use cases:** Failed product launches, broken relationships, project failures

---

## Technical Approaches Discussed

### Option 1: Manual Pattern Capture (Current State)
**How it works:**
- Manually review test logs
- Extract patterns into `docs/patterns/pattern-library.md`
- Update fork detection logic in `.claude/commands/explore.md`

**Pros:** Quality control, intentional curation
**Cons:** Slow, doesn't scale, requires human review

### Option 2: Semi-Automated Pattern Capture
**How it could work:**
```
After each `/explore` session:
1. User rates session (helpful/not helpful)
2. If helpful, ask: "New pattern or existing one?"
3. If new, capture: initial framing, real problem, key questions, recommendation
4. Write to patterns/discovered/ directory
5. Human reviews and promotes to main library
```

**Pros:** Faster capture, user participation, human quality control
**Cons:** Still requires human review, adds friction for users

### Option 3: Fully Automated Pattern Mining
**How it could work:**
```
Background process:
1. Analyze all `/explore` sessions
2. Cluster similar decision framings
3. Identify common question sequences
4. Extract pattern templates
5. Propose new fork patterns
6. Test against historical sessions
7. Auto-deploy if performance improvement detected
```

**Pros:** Fully automated, scales infinitely, continuous improvement
**Cons:** Complex, requires significant data, risk of overfitting

---

## The Recursive Pattern Learning Challenge

**The Good Recursion:**
- Pattern library grows → Fork detection improves → More patterns captured
- Each improvement compounds on previous ones
- System gets smarter over time

**The Bad Recursion:**
- Too many patterns → Detection logic becomes brittle
- Edge cases multiply → False positives increase
- Overfitting → System loses generalization ability

**The Balance:**
Need a **pruning mechanism** alongside growth:
- Patterns that don't improve outcomes get retired
- Similar patterns get merged
- Pattern library stays at optimal size (10-20 patterns, not 1000)

---

## Recommended Hybrid Approach

**Phase 1: Enhanced Manual Capture (Next 3-6 months)**
Add tooling to make manual pattern capture easier:
- `/capture-pattern` command after test sessions
- Asks: initial framing, real problem, breakthrough question, best fork
- Outputs: draft pattern markdown + suggested detection logic

**Phase 2: Pattern Analytics (6-12 months)**
Add analytics to existing patterns:
- Which patterns match most frequently?
- Which fork options get chosen?
- Which patterns lead to highest satisfaction?
- Enables: pattern retirement, fork refinement, detection improvement

**Phase 3: Semi-Automated Discovery (12+ months)**
Once you have 50+ sessions and solid analytics:
- Pattern mining agent clusters similar decisions
- Identifies common question sequences
- Proposes new patterns
- Human reviews and approves

---

## Key Design Decisions (Unresolved)

### Question 1: Where does pattern data live?
- Option A: Local files (`patterns/captured/session-*.md`)
- Option B: Database (SQLite for simplicity)
- Option C: Git repo (version controlled patterns)

**Tentative recommendation:** Git repo for now (version control), database later (analytics)

### Question 2: How do you measure "pattern quality"?
- User satisfaction rating after session
- Breakthrough moment (user says "yes, that's it!")
- Time to recommendation (faster = better pattern match)
- Return usage (user comes back = pattern worked)

**Tentative recommendation:** Start with user satisfaction, add others over time

### Question 3: When do patterns get promoted to main library?
- After N successful uses (e.g., 3 sessions)
- After human review confirms quality
- After validation against test scenarios
- After fork detection logic written and tested

**Tentative recommendation:** All of the above (quality > quantity)

---

## Immediate Next Steps (If We Pursue This)

1. **Add session logging to `/explore`**
   - Log to `.outcomist/sessions/YYYY-MM-DD-HH-MM-SS.md`
   - Contains: decision, fork chosen, questions, answers, recommendation, satisfaction

2. **Create `/analyze-sessions` command**
   - Reviews recent sessions
   - Suggests: recurring patterns, breakthrough questions, missing forks

3. **Add pattern validation tool**
   - `/validate-pattern [pattern-file]`
   - Tests: detection logic on test cases, improvement vs existing forks, false positives

---

## User's Perspective

**User said:** "I want to capture patterns through usage. Not sure if this is possible."

**User also said:** "Let's park this discussion. I want to revisit it later. I have different thoughts but don't have time to solve it now."

**Status:** Parked pending user's thoughts on implementation approach.

---

## Context for Future Sessions

**What we just shipped (v4.3):**
- 5 adaptive fork patterns replace hardcoded "validation vs guidance"
- Evidence from 9 test cases: 88% improvement rate, 0% regression
- Improved formatting with headers, blockquotes, proper spacing

**Why this matters:**
- v4.3 proves adaptive forks work better than hardcoded
- Next evolution: forks that adapt not just per-session, but across all users over time
- Self-learning would compound the v4.3 improvements

**Open questions:**
- User has "different thoughts" on how this should work (not yet shared)
- Need to balance automation vs quality control
- Need to solve the "too many patterns" problem (pruning mechanism)
- Implementation timeline and priority vs other features

---

**Next steps when revisiting:**
1. User shares their thoughts on how self-learning should work
2. Decide on implementation approach (manual → semi-automated → automated)
3. Define pattern quality metrics
4. Build Phase 1 tooling (session logging + `/capture-pattern`)
