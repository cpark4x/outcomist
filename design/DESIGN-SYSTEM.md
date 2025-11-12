# Outcomist Design System

**Version:** 1.0
**Last Updated:** 2025-01-11
**Status:** Foundation

---

## Purpose

This design system provides a comprehensive, systematic approach to creating consistent, professional, and accessible user interfaces for Outcomist. It establishes the visual and interaction patterns that make Outcomist feel cohesive, trustworthy, and distinct.

**Goals:**
- **Consistency**: Every touchpoint feels like part of the same product
- **Quality**: 9/10 polish through systematic application of principles
- **Efficiency**: Designers and developers can build quickly with confidence
- **Scalability**: Patterns work across web, mobile, and future platforms

---

## Design Principles

### 1. Structured Clarity
Decision-making is complex. Our interface makes it clear.

**What This Means:**
- Always show where the user is in their journey
- Use visual hierarchy to guide attention
- Reduce cognitive load through organization
- Make phase transitions explicit and understandable

### 2. Professional Confidence
Not playful chat, not corporate boring. Expert advisor.

**What This Means:**
- Visual refinement signals credibility
- Typography is readable and authoritative
- Colors convey stability and trust
- Motion is purposeful, never frivolous

### 3. Content-First Simplicity
The conversation is the product. UI recedes.

**What This Means:**
- Generous whitespace around conversation
- Minimal chrome (header/sidebar)
- No competing visual noise
- Focus on current message/task

### 4. Progressive Disclosure
Show what's relevant, when it's relevant.

**What This Means:**
- Welcome screen is minimal (headline + input)
- Phase indicators appear during conversation
- Advanced features hidden until needed
- Complexity introduced gradually

### 5. Responsive Thoughtfulness
Adapts to context and user needs.

**What This Means:**
- Different layouts for different states
- Touch targets sized appropriately
- Animations respect preferences
- Text scales for readability

---

## Foundation

### Typography

#### Type Scale

Our type scale follows a rational progression that creates clear hierarchy.

```scss
$font-size-xs: 12px;     // Captions, labels, metadata
$font-size-sm: 14px;     // Secondary text, descriptions
$font-size-base: 16px;   // Body text (default)
$font-size-md: 18px;     // Emphasized body text
$font-size-lg: 20px;     // Small headings
$font-size-xl: 24px;     // Section headings
$font-size-2xl: 32px;    // Page headlines
$font-size-3xl: 40px;    // Hero headlines (rare)
```

**Usage Guidelines:**
- **Body text**: 16px (never smaller)
- **Headings**: Create clear jumps (16 → 24 → 32, not 16 → 18 → 20)
- **UI labels**: 13-14px acceptable for metadata
- **Mobile**: Increase base to 17px for readability

#### Font Families

```scss
$font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                   'Roboto', 'Oxygen', 'Ubuntu', sans-serif;
$font-family-mono: 'SF Mono', Monaco, 'Cascadia Code',
                   'Roboto Mono', Consolas, monospace;
```

**Why System Fonts:**
- Native feel on each platform
- Zero loading time
- Optimized for screen readability
- Professional without being generic

#### Font Weights

```scss
$font-weight-normal: 400;    // Body text
$font-weight-medium: 500;    // Labels, navigation
$font-weight-semibold: 600;  // Emphasis, current state
$font-weight-bold: 700;      // Strong emphasis, headlines
```

**Usage Guidelines:**
- Default body: 400
- UI labels: 500
- Active/selected states: 600
- Headlines: 600-700
- Avoid 300 (too light for screens)

#### Line Height

```scss
$line-height-tight: 1.25;    // Headlines
$line-height-base: 1.5;      // Body text
$line-height-relaxed: 1.6;   // Long-form reading
```

**Usage Guidelines:**
- Headlines: 1.25 (tighter for visual impact)
- Interface text: 1.5 (balance of density and readability)
- Message content: 1.6 (easier reading for longer text)

#### Letter Spacing

```scss
$letter-spacing-tight: -0.02em;   // Large headings
$letter-spacing-normal: 0;         // Body text
$letter-spacing-wide: 0.05em;      // All-caps labels
```

---

### Color System

#### Primary Colors

**Blue (Brand & Interactive)**

```scss
$blue-50: #F0F5FF;   // Backgrounds, subtle highlights
$blue-100: #D6E4FF;  // Hover backgrounds
$blue-300: #85B3FF;  // Disabled states
$blue-500: #3B7FE8;  // Primary actions, links (default)
$blue-700: #2563EB;  // Hover states
$blue-900: #1E40AF;  // Active/pressed states
```

