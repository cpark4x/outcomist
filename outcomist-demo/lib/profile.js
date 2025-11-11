/**
 * Profile Management System
 *
 * Unified profile storage for both web and CLI with automatic learning.
 * Uses file-based storage for simplicity and universality.
 *
 * Features:
 * - Automatic extraction: Facts mentioned in conversation are automatically extracted and saved
 * - Smart merging: New facts merged with existing profile, avoiding duplicates
 * - Context injection: Profile automatically injected into conversation context
 * - Privacy-first: All data stored locally, gitignored
 *
 * Profile fields:
 * - name, age, role: Basic info
 * - goals, constraints, skills, values: Arrays of strings
 * - preferences.personalFacts: Other facts (e.g., "has 2 kids aged 8 and 10")
 */

import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Profile storage directory
const PROFILES_DIR = path.join(__dirname, '..', 'profiles');

/**
 * Load user profile
 * @returns {Promise<Object>} User profile or default empty profile
 */
export async function loadProfile() {
  const profilePath = path.join(PROFILES_DIR, 'self.json');

  try {
    const data = await fs.readFile(profilePath, 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    // Return default empty profile if file doesn't exist
    return createEmptyProfile();
  }
}

/**
 * Save user profile
 * @param {Object} profile - Profile data to save
 * @returns {Promise<void>}
 */
export async function saveProfile(profile) {
  const profilePath = path.join(PROFILES_DIR, 'self.json');

  // Ensure directory exists
  await fs.mkdir(PROFILES_DIR, { recursive: true });

  // Update timestamp
  profile.updatedAt = new Date().toISOString();

  // Save profile
  await fs.writeFile(
    profilePath,
    JSON.stringify(profile, null, 2),
    'utf-8'
  );
}

/**
 * Create empty profile with defaults
 * @returns {Object} Empty profile structure
 */
function createEmptyProfile() {
  return {
    profileId: 'self',
    name: null,
    age: null,
    role: null,
    goals: [],
    constraints: [],
    values: [],
    skills: [],
    preferences: {},
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  };
}

/**
 * Generate profile context string for injection into conversations
 * @param {Object} profile - User profile
 * @returns {string} Context string to prepend to prompts
 */
export function getProfileContext(profile) {
  if (!profile || (!profile.goals?.length && !profile.role && !profile.constraints?.length)) {
    return ''; // No context available
  }

  const parts = [];

  if (profile.name) {
    parts.push(`User's name: ${profile.name}`);
  }

  if (profile.age) {
    parts.push(`Age: ${profile.age}`);
  }

  if (profile.role) {
    parts.push(`Role: ${profile.role}`);
  }

  if (profile.goals?.length > 0) {
    parts.push(`Goals: ${profile.goals.join(', ')}`);
  }

  if (profile.skills?.length > 0) {
    parts.push(`Skills: ${profile.skills.join(', ')}`);
  }

  if (profile.constraints?.length > 0) {
    parts.push(`Constraints: ${profile.constraints.join(', ')}`);
  }

  if (profile.values?.length > 0) {
    parts.push(`Values: ${profile.values.join(', ')}`);
  }

  if (parts.length === 0) {
    return '';
  }

  return `\n\n# User Profile Context\n\nYou have the following information about this user from previous conversations:\n\n${parts.join('\n')}\n\nUse this context to personalize your guidance. Reference it naturally when relevant, and avoid asking questions you already know the answer to.\n`;
}

/**
 * Generate extraction prompt for Claude
 * @param {string} userMessage - User's message
 * @param {string} assistantResponse - Assistant's response
 * @returns {string} Prompt for extraction
 */
export function getExtractionPrompt(userMessage, assistantResponse) {
  return `Analyze this conversation and extract any personal facts the user mentioned about themselves. Return ONLY a JSON object (no markdown, no explanation) with these fields:

{
  "name": "string or null",
  "age": "number or null",
  "role": "string or null",
  "goals": ["array of strings"],
  "constraints": ["array of strings"],
  "skills": ["array of strings"],
  "values": ["array of strings"],
  "personalFacts": ["other facts mentioned, e.g., 'has 2 kids aged 8 and 10'"]
}

Only include facts explicitly stated by the user. If nothing new was mentioned, return all fields as null or empty arrays.

User message: "${userMessage}"
Assistant response: "${assistantResponse}"`;
}

/**
 * Merge extracted facts into existing profile
 * @param {Object} currentProfile - Current profile
 * @param {Object} extractedFacts - Facts extracted from conversation
 * @returns {Object} Merged profile
 */
export function mergeProfileFacts(currentProfile, extractedFacts) {
  const merged = { ...currentProfile };

  // Update simple fields if new data provided
  if (extractedFacts.name) merged.name = extractedFacts.name;
  if (extractedFacts.age) merged.age = extractedFacts.age;
  if (extractedFacts.role) merged.role = extractedFacts.role;

  // Merge arrays (avoid duplicates)
  const mergeArray = (current, newItems) => {
    if (!newItems || newItems.length === 0) return current;
    const combined = [...current, ...newItems];
    return [...new Set(combined)]; // Remove duplicates
  };

  merged.goals = mergeArray(merged.goals || [], extractedFacts.goals || []);
  merged.constraints = mergeArray(merged.constraints || [], extractedFacts.constraints || []);
  merged.skills = mergeArray(merged.skills || [], extractedFacts.skills || []);
  merged.values = mergeArray(merged.values || [], extractedFacts.values || []);

  // Handle personalFacts as a special array in preferences
  if (!merged.preferences) merged.preferences = {};
  if (!merged.preferences.personalFacts) merged.preferences.personalFacts = [];
  merged.preferences.personalFacts = mergeArray(
    merged.preferences.personalFacts,
    extractedFacts.personalFacts || []
  );

  return merged;
}
