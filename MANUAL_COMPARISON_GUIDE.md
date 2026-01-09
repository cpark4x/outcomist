# Manual Comparison Guide: explore.md vs explore_v2.md

**Goal**: Validate that library-based explore_v2 produces quality matching original  
**Time Required**: 30 minutes  
**Tests**: 3 scenarios, side-by-side comparison

---

## How to Run This Comparison

### Setup

1. **Open two Claude CLI sessions** (or one session, run tests sequentially)
2. Navigate to the outcomist directory in both
3. Prepare to copy/paste results into this document

### For Each Test Scenario

**In Session 1** (Original):
```
/explore [decision from scenario below]
```
Copy the Tier 1 response

**In Session 2** (Library version):
```
/explore_v2 [same decision]
```
Copy the Tier 1 response

**Compare using criteria below**

---

## Test Scenario 1: Office Redesign

### Decision Input
```
I want to redesign my office to make it more inspiring for work
```

### Expected Pattern
**Personal Sanctuary Pattern** (confidence: 0.24)

### What to Look For

**Pattern Recognition:**
- [ ] Identifies this is about personal space, not work optimization
- [ ] Mentions "inspiring" keyword from user's input
- [ ] Reframes from "work space" to "personal retreat/sanctuary"

**Tone:**
- [ ] Conversational (not academic)
- [ ] No jargon like "environmental psychology optimization"
- [ ] Quotes user's word "inspiring" directly
- [ ] Sounds like consultant, not textbook

**Quality Benchmarks:**
```
✅ Good: "I notice you said 'inspiring' - this sounds less like work 
         optimization and more like creating a space that feels like YOURS"

❌ Bad:  "Your desire reveals a need for environmental psychology 
         optimization to externalize your internal motivation"
```

---

### RESULTS - Fill In After Testing

#### Original explore.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Quotes "inspiring"**: [Yes/No]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Library explore_v2.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Quotes "inspiring"**: [Yes/No]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Comparison:
**Quality difference**: [Same/Better/Worse]  
**Specific differences**: [Note any differences]  
**Verdict**: [✅ V2 matches quality | ⚠️ V2 needs improvement | ❌ V2 worse]

---

## Test Scenario 2: Client vs Product

### Decision Input
```
Should I take this $6K/month client work or focus on my $2K MRR product? The market is tough and I'm thankful for the stable client money.
```

### Expected Pattern
**Scarcity Mindset Hiding Opportunity** (confidence: 0.23)

### What to Look For

**Pattern Recognition:**
- [ ] Identifies scarcity mindset / fear-based framing
- [ ] Recognizes "market is tough" as scarcity narrative
- [ ] Notes "thankful" as fear language
- [ ] Reframes from "stable vs risky" to underlying fear

**Specificity:**
- [ ] Quotes "$6K/month" and "$2K MRR" directly (not "client work" and "product")
- [ ] References "market is tough" and "thankful" from user's words
- [ ] Uses concrete language, not abstract

**Tone:**
- [ ] Direct and punchy
- [ ] No business jargon ("asymmetric opportunity", "scalable growth trajectory")
- [ ] Conversational language

**Quality Benchmarks:**
```
✅ Good: "You're framing this as 'stable vs risky' - but you said market 
         is tough and you're thankful. That's scarcity mindset talking, 
         not your actual situation."

❌ Bad:  "You're presenting a false dichotomy between short-term stability 
         and long-term potential, revealing underlying risk aversion masked 
         as practical decision-making."
```

---

### RESULTS - Fill In After Testing

#### Original explore.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Quotes "$6K" and "$2K"**: [Yes/No]  
**Quotes user phrases**: [Yes/No - which ones?]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Library explore_v2.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Quotes "$6K" and "$2K"**: [Yes/No]  
**Quotes user phrases**: [Yes/No - which ones?]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Comparison:
**Quality difference**: [Same/Better/Worse]  
**Specific differences**: [Note any differences]  
**Verdict**: [✅ V2 matches quality | ⚠️ V2 needs improvement | ❌ V2 worse]