**Usage:**
- Primary buttons: $blue-500 background
- Links: $blue-500 text
- Hover: $blue-700
- Active/pressed: $blue-900
- Disabled: $blue-300
- Subtle backgrounds: $blue-50

#### Neutral Colors (Grays)

```scss
// Text Colors
$gray-900: #0D0F11;  // Primary text (headlines, emphasis)
$gray-800: #1A1D21;  // Body text
$gray-600: #4A4E55;  // Secondary text
$gray-500: #6B7280;  // Placeholder, disabled text
$gray-400: #94969A;  // Metadata, captions

// UI Colors
$gray-300: #B8BABD;  // Disabled states, subtle borders
$gray-200: #E4E6E8;  // Borders, dividers
$gray-100: #F3F4F6;  // Hover backgrounds
$gray-50: #F8F9FA;   // Subtle backgrounds
$gray-25: #FAFBFC;   // Page background
```

**Usage:**
- Headlines: $gray-900 (maximum contrast)
- Body text: $gray-800 (slightly softer for reading)
- Secondary info: $gray-600
- Placeholders: $gray-500
- Metadata: $gray-400
- Borders: $gray-200
- Backgrounds: $gray-50 or $gray-25

#### Semantic Colors

**Success (Green)**

```scss
$green-50: #F0FDF4;
$green-500: #10B981;
$green-700: #047857;
```

**Warning (Amber)**

```scss
$amber-50: #FFFBEB;
$amber-500: #F59E0B;
$amber-700: #B45309;
```

**Error (Red)**

```scss
$red-50: #FEF2F2;
$red-500: #EF4444;
$red-700: #B91C1C;
```

**Info (Cyan)**

```scss
$cyan-50: #ECFEFF;
$cyan-500: #06B6D4;
$cyan-700: #0E7490;
```

**Usage:**
- Success messages, confirmations: $green-500
- Warnings, cautions: $amber-500
- Errors, destructive actions: $red-500
- Informational notices: $cyan-500
- Backgrounds: Use -50 variants
- Text/icons: Use -500 for normal, -700 for emphasis

#### Accessibility

**Contrast Requirements:**
- Body text (16px): 4.5:1 minimum
- Large text (24px+): 3:1 minimum
- UI components: 3:1 minimum

**Valid Combinations:**
- ✅ $gray-900 on white (16.1:1)
- ✅ $gray-800 on white (13.5:1)
- ✅ $blue-500 on white (4.89:1)
- ✅ White on $blue-500 (4.89:1)
- ❌ $gray-500 on white (3.8:1) - fails for body text
- ❌ $gray-400 on white (2.9:1) - captions only

---

### Spacing System

Our spacing system uses multiples of 4px for consistency.

```scss
$space-1: 4px;
$space-2: 8px;
$space-3: 12px;
$space-4: 16px;
$space-5: 20px;
$space-6: 24px;
$space-8: 32px;
$space-10: 40px;
$space-12: 48px;
$space-16: 64px;
$space-20: 80px;
$space-24: 96px;
```

**Usage Guidelines:**
- **Tight spacing**: 4-8px (related elements, inline items)
- **Default spacing**: 16-24px (component padding, gaps)
- **Section spacing**: 32-48px (between major sections)
- **Layout spacing**: 64-96px (page margins, hero sections)

**Examples:**
```scss
// Button padding
padding: $space-3 $space-6;  // 12px 24px

// Message gap
gap: $space-4;  // 16px

// Section margin
margin-bottom: $space-12;  // 48px

// Page padding
padding: $space-6;  // 24px
```

---

### Border Radius

```scss
$radius-sm: 4px;    // Small elements (badges, tags)
$radius-md: 8px;    // Buttons, inputs, cards
$radius-lg: 12px;   // Large cards, modals
$radius-xl: 16px;   // Hero elements (rare)
$radius-full: 9999px;  // Pills, avatars
```

**Usage:**
- Buttons: $radius-md (8px)
- Input fields: $radius-md (8px)
- Message bubbles: $radius-lg (12px)
- Cards: $radius-lg (12px)
- Pills/badges: $radius-full

---

### Shadows

Shadows create depth and hierarchy.

