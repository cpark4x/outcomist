# Tier 1 Format Improvement: Question-First Design

**Date:** 2025-01-06
**Issue:** Generic fork pattern templates confusing users when they don't match decision context
**Solution:** Question-first format that shows explicit questions instead of abstract fork options

---

## The Problem

### User Feedback
> "this is not good. it's confusing"

**Context:** User asked `/explore what should we work on next for outcomist?` and received a Prioritization fork with options:
- "Compare alternatives"
- "Understand current state"

**Why it failed:** These generic options didn't match the meta-decision context. User couldn't parse what was actually being asked.

### Root Cause
The v4.3 adaptive fork patterns work well for typical user decisions with clear framing, but struggle with:
- Meta decisions (about the product itself)
- Open-ended strategic planning questions
- Cases where fork templates don't adapt to specific context
- Product owner decisions vs end-user decisions

---

## The Solution: Question-First Format

### Design Principle
**Lead with the actual questions you'll ask**, not abstract fork pattern templates.

### Format Structure

```markdown
# Tier 1: Pattern Recognition

[PARAGRAPH 1: Pattern identification and reframe (30-50 words)]

> **[Key reframe as blockquote - the "real question"]**

[PARAGRAPH 2: Create hunger - hint at complexity without solving (40-60 words)]

---

### Here's what I need to understand:

**To [outcome user wants], I need to explore:**

1. **[Concrete question 1]** - [Why this matters / what it reveals]
2. **[Concrete question 2]** - [Why this matters / what it reveals]
3. **[Concrete question 3]** - [Why this matters / what it reveals]
4. **[Concrete question 4]** - [Why this matters / what it reveals]

*I'll ask 4-5 questions (~10 min), then deliver a clear recommendation.*

---

### Ready to dig in?

Reply with:
- **"yes"** to start discovery
- **"show me"** to see the first question now
- **Ask anything** if you need clarification
```

---

## Before/After Examples

### Example 1: Meta-Decision (The Failing Case)

**Question:** `/explore what should we work on next for outcomist?`

#### BEFORE (v4.3 with Fork Template):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "what should we work on next?" - but that's not the real question.

> **The real question is: "Where should Outcomist focus energy to maximize impact vs effort?"**

This is a prioritization decision disguised as a roadmap question.

---

### Two Ways to Explore This

Which path would help you more right now?

**Compare alternatives**
- Evaluate different feature options against each other
- Which feature delivers most value for effort?

**Understand current state**
- Map what's working and what's blocking progress
- Where are users getting stuck today?

*Or just say "show me" and I'll ask the first question.*

---

### What happens next

I'll ask 4-5 questions (~10 min) tailored to whichever path you choose, then deliver a clear recommendation.
```

**User reaction:** "this is not good. it's confusing"

#### AFTER (Question-First Format):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "what should we work on next?" - but that's not the real question.

> **The real question is: "Where should Outcomist focus energy to maximize impact vs effort?"**

This is a prioritization decision disguised as a roadmap question. You need to compare what you *could* build against what will *actually move the needle* for users.

---

### Here's what I need to understand:

**To recommend the highest-impact next move, I need to explore:**

1. **What's blocking users today?** - Where do sessions break down or fail to deliver value?
2. **What features are on your radar?** - What improvements are you considering?
3. **What's your capacity?** - How much complexity can you take on right now?
4. **What does success look like?** - More users? Better outcomes? Specific metrics?

*I'll ask 4-5 questions (~10 min) to understand these dimensions, then deliver a clear recommendation on where to focus next.*

---

### Ready to dig in?

Reply with:
- **"yes"** to start discovery
- **"show me"** to see the first question now
- **Ask anything** if you need clarification
```

**Expected improvement:** User can see exactly what territory will be explored without abstract fork options.

---

### Example 2: Prioritization Decision (Typical Case)

**Question:** `/explore should I build feature X or feature Y?`

#### BEFORE (v4.3 with Fork Template):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "should I build X or Y?" - but that's not the real question.

> **The real question is: "Which feature aligns better with my goals and constraints?"**

This looks like a binary choice, but really you're prioritizing based on multiple dimensions.

---

### Two Ways to Explore This

Which path would help you more right now?

**Compare alternatives**
- Evaluate Feature X vs Feature Y head-to-head
- Which delivers more value for effort?

**Understand current state**
- Map your goals and constraints first
- What's most important to optimize for?

*Or just say "show me" and I'll ask the first question.*

---

### What happens next

