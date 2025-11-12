# Outcomist Demo - Phase 3: The Web App

**Duration**: 4-5 minutes
**Focus**: Beautiful UI wrapping the CLI tool + profile learning feature

---

## Opening (30 seconds)

"In Phase 1, we saw Amplifier - the framework.
In Phase 2, we saw /explore - the CLI command.

Now let's see the web app: a beautiful interface that makes Outcomist accessible to anyone, not just developers.

Plus, we'll see the profile learning feature - something that emerged naturally from building this UI."

---

## Launch the Demo (30 seconds)

### Open the Intro Slide

```bash
open ~/amplifier/outcomist/outcomist-demo/demo_intro_slide.html
```

**Talk Through**:
- "Clean, professional intro slide"
- "Compass logo representing decision exploration"
- "Dark aesthetic with blue accent"
- "Click 'Launch Demo' to enter the app"

### Click Through to App

**Viewers see**:
- Clean welcome screen
- Outcomist logo and tagline
- Example prompts to get started
- Input box ready

---

## The Welcome Experience (45 seconds)

### Show: Welcome Screen Design

**Point out**:
- "No navigation clutter - just the decision prompt"
- "Example questions to spark ideas"
- "Clean, approachable design"
- "This is about removing friction to thinking"

### Design Philosophy

**Talk Through**:
- "Built following Amplifier's design principles"
- "Ruthless simplicity - only what's needed"
- "Accessibility first - proper contrast, semantic HTML"
- "Design tokens for consistency (--space-*, --blue-500)"

---

## Live Demo: Decision Exploration (2 minutes)

### Start a Conversation

**Type**:
```
I want to redesign my office to make it more inspiring and productive.
It's where I work, play games, and store my personal stuff.
```

### Phase 1: Discovery Questions (~45 seconds)

**Outcomist asks**:
- Questions about your space
- How you use it
- What's not working

**Show UI Features**:
- "Notice the clean message bubbles"
- "Markdown formatting (bold, bullets) renders beautifully"
- "Phase indicator at top: 'Explore → Review → Build'"
- "Progress dots show we're in phase 1"

**Answer a Few Questions**:
```
What's inspiring to you?
→ "Natural light, plants, minimal clutter..."

How do gaming and work coexist?
→ "Same desk, switch modes..."
```

### Phase 2: Pattern Synthesis (~30 seconds)

**Outcomist reflects**:
- Synthesizes what you shared
- Identifies tensions
- Confirms understanding

**Show UI**:
- "Phase indicator moves to 'Review'"
- "Progress dot updates"
- "Clean typography hierarchy"

### Phase 3: Building Options (~45 seconds)

**Outcomist proposes**:
- Specific redesign options
- Quick reply buttons appear
- Each option grounded in your context

**Show UI**:
- "Phase moves to 'Build'"
- "Quick reply buttons for interaction"
- "Can click or type response"

---

## The Profile Learning Feature (1 minute)

### Show: Profile Button

**Click profile button (top right)**

**Talk Through**:
- "This emerged while building the web app"
- "The CLI doesn't track you across conversations"
- "But a web app should remember context"

### What It Learned

**Show profile modal**:
```
About You:
• Values inspiration through natural elements
• Uses same space for work and gaming
• Prefers minimal clutter
• Works from home regularly
```

**Talk Through**:
- "It learned this from our conversation"
- "No explicit profile creation - just natural interaction"
- "Future conversations use this context automatically"

### Ask a Question Using Profile

**Click "Ask Question" tab**

**Try**:
```
What plants would work well for my space?
```

**Outcomist responds**:
- Uses profile context (knows your space preferences)
- Tailored recommendations
- References earlier conversation

**Talk Through**:
- "It remembers I value natural elements"
- "It knows my space constraints"
- "Personalized without me repeating myself"

---

## The Technical Architecture (1 minute)

### Show: How It All Connects

**Terminal**:
```bash
cd ~/amplifier/outcomist/outcomist-demo
tree -L 2 src/
```

**Talk Through**:
```
src/
├── components/         # Svelte UI components
│   ├── layout/        # Header, Sidebar
│   ├── messages/      # Message bubbles
│   ├── input/         # Chat input
│   └── profile/       # Profile modal
├── stores/            # State management
│   └── conversation.ts
├── styles/            # Design system
│   └── colors.css     # Design tokens
└── containers/
    └── ChatContainer.svelte  # Main app
```

### The Backend Integration

**Show**:
```bash
cat outcomist-demo/server.js | grep -A 10 "/api/explore"
```

**Key Points**:
```javascript
// Load /explore prompt from CLI
const EXPLORE_SYSTEM_PROMPT = fs.readFileSync(
  '../.claude/commands/explore.md'
);

// Call Claude API with same prompt
const response = await client.messages.create({
  system: EXPLORE_SYSTEM_PROMPT,
  messages: conversationHistory
});
```

