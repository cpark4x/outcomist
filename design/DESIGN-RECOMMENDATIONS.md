# Outcomist Design Recommendations

**Version:** 1.0
**Last Updated:** 2025-01-11
**Status:** Implementation Roadmap

---

## Purpose

This document provides specific, actionable design recommendations for elevating Outcomist from its current state (functional 6/10) to target quality (sophisticated 9/10).

**Use this document for:**
- Sprint planning (what to build next)
- Design reviews (checklist for quality)
- Implementation guidance (specific changes)
- Progress tracking (what's done, what remains)

---

## Quick Summary

**Current State:** Functional foundation with good bones (6/10)
**Target State:** Professional, refined, trustworthy (9/10)
**Estimated Effort:** 8-12 days of focused work
**Priority Approach:** Foundation → Core Experience → Polish → Edge Cases

---

## Phase 1: Foundation (2-3 days)

**Goal:** Establish systematic design quality through tokens and standards

### 1.1 Implement Typography Scale

**Current Problem:**
- Inconsistent sizes (12, 13, 14, 15, 16, 32px)
- Weights underutilized (mostly 500/600)
- No clear hierarchy

**Recommendation:**
Create `src/styles/typography.css`:

```css
/* Typography Scale */
:root {
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-md: 18px;
  --font-size-lg: 20px;
  --font-size-xl: 24px;
  --font-size-2xl: 32px;
  --font-size-3xl: 40px;

  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.6;
}

/* Typography Classes */
.heading-1 {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
  color: var(--gray-900);
}

.heading-2 {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
  color: var(--gray-900);
}

.body {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-normal);
  line-height: var(--line-height-base);
  color: var(--gray-800);
}

.body-emphasis {
  font-weight: var(--font-weight-medium);
  color: var(--gray-900);
}

.caption {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-normal);
  line-height: var(--line-height-base);
  color: var(--gray-600);
}

.label {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-base);
  color: var(--gray-700);
}
```

**Apply to:**
- `WelcomeScreen.svelte` h1 → `.heading-1`
- `Header.svelte` title → `.body-emphasis`
- `MessageBubble.svelte` content → `.body`
- All labels/captions → `.caption` or `.label`

**Success Metric:**
- No hardcoded font-size values in components
- Clear visual hierarchy between text elements
- Consistent weight usage across app

**Effort:** 3-4 hours

---

### 1.2 Implement Color System

**Current Problem:**
- 13 shades of gray with unclear naming
- Single blue (#3B7FE8) with no hover/active/disabled variants
- No semantic colors (success, error, warning)

**Recommendation:**
Create `src/styles/colors.css`:

```css
:root {
  /* Blues (Brand & Interactive) */
  --blue-50: #F0F5FF;
  --blue-100: #D6E4FF;
  --blue-300: #85B3FF;
  --blue-500: #3B7FE8;
  --blue-700: #2563EB;
  --blue-900: #1E40AF;

  /* Grays (Neutrals) */
  --gray-25: #FAFBFC;
  --gray-50: #F8F9FA;
  --gray-100: #F3F4F6;
  --gray-200: #E4E6E8;
  --gray-300: #B8BABD;
  --gray-400: #94969A;
  --gray-500: #6B7280;
  --gray-600: #4A4E55;
  --gray-700: #3D4043;
  --gray-800: #1A1D21;
  --gray-900: #0D0F11;

  /* Semantic Colors */
  --success-50: #F0FDF4;
  --success-500: #10B981;
  --success-700: #047857;

  --error-50: #FEF2F2;
  --error-500: #EF4444;
  --error-700: #B91C1C;

  --warning-50: #FFFBEB;
  --warning-500: #F59E0B;
  --warning-700: #B45309;

  /* Semantic Aliases */
  --text-primary: var(--gray-900);
  --text-secondary: var(--gray-600);
  --text-tertiary: var(--gray-500);
  --text-disabled: var(--gray-400);

  --bg-primary: white;
  --bg-secondary: var(--gray-50);
  --bg-tertiary: var(--gray-100);

  --border-default: var(--gray-200);
  --border-emphasis: var(--gray-300);
}
```

**Apply to:**
- Replace all hardcoded colors with CSS variables
- Update buttons to use blue scale (hover: --blue-700, active: --blue-900)
- Add semantic colors for future error/success states

**Success Metric:**
- Zero hardcoded hex colors in components
- Hover/active states use appropriate blue shades
- Easy theme switching (change CSS variables only)

**Effort:** 4-5 hours

---

### 1.3 Implement Spacing System

**Current Problem:**
- Inconsistent padding (16px, 20px, 24px, 48px with no pattern)
- Magic numbers throughout

**Recommendation:**
Create `src/styles/spacing.css`:

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
}

/* Utility Classes */
.p-4 { padding: var(--space-4); }
.p-6 { padding: var(--space-6); }
.px-4 { padding-left: var(--space-4); padding-right: var(--space-4); }
.py-4 { padding-top: var(--space-4); padding-bottom: var(--space-4); }
.gap-4 { gap: var(--space-4); }
.mb-6 { margin-bottom: var(--space-6); }
/* etc. */
```

**Apply to:**
- Replace all hardcoded padding/margin/gap values
- Use multiples of 4px only
- Document exceptions if needed (with reasoning)

**Success Metric:**
- No random spacing values
- Visual rhythm feels consistent
- Easy to adjust globally if needed

**Effort:** 3-4 hours

---

### 1.4 Implement Motion System

**Current Problem:**
- Inconsistent durations (150ms, 200ms, 250ms, 600ms)
- No easing curve system
- No reduced-motion support

**Recommendation:**
Create `src/styles/motion.css`:

```css
:root {
  --duration-instant: 100ms;
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 600ms;

  --ease-out: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-in: cubic-bezier(0.32, 0, 0.67, 0);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Default Transition */
.transition-default {
  transition: all var(--duration-fast) var(--ease-out);
}

/* Reduced Motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Apply to:**
- Buttons: 150ms ease-out
- Hover effects: 150ms ease-out
- Modals: 250ms ease-out (open), 200ms ease-in (close)
- Page transitions: 400ms ease-out

**Success Metric:**
- Consistent animation timing across app
- Reduced-motion respected
- Animations feel purposeful, not janky

**Effort:** 2-3 hours

---

## Phase 2: Core Experience (3-4 days)

**Goal:** Elevate the key user touchpoints to 9/10 quality

### 2.1 Welcome Screen Refinement

**Current Problem:**
- Generic headline "What are you deciding?"
- No phase preview
- Logo is SVG text (not scalable asset)

**Recommendations:**

#### 2.1.1 Rewrite Headline

**Current:**
```svelte
<h1>What are you deciding?</h1>
```

**Recommended:**
```svelte
<h1 class="heading-1" style="font-size: 40px; margin-bottom: 16px;">
  Turn uncertainty into clarity
</h1>
<p class="body" style="font-size: 18px; color: var(--gray-600); margin-bottom: 48px;">
  Structured exploration of your decision through discovery, review, and execution
</p>
```

**Why:** Establishes unique value proposition, differentiates from generic AI chat

**Effort:** 30 minutes

---

#### 2.1.2 Add Phase Timeline

**Location:** Below headline, above input

**Implementation:**
```svelte
<div class="phase-timeline">
  <div class="phase-card">
    <div class="phase-icon">🔍</div>
    <div class="phase-name">Discover</div>
    <div class="phase-desc">~10 min</div>
  </div>
  <div class="phase-arrow">→</div>
  <div class="phase-card">
    <div class="phase-icon">📋</div>
    <div class="phase-name">Review</div>
    <div class="phase-desc">Proposal</div>
  </div>
  <div class="phase-arrow">→</div>
  <div class="phase-card">
    <div class="phase-icon">⚡</div>
    <div class="phase-name">Execute</div>
    <div class="phase-desc">Action Plan</div>
  </div>
</div>

<style>
.phase-timeline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-4);
  margin-bottom: var(--space-12);
}

.phase-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--space-4) var(--space-6);
  background: var(--gray-50);
  border: 1px solid var(--border-default);
  border-radius: 8px;
  min-width: 120px;
}

.phase-icon {
  font-size: 24px;
  margin-bottom: var(--space-2);
}

.phase-name {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-1);
}

.phase-desc {
  font-size: var(--font-size-xs);
  color: var(--text-secondary);
}

.phase-arrow {
  color: var(--gray-400);
  font-size: 18px;
}
</style>
```

**Why:** Sets expectations, builds trust, shows structured approach

**Effort:** 1-2 hours

---

#### 2.1.3 Create Real Logo Asset

**Current:** SVG with `<text>` element (not scalable)

**Recommended:** Commission or create proper vector logo

**Temporary Fix:** Use refined wordmark styling

```svelte
<!-- Replace in WelcomeScreen.svelte -->
<div class="logo-wordmark">
  <span class="logo-text">OUTCOMIST</span>
</div>

<style>
.logo-wordmark {
  position: absolute;
  top: 24px;
  left: 24px;
}

.logo-text {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--blue-500);
  /* Or gradient: */
  background: linear-gradient(90deg, #3B7FE8, #2563EB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
```

**Effort:** 1 hour (temporary), 4-6 hours (proper asset)

---

### 2.2 Message Styling Enhancement

**Current Problem:**
- User bubble flat blue (#3B7FE8)
- Assistant bubble too pale (#F5F7F9 vs #FAFBFC background)
- Shadows barely visible
- Tail-style corners feel dated

**Recommendations:**

#### 2.2.1 Refine Message Bubbles

**File:** `src/components/messages/MessageBubble.svelte`

**Current:**
```svelte
<style>
.message-bubble {
  background-color: {role === 'user' ? '#3B7FE8' : '#F5F7F9'};
  border-radius: {role === 'user' ? '12px 12px 4px 12px' : '12px 12px 12px 4px'};
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
</style>
```

**Recommended:**
```svelte
<style>
.message-bubble {
  padding: var(--space-4) var(--space-5);
  border-radius: 12px;  /* Modern, no tails */
  font-size: var(--font-size-base);
  line-height: var(--line-height-relaxed);
  max-width: 600px;
}

.message-user {
  background: var(--blue-500);
  color: white;
  margin-left: auto;
  box-shadow: 0 1px 3px rgba(59, 127, 232, 0.3);
}

.message-assistant {
  background: white;
  color: var(--gray-800);
  border: 1px solid var(--border-default);
  margin-right: auto;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.message-system {
  background: var(--blue-50);
  color: var(--gray-800);
  border-left: 3px solid var(--blue-500);
  margin: var(--space-6) auto;
  max-width: 700px;
}
</style>
```

**Why:**
- Better contrast between assistant bubble and background
- Subtle colored shadows enhance depth
- Modern rounded corners (no tails)
- Consistent with design system

**Effort:** 1 hour

---

### 2.3 Header Simplification

**Current Problem:**
- Logo + breadcrumbs + title + profile competing for attention
- Unclear hierarchy
- Title in absolute position (brittle)

**Recommendation:** Implement mockup Option 2 or 3

#### Option 2: Remove Logo from Header (Cleanest)

```svelte
<!-- Header.svelte -->
<header class="header">
  <div class="phases">
    <span class="phase" class:active={currentPhase === 'discover'}>Discover</span>
    <span class="arrow">→</span>
    <span class="phase" class:active={currentPhase === 'review'}>Review</span>
    <span class="arrow">→</span>
    <span class="phase" class:active={currentPhase === 'execute'}>Execute</span>
  </div>

  <div class="title">{projectTitle || 'New Decision'}</div>

  <button class="btn-secondary" on:click={openProfile}>
    Profile
  </button>
</header>

<style>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6);
  background: white;
  border-bottom: 1px solid var(--border-default);
}

.phases {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.phase {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--gray-400);
  transition: color var(--duration-fast) var(--ease-out);
}

.phase.active {
  color: var(--blue-500);
  font-weight: var(--font-weight-semibold);
}

.arrow {
  color: var(--gray-200);
  font-size: 18px;
}

.title {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--text-primary);
}
</style>
```

**Why:**
- Clean, focused, content-first
- Clear hierarchy (phases → title → actions)
- No competing attention centers

**Effort:** 2 hours

---

### 2.4 Phase Transition Cards

**Current Problem:**
- Phase changes happen invisibly
- Users don't understand journey structure

**Recommendation:** Implement in-stream phase cards (Variation 3 from mockups)

**Implementation:**
```svelte
<!-- PhaseTransitionCard.svelte -->
<script lang="ts">
  export let phase: 'discover' | 'review' | 'execute';
  export let onDismiss: () => void;

  const phaseInfo = {
    discover: {
      icon: '🔍',
      title: 'Phase 1: Discover',
      description: 'I\'ll ask questions to understand your priorities, constraints, and what matters most.',
      duration: '~10 minutes',
      next: 'Review Proposal'
    },
    review: {
      icon: '📋',
      title: 'Phase 2: Review Proposal',
      description: 'Based on our conversation, I\'ll share my recommendation and detailed reasoning.',
      duration: '~5 minutes',
      next: 'Execute Plan'
    },
    execute: {
      icon: '⚡',
      title: 'Phase 3: Execute Plan',
      description: 'I\'ll provide actionable steps to implement your decision with confidence.',
      duration: '~5 minutes',
      next: null
    }
  };

  const info = phaseInfo[phase];
</script>

<div class="phase-card">
  <button class="dismiss-btn" on:click={onDismiss} aria-label="Dismiss">
    ×
  </button>

  <div class="phase-header">
    <span class="phase-icon">{info.icon}</span>
    <span class="phase-title">{info.title}</span>
  </div>

  <p class="phase-description">{info.description}</p>

  <div class="phase-meta">
    <span class="phase-duration">{info.duration}</span>
    {#if info.next}
      <span class="phase-next">Next: {info.next}</span>
    {/if}
  </div>
</div>

<style>
.phase-card {
  position: relative;
  background: var(--blue-50);
  border-left: 3px solid var(--blue-500);
  border-radius: 12px;
  padding: var(--space-6);
  margin: var(--space-6) auto;
  max-width: 700px;
  animation: slideIn 300ms var(--ease-out);
}

.dismiss-btn {
  position: absolute;
  top: var(--space-3);
  right: var(--space-3);
  width: 24px;
  height: 24px;
  border: none;
  background: transparent;
  color: var(--gray-500);
  font-size: 24px;
  line-height: 1;
  cursor: pointer;
  transition: color var(--duration-fast) var(--ease-out);
}

.dismiss-btn:hover {
  color: var(--gray-700);
}

.phase-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}

.phase-icon {
  font-size: 24px;
}

.phase-title {
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  color: var(--text-primary);
}

.phase-description {
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
  color: var(--gray-700);
  margin-bottom: var(--space-4);
}

.phase-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: var(--font-size-sm);
}

.phase-duration {
  color: var(--gray-600);
  font-weight: var(--font-weight-medium);
}

.phase-next {
  color: var(--gray-500);
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
```

**Backend Change:** API should return phase metadata when transitioning:
```json
{
  "response": "...",
  "phaseTransition": {
    "phase": "review",
    "show": true
  }
}
```

**Effort:** 3-4 hours

---

## Phase 3: Polish (2-3 days)

**Goal:** Interaction states, spacing, accessibility

### 3.1 Interaction States

**Problem:** Buttons lack proper hover/active/disabled/focus states

**Recommendations:**

#### 3.1.1 Button States

```scss
// Add to all buttons
.btn {
  transition: all var(--duration-fast) var(--ease-out);
  cursor: pointer;

  &:hover {
    transform: translateY(-1px);
  }

  &:active {
    transform: translateY(0);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
  }

  &:focus-visible {
    outline: none;
    box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.1);
  }
}
```

**Effort:** 2 hours

---

#### 3.1.2 Input States

```scss
.input {
  &:hover:not(:disabled) {
    border-color: var(--gray-300);
  }

  &:focus {
    border-color: var(--blue-500);
    box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.1);
  }

  &:disabled {
    background: var(--gray-50);
    color: var(--gray-500);
    cursor: not-allowed;
  }

  &.error {
    border-color: var(--error-500);

    &:focus {
      box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
    }
  }
}
```

**Effort:** 1 hour

---

### 3.2 Spacing & Rhythm

**Task:** Audit all components and apply spacing system

**Checklist:**
- [ ] Header padding: `var(--space-6)`
- [ ] Message padding: `var(--space-4) var(--space-5)`
- [ ] Input padding: `var(--space-5) var(--space-6)`
- [ ] Card padding: `var(--space-6)`
- [ ] Gap between messages: `var(--space-4)`
- [ ] Section margins: `var(--space-12)`

**Effort:** 3-4 hours

---

### 3.3 Accessibility Basics

#### 3.3.1 Focus Indicators

**Requirement:** All interactive elements must have visible focus

**Implementation:**
```css
/* Global focus style */
*:focus-visible {
  outline: 2px solid var(--blue-500);
  outline-offset: 2px;
}

