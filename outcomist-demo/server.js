import 'dotenv/config';
import express from 'express';
import Anthropic from '@anthropic-ai/sdk';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { loadProfile, saveProfile, getProfileContext, getExtractionPrompt, mergeProfileFacts } from './lib/profile.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

// Get API key from environment or Claude Code config
let apiKey = process.env.ANTHROPIC_API_KEY;

// If not in env, try to read from Claude Code config
if (!apiKey) {
  try {
    const homeDir = process.env.HOME || process.env.USERPROFILE;
    const configPath = path.join(homeDir, '.anthropic', 'api_key');
    if (fs.existsSync(configPath)) {
      apiKey = fs.readFileSync(configPath, 'utf-8').trim();
      console.log('✓ Loaded API key from ~/.anthropic/api_key');
    }
  } catch (error) {
    console.error('Failed to load API key from config:', error.message);
  }
}

if (!apiKey) {
  console.error('❌ ERROR: ANTHROPIC_API_KEY not found!');
  console.error('Please set it in your environment or create ~/.anthropic/api_key');
  process.exit(1);
}

// Initialize Anthropic client
const client = new Anthropic({
  apiKey: apiKey
});

// Load the /explore prompt from the CLI command file
const explorePromptPath = path.join(__dirname, '../.claude/commands/explore.md');
let EXPLORE_SYSTEM_PROMPT = '';

try {
  EXPLORE_SYSTEM_PROMPT = fs.readFileSync(explorePromptPath, 'utf-8');
  console.log('✓ Loaded /explore prompt from .claude/commands/explore.md');
} catch (error) {
  console.error('❌ Failed to load /explore prompt:', error.message);
  console.log('Using fallback prompt');
  EXPLORE_SYSTEM_PROMPT = 'You are Outcomist, a decision exploration tool that helps users think through decisions.';
}

// Endpoint to call /explore command with real Claude API
app.post('/api/explore', async (req, res) => {
  const { message, conversationHistory } = req.body;

  try {
    // Load user profile for context injection
    const profile = await loadProfile();
    const profileContext = getProfileContext(profile);

    // Build message history for Claude
    const messages = [];

    // Add conversation history if exists
    if (conversationHistory && conversationHistory.length > 0) {
      conversationHistory.forEach(msg => {
        messages.push({
          role: msg.role,
          content: msg.content
        });
      });
    }

    // Add current message
    messages.push({
      role: 'user',
      content: message
    });

    // Build system prompt with profile context
    const systemPrompt = EXPLORE_SYSTEM_PROMPT + profileContext;

    // Call Claude API with the /explore system prompt + profile context
    const response = await client.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 4096,
      system: systemPrompt,
      messages: messages
    });

    // Extract the response text
    const responseText = response.content[0].text;

    // Extract profile information in background (don't block response)
    extractProfileFacts(message, responseText).catch(err => {
      console.error('Profile extraction error (non-blocking):', err.message);
    });

    res.json({
      response: responseText,
      needsInput: true  // Always return true to continue conversation
    });

  } catch (error) {
    console.error('Error calling Claude API:', error);
    res.status(500).json({
      error: 'Failed to process request',
      details: error.message
    });
  }
});

/**
 * Extract profile facts from conversation turn (async, non-blocking)
 */
async function extractProfileFacts(userMessage, assistantResponse) {
  try {
    // Generate extraction prompt
    const extractionPrompt = getExtractionPrompt(userMessage, assistantResponse);

    // Call Claude to extract facts
    const extractionResponse = await client.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1024,
      system: 'You are a profile extraction assistant. Extract personal facts mentioned by the user and return ONLY valid JSON.',
      messages: [{
        role: 'user',
        content: extractionPrompt
      }]
    });

    // Parse extracted facts
    const extractedText = extractionResponse.content[0].text.trim();
    // Remove markdown code blocks if present
    const jsonText = extractedText.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
    const extractedFacts = JSON.parse(jsonText);

    // Check if any facts were found
    const hasNewFacts = extractedFacts.name ||
                       extractedFacts.age ||
                       extractedFacts.role ||
                       (extractedFacts.goals && extractedFacts.goals.length > 0) ||
                       (extractedFacts.constraints && extractedFacts.constraints.length > 0) ||
                       (extractedFacts.skills && extractedFacts.skills.length > 0) ||
                       (extractedFacts.values && extractedFacts.values.length > 0) ||
                       (extractedFacts.personalFacts && extractedFacts.personalFacts.length > 0);

    if (hasNewFacts) {
      // Load current profile
      const currentProfile = await loadProfile();

      // Merge extracted facts
      const updatedProfile = mergeProfileFacts(currentProfile, extractedFacts);

      // Save updated profile
      await saveProfile(updatedProfile);

      console.log('✓ Profile updated with new facts:', {
        name: extractedFacts.name,
        age: extractedFacts.age,
        role: extractedFacts.role,
        goals: extractedFacts.goals?.length || 0,
        constraints: extractedFacts.constraints?.length || 0,
        skills: extractedFacts.skills?.length || 0,
        values: extractedFacts.values?.length || 0,
        personalFacts: extractedFacts.personalFacts?.length || 0
      });
    }
  } catch (error) {
    // Log but don't throw - extraction failures shouldn't break the main flow
    console.error('Profile extraction failed:', error.message);
  }
}

// Profile API endpoints
app.get('/api/profile', async (req, res) => {
  try {
    const profile = await loadProfile();
    res.json(profile);
  } catch (error) {
    console.error('Error loading profile:', error);
    res.status(500).json({
      error: 'Failed to load profile',
      details: error.message
    });
  }
});

app.post('/api/profile', async (req, res) => {
  try {
    const profile = req.body;
    await saveProfile(profile);
    res.json({ success: true });
  } catch (error) {
    console.error('Error saving profile:', error);
    res.status(500).json({
      error: 'Failed to save profile',
      details: error.message
    });
  }
});

// Generate AI-powered conversation title
app.post('/api/generate-title', async (req, res) => {
  const { userMessage, conversationContext } = req.body;

  try {
    const titlePrompt = `Generate a concise, natural title (3-6 words) for a conversation that starts with this user message:

"${userMessage}"

${conversationContext ? `\nAdditional context from conversation:\n${conversationContext}` : ''}

Requirements:
- Be specific and descriptive
- Use natural language (not literal quotes)
- Capture the essence of the decision or topic
- 3-6 words maximum
- No quotes, colons, or punctuation at the end
- Start with a capital letter

Examples of good titles:
- "Family vacation to Vegas"
- "Career transition options"
- "Buying first home"
- "Starting a side business"

Return ONLY the title, nothing else.`;

    const response = await client.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 100,
      temperature: 0.7,
      system: 'You are a title generation assistant. Generate concise, natural conversation titles.',
      messages: [{
        role: 'user',
        content: titlePrompt
      }]
    });

    const title = response.content[0].text.trim();

    res.json({ title });

  } catch (error) {
    console.error('Error generating title:', error);
    res.status(500).json({
      error: 'Failed to generate title',
      details: error.message
    });
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Outcomist backend running on http://localhost:${PORT}`);
  console.log(`📝 Using /explore prompt from: ${explorePromptPath}`);
});