```scss
// Elevation 1: Subtle lift
$shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);

// Elevation 2: Cards, buttons
$shadow-md: 0 1px 3px rgba(0, 0, 0, 0.08),
            0 1px 2px rgba(0, 0, 0, 0.04);

// Elevation 3: Dropdowns, popovers
$shadow-lg: 0 4px 6px rgba(0, 0, 0, 0.07),
            0 2px 4px rgba(0, 0, 0, 0.05);

// Elevation 4: Modals, overlays
$shadow-xl: 0 10px 15px rgba(0, 0, 0, 0.1),
            0 4px 6px rgba(0, 0, 0, 0.05);

// Focus state
$shadow-focus: 0 0 0 3px rgba(59, 127, 232, 0.1);
```

**Usage:**
- Default cards: $shadow-sm
- Hover state: $shadow-md
- Dropdowns: $shadow-lg
- Modals: $shadow-xl
- Focus rings: $shadow-focus

---

### Motion & Animation

Motion should be purposeful and performant.

#### Durations

```scss
$duration-instant: 100ms;    // Immediate feedback (hover)
$duration-fast: 150ms;       // Quick transitions (toggles)
$duration-base: 250ms;       // Standard transitions (default)
$duration-slow: 400ms;       // Deliberate transitions (modals)
$duration-slower: 600ms;     // Dramatic transitions (page changes)
```

#### Easing

```scss
$ease-out: cubic-bezier(0.33, 1, 0.68, 1);      // Entrances (default)
$ease-in: cubic-bezier(0.32, 0, 0.67, 0);       // Exits
$ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);   // Both directions
$ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); // Bounce (special)
```

**Usage Guidelines:**
- **Hover effects**: 150ms, ease-out
- **Toggle states**: 150ms, ease-out
- **Button press**: 100ms, ease-in
- **Modal open**: 250ms, ease-out
- **Modal close**: 200ms, ease-in
- **Slide transitions**: 250ms, ease-out
- **Spring effects**: 300ms, ease-spring (rare, use sparingly)

#### Reduced Motion

Always respect user preferences:

```scss
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Components

### Buttons

#### Primary Button

The main call-to-action. Use sparingly (1-2 per screen).

```scss
.btn-primary {
  background: $blue-500;
  color: white;
  padding: $space-3 $space-6;  // 12px 24px
  border-radius: $radius-md;
  font-size: $font-size-base;
  font-weight: $font-weight-medium;
  border: none;
  cursor: pointer;
  transition: all $duration-fast $ease-out;

  &:hover {
    background: $blue-700;
    transform: translateY(-1px);
    box-shadow: $shadow-md;
  }

  &:active {
    background: $blue-900;
    transform: translateY(0);
  }

  &:disabled {
    background: $blue-300;
    cursor: not-allowed;
    transform: none;
  }

  &:focus-visible {
    outline: none;
    box-shadow: $shadow-focus;
  }
}
```

#### Secondary Button

Alternative actions, less emphasis.

```scss
.btn-secondary {
  background: transparent;
  color: $gray-800;
  padding: $space-3 $space-6;
  border-radius: $radius-md;
  font-size: $font-size-base;
  font-weight: $font-weight-medium;
  border: 1px solid $gray-200;
  cursor: pointer;
  transition: all $duration-fast $ease-out;

  &:hover {
    background: $gray-50;
    border-color: $gray-300;
  }

  &:active {
    background: $gray-100;
  }

  &:disabled {
    color: $gray-500;
    cursor: not-allowed;
  }

  &:focus-visible {
    outline: none;
    box-shadow: $shadow-focus;
  }
}
```

#### Icon Button

Square button for icons (sidebar, toolbars).

```scss
.btn-icon {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: $radius-md;
  border: none;
  background: transparent;
  color: $gray-600;
  cursor: pointer;
  transition: all $duration-fast $ease-out;

  &:hover {
    background: $gray-100;
    color: $gray-900;
  }

  &:active {
    background: $gray-200;
    transform: scale(0.95);
  }

  &.active {
    background: $blue-50;
    color: $blue-500;
  }
}
```

**Accessibility:**
- Minimum touch target: 44×44px
- Include `aria-label` for icon-only buttons
- Visible focus indicator required

---

### Input Fields

#### Text Input

```scss
.input-text {
  width: 100%;
  padding: $space-4 $space-4;  // 16px
  font-size: $font-size-base;
  font-family: $font-family-base;
  border: 1px solid $gray-200;
  border-radius: $radius-md;
  background: white;
  color: $gray-900;
  transition: all $duration-fast $ease-out;

  &::placeholder {
    color: $gray-500;
  }

  &:hover {
    border-color: $gray-300;
  }

  &:focus {
    outline: none;
    border-color: $blue-500;
    box-shadow: $shadow-focus;
  }

  &:disabled {
    background: $gray-50;
    color: $gray-500;
    cursor: not-allowed;
  }

  &.error {
    border-color: $red-500;

    &:focus {
      box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
    }
  }
}
```

#### Textarea

```scss
.input-textarea {
  @extend .input-text;
  min-height: 120px;
  resize: vertical;
  line-height: $line-height-base;
  padding: $space-5 $space-6;  // 20px 24px
}
```

**Accessibility:**
- Labels required (visible or aria-label)
- Error messages linked with aria-describedby
- Placeholder is not a substitute for label

---

### Message Bubbles

#### User Message

```scss
.message-user {
  background: $blue-500;
  color: white;
  padding: $space-4 $space-5;  // 16px 20px
  border-radius: $radius-lg;
  font-size: $font-size-base;
  line-height: $line-height-relaxed;
  max-width: 600px;
  margin-left: auto;
  box-shadow: $shadow-sm;
}
```

#### Assistant Message

```scss
.message-assistant {
  background: white;
  color: $gray-800;
  padding: $space-4 $space-5;
  border-radius: $radius-lg;
  border: 1px solid $gray-200;
  font-size: $font-size-base;
  line-height: $line-height-relaxed;
  max-width: 600px;
  margin-right: auto;
  box-shadow: $shadow-sm;
}
```

#### System Message (Phase Cards)

```scss
.message-system {
  background: $blue-50;
  color: $gray-800;
  padding: $space-4 $space-6;
  border-radius: $radius-lg;
  border-left: 3px solid $blue-500;
  font-size: $font-size-sm;
  line-height: $line-height-base;
  max-width: 700px;
  margin: $space-6 auto;
}
```

---

### Cards

#### Basic Card

```scss
.card {
  background: white;
  border: 1px solid $gray-200;
  border-radius: $radius-lg;
  padding: $space-6;
  box-shadow: $shadow-sm;
  transition: all $duration-fast $ease-out;

  &:hover {
    box-shadow: $shadow-md;
    border-color: $gray-300;
  }
}
```

#### Interactive Card (Clickable)

```scss
.card-interactive {
  @extend .card;
  cursor: pointer;

  &:hover {
    transform: translateY(-2px);
    box-shadow: $shadow-lg;
  }

  &:active {
    transform: translateY(0);
  }
}
```

---

### Loading States

#### Spinner

```scss
.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid $gray-200;
  border-top-color: $blue-500;
  border-radius: $radius-full;
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

#### Skeleton Loader

```scss
.skeleton {
  background: linear-gradient(
    90deg,
    $gray-100 0%,
    $gray-50 50%,
    $gray-100 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: $radius-md;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

### Focus Indicators

All interactive elements must have visible focus indicators for keyboard navigation.

```scss
// Global focus style
*:focus-visible {
  outline: 2px solid $blue-500;
  outline-offset: 2px;
}

// Custom focus for specific components
.btn-primary:focus-visible,
.input-text:focus-visible {
  outline: none;
  box-shadow: $shadow-focus;
}
```

---

## Layout Patterns

### Page Layout

```
┌─────────────────────────────────────────┐
│ Sidebar (60px)  │  Main Content Area   │
│                 │                       │
│  [icon]         │  Header (optional)    │
│  [icon]         │  ─────────────────    │
│  [icon]         │                       │
│                 │  Content              │
│                 │                       │
│                 │                       │
└─────────────────────────────────────────┘
```

**Grid:**
- Sidebar: 60px fixed width
- Main: Flexible (100% - 60px)
- Content max-width: 900px centered
- Padding: 24px minimum

### Welcome Screen

```
┌─────────────────────────────────────────┐
│                                         │
│  Logo (top-left)                        │
│                                         │
│                                         │
│         Centered Content                │
│         ───────────────                 │
│         Headline                        │
│         Phase Timeline                  │
│         Input                           │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

**Specs:**
- Content max-width: 700px
- Vertical centering with padding-bottom offset (25vh)
- Logo absolute positioned (24px, 24px)

### Conversation Layout

