# Outcomist Design Quick Reference

**For rapid lookups and common decisions**

---

## Design Tokens (Copy-Paste Ready)

### Colors

```css
/* Primary (Blue) */
--blue-50: #F0F5FF;
--blue-500: #3B7FE8;   /* Primary actions, links */
--blue-700: #2563EB;   /* Hover states */

/* Neutrals (Gray) */
--gray-25: #FAFBFC;    /* Page background */
--gray-50: #F8F9FA;    /* Subtle backgrounds */
--gray-200: #E4E6E8;   /* Borders */
--gray-500: #6B7280;   /* Placeholders */
--gray-800: #1A1D21;   /* Body text */
--gray-900: #0D0F11;   /* Headlines */

/* Semantic */
--success-500: #10B981;
--error-500: #EF4444;
--warning-500: #F59E0B;
```

### Typography

```css
/* Sizes */
--font-size-sm: 14px;    /* Labels, captions */
--font-size-base: 16px;  /* Body text */
--font-size-xl: 24px;    /* Section headings */
--font-size-2xl: 32px;   /* Page headlines */

/* Weights */
--font-weight-normal: 400;    /* Body */
--font-weight-medium: 500;    /* Labels */
--font-weight-semibold: 600;  /* Emphasis */
--font-weight-bold: 700;      /* Headlines */
```

### Spacing

```css
--space-2: 8px;    /* Tight spacing */
--space-4: 16px;   /* Default spacing */
--space-6: 24px;   /* Generous spacing */
--space-12: 48px;  /* Section spacing */
```

### Motion

```css
--duration-fast: 150ms;  /* Hover, toggles */
--duration-base: 250ms;  /* Standard transitions */
--ease-out: cubic-bezier(0.33, 1, 0.68, 1);
```

---

## Common Component Patterns

### Button (Primary)

```svelte
<button class="btn-primary">
  Click Me
</button>

<style>
.btn-primary {
  background: var(--blue-500);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 150ms ease-out;
}

.btn-primary:hover {
  background: var(--blue-700);
  transform: translateY(-1px);
}

.btn-primary:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.1);
}
</style>
```

### Input Field

```svelte
<input
  type="text"
  class="input"
  placeholder="Enter text..."
/>

<style>
.input {
  width: 100%;
  padding: 16px;
  font-size: 16px;
  border: 1px solid var(--gray-200);
  border-radius: 8px;
  transition: all 150ms ease-out;
}

.input:focus {
  border-color: var(--blue-500);
  box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.1);
  outline: none;
}
</style>
```

### Message Bubble (User)

```svelte
<div class="message-user">
  Message content here
</div>

<style>
.message-user {
  background: var(--blue-500);
  color: white;
  padding: 16px 20px;
  border-radius: 12px;
  max-width: 600px;
  margin-left: auto;
  box-shadow: 0 1px 3px rgba(59, 127, 232, 0.3);
}
</style>
```

### Message Bubble (Assistant)

```svelte
<div class="message-assistant">
  Message content here
</div>

<style>
.message-assistant {
  background: white;
  color: var(--gray-800);
  padding: 16px 20px;
  border-radius: 12px;
  border: 1px solid var(--gray-200);
  max-width: 600px;
  margin-right: auto;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}
</style>
```

### Card

```svelte
<div class="card">
  Card content
</div>

<style>
.card {
  background: white;
  border: 1px solid var(--gray-200);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
</style>
```

---

## Decision Frameworks

### "Should I add this feature?"

Ask:
1. Does it help users make better decisions?
2. Does it enhance trust?
3. Does it support (not distract from) conversation?
4. Is it needed now or only sometimes?
5. Does it work across devices?

**If 3+ "no" → Don't add it**

### "How should I style this?"

