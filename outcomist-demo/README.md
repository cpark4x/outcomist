# Outcomist Web Demo

A professional web interface for the Outcomist decision exploration tool. The demo connects to the real `/explore` CLI command via a backend API, providing the full v4.8 decision exploration experience with a sophisticated 9.5/10 quality UI.

## Features

### Fully Functional Decision Exploration
- **Real `/explore` Integration**: Connects to actual Outcomist v4.8 CLI command
- **Pattern Recognition**: Matches user input against 9 decision patterns
- **Question Type Detection**: Automatically routes information/execution/decision questions
- **Adaptive Questioning**: Context-aware 2-round discovery structure
- **Trade-off Discovery**: Identifies and presents conflicting priorities
- **Personalized Recommendations**: Generates specific, actionable advice
- **Automatic Profile Learning**: Automatically extracts and remembers personal facts from conversations (name, goals, constraints, skills, family details) to personalize future interactions without asking the same questions

### Refined Conversational UI
- **9.5/10 Quality Design**: Professional, conversation-focused interface
- **Dynamic Project Titles**: Intelligent title generation from conversation context with topic shift detection
- **Professional Header**: Minimal header bar with branding and contextual project name
- **Voice Input**: Speech-to-text using Web Speech API with visual recording feedback
- **Adaptive Discovery Preview**: Conversational (straightforward) or detailed (complex) based on question
- **OKLCH Color System**: Modern color science for perceptual accuracy
- **Sophisticated Animations**: Spring physics, staggered reveals, smooth transitions
- **Accessibility-First**: WCAG AA compliant, full keyboard navigation, reduced motion support
- **Responsive Layout**: Optimized for reading (680px max-width, 32px generous spacing)
- **Design System**: Comprehensive design tokens (see [docs/DESIGN.md](docs/DESIGN.md))

## Running the Demo

### Prerequisites
- Node.js 18+ installed
- `ANTHROPIC_API_KEY` environment variable set

### Install Dependencies
```bash
npm install
```

### Configuration

**Environment Variables:**
- `ANTHROPIC_API_KEY` (required): Your Anthropic API key
- `EXPLORE_PROMPT_PATH` (optional): Custom path to explore.md prompt file
  - Default: `../.claude/commands/explore.md` (relative to server.js)
  - Example: `EXPLORE_PROMPT_PATH=/custom/path/explore.md npm run server`

### Start Backend Server
The backend connects to the real `/explore` CLI command:

```bash
npm run server
```

Server runs on `http://localhost:3001`

### Start Frontend (separate terminal)
```bash
npm run dev
```

Frontend runs on `http://localhost:5176` (or next available port)

### Build for Production
```bash
npm run build
npm run preview
```

## Testing with Scenarios

The demo works with test scenarios from `/docs/testing/test-scenarios.md`. Try these:

### Test #2: Office Redesign (Personal Sanctuary Pattern)
```
I want to redesign my office to make it more inspiring and productive. It's where I work, play games, and store my personal stuff.
```

### Test #7: Client vs Product (Scarcity Mindset Pattern)
```
Should I take a $6K/month stable client or focus on my $2K MRR product that's growing?
```

### Test #9: Stuck in Build Phase
```
I need help finishing my product. I have 179 user stories across 4 epics but can't get one flow to demo state.
```

## Architecture

### Tech Stack
- **Frontend**: Svelte 5 + TypeScript
- **Backend**: Express + Anthropic SDK (connects to real `/explore` CLI)
- **Styling**: Tailwind CSS with OKLCH color tokens
- **Build**: Vite
- **Icons**: lucide-svelte
- **State**: Svelte stores (reactive conversation state)

### File Structure
```
src/
├── containers/
│   └── ChatContainer.svelte       # Orchestration layer (logic + title generation)
├── components/
│   ├── layout/
│   │   └── Header.svelte          # Branding + dynamic project title + profile button
│   ├── profile/
│   │   └── ProfileModal.svelte    # User profile editor (modal UI)
│   ├── messages/
│   │   ├── MessageBubble.svelte   # Single message display
│   │   ├── MessageList.svelte     # Scrollable message container
│   │   └── StreamingIndicator.svelte
│   ├── input/
│   │   ├── ChatInput.svelte       # Pure input component
│   │   ├── VoiceButton.svelte     # Voice input with Web Speech API
│   │   └── SendButton.svelte      # Send button
│   └── empty-states/
│       └── WelcomeScreen.svelte   # Empty state UI
├── design/
│   ├── tokens.ts                  # Design system tokens
│   ├── animations.ts              # Animation specifications
│   └── utilities.ts               # Shared UI helpers
├── stores/
│   └── conversation.ts            # Conversation state (messages + projectTitle)
└── App.svelte                     # Root component

lib/
└── profile.js                     # Profile storage & context generation

profiles/
└── self.json                      # User profile data (gitignored)

server.js                          # Express server (connects to /explore + profile API)
```

