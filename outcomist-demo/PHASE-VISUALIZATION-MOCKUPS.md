# Phase Visualization Design Variations

**Goal**: Show users the 3-phase Outcomist journey so they understand what to expect

**Phases**:
1. **Discover** - Deep exploration through questions
2. **Review Proposal** - See recommendation and reasoning
3. **Execute** - Get actionable implementation plan

---

## Design Variation 1: Welcome Screen Timeline

**Location**: Welcome screen (before starting conversation)
**Visibility**: Always visible on first load
**Style**: Horizontal timeline below the "What are you deciding?" headline

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│                                                 │
│          What are you deciding?                 │
│                                                 │
│   ┌─────────┐  →  ┌─────────┐  →  ┌─────────┐ │
│   │ Discover│      │ Review  │      │ Execute │ │
│   │ ~10 min │      │ Proposal│      │  Plan   │ │
│   └─────────┘      └─────────┘      └─────────┘ │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │ Describe your decision...               │   │
│  │                                         │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Card style**: Subtle gray background (#F8F9FA)
- **Border**: 1px solid #E4E6E8
- **Typography**: 14px, font-weight: 500
- **Arrows**: Simple → unicode or subtle SVG
- **Spacing**: 16px between cards
- **Animation**: Subtle fade-in on load

### Pros
✅ Sets expectations upfront
✅ Builds confidence ("I know what's coming")
✅ Minimal visual weight
✅ Doesn't interrupt main CTA

### Cons
❌ Adds visual clutter before starting
❌ May feel like unnecessary ceremony
❌ Some users might ignore it

---

## Design Variation 2: Sticky Header Progress Bar

**Location**: Top of screen (appears after conversation starts)
**Visibility**: Always visible during conversation
**Style**: Compact horizontal progress indicator

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│ OUTCOMIST         Planning family vacation       │
│                                                  │
│ [●────○────○]  Discover → Review → Execute      │
└─────────────────────────────────────────────────┘
│                                                  │
│  User: Help me plan trip to vegas...            │
│                                                  │
│  Outcomist: I'll help you plan...               │
```

### Design Specs
- **Position**: Below header, sticky on scroll
- **Height**: 32px
- **Progress dots**:
  - Active: Filled circle (#3B7FE8)
  - Inactive: Outline circle (#E4E6E8)
  - Completed: Filled with checkmark
- **Typography**: 12px, color: #94969A
- **Background**: White with subtle bottom border

### Pros
✅ Constant visibility (always aware of progress)
✅ Minimal space usage
✅ Updates as conversation progresses
✅ Familiar pattern (users understand progress bars)

### Cons
❌ Takes up screen real estate during entire conversation
❌ May feel restrictive/linear (even though flow is adaptive)
❌ Doesn't explain what each phase means

---

## Design Variation 3: Contextual Phase Cards (In-Stream)

**Location**: Inline with conversation messages
**Visibility**: Appears at phase transitions
**Style**: Special system message card

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│  User: Help me plan trip to vegas...            │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  Outcomist: I'll help you plan...               │
└─────────────────────────────────────────────────┘

┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  📍 Phase 1: Discover                          ┃
┃                                                 ┃
┃  I'll ask questions to understand your         ┃
┃  priorities, constraints, and what matters     ┃
┃  most. (~10 min)                               ┃
┃                                                 ┃
┃  Next: Review Proposal → Execute Plan          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌─────────────────────────────────────────────────┐
│  Outcomist: What's your current situation...    │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Background**: Subtle blue tint (#F0F5FF)
- **Border**: 2px solid #3B7FE8 (left side only)
- **Padding**: 16px
- **Icon**: Emoji or simple icon (📍, 🔍, ✓)
- **Typography**:
  - Title: 15px, font-weight: 500
  - Body: 14px, line-height: 1.5
  - Next: 12px, color: #94969A

### Pros
✅ Appears exactly when relevant (just-in-time context)
✅ Explains what's happening NOW
✅ No permanent screen real estate cost
✅ Feels natural in conversation flow
✅ Can be dismissed if user wants

### Cons
❌ User doesn't see full journey upfront
❌ Adds extra messages to conversation
❌ May feel like interruption

---

## Design Variation 4: Expandable Journey Map (Sidebar)

**Location**: Right sidebar (collapsible)
**Visibility**: Always accessible, starts collapsed
**Style**: Vertical sidebar panel

### Visual Layout

```
┌──────────────────────────┬──────────────┐
│ OUTCOMIST    [Profile]   │  ≡ Journey   │
├──────────────────────────┼──────────────┤
│                          │              │
│  User: Help me...        │ ✓ Discover   │
│                          │   ~10 min    │
│  Outcomist: I'll...      │   ├─ Phase 1 │
│                          │              │
│                          │ ○ Review     │
│                          │   Proposal   │
│                          │   ├─ Phase 2 │
│                          │              │
│                          │ ○ Execute    │
│                          │   Plan       │
│                          │   └─ Phase 3 │
│                          │              │
│                          │ [Collapse]   │
└──────────────────────────┴──────────────┘
```

### Design Specs
- **Width**: 240px expanded, 48px collapsed
- **Trigger**: "≡ Journey" button or icon in header
- **Animation**: Smooth slide-in/out (200ms)
- **Checkmarks**: ✓ for completed, ○ for pending
- **Active phase**: Highlighted background (#F0F5FF)
- **Typography**: 14px, mixed weights

### Pros
✅ Always accessible without taking space
✅ Shows full journey at a glance
✅ Can expand for details when needed
✅ Doesn't interrupt conversation flow
✅ Users can check progress anytime

### Cons
❌ Hidden by default (users might not discover it)
❌ Requires extra click to view
❌ Mobile implementation challenging

---

## Design Variation 5: Tooltip on Logo/Title

**Location**: Hover/click on Outcomist logo or conversation title
**Visibility**: On-demand (hidden until interaction)
**Style**: Elegant tooltip popup

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│ OUTCOMIST▼        Planning family vacation      │
│  ┌───────────────────────────────────┐          │
│  │ Outcomist follows 3 phases:       │          │
│  │                                   │          │
│  │ 1. Discover (~10 min)             │          │
│  │    Deep exploration of your       │          │
│  │    priorities and constraints     │          │
│  │                                   │          │
│  │ 2. Review Proposal                │          │
│  │    See recommendation & reasoning │          │
│  │                                   │          │
│  │ 3. Execute Plan                   │          │
│  │    Get actionable steps           │          │
│  └───────────────────────────────────┘          │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Trigger**: Click or hover on logo/wordmark
- **Popup style**: Rounded 12px, subtle shadow
- **Background**: White with 1px border #E4E6E8
- **Padding**: 16px
- **Typography**: 14px, line-height: 1.6
- **Animation**: Fade + scale (150ms)
- **Dismissal**: Click outside or X button

### Pros
✅ Zero visual clutter when not needed
✅ Discoverable (logo is natural place to look)
✅ Can be detailed without impacting UI
✅ User-initiated (feels helpful, not pushy)

### Cons
❌ Easy to miss (many users won't discover it)
❌ Not proactive (doesn't set expectations upfront)
❌ Mobile: Hover doesn't work, requires tap

---

## Design Variation 6: Animated Welcome Overlay

**Location**: Full-screen overlay on first visit
**Visibility**: Shows once (remembers in localStorage)
**Style**: Beautiful onboarding modal

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│                                                 │
│                                                 │
│          Welcome to Outcomist                   │
│                                                 │
│       Your decision exploration partner         │
│                                                 │
│                                                 │
│   ┌─────────┐  →  ┌─────────┐  →  ┌─────────┐ │
│   │    🔍   │      │    📋   │      │    ⚡   │ │
│   │Discover │      │ Review  │      │Execute  │ │
│   │ ~10 min │      │Proposal │      │  Plan   │ │
│   └─────────┘      └─────────┘      └─────────┘ │
│                                                 │
│   I'll guide you through these 3 phases to      │
│   help you make a well-informed decision        │
│                                                 │
│                                                 │
│              [Get Started →]                    │
│                                                 │
│              Don't show again                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Overlay**: Semi-transparent black (#00000080)
- **Modal**: White, centered, max-width: 600px
- **Cards**: Subtle elevation, rounded corners
- **Icons**: Colorful but tasteful
- **Button**: Primary blue (#3B7FE8)
- **Animation**: Fade + scale on enter/exit

### Pros
✅ Impossible to miss (full attention)
✅ Beautiful first impression
✅ Sets clear expectations upfront
✅ Can be rich/detailed
✅ Only shows once (not annoying)

### Cons
❌ Blocks immediate action (friction)
❌ Feels like traditional onboarding (potentially boring)
❌ Some users hate modals
❌ Skippable = many will skip

---

## Design Variation 7: Minimal Badge in Input

**Location**: Inside the main input area
**Visibility**: Subtle, always present
**Style**: Small badge/chip

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│                                                 │
│          What are you deciding?                 │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │ Describe your decision...               │   │
│  │                                         │   │
│  │                                         │   │
│  │                                         │   │
│  │                            [Phase 1/3]  │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Position**: Bottom-right of textarea (above buttons)
- **Style**: Pill shape, subtle gray (#F8F9FA)
- **Border**: 1px solid #E4E6E8
- **Typography**: 12px, font-weight: 500
- **Hover**: Shows tooltip with phase names
- **Size**: ~60px × 24px

### Pros
✅ Ultra-minimal (barely there)
✅ No additional UI elements
✅ Updates as user progresses
✅ Optional hover for details

### Cons
❌ Too subtle (may be missed entirely)
❌ Doesn't explain what phases mean
❌ Competes with voice/send buttons for space

---

## Design Variation 8: Assistant Message Header

**Location**: Top of each Outcomist message
**Visibility**: Part of every message
**Style**: Metadata line above message content

### Visual Layout

```
┌─────────────────────────────────────────────────┐
│  Outcomist · Phase 1: Discover · Question 2/5  │
│  ─────────────────────────────────────────────  │
│                                                 │
│  What's your current situation with this trip? │
│                                                 │
│  • Is this already booked (flights/hotels)?    │
│  • Any specific must-dos with kids that age?   │
│  • Family dynamic preferences?                 │
└─────────────────────────────────────────────────┘
```

### Design Specs
- **Position**: Top of each assistant message
- **Typography**: 12px, color: #94969A
- **Separator**: Thin line or subtle divider
- **Format**: "Name · Phase · Context"
- **Optional**: Make phase clickable for more info

### Pros
✅ Continuous reinforcement (every message)
✅ Shows progress naturally
✅ No separate UI component needed
✅ Contextual (know where you are in conversation)

### Cons
❌ Adds noise to every message
❌ May feel repetitive
❌ Doesn't explain phases upfront

---

## Recommendation Matrix

| Variation | Visual Weight | Upfront Clarity | Ongoing Visibility | Implementation | Mobile-Friendly |
|-----------|--------------|-----------------|-------------------|----------------|-----------------|
| 1. Welcome Timeline | Medium | ⭐⭐⭐⭐⭐ | ⭐ | Easy | ⭐⭐⭐⭐⭐ |
| 2. Sticky Progress Bar | Low | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Medium | ⭐⭐⭐ |
| 3. In-Stream Cards | Medium | ⭐⭐⭐ | ⭐⭐⭐⭐ | Easy | ⭐⭐⭐⭐⭐ |
| 4. Sidebar Journey | Low | ⭐⭐ | ⭐⭐⭐⭐ | Hard | ⭐⭐ |
| 5. Logo Tooltip | None | ⭐ | ⭐⭐ | Easy | ⭐⭐⭐ |
| 6. Welcome Overlay | High | ⭐⭐⭐⭐⭐ | ⭐ | Easy | ⭐⭐⭐⭐ |
| 7. Input Badge | Very Low | ⭐ | ⭐⭐⭐ | Easy | ⭐⭐⭐⭐ |
| 8. Message Headers | Low | ⭐⭐ | ⭐⭐⭐⭐⭐ | Easy | ⭐⭐⭐⭐⭐ |

---

## Hybrid Approach: Best of Multiple Variations

**Recommendation**: Combine **#1 (Welcome Timeline)** + **#3 (In-Stream Cards)**

### Why This Combo Works

**Phase 1: First Impression**
- Show Welcome Timeline on initial screen
- Sets expectations: "Here's the journey"
- User starts with confidence

**Phase 2: During Discovery**
- Remove timeline once conversation starts
- No permanent UI clutter
- Feels like natural conversation

**Phase 3: Phase Transitions**
- Show In-Stream Card when transitioning to "Review Proposal"
- User gets clear signal: "We're moving to the next phase"
- Reinforces the journey they saw upfront

### Visual Flow

```
┌─ WELCOME SCREEN ──────────────────────────────┐
│                                               │
│          What are you deciding?               │
│                                               │
│   [Discover] → [Review] → [Execute]          │
│                                               │
│  ┌─────────────────────────────────┐         │
│  │ Describe your decision...       │         │
│  └─────────────────────────────────┘         │
└───────────────────────────────────────────────┘

                    ↓ User starts

┌─ CONVERSATION (Discovery Phase) ──────────────┐
│ OUTCOMIST    Planning family vacation         │
├───────────────────────────────────────────────┤
│                                               │
│  User: Help me plan trip to vegas...          │
│                                               │
│  Outcomist: I'll help you plan...            │
│  What's your current situation...             │
└───────────────────────────────────────────────┘

                    ↓ After discovery

┌─ PHASE TRANSITION CARD ───────────────────────┐
│  📋 Moving to Phase 2: Review Proposal        │
│                                               │
│  Based on our conversation, I'll now share   │
│  my recommendation and reasoning.             │
│                                               │
│  Next: Execute Plan                           │
└───────────────────────────────────────────────┘

┌─ CONVERSATION (Review Phase) ─────────────────┐
│  Outcomist: Based on what you've shared...   │
└───────────────────────────────────────────────┘
```

---

## Implementation Priority

### High Priority (Ship First)
1. **Welcome Timeline** - Easy win, minimal code
2. **In-Stream Cards** - Clear phase transitions

### Medium Priority (Next Iteration)
3. **Logo Tooltip** - For users who want to reference journey

### Low Priority (Future Enhancement)
4. **Sticky Progress Bar** - If users request ongoing visibility

### Skip
- Welcome Overlay - Too much friction
- Sidebar - Too complex for MVP
- Message Headers - Too repetitive
- Input Badge - Too subtle

---

## Next Steps

1. **Create Welcome Timeline Component**
   - Add to WelcomeScreen.svelte
   - Below headline, above input
   - Subtle, minimal design

2. **Create Phase Transition Card Component**
   - Special message type in conversation
   - Triggered by backend at phase boundaries
   - Dismissible but informative

3. **Update Server to Signal Phase Changes**
   - Add phase metadata to API responses
   - Frontend detects and shows transition card

4. **Test with Real Users**
   - Does it build confidence?
   - Do users understand the journey?
   - Is it helpful or just clutter?

---

**Current UI Philosophy**: Conversational, minimal, natural expert tone
**Design Goal**: Add just enough structure to build confidence without adding ceremony
**Success Metric**: Users feel guided, not constrained
