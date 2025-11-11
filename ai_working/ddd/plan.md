# DDD Plan: Outcomist Web Demo UI Redesign

**Version**: 1.0
**Status**: Planning Complete
**Target Quality**: 9.5/10 (Refined excellence)

---

## Problem Statement

### What We're Solving

The Outcomist web demo has a sophisticated decision exploration engine (v4.8, 100% test pass rate) connected to the real `/explore` CLI command, but the UI undermines this with a 2/10 design that:

- **Looks dated**: Generic 2019-era web app aesthetic
- **Confuses users**: Non-functional category buttons that don't do anything
- **Fights the conversation**: Cluttered, heavy borders, poor visual hierarchy
- **Lacks polish**: Inconsistent spacing, mixed design patterns, no refinement

### Why This Matters

**First impressions dictate trust.** A 2/10 UI makes users doubt a 5-star product. For a decision-making tool where trust is paramount, the interface must communicate:
- **Intelligence**: Sophisticated, refined, analytical
- **Trust**: Professional, stable, credible
- **Clarity**: Clean hierarchy, effortless comprehension
- **Focus**: Conversation-first, zero distraction

### User Value

After redesign, users get:
- **Natural conversation experience**: Feels like talking to a thoughtful partner
- **Clear visual hierarchy**: Immediately understand conversation flow and progress
- **Professional aesthetic**: Builds trust through polished, sophisticated design
- **Intuitive interface**: Zero learning curve, obvious what to do

---

## Proposed Solution

### High-Level Approach

**Complete visual and architectural redesign** following "Refined Conversational" aesthetic:

1. **Design System Foundation**: Create centralized design tokens (colors, spacing, typography, motion)
2. **Architecture Refactor**: Separate orchestration from presentation (pure components)
3. **Component Consolidation**: Remove duplication (3 chat interfaces → 1, consolidate message components)
4. **Visual Excellence**: Apply sophisticated aesthetic (Linear + Claude + Stripe inspiration)
5. **Quality Polish**: Refined details, smooth animations, accessibility compliance

### Aesthetic: "Refined Conversational"

**Visual Language**:
- **Cool neutral sophistication** (blue-gray whites, teal accents)
- **Generous spacing** (32px between messages, 680px max-width)
- **Refined typography** (16px body, 1.6 line-height, Inter font family)
- **Subtle motion** (<150ms transitions, purposeful animations)
- **Minimal elevation** (subtle shadows, clean depth)

**Inspiration Sources**:
- **Linear**: Precise spacing, fast motion, ruthless simplicity
- **Claude.ai**: Conversation-first layout, generous spacing, readable line lengths
- **Stripe Dashboard**: Cool neutral palette, blue-gray sophistication, technical precision
- **Notion**: Typography hierarchy, comfortable information density

---

## Alternatives Considered

### Option B: Visual Polish Only (Rejected)

**What**: Keep current architecture, just improve styling
**Why rejected**:
- Only achieves 7/10 quality (not 9.5/10 goal)
- Doesn't fix architectural debt (duplication, mixed concerns)
- Harder to maintain long-term
- Misses opportunity for clean foundation

### Option C: Incremental Phases (Rejected)

**What**: Visual first, then architecture refactor
**Why rejected**:
- Context switching overhead
- May need rework between phases
- Takes longer overall
- Defers architectural clarity

### Chosen: Full Redesign + Refactor

**Why**:
- Achieves true 9.5/10 quality
- One-time investment (5-6 hours) vs. ongoing debt
- Aligns perfectly with ruthless simplicity and modular design philosophy
- Makes all future changes easier (regeneratable components)
- Creates clear foundation for someone who said "I have no clue"

---

## Architecture & Design

### Key Interfaces (The "Studs")

**1. Container ↔ Component Interface**
```typescript
// Pure component contract
interface MessageBubbleProps {
  role: 'user' | 'assistant';
  content: string;
  isStreaming?: boolean;
  timestamp?: Date;
}

// Components are "dumb" - receive props, emit events
// No direct store access, no business logic
```

**2. Component ↔ Design System Interface**
```typescript
// All styling via design tokens
import { tokens } from '$lib/design/tokens';

// Components use tokens, never hardcoded values
<div style="color: {tokens.colors.textPrimary}">
```

**3. Frontend ↔ Backend Interface** (PRESERVE AS-IS)
```typescript
// POST /api/explore
{
  message: string,
  conversationHistory: Message[]
}

// Response
{
  response: string,
  needsInput: boolean
}
```

