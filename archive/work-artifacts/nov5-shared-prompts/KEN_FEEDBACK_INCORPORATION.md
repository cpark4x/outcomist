# Ken's Test Scenario #9 - Feedback Incorporation Analysis

**Date**: November 5, 2025
**Test**: Scenario #9 - Stuck in Build Phase
**Tester**: Ken
**Current Status**: Shared prompt library created today

---

## Ken's Key Improvement Suggestions

### 1. 🟡 Time Expectation Not Set Upfront

**Ken's Feedback:**
> "I don't know how long the interview process would take because my problem was pretty big. If I were to present a small problem, I'm not sure how I would know that I would get outcomist to do this interview in a shorter session"

**Suggested Fix:**
> "Want me to dig deeper? I'll ask 4-5 questions (~10 min) to understand..."

**Current Status in Shared Prompts**: ❌ **NOT ADDRESSED**

**Where it should be**: Tier 1 prompt (when offering Tier 2)

**Our Tier 1 prompt** (in `outcomist_shared/prompts.py`):
```python
TIER_1_SYSTEM_PROMPT = """...
[INSIGHT - 2-3 sentences]
...
[KEY QUESTION - 1 sentence]
...
"""
```

**Issue**: No mention of time investment or escape hatch for smaller problems.

---

### 2. ✅ Summary Before Recommendation

**Ken's Feedback:**
> "✅ Summary Before Recommendation - Listed back what was heard... User confirmed accuracy... Separated listening from advocating"

**Current Status in Shared Prompts**: ✅ **FULLY ADDRESSED**

**Our Summary Prompt** (in `outcomist_shared/prompts.py`):
```python
TIER_2_SUMMARY_SYSTEM_PROMPT = """Your task is to summarize what you've heard WITHOUT judgment before giving a recommendation.

CRITICAL RULES:
- List 3-4 key facts you learned
- NO JUDGMENT - just state what they told you
- Use bullet points (•)
- Reference their specific words and data
- This is about LISTENING, not ADVISING
- Keep each point concise
```

**Alignment**: Perfect match. Ken's feedback validated this is working well.

---

### 3. ✅ "Show Me" Questions

**Ken's Feedback:**
> "✅ 'Show Me' Questions - Asked to see actual docs... Seeing real artifacts revealed: 179 stories, complex epic structure... Much more valuable than asking user to describe docs"

**Ken's Suggestion to Strengthen:**
> "Don't accept descriptions when evidence is available. Request EVIDENCE: - User describes problem → 'Show me an example'"

**Current Status in Shared Prompts**: ⚠️ **PARTIALLY ADDRESSED**

**Round 1 Prompt** (current):
```python
- Ask about their PERSONAL situation, feelings, or constraints
- Avoid asking users to research external/market data
- Focus on THEIR OWN situation and data
```

**Issue**: While we focus on personal data, we don't explicitly encourage "Show Me" evidence-gathering.

**Missing**: No explicit guidance like "When user describes docs/problems/errors, ask to see them"

---

### 4. 🟡 Could Have Probed for "Reviewable Artifact" Earlier

**Ken's Feedback:**
> "After seeing '179 stories' in Round 1, could have immediately asked: 'Quick check: do you have a 2-minute demo video you can show someone right now?'"

**Suggested Addition:**
```
When user is building something, ask early in Round 1:
"Do you have something reviewable right now - a video, screenshot,
prototype, demo - that shows what you've built? Or is it all in-progress?"
```

**Current Status in Shared Prompts**: ❌ **NOT ADDRESSED**

**Issue**: Our prompts don't include specific guidance for project/product decisions.

---

### 5. 🟡 Workflow Probe Came Late

**Ken's Feedback:**
> "User mentioned 'vibe coding with LLMs' and 'no-code constraint' in first message, but workflow wasn't explored until Tier 2 Round 1."

**Suggested Addition:**
```
When user mentions specific constraints ("vibe coding", "no-code", "solo",
"non-technical"), immediately probe:

"Walk me through your typical workflow when you try to [do the thing].
Where does it usually break down?"
```

**Current Status in Shared Prompts**: ❌ **NOT ADDRESSED**

**Issue**: No specific guidance for constraint-based workflow probing.

---

### 6. ✅ Specific, Actionable Recommendation

