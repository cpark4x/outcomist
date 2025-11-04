# Explore Command Improvements

**Date**: 2025-11-04
**Source**: Test #8 feedback (Gurkaran - workout app scenario)
**Status**: Proposed improvements based on real user feedback

---

## Summary of Issues

Test #8 revealed critical weaknesses in `/explore` command:

1. **Assumption-based questions** instead of data-gathering
2. **Bias leaked into discovery** (recommending before fully listening)
3. **Didn't check user intent** (validation vs execution)
4. **Mixed listening with advocating** (felt opinionated too early)

**User feedback**: "i understand the core problem myself more deeply (win)" BUT "seemed to bias towards not building" and "would have wanted it to interview me in a more open ended way"

---

## Proposed Changes

### 1. Add Intent Check to Tier 1

**Current Tier 1 Structure:**
```
[PATTERN + REFRAME]
[CREATE HUNGER]
[CALL TO ACTION with question preview]
```

**Proposed Addition:**

After the call to action, add:

```
Before we dig deeper, let me understand your intent:

**Are you looking for validation on WHETHER to pursue this, or guidance on HOW to execute it well?**

(This helps me tailor the questions to what you actually need)
```

**Why**: Prevents biasing toward "don't do it" when user wants execution guidance.

---

### 2. Update Question Types: Add "Show Me" Questions

**Current problem**: Questions are assumption-based
- "What made those fail?"
- "What specifically makes it hard?"

**Proposed improvement**: Request real data first

**New question type: "Show Me" (Data Request)**

**When to use**: When user describes a system, process, or problem

**Format**:
- "Can you show me your [current system]? Paste an example so I can see exactly what you're working with."
- "Walk me through what a typical [use case] looks like - give me a specific example."
- "Can you share the [artifact] so I can understand how you [do the thing]?"

**Benefits**:
- Gets REAL data instead of assumptions
- Reveals patterns you can't predict
- Makes user feel heard (not judged)

**Example from Test #8**:

**What I asked (assumption-based)**:
> "What specifically made those fail? Was it forgetting to log, too tedious, or losing track?"

**What I should have asked (data-based)**:
> "Can you show me what your Apple Notes tracking looks like? Just paste an example week or month so I can see your format."

---

### 3. Add "Summary Before Recommendation" Step

**Current problem**: Recommendation feels like it comes DURING discovery, not after

**Proposed addition**: Pause after Round 2, before recommendation

**New step structure**:

```
[ROUND 1: 2-3 questions]
[ROUND 2: 2-3 questions]

↓

[SUMMARY STEP - NEW]
Let me summarize what I've heard to make sure I understand:

• [Key fact 1 - no judgment]
• [Key fact 2 - no judgment]
• [Key fact 3 - no judgment]

Does that capture it accurately?

[WAIT FOR USER CONFIRMATION]

↓

[DELIVER RECOMMENDATION]
Based on this, here's my recommendation...
```

**Why**:
- Separates listening from advocating
- User feels heard before being advised
- Gives user chance to correct misunderstandings
- Makes bias less likely (facts laid out objectively first)

---

### 4. Don't Assume Capabilities or Constraints

**Current problem**: I assumed "building apps is hard" and "AI won't do it in hours"

**Proposed change**: Ask about capabilities, don't assume

**New Round 2 question type: Capability Check**

**Examples**:
- "What's your experience with building apps or using AI coding tools?"
- "What timeline seems realistic to you for this?"
- "Is building itself part of the value for you (learning, enjoyment), or purely utility?"

**Why**:
- User might have skills/context you don't know
- Building might have value beyond the end product
- Your assumptions about "hard" might not match their reality

---

### 5. Recognize "Building as Value" Pattern

**New awareness**: Some users want to build for reasons beyond utility

**Reasons to build despite existing solutions**:
- Learning/skill development
- Enjoyment of creation process
- Portfolio/resume building
- Full customization control
- Understanding how it works

**Implication**: Don't dismiss building just because existing solutions exist

**Better recommendation pattern**:
```
If user shows building capability + interest:
  → Present "build" as viable option alongside "use existing"
  → Focus on HOW to build well, not WHETHER to build

If user shows low capability or pure utility goal:
  → Present "use existing" first
  → Build as fallback if existing doesn't work
```

---

## Updated `/explore` Command Flow

### Tier 1: Pattern Recognition (30 seconds)

```
[PARAGRAPH 1: PATTERN + REFRAME]
- Identify deeper pattern
- Reframe question
- Reference user's words

[PARAGRAPH 2: CREATE HUNGER - OPTIONAL]
- Hint at complexity
- Create curiosity

[CALL TO ACTION]
Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand:
• [Preview questions]

Ready to explore?

[NEW: INTENT CHECK]
Before we dig deeper, let me understand your intent:

Are you looking for validation on WHETHER to pursue this, or
guidance on HOW to execute it well?

(This helps me tailor the questions to what you actually need)
```

---

### Tier 2: Discovery (5-10 minutes)

```
[ROUND 1: 2-3 HIGH-LEVEL QUESTIONS]
- Get the landscape
- REQUEST REAL DATA (use "Show Me" questions)
- One question at a time

↓

[QUICK ANALYSIS: 30-50 words]
- Show you're listening
- Surface initial patterns

↓

[ROUND 2: 2-3 TARGETED QUESTIONS]
- Dig deeper based on Round 1
- CHECK CAPABILITIES (don't assume)
- Adapt based on answers

↓

[NEW: SUMMARY STEP]
Let me summarize what I've heard:
• [Key facts, no judgment]

Does that capture it accurately?

[WAIT FOR CONFIRMATION]

↓

[DELIVER RECOMMENDATION]
- Based on THEIR context (not your assumptions)
- Clear stance with reasoning
- Specific to THEIR situation
- Multiple paths if appropriate
```

---

## Implementation Priority

### High Priority (Do First)

1. **Add intent check to Tier 1**
   - Simple addition
   - Prevents major bias issues
   - Quick win

2. **Add summary step before recommendation**
   - Critical for separating listening from advocating
   - Prevents feeling "judged too early"

### Medium Priority (Do Soon)

3. **Update question framework with "Show Me" questions**
   - Requires retraining how to ask questions
   - Big impact on quality

4. **Add capability check questions to Round 2**
   - Prevents wrong assumptions
   - Helps tailor recommendations

### Low Priority (Nice to Have)

5. **Build "validation vs execution" pattern recognition**
   - Helps identify intent from initial framing
   - Can inform which questions to ask

---

## Testing These Improvements

**Next steps**:
1. Update `/explore` command with intent check and summary step
2. Test with 2-3 new scenarios
3. Check if users feel:
   - Less judged during discovery
   - More heard before recommendations
   - Recommendations match their actual needs

**Success criteria**:
- User feels understood (like Test #8: "win")
- User doesn't feel biased against (unlike Test #8: "seemed to bias")
- Recommendations match user's actual context and capabilities

---

## Links

- [Test Log #8](../archive/test-logs/TEST_LOG_NOV4_WORKOUT_APP.md) - Source of feedback
- [Explore Command](.claude/commands/explore.md) - Current implementation
- [Question Framework](../docs/patterns/question-framework.md) - Question quality heuristics

---

**Status**: Proposed improvements awaiting implementation
**Next**: Update explore.md command file with these changes