```
┌─────────────────────────────────────────┐
│ Sidebar │ Header                        │
│         │ ───────────────────────────   │
│  [O]    │                               │
│  ─      │  Message List                 │
│  [+]    │  (scrollable)                 │
│  [⏱]    │                               │
│  [🔍]   │                               │
│         │                               │
│         │ ───────────────────────────   │
│         │ Input Area (fixed bottom)     │
└─────────────────────────────────────────┘
```

**Specs:**
- Header height: ~72px (flexible based on content)
- Message list: Scrollable, max-width 900px centered
- Input: Fixed bottom, max-width 900px centered
- Padding: 24px sides, 20px top/bottom for input

---

## Responsive Breakpoints

```scss
$breakpoint-sm: 640px;   // Mobile landscape
$breakpoint-md: 768px;   // Tablet portrait
$breakpoint-lg: 1024px;  // Tablet landscape
$breakpoint-xl: 1280px;  // Desktop
$breakpoint-2xl: 1536px; // Large desktop
```

**Responsive Adjustments:**

**Mobile (<640px):**
- Hide sidebar or collapse to hamburger
- Reduce padding (16px instead of 24px)
- Stack elements vertically
- Increase base font size to 17px
- Full-width buttons

**Tablet (640-1024px):**
- Sidebar visible but narrower (48px)
- Maintain two-column layout
- Slightly reduced padding (20px)

**Desktop (>1024px):**
- Full sidebar (60px)
- Generous padding (24px+)
- Max-width constraints for readability

---

## Accessibility Guidelines

### Color Contrast

**Text:**
- Large text (24px+): 3:1 minimum
- Regular text (16px): 4.5:1 minimum
- Enhanced (AAA): 7:1 recommended

**UI Components:**
- Icons: 3:1 minimum
- Borders: 3:1 minimum
- Focus indicators: 3:1 minimum

### Keyboard Navigation

**Required:**
- All interactive elements keyboard accessible
- Visible focus indicators
- Logical tab order
- Skip links for main content
- Escape key closes modals/dropdowns

### Screen Readers

**Required:**
- Semantic HTML (nav, main, article, etc.)
- ARIA labels on icon-only buttons
- ARIA live regions for dynamic content
- Alternative text for images
- Form labels properly associated

### Motion

**Required:**
- Respect `prefers-reduced-motion`
- Animations optional, not essential
- Disable animations when preference set

---

## Design Tokens (JSON)

For programmatic access:

```json
{
  "colors": {
    "blue": {
      "50": "#F0F5FF",
      "500": "#3B7FE8",
      "700": "#2563EB"
    },
    "gray": {
      "25": "#FAFBFC",
      "50": "#F8F9FA",
      "200": "#E4E6E8",
      "500": "#6B7280",
      "800": "#1A1D21",
      "900": "#0D0F11"
    }
  },
  "spacing": {
    "1": "4px",
    "4": "16px",
    "6": "24px",
    "12": "48px"
  },
  "fontSize": {
    "sm": "14px",
    "base": "16px",
    "xl": "24px",
    "2xl": "32px"
  },
  "fontWeight": {
    "normal": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700
  },
  "borderRadius": {
    "md": "8px",
    "lg": "12px",
    "full": "9999px"
  },
  "duration": {
    "fast": "150ms",
    "base": "250ms"
  }
}
```

---

## Usage Guidelines

### When to Use This System

✅ **Always:**
- New components
- UI refactoring
- Bug fixes that touch styling
- Feature additions

✅ **Consult:**
- When creating custom patterns
- When deviating from standards
- When unsure about approach

❌ **Never:**
- Arbitrary values (use tokens)
- Inline styles (use classes)
- Magic numbers (document reasoning)

### Contributing

When extending this system:

1. **Propose changes** in design folder
2. **Document rationale** (why this change?)
3. **Show examples** (how is it used?)
4. **Update tokens** (maintain consistency)
5. **Test accessibility** (contrast, keyboard, screen reader)

---

## Maintenance

**Review Cadence:**
- Minor updates: As needed
- Major review: Quarterly
- Breaking changes: Major version bump

**Version History:**
- 1.0 (2025-01-11): Initial design system foundation

---

## Resources

- [Figma Design File](#) - TBD
- [Component Library](#) - TBD
- [Design Tokens (JSON)](#) - TBD
- [Accessibility Checklist](./ACCESSIBILITY.md) - TBD

---

**Questions or suggestions?** Open an issue or contact the design team.