**Ken's Feedback:**
> "✅ Specific, Actionable Recommendation - Not abstract ('cut scope') but concrete ('define 7-step hero flow')"

**Current Status in Shared Prompts**: ✅ **ADDRESSED**

**Our Recommendation Prompt**:
```python
TIER_2_RECOMMENDATION_SYSTEM_PROMPT = """...
CRITICAL RULES:
- Clear stance with reasoning
- Specific to THEIR situation (reference their answers)
- Actionable next steps
```

**Alignment**: Good match - emphasizes specificity and actionability.

---

### 7. 🟡 Co-Creation Could Be Offered Explicitly

**Ken's Feedback:**
> "User had to ASK for help creating DEMO_V1.md"

**Suggested Fix:**
> "Want me to help you create DEMO_V1.md together, or do you want to take it from here?"

**Current Status in Shared Prompts**: ❌ **NOT ADDRESSED**

**Issue**: Our recommendation prompt doesn't explicitly offer co-creation.

---

### 8. ✅ Avoid Asking Users to Research External Data

**Ken's Test Validated This Works:**
- Ken's scenario focused on personal context (his docs, his workflow, his constraints)
- No evidence of being asked to research market data
- Questions focused on "Show Me" actual artifacts

**Current Status in Shared Prompts**: ✅ **FULLY ADDRESSED** (added today)

**Our Prompts** (Round 1 & 2):
```python
- Avoid asking users to research external/market data
- Focus on THEIR OWN situation and data
```

**Alignment**: Perfect - this was added today based on previous feedback.

---

### 9. ✅ Check Capabilities - Don't Assume User Lacks Skills

**Relevant to Ken's Scenario:**
- Ken is non-technical (no-code constraint) but not inexperienced
- Outcomist didn't assume Ken lacked understanding
- Asked about workflow, not "Do you know how to..."

**Current Status in Shared Prompts**: ✅ **FULLY ADDRESSED** (added today)

**Our Round 2 Prompt**:
```python
- Check capabilities - don't assume user lacks skills
```

**Alignment**: Perfect - this was added today.

---

## Summary Scorecard

| Ken's Feedback Item | Status | Priority |
|---------------------|--------|----------|
| Time expectation not set upfront | ❌ Not addressed | High |
| Summary before recommendation | ✅ Fully addressed | N/A (working) |
| "Show Me" questions | ⚠️ Partially addressed | Medium |
| Reviewable artifact probe | ❌ Not addressed | Medium |
| Workflow probe for constraints | ❌ Not addressed | Medium |
| Specific actionable recommendations | ✅ Addressed | N/A (working) |
| Co-creation offer explicit | ❌ Not addressed | Low |
| Avoid asking to research external data | ✅ Fully addressed | N/A (added today) |
| Check capabilities | ✅ Fully addressed | N/A (added today) |

**Score**: 4/9 Fully Addressed, 1/9 Partially Addressed, 4/9 Not Addressed

---

## What We DID Incorporate (from today's work)

