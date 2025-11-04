# Outcomist Pattern Library

**Last Updated**: 2025-11-04
**Status**: 6 patterns captured from 5 test scenarios
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