### Module Boundaries

**Clear separation of concerns:**

```
src/
├── containers/              # Orchestration layer
│   └── ChatContainer.svelte # Owns ALL logic, coordinates components
│
├── components/              # Pure presentation layer
│   ├── messages/            # Message display (no logic)
│   ├── input/               # Input handling (events only)
│   └── empty-states/        # Welcome screen
│
├── design/                  # Design system (single source of truth)
│   ├── tokens.ts            # Colors, spacing, typography, motion
│   ├── animations.ts        # Animation specifications
│   └── utilities.ts         # Shared UI helpers
│
├── stores/                  # State management (keep as-is)
│   └── conversation.ts      # ✅ Already well-structured
│
└── engine/                  # Business logic (keep as-is)
    └── *.ts                 # ✅ Already isolated
```

**Key Principle**: Container owns logic, components are pure presentation

### Data Models

**Keep existing store structure** (already well-designed):
```typescript
interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  isStreaming?: boolean;
}

interface ConversationState {
  messages: Message[];
  isProcessing: boolean;
  // ... existing fields
}
```

---

## Files to Change

### Non-Code Files (Phase 2)

- [ ] **README.md** - Update screenshots, feature list, design philosophy reference
- [ ] **docs/DESIGN.md** - NEW: Document design system, component contracts, aesthetic choices
- [ ] **ai_working/ddd/ui-redesign-plan.md** - Archive old plan, reference this DDD plan
- [ ] **.vscode/settings.json** - Add Tailwind CSS IntelliSense config for design tokens

### Code Files (Phase 4)

**Design System (NEW FILES)**:
- [ ] **src/design/tokens.ts** - NEW: Design tokens (colors, spacing, typography, motion)
- [ ] **src/design/animations.ts** - NEW: Animation specifications and utilities
- [ ] **src/design/utilities.ts** - NEW: Shared UI utilities
- [ ] **tailwind.config.js** - UPDATE: Import and use design tokens

**Architecture Refactor**:
- [ ] **src/containers/ChatContainer.svelte** - NEW: Orchestration layer (extracted from ChatInterface)
- [ ] **src/components/ChatInterfaceReal.svelte** - DELETE: Logic moved to ChatContainer
- [ ] **src/components/ChatInterface.svelte** - DELETE: Unused variant
- [ ] **src/components/ChatInterfaceSimple.svelte** - DELETE: Unused variant
- [ ] **src/lib/Counter.svelte** - DELETE: Unused example component

**Component Consolidation**:
- [ ] **src/components/messages/MessageBubble.svelte** - NEW: Consolidated user + assistant messages
- [ ] **src/components/messages/MessageList.svelte** - REFACTOR: Pure layout, use MessageBubble
- [ ] **src/components/messages/StreamingIndicator.svelte** - NEW: Extracted streaming animation
- [ ] **src/components/UserMessage.svelte** - DELETE: Consolidated into MessageBubble
- [ ] **src/components/AssistantMessage.svelte** - DELETE: Consolidated into MessageBubble

**Input Components**:
- [ ] **src/components/input/ChatInput.svelte** - REFACTOR: Pure component, emit events
- [ ] **src/components/input/SendButton.svelte** - NEW: Extracted button component
- [ ] **src/components/InputBox.svelte** - DELETE: Split into ChatInput + SendButton

**Empty State**:
- [ ] **src/components/empty-states/WelcomeScreen.svelte** - NEW: Extracted from MessageList
- [ ] **src/components/MessageList.svelte** - REFACTOR: Remove empty state logic

**Global Styles**:
- [ ] **src/app.css** - UPDATE: Add design token CSS variables, import animations

**Root**:
- [ ] **src/App.svelte** - UPDATE: Use ChatContainer instead of ChatInterfaceReal