/* Component-specific overrides */
.btn-primary:focus-visible,
.input:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.1);
}
```

**Effort:** 1 hour

---

#### 3.3.2 ARIA Labels

**Requirement:** Icon-only buttons need labels

**Implementation:**
```svelte
<!-- Icon buttons in Sidebar.svelte -->
<button class="nav-item" aria-label="New decision" title="New decision">
  <svg>...</svg>
</button>

<button class="nav-item" aria-label="Recent decisions" title="Recent decisions">
  <svg>...</svg>
</button>

<!-- Voice button -->
<button aria-label="Record voice message" title="Record voice message">
  <MicrophoneIcon />
</button>
```

**Effort:** 1-2 hours

---

#### 3.3.3 Color Contrast Validation

**Task:** Verify all text meets WCAG AA standards

**Tool:** Use browser extensions or automated testing

**Required:**
- Body text (16px): 4.5:1 minimum
- Large text (24px+): 3:1 minimum
- UI components: 3:1 minimum

**Effort:** 1-2 hours

---

## Phase 4: Edge Cases (1-2 days)

**Goal:** Handle failure modes gracefully

### 4.1 API Failure States

**Implement:**
```svelte
<!-- ErrorMessage.svelte -->
<div class="error-message">
  <div class="error-icon">⚠️</div>
  <div class="error-content">
    <h4>Unable to connect</h4>
    <p>Please check that the backend server is running and try again.</p>
    <button class="btn-secondary" on:click={retry}>Retry</button>
  </div>