## How It Works

### Backend Integration
The demo connects to the real Outcomist v4.8 engine:

1. **User Input** → Frontend (`ChatInput` component)
2. **API Call** → Backend (`POST /api/explore`)
3. **CLI Execution** → Real `/explore` command processes conversation
4. **Claude API** → Anthropic Claude Sonnet 4 generates response
5. **Response** → Backend returns assistant message
6. **UI Update** → Frontend displays message with animation

All decision exploration logic (pattern recognition, adaptive questioning, trade-off discovery) runs through the actual v4.8 CLI command—not a simulation.

### Automatic Profile Learning

The system automatically learns about you as you chat, eliminating the need to repeat yourself:

**How it works:**
1. **During conversation** - You mention facts naturally ("I have two kids aged 8 and 10", "I'm a solo founder")
2. **Automatic extraction** - After each response, Claude analyzes the conversation and extracts personal facts
3. **Profile storage** - Facts are merged into your profile (`profiles/self.json`) without duplicates
4. **Future conversations** - Profile context is automatically injected, so Claude remembers without asking

**What gets learned:**
- Basic info (name, age, role)
- Goals, constraints, skills, values
- Personal facts (family details, work situation, preferences)

**Privacy:**
- Profile data stored locally only
- File is gitignored (never committed)
- You can view/edit via Profile button in header
- Manual profile management still available if preferred

**Example:**
```
First chat: "I have two kids aged 8 and 10. I'm building a SaaS product."
→ Profile learns: role="solo founder", goals=["build SaaS product"], personalFacts=["has 2 kids aged 8 and 10"]

New chat: "My kids need attention but I also need to launch."
→ Claude responds knowing you're a solo founder with kids, doesn't re-ask
```

### Design System

The interface uses a comprehensive design system ([docs/DESIGN.md](docs/DESIGN.md)):

- **OKLCH Colors**: Perceptually uniform color space for better visual consistency
- **8px Grid**: All spacing follows 8px base unit for rhythm
- **Typography**: Inter font, 16px body text, 1.6 line-height (optimal readability)
- **Animations**: Spring physics easing, 150ms message entrance, reduced motion support
- **Layout**: 680px max-width (optimal line length), 32px generous spacing between messages

### Component Architecture

**Separation of Concerns**:
- `ChatContainer`: Owns all logic (API calls, state management, orchestration)
- Components: Pure presentation (props in, events out, no side effects)
- Design Tokens: Single source of truth for styling

**This architecture makes components**:
- Testable (pure functions of props)
- Reusable (clear interfaces)
- Regeneratable (can rebuild from specs without breaking system)

## Design Credits

Inspired by:
- **Linear**: Precise spacing, fast motion, ruthless simplicity
- **Claude.ai**: Conversation-first layout, generous spacing, readable line lengths
- **Stripe Dashboard**: Cool neutral sophistication, technical precision
- **October App** (`/Users/chrispark/workspaces/workspaces/client/october-app/`): Spring physics, OKLCH colors, staggered animations

## Development

### Design System
See [docs/DESIGN.md](docs/DESIGN.md) for:
- Complete design token specifications
- Component architecture and contracts
- Animation system details
- Accessibility standards
- Development guidelines

### Adding Components
1. Define contract (Props/Events interfaces)
2. Write spec (purpose, contract, visual design)
3. Build component using design tokens
4. Test accessibility (contrast, keyboard nav, screen reader)
5. Document in `docs/DESIGN.md`

### Modifying Design Tokens
1. Update `src/design/tokens.ts`
2. Validate contrast ratios (WCAG AA: 4.5:1 minimum)
3. Test across all components
4. Document changes in git commit

---

**Powered by Outcomist v4.8** | **Quality Target: 9.5/10** | **WCAG AA Compliant**