Use this priority order:
1. **Hierarchy:** Size, weight, color guide attention
2. **Consistency:** Match existing patterns
3. **Clarity:** Purpose obvious at glance
4. **Refinement:** Polish details (shadows, spacing, borders)
5. **Accessibility:** Contrast, touch targets, keyboard

### "What animation timing?"

- **Instant feedback** (<100ms): Hover, highlighting
- **Quick transition** (150ms): Toggles, button states
- **Standard** (250ms): Modals, slides, default
- **Deliberate** (400ms+): Page changes, dramatic

**Default:** 150ms for most interactions

---

## Accessibility Checklist

### Color Contrast
- [ ] Body text (16px): 4.5:1 minimum
- [ ] Large text (24px+): 3:1 minimum
- [ ] UI components: 3:1 minimum

### Keyboard Navigation
- [ ] All interactive elements keyboard accessible
- [ ] Visible focus indicators
- [ ] Logical tab order
- [ ] Escape closes modals

### Screen Readers
- [ ] Icon-only buttons have `aria-label`
- [ ] Form inputs have labels
- [ ] Dynamic content in `aria-live` regions
- [ ] Semantic HTML (`nav`, `main`, `article`)

### Motion
- [ ] `prefers-reduced-motion` respected
- [ ] Animations optional, not essential

---

## Common Mistakes to Avoid

### ❌ Hardcoded Values
```css
/* Bad */
font-size: 16px;
color: #3B7FE8;
padding: 20px;

/* Good */
font-size: var(--font-size-base);
color: var(--blue-500);
padding: var(--space-5);
```

### ❌ Missing Focus States
```css
/* Bad */
.button:hover {
  background: blue;
}

/* Good */
.button:hover {
  background: blue;
}
.button:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

### ❌ Inaccessible Colors
```css
/* Bad - fails contrast */
color: #94969A;  /* on white background */

/* Good */
color: var(--gray-800);  /* sufficient contrast */
```

### ❌ Absolute Positioning
```css
/* Bad - brittle */
position: absolute;
left: 50%;
transform: translateX(-50%);

/* Good - flexible */
display: flex;
justify-content: center;
```

### ❌ Magic Numbers
```css
/* Bad */
padding-bottom: 25vh;  /* Why 25? */

/* Good */
padding-bottom: var(--space-20);  /* System value */
```

---

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 639px) {
  /* Full-width, larger touch targets, simpler layout */
}

/* Tablet */
@media (min-width: 640px) and (max-width: 1023px) {
  /* Two-column, optimized for both orientations */
}

/* Desktop */
@media (min-width: 1024px) {
  /* Full sidebar, generous spacing, hover states */
}
```

---

## File Organization

```
src/
├── styles/
│   ├── tokens.css          # All design tokens
│   ├── typography.css      # Type classes
│   ├── colors.css          # Color utilities
│   ├── spacing.css         # Spacing utilities
│   └── motion.css          # Animation utilities
├── components/
│   ├── Button.svelte
│   ├── Input.svelte
│   ├── MessageBubble.svelte
│   └── Card.svelte
└── App.svelte
```

---

## Git Workflow

### Branch Naming
```
design/component-name
design/feature-name
design/fix-description
```

### Commit Messages
```
design: Add typography scale tokens
design: Refine message bubble styling
design: Fix button focus states
```

---

## Testing Checklist

Before submitting:
- [ ] Matches design system tokens
- [ ] All interaction states work (hover/active/focus/disabled)
- [ ] Keyboard accessible
- [ ] Color contrast passes
- [ ] Responsive (mobile/tablet/desktop)
- [ ] Motion respects `prefers-reduced-motion`
- [ ] No console errors/warnings

---

## Resources

### Tools
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/devtools/)

### Documentation
- [Full Design System](./DESIGN-SYSTEM.md)
- [Design Philosophy](./DESIGN-PHILOSOPHY.md)
- [Design Recommendations](./DESIGN-RECOMMENDATIONS.md)

---

**Questions?** Check the full documentation or ask the design team.
