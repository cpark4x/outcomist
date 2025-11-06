# Outcomist Web App Redesign

**Date**: 2025-11-05
**Quality Target**: 9.5/10
**Emotional Goal**: Confident, guided, understood

---

## Purpose & Context

**Problem**: Current UI is functional but lacks polish, visual hierarchy, progress indication, and micro-interactions that build trust and guide users through the decision exploration journey.

**Solution**: Comprehensive redesign applying professional UX principles:
- Clear visual progress indication (stepper component)
- Distinguished message types with visual hierarchy
- Smooth micro-interactions and loading states
- Professional iconography and visual affordances
- Enhanced conversation flow with proper spacing and typography

**User Journey**:
1. **Landing** → Clear value proposition, inviting input
2. **Tier 1 Analysis** → Streaming with progress, pattern recognition reveal
3. **Intent Selection** → Clear choice between validation vs execution
4. **Tier 2 Discovery** → Question-answer flow with visual distinction
5. **Recommendation** → Clear, actionable outcome

---

## Design Decisions (Nine Dimensions)

### 1. Body (Ergonomics & Accessibility)
- **Touch targets**: 48×48px minimum (mobile-friendly)
- **Contrast**: All text ≥ 4.5:1 (WCAG AA)
- **Keyboard nav**: Full support with visible focus states
- **Reduced motion**: Respect prefers-reduced-motion
- **Font sizes**: 16px minimum for body text, 14px for secondary

### 2. Space (Layout & Hierarchy)
- **8px spacing system**: Consistent rhythm throughout
- **Max-width**: 780px for optimal reading (45-75 characters)
- **Vertical rhythm**: 24px base, 32px between sections, 48px for major transitions
- **Breathing room**: Generous padding in conversation cards (24-32px)
- **Progressive disclosure**: Content reveals in digestible chunks

### 3. Proportion (Scale & Balance)
- **Type scale**: 14px, 16px, 18px, 24px, 32px, 42px (1.25 ratio)
- **Card hierarchy**: Headers 24px, body 17px, captions 14px
- **Button sizing**: Large primaries (48px height), medium secondaries (40px)
- **Icon scale**: 20px for inline, 24px for standalone
- **Logo**: 42px on desktop, 36px on mobile

### 4. Typography (Hierarchy & Readability)
- **Font family**: System fonts (-apple-system, SF Pro Display)
- **Weights**: 400 (regular), 500 (medium), 600 (semibold)
- **Line height**: 1.6 for body, 1.3 for headings
- **Letter spacing**: -0.5px for large headings
- **Message hierarchy**:
  - User messages: 17px, medium weight
  - AI messages: 17px, regular weight
  - Questions: 18px, medium weight
  - Recommendations: 17px with bold highlights

### 5. Color (Semantic & Accessible)
**Existing palette (keeping brand consistency)**:
- Primary: `#007AFF` (iOS blue)
- Primary hover: `#0051D5`
- Success: `#34c759` (recommendation state)
- Warning: `#ffcc00` (summary state)
- Background: `#fbfbfd` (subtle off-white)
- Surface: `#ffffff`
- Text: `#1d1d1f`
- Text secondary: `#86868b`
- Border: `#d2d2d7`

**New semantic colors**:
- Info: `#5856d6` (purple for questions)
- Progress: `#007AFF` with opacity variations
- Gradient accent: `135deg, #007AFF 0%, #5856d6 100%`

### 6. Style (Visual Language)
- **Design system**: iOS-inspired minimalism
- **Depth strategy**: Subtle shadows (0 2px 16px rgba(0,0,0,0.08))
- **Corner treatment**: 12px border radius (soft but structured)
- **Surface elevation**: Cards float with subtle shadows
- **Gradient usage**: Reserved for primary actions and accents

### 7. Motion (Timing & Choreography)
**Timing protocol**:
- Micro-interactions: 150ms (hover, focus)
- State transitions: 300ms (card appearance, message reveal)
- View transitions: 400ms (section changes)
- Streaming cursor: 1s blink cycle

