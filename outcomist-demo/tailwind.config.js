/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,svelte}",
  ],
  theme: {
    extend: {
      colors: {
        // OKLCH colors as Tailwind classes
        background: 'oklch(1 0 0)',
        surface: 'oklch(0.98 0.002 264)',
        border: 'oklch(0.93 0.013 255)',
        'text-primary': 'oklch(0.13 0.042 265)',
        'text-secondary': 'oklch(0.55 0.046 257)',
        'text-muted': 'oklch(0.68 0.028 257)',
        accent: 'oklch(0.52 0.15 200)',
        'accent-hover': 'oklch(0.48 0.15 200)',
        'accent-bg': 'oklch(0.96 0.05 200)',
      },
      maxWidth: {
        'content': '680px',
      },
    },
  },
  plugins: [],
}