I'll ask 4-5 questions (~10 min) tailored to whichever path you choose, then deliver a clear recommendation.
```

#### AFTER (Question-First Format):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "should I build X or Y?" - but that's not the real question.

> **The real question is: "Which feature aligns better with my goals and constraints?"**

This looks like a binary choice, but really you're prioritizing based on multiple dimensions: user impact, development effort, strategic alignment, and risk.

---

### Here's what I need to understand:

**To recommend which feature to prioritize, I need to explore:**

1. **What problem does each feature solve?** - For whom, and how badly do they need it?
2. **What's your capacity and timeline?** - How complex are these to build, and when do you need results?
3. **What are your strategic goals?** - Which feature moves you closer to your north star?
4. **What's the risk if you choose wrong?** - Can you change course later, or is this decision sticky?

*I'll ask 4-5 questions (~10 min) to understand these trade-offs, then deliver a clear recommendation on which feature to build first.*

---

### Ready to dig in?

Reply with:
- **"yes"** to start discovery
- **"show me"** to see the first question now
- **Ask anything** if you need clarification
```

**Why this works better:** Even for typical decisions, showing the actual questions is clearer than abstract fork options.

---

### Example 3: Existence Decision

**Question:** `/explore should I start a podcast about design systems?`

#### BEFORE (v4.3 with Fork Template):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "should I start a podcast?" - but that's not the real question.

> **The real question is: "Is this a meaningful use of my time and energy?"**

This is an existence decision disguised as a tactical question.

---

### Two Ways to Explore This

Which path would help you more right now?

**Validate desirability**
- Test if there's actually an audience for this
- Would people listen and engage?

**Understand feasibility**
- Map what it would actually take to do well
- Can you sustain this long-term?

*Or just say "show me" and I'll ask the first question.*

---

### What happens next

I'll ask 4-5 questions (~10 min) tailored to whichever path you choose, then deliver a clear recommendation.
```

#### AFTER (Question-First Format):

```markdown
# Tier 1: Pattern Recognition

You're framing this as "should I start a podcast?" - but that's not the real question.

> **The real question is: "Is this a meaningful use of my time and energy?"**

This is an existence decision disguised as a tactical question. Before committing months of effort, you need to validate both desirability (will people care?) and feasibility (can I sustain it?).

---

### Here's what I need to understand:

**To recommend whether this is worth pursuing, I need to explore:**

1. **Why this medium, why now?** - What makes podcasting the right format for what you want to say?
2. **Who's your audience?** - Is there unmet demand, or a crowded space?
3. **What's the real cost?** - Time, energy, equipment, editing - can you sustain this?
4. **What's your exit criteria?** - How will you know if this is working or failing?

*I'll ask 4-5 questions (~10 min) to understand these dimensions, then deliver a clear recommendation on whether to pursue this.*

---

### Ready to dig in?

Reply with:
- **"yes"** to start discovery
- **"show me"** to see the first question now
- **Ask anything** if you need clarification
```

---

## Key Design Changes

### 1. Remove Fork Pattern Options
**Before:** "Compare alternatives" vs "Understand current state"
**After:** No abstract options - show the actual questions instead

### 2. Lead with "Here's what I need to understand:"
Makes it immediately clear what territory will be explored.

### 3. Show 4 Concrete Questions
Each with a brief explanation of why it matters or what it reveals.

### 4. Outcome-Oriented Framing
"To recommend [specific outcome], I need to explore:"

### 5. Simplified Call-to-Action
Three clear options:
- "yes" (start full discovery)
- "show me" (jump to first question)
- "ask anything" (get clarification)

### 6. Maintain Time Expectation
Still shows "4-5 questions (~10 min)" to set expectations.

---

## When to Use This Format

### ✅ Use Question-First Format When:
- Meta decisions (about the product itself)
- Strategic planning questions
- Open-ended exploration
- Any case where fork options might be confusing
- **Default for most cases - it's universally clearer**

### ⚠️ Consider Keeping Fork Options For:
- Cases where the fork genuinely helps frame the decision
- When fork options are highly specific and contextual (not generic)
- When user explicitly needs to choose a path before proceeding

**Recommendation:** Make question-first format the **default** for v4.4, with fork patterns as an optional enhancement only when they genuinely add clarity.

---

## Implementation Checklist

- [ ] Update `.claude/commands/explore.md` with new format template
- [ ] Remove or deprecate generic fork pattern templates
- [ ] Update format examples in command specification
- [ ] Test with diverse decision types:
  - [ ] Meta decisions (product direction)
  - [ ] Prioritization (feature X vs Y)
  - [ ] Existence (should I do this?)
  - [ ] Execution (how should I implement?)
  - [ ] Timing (when should I act?)
- [ ] Validate readability and clarity
- [ ] Document in CHANGELOG as v4.4 improvement

---

## Success Metrics

**Good signals:**
- Users don't ask "what are you asking me?"
- Users reply "yes" without confusion
- Users can explain what's about to be explored

**Bad signals:**
- Users say "I don't understand"
- Users ask for clarification on the fork options
- Users disengage at Tier 1

---

## Related Documents

- [Self-Learning Patterns](../vision/self-learning-patterns.md) - Future vision for pattern evolution
- [.claude/commands/explore.md](.claude/commands/explore.md) - Current command specification
- [Test Logs](../../archive/test-logs/) - Real user interactions showing what works

---

**Status:** Design complete, ready for implementation
**Next:** Update explore.md command specification with question-first format