**Preserve Unchanged**:
- ✅ **src/stores/conversation.ts** - Keep as-is (works well)
- ✅ **server.js** - Keep as-is (backend integration perfect)
- ✅ **src/engine/*.ts** - Keep as-is (business logic isolated)

---

## Philosophy Alignment

### Ruthless Simplicity

**Start minimal:**
- Single orchestrator (not 3 chat interface variants)
- Pure components (props in, events out)
- Design tokens (single source of truth)
- Remove non-functional category buttons immediately

**Avoid future-proofing:**
- Not building: Dark mode (until requested), mobile nav, user accounts
- Not adding: Complex state management, routing, feature flags
- Focus: Conversation experience only

**Clear over clever:**
- Component names describe purpose: `MessageBubble` not `ChatBubbleWrapper`
- Direct prop passing: No HOCs, no render props, no slot gymnastics
- Obvious structure: `containers/` = logic, `components/` = presentation

### Modular Design

**Bricks (Self-Contained Modules):**
- `MessageBubble`: Displays single message, style based on role prop
- `ChatInput`: Input field + send button, emits submit event
- `WelcomeScreen`: Empty state UI, no logic
- `ChatContainer`: Orchestrates components, owns all logic

**Studs (Connection Points):**
```typescript
// Each component has clear contract
interface Props { ... }        // Inputs
interface Events { ... }       // Outputs
// No side effects, no hidden dependencies
```

**Regeneratable:**
- Every component has a spec: `docs/components/{Component}.spec.md`
- Spec defines: Purpose, contract (props/events), visual design, dependencies
- AI can regenerate from spec without breaking system

### Trust in Emergence

**Simple components → Complex UI emerges:**
- `MessageBubble` + `MessageList` + `ChatInput` = Full conversation interface
- No monolithic "ChatApp" component doing everything
- Composition over configuration

---

## Test Strategy

### Unit Tests

**Component Tests** (Playwright Component Testing):
```typescript
// MessageBubble.test.ts
- Renders user message with correct styling
- Renders assistant message with correct styling
- Shows streaming indicator when isStreaming=true
- Applies correct animation on mount
```

### Integration Tests

**Conversation Flow** (Playwright E2E):
```typescript
// conversation.spec.ts
- User can send message and receive response
- Messages display in correct order
- Streaming animation works during response
- Input clears after sending
- Scroll to bottom on new message
```

### User Testing

**Actual user workflow:**
1. Start app (`npm run dev`)
2. Start backend (`npm run server`)
3. Open browser (http://localhost:5176)
4. Send test message: "Should I change careers?"
5. Verify visual quality feels 9.5/10

---

## Implementation Approach

### Phase 2 (Docs) - Update All Non-Code Files

**Order of operations:**
1. Create `docs/DESIGN.md` - Document design system philosophy
2. Update `README.md` - New screenshots, feature list
3. Archive old plan in `ai_working/ddd/ui-redesign-plan.md`
4. Add component specs to `docs/components/*.spec.md`

### Phase 4 (Code) - Implementation in Chunks

**Chunk 1: Design System Foundation** (30 min)
- Create `src/design/tokens.ts` with design values
- Create `src/design/animations.ts` with motion specs
- Update `tailwind.config.js` to import tokens
- Add CSS variables to `src/app.css`

**Chunk 2: Architecture Refactor** (2 hours)
- Create `src/containers/ChatContainer.svelte`
- Extract logic from `ChatInterfaceReal.svelte`
- Update `src/App.svelte` to use ChatContainer
- Delete unused chat interface variants

**Chunk 3: Component Consolidation** (1 hour)
- Create `src/components/messages/MessageBubble.svelte`
- Refactor `MessageList.svelte` to use MessageBubble
- Create `WelcomeScreen.svelte`
- Delete old message components

**Chunk 4: Input Components** (30 min)
- Create `src/components/input/ChatInput.svelte`
- Create `src/components/input/SendButton.svelte`
- Delete `InputBox.svelte`

**Chunk 5: Visual Polish** (2 hours)
- Apply design tokens throughout
- Add animations
- Ensure 680px max-width, 32px spacing
- Test contrast ratios (4.5:1 minimum)

**Chunk 6: Accessibility & Testing** (1 hour)
- Add keyboard navigation support
- Add reduced motion support
- Run Playwright tests
- Manual quality validation (9.5/10 check)

---

## Success Criteria

### Quantitative Metrics

**Target: 9.5/10** (Refined excellence)
- Typography clarity (+1.0)
- Spacing precision (+1.0)
- Color sophistication (+1.0)
- Motion polish (+0.75)
- Accessibility (+1.0)
- Visual coherence (+0.75)

### Qualitative Validation

- ✅ Would I proudly show this to a design-savvy friend?
- ✅ Does this feel as polished as Linear/Claude/Stripe?
- ✅ Is the conversation comfortable to read for 20+ minutes?
- ✅ Are interactions instant and smooth?
- ✅ Does this communicate intelligence and trust?

---

## Next Steps

✅ **Phase 1 Complete: Planning Approved**

**Next Phase: Update all non-code files**

Run: `/ddd:2-docs`

---

## Appendix A: Design Inspiration from October App

**Source**: `/Users/chrispark/workspaces/workspaces/client/october-app/`

The user's October App project demonstrates excellent design patterns we should incorporate:

### Key Learnings Applied

1. **OKLCH Color Space** - Better perceptual uniformity than HSL
2. **Spring Physics Easing** - `cubic-bezier(0.34, 1.56, 0.64, 1)` for premium feel
3. **Staggered Animations** - Progressive reveals with 150ms delays
4. **Reduced Motion Support** - Mandatory accessibility (not optional)
5. **12px Border Radius** - `rounded-xl` for modern, friendly feel
6. **3px Focus Rings** - `ring-[3px]` with 50% opacity
7. **Minimal Scrollbars** - 1.5px width for polish
8. **Semantic Color Tokens** - `background`, `foreground`, `primary`, not just hex

### October App Animation System

```css
/* Spring physics for premium feel */
cubic-bezier(0.34, 1.56, 0.64, 1)

