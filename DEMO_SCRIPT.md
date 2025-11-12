# Outcomist Demo Script

## Overview

Outcomist is a decision exploration tool that helps you turn unclear decisions into clear next steps through AI-guided conversation. It works as both a CLI tool and a web app, sharing the same powerful exploration engine.

---

## Demo Flow (7-10 minutes)

### 1. Introduction (1 min)
**Open:** `demo_intro_slide.html`

**Script:**
> "I built Outcomist to solve a problem I kept running into: having important decisions but not knowing where to start. Should I take this contract? Redesign my office? Choose between product directions?
>
> Traditional pros/cons lists feel flat. Outcomist guides you through deep exploration - asking the right questions, uncovering what really matters, and helping you see the full picture.
>
> Let me show you both interfaces - the CLI for quick explorations, and the web app for richer conversations."

---

### 2. CLI Demo - Quick Decision (2-3 min)

**Context Setting:**
> "Let's start with the CLI. This is perfect for quick decisions where you want fast, focused guidance."

**Terminal Setup:**
```bash
cd ~/amplifier/outcomist
```

**Demo Scenario: "Client wants ongoing work $6K/month"**

**Run:**
```bash
claude -p .claude/commands/explore.md "Client wants ongoing work $6K/month (90% of time). Means pausing product for 6+ months. Product has traction (100 users, $2K MRR growing). Stable money or bet on product?"
```

**What to highlight:**
- ✅ Instant structured exploration
- ✅ Discovers hidden dimensions (runway, opportunity cost, reversibility)
- ✅ Asks clarifying questions naturally
- ✅ No UI needed - just pure conversation
- ✅ Same engine that powers the web app

**Response Pattern Expected:**
```
Let me help you explore this decision...

Key Dimensions to Consider:
1. Financial Security vs Growth Potential
2. Opportunity Cost (6 months of product momentum)
3. Customer Impact (100 users relying on you)
...

Critical Questions:
- What's your current runway without this contract?
- How much would product growth slow during the 6 months?
- Is the contract month-to-month or locked in?
...

Next Steps:
[Concrete actions based on your answers]
```

**Talking Point:**
> "Notice how it doesn't just give advice - it helps you think through the decision systematically. This same conversation engine powers both interfaces."

---

### 3. Web Demo - Rich Decision Exploration (4-5 min)

**Open:** http://localhost:5174

**Context Setting:**
> "Now let's see the web interface. Same engine, but with a richer experience - profile learning, conversation history, visual progress tracking."

#### Part A: Profile Learning (1 min)

**Action:** Click "Profile" button

**Show:**
- Empty profile initially
- Explain: "The system learns about you as you use it"

**Talking Point:**
> "Notice the profile is empty. As we explore decisions, Outcomist learns your goals, constraints, values - making future conversations even more personalized."

#### Part B: Decision Exploration (3 min)

**Demo Scenario: "Redesigning my home office"**

**Message 1:**
```
I want to redesign my office to make it more inspiring and productive. It's where I work, play games, and store my personal stuff.
```

**What to highlight:**
- ✅ Phase indicator (Explore → Review → Build)
- ✅ Progress dots showing where you are
- ✅ Natural conversation flow
- ✅ AI learns context from your message

**Expected Response Pattern:**
```
Let me help you think through this office redesign...

Understanding Your Space:
- Work zone (your primary income source)
- Gaming zone (your recharge space)
- Storage (personal belongings)

Key Questions:
1. What makes you feel most productive? (lighting, layout, etc.)
2. How much space do you have?
3. What's your budget range?
...
```

**Message 2:** (Answer a few questions)
```
About 12x10 feet. Budget is $2-3K. I feel most productive with natural light and minimal clutter. Gaming setup needs to feel separate from work.
```

**What to highlight:**
- ✅ Conversation builds on context
- ✅ System remembers your constraints
- ✅ Phase transitions naturally (Explore → Review)
- ✅ Profile learns from this conversation

**Check Profile Again:**
> "Let's check the profile now..."

**Action:** Click "Profile" → "Show Profile"

**Show:**
- System has learned: budget constraints, space limitations, productivity preferences
- These inform future conversations

