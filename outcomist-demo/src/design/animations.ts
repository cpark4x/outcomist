import { animation } from './tokens';

// Message entrance animation
export const slideInUp = {
  keyframes: {
    from: { opacity: 0, transform: 'translateY(12px)' },
    to: { opacity: 1, transform: 'translateY(0)' },
  },
  duration: animation.duration.normal,
  easing: animation.easing.out,
};

// Streaming indicator pulse
export const pulseOnce = {
  keyframes: {
    '0%, 100%': { opacity: 1 },
    '50%': { opacity: 0.5 },
  },
  duration: '600ms',
  easing: 'ease-in-out',
  iterationCount: 'infinite',
};

// Focus ring animation
export const focusRing = {
  ring: '3px',
  ringOpacity: '50%',
  transition: `all ${animation.duration.fast} ${animation.easing.out}`,
};

// Reduced motion support (mandatory)
export const reducedMotion = `
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
  }
`;