</div>
```

**Effort:** 2 hours

---

### 4.2 Loading States

**Implement:**
```svelte
<!-- LoadingIndicator.svelte -->
<div class="loading">
  <div class="spinner"></div>
  <span>Thinking...</span>
</div>

<style>
.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid var(--gray-200);
  border-top-color: var(--blue-500);
  border-radius: 50%;
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
```

**Effort:** 1 hour

---

### 4.3 Empty States

**Implement:**
- Empty profile (no data yet)
- Empty conversation history
- No quick replies available

**Effort:** 2-3 hours

---

## Implementation Priority

### Sprint 1: Foundation (Week 1)
- ✅ Typography scale
- ✅ Color system
- ✅ Spacing system
- ✅ Motion system

### Sprint 2: Core Experience (Week 2)
- ✅ Welcome screen refinement
- ✅ Message styling
- ✅ Header simplification
- ✅ Phase transition cards

### Sprint 3: Polish (Week 3)
- ✅ Interaction states
- ✅ Spacing audit
- ✅ Accessibility basics

### Sprint 4: Edge Cases (Week 3-4)
- ✅ Error states
- ✅ Loading states
- ✅ Empty states

---

## Success Criteria

### Visual Quality (9/10)
- [ ] Consistent typography hierarchy
- [ ] Cohesive color usage
- [ ] Systematic spacing
- [ ] Refined shadows and depth
- [ ] Professional polish throughout

### Interaction Quality (9/10)
- [ ] All states implemented (hover/active/disabled/focus)
- [ ] Smooth, purposeful animations
- [ ] Responsive feedback
- [ ] No janky transitions

### User Experience (9/10)
- [ ] Clear mental model of journey
- [ ] Always know where you are
- [ ] Errors handled gracefully
- [ ] Loading states visible
- [ ] Accessible to all users

### Brand Identity (9/10)
- [ ] Distinct from generic AI chat
- [ ] Professional and trustworthy
- [ ] Consistent voice and tone
- [ ] Memorable design touches

---

## Tracking Progress

Use this checklist to track implementation:

```markdown
## Foundation
- [ ] Typography scale implemented
- [ ] Color system implemented
- [ ] Spacing system implemented
- [ ] Motion system implemented

## Core Experience
- [ ] Welcome headline rewritten
- [ ] Phase timeline added
- [ ] Logo refined
- [ ] Message bubbles enhanced
- [ ] Header simplified
- [ ] Phase transition cards created

## Polish
- [ ] Button states complete
- [ ] Input states complete
- [ ] Spacing audit done
- [ ] Focus indicators visible
- [ ] ARIA labels added
- [ ] Contrast validated

## Edge Cases
- [ ] API errors handled
- [ ] Loading states shown
- [ ] Empty states designed
```

---

## Next Steps

1. **Review & Prioritize**: Team reviews recommendations, confirms priorities
2. **Sprint Planning**: Break work into manageable tickets
3. **Design Review**: Each component reviewed against design system
4. **User Testing**: Validate improvements with real users
5. **Iterate**: Refine based on feedback

---

## Questions?

Refer to:
- [Design System](./DESIGN-SYSTEM.md) for tokens and components
- [Design Philosophy](./DESIGN-PHILOSOPHY.md) for guiding principles
- Zen-architect analysis for detailed issues

**Let's elevate Outcomist to 9/10. 🚀**
