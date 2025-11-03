# Outcomist Test Scenarios

**Purpose**: Ruthlessly curated test suite to validate Outcomist's effectiveness across diverse decision types, stakes levels, and user contexts. Every scenario tests something unique with no easy answers.

**Total**: 20 scenarios - Final list, locked for systematic testing

---

## The Final 20

| # | Type | Scenario | Stakes | What This Tests |
|---|------|----------|--------|-----------------|
| 1 | Personal | Want to get healthy. Options: Gym membership $100/mo, home equipment $500 one-time, or just walk daily free. Which actually works? I've failed at all three before. | Medium | Pattern recognition vs personal history |
| 2 | Personal | Moving to new home? Current mortgage $2K/month, found place $3.5K/month, better schools. Can afford but tight. Two kids, spouse worried. | High | Family dynamics + financial stress |
| 3 | Personal | Kitchen renovation $50K. Contractor says custom cabinets worth $15K more. We cook daily, want 15+ years. | High | Sales pitch detection + ROI |
| 4 | Personal | Want to take family to Europe 2 weeks. Costs $12K. Can afford but means no house down payment this year. Do it now (kids 8 & 10) or wait 2 years? | High | Opportunity cost + timing |
| 5 | Workplace | Manager piling on work, I'm drowning. Push back, work longer, or look for new job? Mortgage + family = can't just quit. | Medium | Constraint-based decision |
| 6 | Workplace | Teammate takes credit for my ideas. Happened 3 times. Confront, tell manager, or let it go? He's well-liked. | Medium | Political complexity |
| 7 | Workplace | Got offer for 20% more pay but love current team. New company unknown culture. Have 1 week to decide. | High | Time pressure + incomplete info |
| 8 | Workplace | RTO policy announced. I'm in different state now (moved during remote). Relocate and uproot family or quit with no backup job? | High | Lose-lose scenario |
| 9 | Manager | Report underperforming 3 months despite feedback. PIP, different role, or more time? They have family, mortgage. | High | Empathy vs accountability |
| 10 | Manager | Team burned out from 6-month crunch. Leadership wants another major project. Push back or make it work? | High | Advocacy vs delivery pressure |
| 11 | Freelance | Client wants ongoing work $6K/month (90% of time). Means pausing product for 6+ months. Product has traction (100 users, $2K MRR growing). Stable money or bet on product? | High | Opportunity cost + risk tolerance |
| 12 | Freelance | Been freelancing 2 years, inconsistent income ($3K-$8K/month). Client offered full-time $120K. Miss the freedom. | High | Stability vs autonomy |
| 13 | Business | Revenue $180K but lumpy ($30K one month, $5K next). Can't predict. Hire $60K employee (need help desperately) or stay solo and turn down work? | High | Uncertainty + resource constraint |
| 14 | Product | 10 customers want Feature X (nice-to-have). 2 customers want Feature Y (make-or-break for renewal, $50K ARR). Build for 10 or 2? Renewals in 8 weeks. | Medium | Wrong framing + time pressure |
| 15 | Product | Sold company for $1.5M (good price). Been 6 months, miss it. Always wondered 'what if I kept building?' Start new company in same space? | High | Post-exit regret + identity |
| 16 | Product | Main product not gaining traction after 2 years. $400K invested, 6 months runway left. Pivot or double down? | Very High | Crisis decision + sunk cost fallacy |
| 17 | Competitive | Competitor launched feature we've been building 6 months. Rush ours out (buggy) or stick to plan (3 more months)? | High | Quality vs speed tradeoff |
| 18 | Productivity | 3+ hours/day in meetings, can't focus. Manager expects both attendance and output. Decline meetings or work nights/weekends? Hitting burnout. | Medium | Systemic problem detection |
| 19 | Ethical | Boss asked me to manipulate metrics for investor deck. Not lying but misleading. Say no and risk job? Economy rough, no backup. | High | Ethical dilemma + constraint |
| 20 | Tech/Career | AI tool could automate 50% of my job. Learn it (risk making myself obsolete) or avoid it (risk irrelevance)? I'm 45, been doing this 20 years. | High | Existential career question |

---

## Why These 20

**Coverage:**
- Personal life: 4 scenarios (health, home, renovation, travel)
- Workplace: 4 scenarios (workload, politics, job offer, RTO)
- Management: 2 scenarios (performance, burnout)
- Freelance/Solo: 2 scenarios (client vs product, stability vs freedom)
- Business/Product: 5 scenarios (hiring, features, post-exit, pivot, competitive)
- Cross-cutting: 3 scenarios (productivity, ethical, AI/career)

**What Makes These Great:**
- ✅ No easy answers - every scenario has real tradeoffs
- ✅ Emotional + logical weight - not just math problems
- ✅ Real constraints - time, money, relationships, uncertainty
- ✅ Lose-lose scenarios - #8, #16, #19 have no perfect choice
- ✅ Wrong question scenarios - #14 tests redirection ability
- ✅ Crisis + time pressure - #7, #14, #16, #17
- ✅ Political/ethical complexity - #6, #9, #19
- ✅ Existential weight - #12, #15, #16, #20
- ✅ Personal failure history - #1 tests pattern vs individual context
- ✅ Incomplete information - #7, #13, #16 require decision with uncertainty

---

## Testing Framework

### What to Test for Each Scenario

**Tier 1 (30 seconds):**
- [ ] Pattern recognition feels accurate and relevant
- [ ] Language is varied (not robotic repetition)
- [ ] Honest inference clearly marked
- [ ] Call-to-action is clear ("Want to explore deeper? Or happy with this?")
- [ ] Immediate value delivered even if user stops here

**Tier 2 (5-10 min):**
- [ ] Discovery questions feel relevant
- [ ] Questions are easy to answer
- [ ] "Best guess is fine" permission given
- [ ] Brief delivered with clear recommendation
- [ ] Actionable next steps provided

**Tier 3 (20-30+ min):**
- [ ] Three-round structure feels digestible
- [ ] Analysis between rounds shows listening
- [ ] Follow-up questions adapt based on previous answers
- [ ] Multiple choice includes escape hatches ("Other/Also: ___")
- [ ] Doesn't assume expert knowledge
- [ ] Comprehensive recommendation with alternatives
- [ ] Risk analysis feels honest

**Special Cases:**
- [ ] "Wrong question" scenarios: Does it redirect to real problem?
- [ ] Vague scenarios: Does it gracefully handle lack of specifics?
- [ ] Multi-stakeholder: Does it surface conflicts/tradeoffs?

### Success Criteria

**Must have:**
- Feels like conversation, not interrogation
- Recommendations are specific to user's context (not generic)
- Clear stance ("I recommend X") not endless options
- Honest about evidence basis (no invented stats)
- Time matches stakes

**Nice to have:**
- User says "this helped me see something I missed"
- User feels confident enough to make decision
- Output is actionable (next steps are clear)

---

## Testing Log

| Scenario | Tested Date | Tier Reached | Pass/Fail | Notes |
|----------|-------------|--------------|-----------|-------|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |
| ... | | | | |