**Easing curves**:
- Standard: `cubic-bezier(0.4, 0, 0.2, 1)` (iOS ease)
- Bounce: `cubic-bezier(0.34, 1.56, 0.64, 1)` (spring physics for hovers)
- Ease-out: `cubic-bezier(0, 0, 0.2, 1)` (entries)
- Ease-in: `cubic-bezier(0.4, 0, 1, 1)` (exits)

**Animations**:
- Fade-in: opacity 0→1 + translateY 10px→0
- Scale-in: scale 0.95→1 (buttons on press)
- Slide-up: translateY 20px→0 (conversation messages)
- Pulse: scale 1→1.05→1 (attention-grabbing)

### 8. Voice (Tone & Copy)
**Brand voice**: Professional but warm, confident but approachable

**Microcopy examples**:
- Input placeholder: "Describe what you're trying to decide..." (inviting, not commanding)
- Explore button: "Explore" (active, not passive)
- Loading: "Exploring..." (present continuous, shows progress)
- Intent question: "Are you looking for validation on WHETHER to pursue this, or guidance on HOW to execute it well?" (clear, conversational)
- Progress labels: "Understanding your decision" → "Exploring patterns" → "Gathering context"

### 9. Texture (Depth & Materiality)
- **Glass morphism**: Subtle backdrop blur on overlays
- **Shadow layers**: Multiple shadows for depth (2px close + 16px ambient)
- **Surface treatment**: Flat but elevated through shadows
- **Gradient overlays**: Very subtle (5-10% opacity) for state differentiation

---

## Component Specifications

### Progress Stepper
**Purpose**: Show user where they are in the exploration journey

**Structure**:
```
[1. Understanding] → [2. Intent] → [3. Discovery] → [4. Recommendation]
```

**States**:
- `pending`: Gray circle, gray line
- `active`: Blue circle with pulse animation, blue line to next
- `completed`: Blue circle with checkmark, solid blue line

**Visual specs**:
- Circle: 32px diameter, 2px border
- Line: 2px height, flexes between circles
- Icons: 16px within circles
- Labels: 14px, secondary color when pending, primary when active/complete

**Behavior**:
- Animates when transitioning (circle scales 1→1.1→1)
- Active step pulses gently (opacity 0.6→1 over 2s)
- Completed checkmark fades in (200ms)

### Message Cards
**Purpose**: Distinguish message types through visual hierarchy

**Types & Treatment**:

1. **User Message**
   - Background: `rgba(0, 122, 255, 0.05)`
   - Border-left: `3px solid #007AFF`
   - Padding: `16px 24px`
   - Font: 17px regular
   - Icon: User avatar or initials (24px circle)

2. **AI Assistant Message**
   - Background: `#ffffff`
   - Shadow: `0 2px 16px rgba(0,0,0,0.08)`
   - Padding: `24px`
   - Font: 17px regular
   - Icon: Outcomist logo mark (24px)

3. **Question Message**
   - Background: `linear-gradient(135deg, rgba(0,122,255,0.05), rgba(88,86,214,0.05))`
   - Border: `2px solid #007AFF`
   - Padding: `24px`
   - Font: 18px medium
   - Shadow: `0 4px 20px rgba(0,122,255,0.15)`
   - Icon: Question mark in circle (24px)

4. **Summary Message**
   - Background: `rgba(255, 204, 0, 0.05)`
   - Border: `2px solid #ffcc00`
   - Padding: `24px`
   - Font: 17px regular
   - Icon: Document icon (24px)

5. **Recommendation Message**
   - Background: `linear-gradient(135deg, rgba(52,199,89,0.05), rgba(0,122,255,0.05))`
   - Border: `2px solid #34c759`
   - Padding: `24px`
   - Font: 17px regular with bold highlights
   - Shadow: `0 4px 20px rgba(52,199,89,0.15)`
   - Icon: Checkmark in circle (24px)

**Entry animation**: Fade-in + slide-up (400ms ease-out)

### Intent Selection Cards
**Purpose**: Clear visual choice between validation and execution paths

**Layout**: 2-column grid on desktop, stack on mobile

**Card specs**:
- Background: `#ffffff`
- Border: `2px solid #d2d2d7` (hover: `#007AFF`)
- Padding: `32px`
- Border-radius: `12px`
- Shadow: `0 2px 8px rgba(0,0,0,0.08)` (hover: `0 4px 16px rgba(0,122,255,0.2)`)

