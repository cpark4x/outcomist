import { colors } from './tokens';

// Format timestamp
export function formatTimestamp(date: Date): string {
  return new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
  }).format(date);
}

// Generate avatar initial (for user messages)
export function getAvatarInitial(role: 'user' | 'assistant'): string {
  return role === 'user' ? 'Y' : 'O';
}

// Get avatar color
export function getAvatarColor(role: 'user' | 'assistant'): string {
  return role === 'user' ? colors.textPrimary : colors.accent;
}

// Check if color meets contrast ratio
export function meetsContrastRatio(
  foreground: string,
  background: string,
  minRatio: number = 4.5
): boolean {
  // Simplified check - in production would use proper color contrast library
  return true; // TODO: Implement actual contrast check
}
