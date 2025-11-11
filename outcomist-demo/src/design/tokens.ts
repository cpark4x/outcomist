// OKLCH Color System (perceptually uniform)
export const colors = {
  // Surface colors
  background: 'oklch(1 0 0)',              // Pure white
  surface: 'oklch(0.98 0.002 264)',        // Off-white with blue tint
  border: 'oklch(0.93 0.013 255)',         // Light gray border

  // Text colors
  textPrimary: 'oklch(0.13 0.042 265)',    // Dark slate (16.7:1 contrast)
  textSecondary: 'oklch(0.55 0.046 257)',  // Mid gray (7.2:1 contrast)
  textMuted: 'oklch(0.68 0.028 257)',      // Light gray

  // Accent (teal)
  accent: 'oklch(0.52 0.15 200)',          // Sophisticated teal (4.8:1 contrast)
  accentHover: 'oklch(0.48 0.15 200)',     // Darker teal
  accentBg: 'oklch(0.96 0.05 200)',        // Subtle teal background
};

// Spacing System (8px grid)
export const spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
  xxl: '48px',
};

// Typography System
export const typography = {
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
};

// Animation System
export const animation = {
  duration: {
    instant: '50ms',
    fast: '100ms',
    normal: '150ms',
    deliberate: '250ms',
  },
  easing: {
    out: 'cubic-bezier(0.23, 1, 0.32, 1)',
    inOut: 'cubic-bezier(0.45, 0, 0.55, 1)',
    spring: 'cubic-bezier(0.34, 1.56, 0.64, 1)',  // Spring physics
  },
  stagger: {
    xs: '50ms',
    sm: '100ms',
    md: '150ms',
    lg: '300ms',
  },
};

// Layout Constants
export const layout = {
  maxWidth: '680px',
  messagePadding: '24px',
  messageGap: '32px',
  inputHeight: '56px',
  avatarSize: '40px',
};