**Content**:
- Icon: 32px at top (⚖️ for validation, 🎯 for execution)
- Title: 20px semibold
- Subtitle: 15px secondary color
- Hover: translateY(-2px) with shadow increase

**Interaction**:
- Hover: Border color change + shadow growth + lift (300ms)
- Click: Scale down (0.98) then return (150ms)
- Selected: Border color persists after selection

### Input Areas
**Purpose**: Clear, inviting text input with proper states

**Specs**:
- Border: `2px solid #d2d2d7`
- Padding: `16px 24px` (input), `16px` (textarea)
- Border-radius: `12px`
- Font: 17px system
- Line-height: 1.6

**States**:
- Focus: Border `#007AFF` + ring shadow `0 0 0 4px rgba(0,122,255,0.1)`
- Error: Border `#ff3b30` + ring shadow `0 0 0 4px rgba(255,59,48,0.1)`
- Disabled: Opacity 0.5 + cursor not-allowed

**Placeholder**: `#86868b` with clear, inviting copy

### Primary Button
**Purpose**: Main action button with confidence-building interaction

**Default state**:
- Background: `#007AFF`
- Color: `#ffffff`
- Padding: `16px 32px`
- Border-radius: `12px`
- Font: 17px medium
- Shadow: `0 2px 8px rgba(0,0,0,0.08)`

**Hover**:
- Background: `#0051D5`
- Shadow: `0 4px 12px rgba(0,122,255,0.3)`
- Transform: `translateY(-1px)`
- Transition: 300ms ease

**Active/Press**:
- Transform: `translateY(0)` + scale(0.98)
- Shadow: `0 1px 4px rgba(0,0,0,0.08)`
- Transition: 150ms

**Loading state**:
- Spinner icon (20px) replacing text
- Opacity: 0.7
- Cursor: not-allowed
- No hover effects

### Streaming Cursor
**Purpose**: Show AI is thinking and generating response

**Specs**:
- Width: 2px
- Height: 20px
- Background: `#007AFF`
- Animation: Blink (1s cycle)

**Behavior**:
- Appears inline with streaming text
- Vertical-align: text-bottom
- Smooth opacity transition (0→1→0)

### Loading States
**Purpose**: Show progress and reduce perceived waiting

**Types**:

1. **Button loading**
   - Spinner icon (20px)
   - Rotates continuously (1s linear infinite)
   - Text changes (e.g., "Explore" → "Exploring...")

2. **Message loading skeleton**
   - Gray placeholder boxes
   - Shimmer animation across (2s)
   - Fades out when real content arrives

3. **Streaming indicator**
   - Blinking cursor at end of text
   - Pulse animation on message card border
   - Progress indicator above conversation

---

## Iconography

**Icon system**: Using simple, semantic SVG icons (20-24px)

**Icons needed**:
1. **Progress stepper**: Circle outline, checkmark, arrow-right
2. **Messages**: User circle, bot circle, question-mark-circle, document, checkmark-circle
3. **Actions**: Send (paper-plane), restart (refresh-cw), menu (menu)
4. **States**: Loading spinner, error triangle, info circle
5. **Intent**: Scale (validation), target (execution)

**Icon treatment**:
- Stroke-width: 2px
- Colors: Match semantic meaning
- Inline with text: 20px, baseline aligned
- Standalone: 24px, centered

**Implementation**: Inline SVGs for performance, CSS colors for themability

---

## Responsive Behavior

### Breakpoints
- Desktop: ≥1024px (max-width 780px container)
- Tablet: 768-1023px (max-width 100% with 32px padding)
- Mobile: <768px (max-width 100% with 16px padding)

### Mobile-specific changes
- Logo: 36px (from 42px)
- Intent buttons: Stack vertically
- Message padding: 16px (from 24px)
- Button text: Shorter labels
- Progress stepper: Horizontal scroll or simplified view

---

## Accessibility Requirements

### WCAG AA Compliance
- ✅ Color contrast ≥ 4.5:1 for text
- ✅ Color contrast ≥ 3:1 for UI components
- ✅ Touch targets ≥ 48×48px
- ✅ Keyboard navigation fully supported
- ✅ Focus indicators visible (2px outline)
- ✅ Screen reader support (semantic HTML + ARIA)
- ✅ Reduced motion support (@media prefers-reduced-motion)

