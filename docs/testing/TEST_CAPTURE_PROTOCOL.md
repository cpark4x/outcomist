# Test Capture Protocol (Internal AI Guideline)

**Purpose**: Claude Code must automatically capture every real-world test during the conversation.

**Last Updated**: 2025-01-07

**Target Audience**: Claude Code agent (not user-facing)

---

## The Problem

**What happened before**:
- Tests conducted but not captured until weeks later
- Test results existed only in conversation history
- Can't rerun tests for regression validation
- User had to manually extract and document

**Example**: Test #12 and #13 were only in conversation until extracted weeks later.

**The fix**: Claude Code proactively captures tests AS THEY HAPPEN.

---

## Claude Code's Automatic Test Capture

### Detection: Recognize When Test Starts

**Signals that a test is beginning**:
- User says: "test this", "try this scenario", "validate this"
- User runs `/explore` with explicit test intent
- User provides decision statement for evaluation
- Context suggests this is regression testing

**As soon as detected**, immediately:

### Step 1: Auto-Create Test Scenario Entry

**Without asking user**, create the test scenario entry in `docs/testing/test-scenarios.md`:

1. Open `/docs/testing/test-scenarios.md`
2. Add new test with this template:

```markdown
## Test #[N]: [Short Name]

**User**: [Name or Anonymous]
**Date**: [YYYY-MM-DD]
**Decision Type**: [Prioritization/Feature/Strategy/etc.]

### Decision Statement
```
[Exact copy-paste of user's decision request]
```

### Context Provided
[Any additional context user provided upfront]

### Expected Challenges
- [What pattern might apply?]
- [What trade-offs might exist?]
- [What factual validation needed?]
```

### Step 2: During Test - Mental Notes

**Track key moments** (don't interrupt test flow):
- User's initial framing
- Each discovery round (Q&A)
- Pattern recognition moments
- User's reactions

**Keep these in working memory for result file.**

### Step 3: Immediately After Test Completes

**As soon as test ends** (user says "done", "thanks", or conversation shifts), create the result file:

1. Navigate to `/docs/testing/results/`
2. Create `test-[ID]-results-v[VERSION].md`
3. Use this structure:

```markdown
# Test #[N] Results - v[VERSION]

**Test**: [Name]
**Version**: v[VERSION]
**Date Tested**: [YYYY-MM-DD]
**Tester**: [Name]
**Score**: [⭐⭐⭐⭐⭐ / 5]

---

## Decision Statement
[Copy from test-scenarios.md]

---

## Tier 1 Response
[What Outcomist said initially]

---

## Discovery Session

### Round 1
**Q1**: [Question]
**A1**: [Answer]

[Continue for all rounds]

---

## Recommendation Provided
[What was recommended and why]

---

## User Feedback
[Direct quotes or paraphrase of user's reaction]

---

## What Worked
[✅ List what worked well]

---

## What Failed
[❌ List what didn't work]

---

## Key Learnings
[Major insights from this test]

---

**Date Documented**: [YYYY-MM-DD]
**Status**: [Pattern captured / Capability validated / Failure analyzed]
```

### Step 4: Auto-Update STATUS.md

**Without asking user**:
1. Open `/docs/testing/results/STATUS.md`
2. Add test to "Documented Results" section
3. Update the summary table with test number, name, version, score, status

### Step 5: Notify User

**After all files created**, tell user:
```
✅ Test #[N] captured:
- Scenario: docs/testing/test-scenarios.md
- Results: docs/testing/results/test-[N]-results-v[VERSION].md
- STATUS updated
```

**User can review or ignore - documentation is done.**

---

## Claude Code's Internal Checklist

**When test starts**:
- [ ] Recognize test is beginning
- [ ] Auto-create scenario entry in test-scenarios.md
- [ ] Track key moments during test

**When test ends**:
- [ ] Immediately create result file
- [ ] Update STATUS.md
- [ ] Notify user that test was captured
- [ ] If new pattern detected, update pattern library

**No user action required** - this is automatic.

---

## Quick Templates

### Scenario Template (Copy-Paste Ready)

```markdown
## Test #[N]: [Short Name]

**User**: [Name]
**Date**: 2025-01-07
**Decision Type**: [Type]

### Decision Statement
```
[User's request]
```

### Context Provided
[Additional context]

### Expected Challenges
- [Challenge 1]
- [Challenge 2]
```

### Result Template (Copy-Paste Ready)

```markdown
# Test #[N] Results - v4.6

**Test**: [Name]
**Version**: v4.6
**Date Tested**: 2025-01-07
**Tester**: [Name]
**Score**: [⭐ score]

---

## Decision Statement
[Copy from scenarios]

---

## Tier 1 Response
[Initial response]

---

## Discovery Session
[Q&A rounds]

---

## Recommendation Provided
[What was recommended]

---

## User Feedback
[User's reaction]

---

## What Worked / Failed / Learned
[Analysis]
```

---

## Exception Handling

### "I forgot to document before the test"

**Fix**: Document immediately after, note "retrospective documentation" in result file.

### "Test was informal/quick"

**Still document it**: Even 2-minute tests provide validation. Use abbreviated format.

### "User feedback was minimal"

**Document what you have**: "User accepted recommendation" or "No explicit feedback" is still data.

### "Test revealed no new insights"

**Still valuable**: Successful pattern application is worth documenting for regression validation.

---

## Examples

### Good Test Capture (Test #12)

**What was captured**:
- Decision statement in test-scenarios.md
- Full transcript with Q&A rounds
- Factual error identified and documented
- User feedback: "never surfaced the trade-off"
- Impact: Triggered v4.6 implementation

**Result**: Complete understanding of failure mode, led to improvement.

### Bad Test Capture (hypothetical)

**What would be lost**:
- "We tested something about diving vacations"
- No decision statement = can't rerun
- No transcript = can't analyze what failed
- No user feedback = don't know if it worked

**Result**: Wasted test, no learning captured.

---

## Success Metrics

**Good test documentation enables**:
1. **Regression testing**: Copy decision statement, rerun with new version
2. **Pattern validation**: See which patterns work in real scenarios
3. **Failure analysis**: Understand exactly what broke and why
4. **Version comparison**: Test #12 v4.5 (failed) vs v4.6 (should pass)

**We know this is working when**:
- Every test has scenario + result files
- Can rerun any test in < 5 minutes
- No "missing test documentation" gaps
- Pattern library examples all link to test results

---

## Automation Ideas (Future)

1. **Pre-test reminder**: Script that checks if test scenario exists before starting
2. **Post-test prompt**: "Test complete - create result file now? (Y/n)"
3. **Weekly report**: List all pending documentation automatically
4. **Template generator**: CLI that creates files from user input

**For now**: Manual protocol, enforced through discipline and checklists.

---

## Links

- [Test Scenarios](./test-scenarios.md) - Single source of truth
- [Test Results](./results/) - Version-specific outcomes
- [STATUS.md](./results/STATUS.md) - Documentation progress
- [Pattern Library](../patterns/pattern-library.md) - Pattern examples

---

**Remember**: Tests without documentation are tests that never happened. Capture everything, immediately.