### ✅ Anti-Research Rules
- **Feedback Source**: Various test scenarios (not just Ken's)
- **What we added**: "Avoid asking users to research external/market data"
- **Impact**: Prevents asking users to look up market trends, pricing, etc.
- **Ken's validation**: His scenario showed this working (focused on personal context)

### ✅ Capability Checking
- **Feedback Source**: User feedback about assumptions
- **What we added**: "Check capabilities - don't assume user lacks skills"
- **Impact**: Respects user expertise
- **Ken's validation**: Relevant to his non-technical-but-experienced profile

### ✅ Summary Before Recommendation
- **Feedback Source**: Multiple test scenarios
- **What we added**: Explicit "NO JUDGMENT - just state what they told you"
- **Impact**: Separates listening from advocating
- **Ken's validation**: He explicitly called this out as working well

### ✅ Specific, Actionable Recommendations
- **Feedback Source**: Test scenarios wanting concrete advice
- **What we added**: "Specific to THEIR situation (reference their answers)"
- **Impact**: Forces concrete recommendations
- **Ken's validation**: He appreciated the concrete DEMO_V1.md recommendation

---

## What We DIDN'T Incorporate Yet

### Priority 1: Time Expectation Setting

**Missing from**: Tier 1 prompt when offering Tier 2

**Should add**:
```python
# In TIER_1_SYSTEM_PROMPT or transition prompt
"This will take about 10 minutes with 4-5 questions.
If your problem is simpler, let me know and I can give you a quick take instead."
```

**Why it matters**: Ken explicitly called this out as affecting user experience.

---

### Priority 2: "Show Me" Evidence Guidance

**Missing from**: Round 1 and Round 2 prompts

**Should add to Round 1**:
```python
- When user describes problems, ask to see them (errors, screenshots, docs)
- "Show me" is better than "Tell me" when evidence exists
- Don't accept descriptions when artifacts are available
```

**Why it matters**: Ken's scenario worked because Outcomist asked to see docs. This should be explicit guidance.

---

### Priority 3: Reviewable Artifact Probe

**Missing from**: Round 1 prompt for project/product decisions

**Should add conditional guidance**:
```python
- If user is building something: Ask early if they have something reviewable
  (demo, video, screenshot, prototype) or if it's all in-progress
```

**Why it matters**: Ken's core blocker (no reviewable demo) could have been surfaced faster.

---

### Priority 4: Workflow/Constraint-Based Probing

**Missing from**: Round 1 prompt

**Should add conditional guidance**:
```python
- When user mentions specific constraints (no-code, solo, non-technical, etc.),
  immediately probe their workflow: "Walk me through how you typically approach this"
```

**Why it matters**: Ken mentioned "vibe coding" and "no-code" upfront, but workflow wasn't explored until later.

---

### Priority 5: Explicit Co-Creation Offer

**Missing from**: Recommendation prompt

**Should add**:
```python
# After delivering recommendation
"Want me to help you create [the artifact/next step] together,
or do you want to take it from here?"
```

**Why it matters**: Makes collaboration explicit. Ken had to ask for help creating DEMO_V1.md.

---

## Recommended Next Steps

### Immediate (Today)
1. ✅ Review Ken's feedback (this document)
2. ⏳ Decide which items to incorporate into shared prompts
3. ⏳ Update `outcomist_shared/prompts.py` with selected improvements
4. ⏳ Sync CLI with updated prompts

### Short-term (This Week)
1. Add time expectation to Tier 1 → Tier 2 transition
2. Add "Show Me" evidence guidance to Round 1
3. Add reviewable artifact probe (conditional on project/product decisions)

### Medium-term (Next Sprint)
1. Add workflow/constraint-based probing to Round 1
2. Add explicit co-creation offer to recommendation
3. Test improvements with another scenario like Ken's

---

## Key Insight from Ken's Test

**Ken's feedback validates our TODAY's work was on the right track:**
- ✅ Anti-research rules (he appreciated focus on personal context)
- ✅ Capability checking (he's non-technical but experienced)
- ✅ Summary before recommendation (he explicitly called this out as working)
- ✅ Specific actionable recommendations (he got concrete DEMO_V1.md)

**But Ken also revealed gaps we haven't addressed yet:**
- ❌ Time expectation setting
- ❌ "Show Me" evidence guidance (implicit but not explicit in prompts)
- ❌ Reviewable artifact probe
- ❌ Workflow/constraint-based probing
- ❌ Explicit co-creation offer

**The gap between "what worked in Ken's session" vs "what's in our prompts":**
- Some good behaviors emerged organically (asking to see docs)
- These should be codified into explicit prompt guidance
- Other improvements (time expectation) are entirely missing

---

## Conclusion

**We incorporated 4/9 of Ken's feedback items** (the ones that overlapped with other feedback sources):
1. Anti-research rules ✅
2. Capability checking ✅
3. Summary before recommendation ✅
4. Specific actionable recommendations ✅

**We have NOT yet incorporated 4/9 items** that are specific to Ken's experience:
1. Time expectation setting ❌ (HIGH PRIORITY)
2. "Show Me" evidence guidance ❌ (MEDIUM PRIORITY)
3. Reviewable artifact probe ❌ (MEDIUM PRIORITY)
4. Workflow/constraint probing ❌ (MEDIUM PRIORITY)
5. Explicit co-creation offer ❌ (LOW PRIORITY)

**Next action**: Decide which of Ken's remaining feedback items to incorporate into the shared prompt library.