**Talking Point:**
> "See how it's learning? Next time I use Outcomist, it'll already know my budget ranges, what I value in my workspace, and how I make decisions."

---

### 4. Technical Architecture (1-2 min)

**Switch to code** (optional, if technical audience)

**Show:**
```bash
tree -L 2 outcomist-demo/
```

**Key Points:**
- ✅ Single prompt file (`.claude/commands/explore.md`) powers both
- ✅ Profile learning system (`lib/profile.js`)
- ✅ Express backend bridges CLI prompt → Web UI
- ✅ Clean separation: UI vs Intelligence

**File to show:**
```bash
cat .claude/commands/explore.md | head -30
```

**Talking Point:**
> "The magic is in this prompt. It's the same whether you're in the terminal or the web browser. The UI just makes it more accessible - the thinking is identical."

---

### 5. The "Why This Matters" Moment (1 min)

**Script:**
> "Here's why this approach is powerful:
>
> **Traditional tools:**
> - Pros/cons lists → Too flat
> - Decision matrices → Too rigid
> - Consultants → Too expensive
>
> **Outcomist:**
> - Guides exploration like a consultant
> - Adapts to your thinking style
> - Learns from every conversation
> - Available instantly, CLI or web
>
> Most importantly: it helps you see dimensions you weren't considering. That contract decision? I wasn't thinking about opportunity cost or customer impact until Outcomist surfaced them.
>
> That's the difference between 'making a decision' and 'exploring a decision space.'"

---

## Demo Variants

### For Technical Audience
- Show the CLI first (they'll appreciate the simplicity)
- Dive into architecture
- Show prompt engineering
- Emphasize: same engine, multiple interfaces

### For Non-Technical Audience
- Start with web demo (more visual)
- Focus on outcomes, not implementation
- Show profile learning heavily
- Emphasize: like having a thinking partner

### For Product/Startup Folks
- Use business decisions as examples
- Show both quick (CLI) and deep (web) exploration
- Emphasize speed: "decision in 5 minutes vs 5 days"
- Connect to outcomes

---

## Demo Tips

### Before Demo
1. **Start servers:**
   ```bash
   npm run dev    # Terminal 1
   npm run server # Terminal 2
   ```
2. **Clear browser profile** (for clean demo)
3. **Prepare terminal** (large font, clean prompt)
4. **Test the intro slide** (make sure it loads)

### During Demo
- **Pace:** Don't rush. Let responses load.
- **Narrate:** Explain what's happening as it happens
- **Improvise:** If AI gives great response, follow that thread
- **Show, don't tell:** Less "this does X", more "watch what happens when..."

### Common Questions

**Q: "How is this different from ChatGPT?"**
> "ChatGPT is a blank slate each time. Outcomist is purpose-built for decisions - it knows how to explore systematically, learn your context, and guide you through phases. Plus it's available in your terminal without leaving your workflow."

**Q: "Does it make the decision for you?"**
> "No - and that's by design. It helps you explore the decision space thoroughly. You make the decision with much more clarity about what matters and why."

**Q: "How does profile learning work?"**
> "As you explore decisions, it extracts facts about your goals, constraints, values. These inform future conversations. It's like having a consultant who remembers your context."

**Q: "Can I use my own prompts/customize it?"**
> "Absolutely. The prompt is just a markdown file. Fork it, customize it, make it yours. The architecture is designed for that."

---

## Post-Demo Resources

Share these links:
- GitHub: `https://github.com/[your-repo]`
- Prompt file: `.claude/commands/explore.md`
- Documentation: `README.md`

---

## Recording Tips

If recording this demo:
1. Use **1920x1080 resolution** (standard HD)
2. **Screen + audio** recording
3. **Intro slide** → **CLI demo** → **Web demo** → **Closing**
4. Keep to **7-10 minutes** total
5. Edit out any long pauses/loading
6. Add **chapter markers**:
   - 0:00 Intro
   - 1:00 CLI Demo
   - 3:00 Web Demo
   - 7:00 Wrap-up

---

## Success Metrics

After the demo, viewers should:
- ✅ Understand: Outcomist helps explore decisions, not make them
- ✅ See: CLI for speed, Web for richness
- ✅ Get: Profile learning makes it smarter over time
- ✅ Want: To try it on their own decisions