---

## Test Scenario 3: Feature Decision

### Decision Input
```
Should I build Feature X for 10 customers or Feature Y for 2 customers? We position ourselves as employees-first.
```

### Expected Pattern
**Popularity Contest Hiding Identity Crisis** (confidence: 0.19-0.21)

### What to Look For

**Pattern Recognition:**
- [ ] Identifies this as values/identity question, not just prioritization
- [ ] Notes "10 vs 2" framing (count-based)
- [ ] Recognizes potential contradiction with "employees-first" positioning
- [ ] Reframes from "which feature" to "who are you building for"

**Insight Quality:**
- [ ] Goes beyond ROI calculation
- [ ] Identifies product identity implications
- [ ] Questions whether volume = right decision

**Tone:**
- [ ] Conversational
- [ ] Direct about the tension
- [ ] No business school language

**Quality Benchmarks:**
```
✅ Good: "You're framing this as 10 vs 2 (volume), but you said you're 
         employees-first. The real question is: does the popular feature 
         align with who you claim to be?"

❌ Bad:  "This represents a strategic positioning dilemma requiring careful 
         stakeholder analysis and values alignment assessment."
```

---

### RESULTS - Fill In After Testing

#### Original explore.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Identifies identity issue**: [Yes/No]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Library explore_v2.md Response:
```
[Paste Tier 1 response here]
```

**Pattern detected**: [Yes/No - which pattern?]  
**Identifies identity issue**: [Yes/No]  
**Tone**: [Conversational/Academic/Mixed]  
**Overall quality**: [1-10]

---

#### Comparison:
**Quality difference**: [Same/Better/Worse]  
**Specific differences**: [Note any differences]  
**Verdict**: [✅ V2 matches quality | ⚠️ V2 needs improvement | ❌ V2 worse]

---

## Overall Assessment

After testing all 3 scenarios, fill this out:

### Quality Comparison

| Aspect | Original | V2 Library | Winner |
|--------|----------|------------|--------|
| Pattern detection | [Score 1-10] | [Score 1-10] | [Original/V2/Tie] |
| Tone (conversational) | [Score 1-10] | [Score 1-10] | [Original/V2/Tie] |
| Quotes user words | [Score 1-10] | [Score 1-10] | [Original/V2/Tie] |
| Insight quality | [Score 1-10] | [Score 1-10] | [Original/V2/Tie] |
| Overall | [Score 1-10] | [Score 1-10] | [Original/V2/Tie] |

### Decision

Based on the comparison:

- [ ] **✅ CUTOVER NOW** - V2 matches or exceeds original quality
- [ ] **⚠️ ITERATE** - V2 is close but needs 1-2 specific improvements
- [ ] **❌ MORE WORK** - V2 has significant quality gaps

### If CUTOVER:
```bash
cd /Users/chrispark/outcomist-review/.claude/commands
mv explore.md explore_legacy.md
mv explore_v2.md explore.md
```

### If ITERATE:
**Specific improvements needed:**
1. [List specific issues found]
2. [What needs to change]
3. [Re-test criteria]

### If MORE WORK:
**Major gaps identified:**
1. [What's missing or wrong]
2. [Root cause]
3. [Recommended approach]

---

## What to Do Right Now

**Step 1**: Run the 3 test scenarios above with both `/explore` and `/explore_v2`

**Step 2**: Fill in the RESULTS sections in this document

**Step 3**: Make your cutover decision based on quality comparison

**Step 4**: Let me know the results and I can help with next steps!

---

**Ready to start?** Run the first test:
```
/explore I want to redesign my office to make it more inspiring for work
```

Then run:
```
/explore_v2 I want to redesign my office to make it more inspiring for work
```

Compare the responses and document them above!