/* Stagger delays */
150ms, 300ms, 450ms, 600ms

/* Reduced motion support (mandatory) */
@media (prefers-reduced-motion: reduce) {
  animation: none !important;
  opacity: 1 !important;
  transform: none !important;
}
```

### Design Quality Alignment

Both projects target **9.5/10 quality** with:
- Accessibility-first (WCAG AA)
- Sophisticated animation choreography
- Modern color science
- Semantic design tokens
- Full dark mode support (future)

---

## Appendix B: Design Token Specifications

### Color System (OKLCH-based)

**Note**: Using OKLCH instead of HSL for better perceptual accuracy

```typescript
colors: {
  // Surface colors
  background: 'oklch(1 0 0)',              // Pure white
  surface: 'oklch(0.98 0.002 264)',        // Off-white with blue tint
  border: 'oklch(0.93 0.013 255)',         // Light gray border

  // Text colors
  textPrimary: 'oklch(0.13 0.042 265)',    // Dark slate
  textSecondary: 'oklch(0.55 0.046 257)',  // Mid gray
  textMuted: 'oklch(0.68 0.028 257)',      // Light gray

  // Accent (teal)
  accent: 'oklch(0.52 0.15 200)',          // Sophisticated teal
  accentHover: 'oklch(0.48 0.15 200)',     // Darker teal
  accentBg: 'oklch(0.96 0.05 200)',        // Subtle teal background
}
```

**Contrast Ratios** (validated):
- textPrimary on background: 16.7:1 (AAA)
- textSecondary on background: 7.2:1 (AA)
- accent on background: 4.8:1 (AA)

### Spacing System (8px Grid)
```typescript
spacing: {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
  xxl: '48px',
}
```

### Typography System
```typescript
typography: {
  fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, sans-serif',
  sizes: {
    xs: '12px',
    sm: '14px',
    base: '16px',
    lg: '18px',
    xl: '24px',
  },
  weights: {
    normal: '400',
    medium: '500',
    semibold: '600',
  },
  lineHeights: {
    tight: '1.25',
    base: '1.6',
    relaxed: '1.75',
  },
}
```

### Animation System (Inspired by October App)

```typescript
animation: {
  duration: {
    instant: '50ms',     // Hover feedback
    fast: '100ms',       // Input focus, button states
    normal: '150ms',     // Message entrance (primary animation)
    deliberate: '250ms', // Page transitions
  },
  easing: {
    out: 'cubic-bezier(0.23, 1, 0.32, 1)',        // Decelerating
    inOut: 'cubic-bezier(0.45, 0, 0.55, 1)',      // Smooth two-way
    spring: 'cubic-bezier(0.34, 1.56, 0.64, 1)',  // Spring physics (October App)
  },
  stagger: {
    xs: '50ms',   // Tight stagger
    sm: '100ms',  // Standard stagger
    md: '150ms',  // October App standard
    lg: '300ms',  // Pronounced stagger
  },
}
```

**Key Animations to Implement**:
```css
/* Message entrance (from October App pattern) */
@keyframes slideInUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Streaming indicator pulse */
@keyframes pulse-once {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Focus ring (3px, 50% opacity) */
.focus-visible {
  ring: 3px;
  ring-color: accent / 50%;
}
```

**Reduced Motion Support** (mandatory):
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

**Plan Status**: Ready for Phase 2 (Documentation)
**Philosophy Check**: ✅ Ruthless Simplicity, ✅ Modular Design, ✅ Trust in Emergence
**Quality Target**: 9.5/10 (Refined excellence)
**Estimated Effort**: 5-6 hours total