**Talk Through**:
- "Backend loads the exact same explore.md we saw in Phase 2"
- "Calls Claude API directly"
- "Web app uses the identical logic as CLI"
- "One specification, two interfaces"

---

## What Makes This Work (45 seconds)

### One Core, Multiple Interfaces

```
.claude/commands/explore.md (THE SPEC)
         ↓           ↓
    CLI Command   Web App
    (Phase 2)    (Phase 3)
```

### The Architecture Benefits

**Talk Through**:
- "Improvements to explore.md benefit both CLI and web"
- "Testing CLI = testing web logic"
- "No duplicate code or diverging behavior"
- "Spec-driven development enables this"

### The Amplifier Advantage

**Talk Through**:
- "Built in days because:"
  - "Framework provided design system"
  - "Patterns were established"
  - "Quality guardrails prevented mistakes"
  - "Focus on unique value (profile learning)"

---

## Closing (30 seconds)

"So that's Outcomist:

**Phase 1**: Built with Amplifier framework - philosophy and patterns
**Phase 2**: Core /explore CLI - structured decision exploration
**Phase 3**: Web app - accessible UI + profile learning

Three tools that work together:
- Amplifier enables rapid quality development
- /explore provides the decision exploration engine
- Web app makes it accessible to everyone

Built in 5 days. Production quality. Ready to use."

---

## Demo Tips

### Setup Before Demo
1. **Start servers**:
   ```bash
   cd ~/amplifier/outcomist/outcomist-demo
   npm run dev        # Terminal 1
   npm run server     # Terminal 2
   ```
2. **Open intro slide**: `demo_intro_slide.html`
3. **Prepare scenario**: Real decision you'd explore

### Window Layout
- **Browser**: Main focus - the web app
- **Terminal**: Background - showing servers running
- **Code**: Quick flashes - showing architecture

### Timing Notes
- ⏱️ **Don't rush welcome screen** - Let viewers absorb clean design
- ⏱️ **Show 2-3 Q&A exchanges** - More feels repetitive
- ⏱️ **Highlight profile feature** - This is unique value
- ⏱️ **Keep architecture brief** - Just show it works

### Common Questions

**Q: "Is this just ChatGPT in a wrapper?"**
A: "No - three differences:
1. Structured three-phase process (not freeform chat)
2. Profile learning across conversations
3. Grounded in the specific /explore methodology

The process is the product, not just the AI."

**Q: "Where's my data stored?"**
A: "Currently local browser storage. Profile data stays in your browser. For production, you'd want backend storage with proper auth."

**Q: "Can I deploy this?"**
A: "Yes - it's a standard Vite/Express app. Deploy frontend to Vercel/Netlify, backend to Railway/Render. Add auth and database for production use."

**Q: "How does profile learning work technically?"**
A: "After each conversation, we call Claude API asking it to extract personal facts. These get saved to profile. Future conversations inject profile as context. Simple but effective."

**Q: "Why Svelte instead of React?"**
A: "Simpler mental model, less boilerplate, better performance. Amplifier philosophy: ruthless simplicity. Svelte fits that."

---

## Visual Highlights for Recording

### Screen Recordings to Capture
1. **Full conversation flow**: Start → Explore → Review → Build
2. **Profile learning**: Show modal, extracted facts
3. **Profile usage**: Ask question using context
4. **Code flash**: Quick show of architecture

### Annotations to Add
- **Arrow**: Phase progression (Explore → Review → Build)
- **Highlight**: Progress dots changing
- **Circle**: Quick reply buttons appearing
- **Zoom**: Profile facts being extracted

### Audio Callouts
- "Notice the phase indicator..."
- "Watch the progress dots..."
- "Here's where it learned about me..."
- "Now it uses that context..."

---

## Success Metrics

Viewer should understand:
- ✅ What the web app provides (accessible UI + profile learning)
- ✅ How it connects to CLI (same explore.md spec)
- ✅ Why architecture matters (one spec, two interfaces)
- ✅ The unique value (profile learning, clean UX)
- ✅ How it was built quickly (Amplifier framework)

Complete story:
- ✅ Phase 1: Framework that enables speed + quality
- ✅ Phase 2: Core logic in CLI command
- ✅ Phase 3: Beautiful UI making it accessible

---

## The Complete Demo Flow (if presenting all 3 phases)

**Total Duration**: 12-14 minutes

1. **Phase 1** (3-4 min): Amplifier framework
2. **Phase 2** (4-5 min): /explore CLI command
3. **Phase 3** (4-5 min): Web app UI

**Transition Phrases**:
- Phase 1→2: "Now let's see what we actually built..."
- Phase 2→3: "Now let's make this accessible to everyone..."

**Closing Summary** (1 min):
"This is how you build modern products:
- Start with a framework that embeds quality
- Build core logic as reusable specs
- Wrap in beautiful, accessible interfaces
- Ship in days, not months

That's Amplifier + Outcomist."
