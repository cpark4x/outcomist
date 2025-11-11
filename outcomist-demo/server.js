import 'dotenv/config';
import express from 'express';
import Anthropic from '@anthropic-ai/sdk';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

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

    // Call Claude API with the /explore system prompt
    const response = await client.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 4096,
      system: EXPLORE_SYSTEM_PROMPT,
      messages: messages
    });

    // Extract the response text
    const responseText = response.content[0].text;

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

app.listen(PORT, () => {
  console.log(`🚀 Outcomist backend running on http://localhost:${PORT}`);
  console.log(`📝 Using /explore prompt from: ${explorePromptPath}`);
});
