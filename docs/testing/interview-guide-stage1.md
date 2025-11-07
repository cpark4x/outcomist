# Stage 1 Testing Guide: /explore Validation Interviews

**Goal**: Validate that `/explore` delivers consistent value for developers/PMs using AI coding tools (Claude Code, Amplifier, GitHub Copilot).

**Target participants**: 5-10 people currently using Claude Code or similar AI tools
**Time per interview**: 20-30 minutes
**Format**: Live session where they use `/explore` with a real decision

---

## Pre-Interview Setup

### What you need:
- [ ] Participant has Claude Code installed
- [ ] Participant has `.claude/commands/explore.md` set up in a project
- [ ] Participant has a real decision they're facing (not hypothetical)
- [ ] Screen sharing enabled so you can observe

### What to tell them upfront:
"I'm testing a decision-making tool called `/explore`. I want you to use it with a real decision you're facing right now. I'll observe and take notes, but I won't guide you - I want to see how it works without my help."

---

## During the Interview

### Part 1: Setup (5 min)

**Observe silently:**
- Can they invoke `/explore` without help?
- Do they understand how to phrase their decision?
- Do they get stuck anywhere?

**If they're stuck for >2 minutes, note what confused them, then help them past it.**

---

### Part 2: Tier 1 - Pattern Recognition (5 min)

**After they receive the Tier 1 response, ask:**

1. **"What's your gut reaction to this response?"**
   - Listen for: confused, intrigued, annoyed, excited
   - Note exact words they use

2. **"Does the reframed question feel accurate?"**
   - Are they nodding or pushing back?
   - Does it reveal something they hadn't articulated?

3. **"Looking at the 4 questions - do they feel relevant?"**
   - Do they say "yes these matter" or "why are you asking that?"
   - Do the questions make them curious or defensive?

4. **"Are you going to say 'yes' to continue?"**
   - If yes: Great, let's keep going
   - If no: Why not? What would need to be different?

**Key signals:**
- ✅ **Good**: "Oh that's a better way to frame it" / "Yeah those questions matter"
- ❌ **Bad**: "I don't understand what you're asking" / "This feels generic"
- 🤷 **Neutral**: "Sure, I guess" (not excited but willing)

---

### Part 3: Tier 2 - Discovery (10 min)

**Let them go through the question rounds naturally.**

**Observe:**
- Do they answer thoughtfully or just give quick responses?
- Do they say "good question" or seem annoyed?
- Do they volunteer more info than asked?
- Do they ask clarifying questions back?

**After 2-3 questions, check in:**
"How's this feeling? Useful or tedious?"

**Key signals:**
- ✅ **Good**: Thoughtful answers, volunteering context, engaged
- ❌ **Bad**: One-word answers, impatient, checking phone
- 🤷 **Neutral**: Answering dutifully but not excited

---

### Part 4: Tier 3 - Recommendation (5 min)

**After they receive the recommendation, ask:**

1. **"Does this recommendation feel actionable?"**
   - Can they picture the next step?
   - Or does it feel too vague/abstract?

2. **"Did you learn something new, or just confirm what you already knew?"**
   - New insight = high value
   - Confirmation = moderate value (still useful)
   - Nothing new = low value

3. **"Would you use this again for another decision?"**
   - Why or why not?

4. **"What would make this more useful?"**
   - Listen for specific gaps, not generic "make it better"

**Key signals:**
- ✅ **Good**: "I'm going to do X next" / "That reframe changed my thinking"
- ❌ **Bad**: "I already knew that" / "This doesn't help me decide"
- 🤷 **Neutral**: "Interesting but not sure what to do with it"

---

## Post-Interview Reflection

### Document immediately:

1. **Decision type tested**: Existence / Prioritization / Execution / Timing / Audience
2. **Overall value delivered**: High / Medium / Low
3. **Biggest win**: What worked really well?
4. **Biggest gap**: What didn't work or confused them?
5. **Would they use it again?**: Yes / Maybe / No

### Look for patterns across interviews:

**After 3-5 interviews, ask yourself:**

- **Consistency**: Does it work for different decision types?
- **Value**: Do people say "I'd use this again"?
- **Clarity**: Do people understand what it's doing without explanation?
- **Friction**: Where do people get stuck or lose interest?

---

## Success Criteria for Stage 1

### ✅ Ready for Stage 2 if:
- 4+ out of 5 people say "I'd use this again"
- People deliver thoughtful answers in Tier 2 (engagement)
- Recommendations feel actionable (not just interesting)
- Different decision types work consistently

### ❌ Not ready if:
- People confused by Tier 1 reframe
- People give one-word answers in Tier 2 (not engaged)
- Recommendations feel generic or unhelpful
- Only works for certain decision types

### 🤷 Needs refinement if:
- Mixed results - some love it, some don't
- Works for some decision types but not others
- People engage but don't find it actionable
- Setup friction prevents people from trying it

---

## After Testing: Decision Point

**If Stage 1 validates (✅ criteria met):**
→ Move to Stage 2: Design `/preview` and `/build`

**If Stage 1 needs refinement (🤷 criteria met):**
→ Fix gaps first, test again, THEN move to Stage 2

**If Stage 1 doesn't validate (❌ criteria met):**
→ Reconsider the approach - maybe `/explore` alone isn't enough value

---

## Notes Section

Use this space during interviews to capture quotes, observations, and insights:

### Interview #10: [Name] - [Decision Type]
**Date**:
**Decision**:
**Gut reaction**:
**Key quote**:
**Value delivered**:
**Would use again?**:
**Notes**:

---

### Interview #11: [Name] - [Decision Type]
**Date**:
**Decision**:
**Gut reaction**:
**Key quote**:
**Value delivered**:
**Would use again?**:
**Notes**:

---

### Interview #12: [Name] - [Decision Type]
**Date**:
**Decision**:
**Gut reaction**:
**Key quote**:
**Value delivered**:
**Would use again?**:
**Notes**:

---

## Quick Reference: What to Watch For

| Stage | Good Signal | Bad Signal |
|-------|-------------|------------|
| **Tier 1** | "That's a better question" | "I don't get what you're asking" |
| **Tier 2** | Thoughtful, detailed answers | One-word, impatient answers |
| **Tier 3** | "I'm going to do X next" | "I already knew that" |
| **Overall** | "I'd use this for other decisions" | "Interesting but not useful" |