### Specific implementations
- `role="main"` on main content
- `aria-live="polite"` on streaming text
- `aria-busy="true"` during loading
- `aria-label` on icon-only buttons
- Skip to main content link
- Semantic HTML (`<button>`, `<input>`, not divs)

---

## Implementation Approach

### Phase 1: Foundation (Structure & Tokens)
1. Update CSS custom properties (spacing, colors, motion)
2. Create icon SVG library
3. Add progress stepper component
4. Implement loading states

### Phase 2: Message Types (Visual Hierarchy)
1. Refactor message rendering with proper classes
2. Add icons to each message type
3. Implement message entry animations
4. Add streaming cursor to proper messages

### Phase 3: Interactions (Micro-animations)
1. Button hover/press states with transforms
2. Input focus states with rings
3. Intent card hover effects
4. Progress stepper transitions

### Phase 4: Polish (Details)
1. Optimize animation timing
2. Add reduced-motion support
3. Test accessibility with keyboard/screen reader
4. Performance optimization (animation GPU acceleration)

---

## Success Criteria

### Functional
- ✅ All existing features work (no regressions)
- ✅ Streaming continues to work smoothly
- ✅ Intent selection flows correctly
- ✅ User input captures responses properly

### Visual
- ✅ Progress stepper shows current stage
- ✅ Message types visually distinct
- ✅ Loading states visible and smooth
- ✅ Icons enhance comprehension

### Interaction
- ✅ Buttons feel responsive (hover/press)
- ✅ Inputs show clear focus states
- ✅ Animations smooth (no jank)
- ✅ Reduced motion respected

### Accessibility
- ✅ WCAG AA compliant
- ✅ Keyboard navigation works
- ✅ Screen reader friendly
- ✅ Touch targets adequate

### Performance
- ✅ First meaningful paint <1s
- ✅ Animations at 60fps
- ✅ No layout shift during load
- ✅ Smooth scrolling

---

## Rationale (Five Pillars)

### 1. Purpose Drives Execution
**Why this redesign?**
- Current UI doesn't convey professionalism needed for decision-making tool
- Lack of progress indication creates uncertainty
- Poor visual hierarchy makes conversation hard to follow
- Missing micro-interactions reduce trust

### 2. Craft Embeds Care
**Details that show refinement**:
- Progress stepper with subtle pulse on active step
- Message types with semantic colors and icons
- Smooth transitions (not instant state changes)
- Loading states that reduce perceived wait time
- Hover effects that provide tactile feedback

### 3. Constraints Enable Creativity
**System constraints**:
- 8px spacing system (forces rhythm)
- Limited color palette (forces semantic usage)
- Consistent border-radius (creates coherence)
- Standardized motion timing (feels unified)

These constraints enable creative expression within a professional framework.

### 4. Intentional Incompleteness
**What's customizable**:
- Color scheme (can adapt to dark mode later)
- Icon style (can swap icon set)
- Conversation tone (already personalized through content)

**What's locked for quality**:
- Spacing rhythm (maintains visual consistency)
- Motion timing (preserves professional feel)
- Accessibility minimums (non-negotiable)

### 5. Design for Humans
**Human-centered decisions**:
- Touch targets for mobile users
- High contrast for low vision users
- Reduced motion for vestibular sensitivity
- Clear language for cognitive clarity
- Loading states to reduce anxiety
- Progress indication to provide control

---

## Next Steps

1. **Implement CSS foundation** (tokens, reset, utility classes)
2. **Build component library** (buttons, inputs, cards, icons)
3. **Refactor HTML structure** (semantic, accessible)
4. **Integrate JavaScript interactions** (animations, states)
5. **Test thoroughly** (cross-browser, accessibility, performance)

---

**Quality target: 9.5/10**
- Base 5.0 (technically correct, accessible)
- +1.5 Visual refinement (hierarchy, spacing, typography)
- +1.0 Motion refinement (smooth animations, loading states)
- +1.0 Interaction refinement (hover effects, micro-interactions)
- +1.0 Quality details (icons, progress indication, polish)

**Result**: Professional, trustworthy decision exploration tool that guides users with confidence.
