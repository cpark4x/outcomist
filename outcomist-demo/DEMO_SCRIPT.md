# Outcomist Demo Script

**Duration:** ~4 minutes
**Purpose:** Show what can be built in 3-4 days using Amplifier

---

## Setup Before Recording

**Make sure these are running:**
```bash
# Terminal 1: Backend server
cd ~/amplifier/outcomist/outcomist-demo
npm run server

# Terminal 2: Web app
cd ~/amplifier/outcomist/outcomist-demo
npm run dev
```

**Have ready:**
- Demo intro slide open: `demo_intro_slide.html`
- Browser at localhost:5173
- Terminal with Claude Code ready
- Decision example ready (see suggestions below)

---

## Script

### Part 1: The Hook (30 seconds)

**[Screen: Demo intro slide]**

> "Most people don't know what they actually want. They ask AI for solutions, but is that even the right problem?
>
> That's why I built Outcomist. AI that drives outcomes, not activities. It helps you figure out what you want before taking action.
>
> I built this in 3-4 days using Amplifier. Two interfaces, same engine. Let me show you how it works."

---

### Part 2: CLI Demo (1.5 minutes)

**[Click "Launch CLI Demo" - Terminal opens]**

> "The CLI runs through Claude Code. I type /explore and describe my decision."

**[Type: `/explore Should I redesign my office to make it more inspiring and productive?`]**

> "Now watch what happens."

**[Let the conversation flow - answer naturally as questions appear]**

**As you go through the Q&A, narrate what you're seeing:**

> "See? Most AI would jump straight to furniture recommendations. But watch what Outcomist is doing..."
>
> [Point out pattern recognition as it happens]
>
> "Look - it's breaking down my thinking... spotting connections I didn't see..."
>
> [Continue answering naturally]
>
> "And here's the key moment - it's not giving me answers. It's helping me think differently about the problem."
>
> [Let the conversation reach a natural insight]
>
> "That's what ChatGPT would have missed. The real question underneath.
>
> That's the CLI. Two days to build."

---

### Part 3: Web Demo (1.5 minutes)

**[Switch to browser at localhost:5173]**

> "Now the web version. Same engine, visual interface."

**[Type a decision]**

> "Should I take a 3-month consulting project that requires 60-hour weeks?"

**[Show it responding with family context]**

> "Watch this. It already knows about my family—my wife and daughter. It's immediately asking about impact on them, not just the money.
>
> **[Click profile sidebar to show what it knows]**
>
> See? It remembers who they are, what matters to me. This isn't generic advice—this is specific to MY life. That's the power of memory. Built in 1-2 days."

---

### Part 4: How I Built This (1 minute)

**[Back to demo intro slide]**

> "Here's how: Amplifier. It's a development approach that combines AI with proven patterns.
>
> Day 1-2: CLI with Claude Code integration. Working tool in 2 days.
> Day 3-4: Web UI with Svelte. Learning as I built. Full app in 1-2 days.
>
> The key? I orchestrated AI to handle implementation while I focused on the experience I wanted to create.
>
> Amplifier provides the patterns. AI provides the execution. I provide the direction.
>
> The result? Something that would have taken weeks took days. And it works—you just saw it.
>
> This is what's possible when you combine clear thinking with the right tools.
>
> Link to Amplifier in the description. Thanks for watching."

**[End recording]**

---

## Decision Examples to Use

Choose scenarios that resonate with your audience:

### Career Decisions
- "Should I leave my $150K job to start consulting? I have 6 months savings and 2 potential clients."
- "Should I accept a 20% pay cut to work at a startup with equity?"
- "Should I move to a new city for a better job opportunity? My family is established here."

### Business Decisions
- "Should I add a freemium tier to my SaaS product? Current MRR is $15K with 50 customers."
- "Should I hire my first employee or stay solo? Revenue is $10K/month but I'm working 70 hours/week."
- "Should I pivot my product or keep pushing current direction? 6 months in, slow growth."

### Product Decisions
- "Should I rebuild our app from scratch or keep patching technical debt?"
- "Should we focus on acquiring new users or improving retention? CAC is $50, LTV is $200."
- "Should I build an API or keep the product self-contained?"

### Personal Decisions
- "Should I buy a house now or keep renting? Rates are high but I'm tired of moving."
- "Should I go back to school for an MBA? It would cost $100K and 2 years."
- "Should I renovate my office to make it more inspiring? It would cost $5K."

**Choose 2-3 different types** to show the breadth of what Outcomist handles.

---

## Technical Setup Checklist

Before recording, verify:

- [ ] Backend server running (port 3001)
- [ ] Web app running (port 5173)
- [ ] Demo intro slide opens correctly
- [ ] CLI `/explore` command works in Claude Code
- [ ] Terminal is in a clean state
- [ ] Browser has no distracting tabs
- [ ] Screen resolution set for recording
- [ ] Audio tested and clear
- [ ] Decision examples ready to copy/paste

---

## Tips for Recording

1. **Speak conversationally** - You're showing a friend, not presenting to executives
2. **Show real exploration** - Don't rush through the Q&A, let it breathe
3. **Be honest about build time** - "3-4 days" is impressive; don't oversell
4. **Highlight the pattern** - This isn't just about Outcomist; it's about what's possible
5. **Keep energy up** - Especially in the technical explanation part
6. **Have water nearby** - 5-7 minutes is longer than it feels

---

## Variations

### Short Version (2-3 minutes)
- Skip one of the demos (CLI or web)
- Show just 1-2 conversation exchanges
- Skip the "Builder's Journey" section
- Jump straight to the closer

### Long Version (10 minutes)
- Show more conversation depth
- Demonstrate the profile learning in detail
- Show conversation history and revisiting past decisions
- Walk through more of the code/architecture
- Discuss specific Amplifier patterns used

### Technical Audience Version
- Start with the architecture
- Show the prompt system
- Explain how profile learning works
- Demonstrate the API integration
- Show code examples

### Business Audience Version
- Focus on the outcomes (clarity, better decisions)
- Skip technical details
- Emphasize speed to market (3-4 days)
- Show more decision examples
- Focus on ROI and value

---

## After Recording

- [ ] Review for audio quality
- [ ] Check for any UI glitches or errors shown
- [ ] Verify timing (aim for 5-7 minutes)
- [ ] Add captions if needed
- [ ] Add Amplifier GitHub link in description
- [ ] Consider adding timestamps in description

---

**Good luck with your demo! You built something impressive—show it with confidence.**
