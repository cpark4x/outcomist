<script lang="ts">
  import { conversation } from '../stores/conversation';
  import MessageList from '../components/messages/MessageList.svelte';
  import ChatInput from '../components/input/ChatInput.svelte';
  import WelcomeScreen from '../components/empty-states/WelcomeScreen.svelte';
  import Header from '../components/layout/Header.svelte';

  const API_URL = 'http://localhost:3001/api/explore';

  $: messages = $conversation.messages;
  $: isProcessing = $conversation.isProcessing;
  $: projectTitle = $conversation.projectTitle;

  // Helper function to generate project title from message content
  function generateProjectTitle(content: string): string {
    // Take first 50 chars, capitalize first letter, remove "i want to" type phrases
    let title = content
      .toLowerCase()
      .replace(/^(i want to|i need to|help me|should i|can i|how do i|what about|how about|now|okay|what if)\s+/i, '')
      .trim();

    // Capitalize first letter
    title = title.charAt(0).toUpperCase() + title.slice(1);

    // Truncate if too long
    if (title.length > 50) {
      title = title.substring(0, 47) + '...';
    }

    return title;
  }

  // Helper to detect if message indicates topic shift
  function isTopicShift(content: string): boolean {
    const shiftIndicators = [
      /^(actually|wait|instead|what about|how about|different question|new topic|switching to|let's talk about|forget that)/i,
      /^(now|okay|alright),?\s+(what about|how about|i want to|should i|can i)/i
    ];
    return shiftIndicators.some(pattern => pattern.test(content.trim()));
  }

  async function handleSubmit(content: string) {
    if (!content.trim() || isProcessing) return;

    // Generate or update project title
    if (messages.length === 0) {
      // First message - always set title
      conversation.setProjectTitle(generateProjectTitle(content.trim()));
    } else if (isTopicShift(content.trim())) {
      // Topic shifted - update title
      conversation.setProjectTitle(generateProjectTitle(content.trim()));
    }

    // Add user message
    conversation.addMessage({
      role: 'user',
      content: content.trim(),
    });

    conversation.setProcessing(true);

    try {
      // Get conversation history
      const conversationHistory = messages.map(msg => ({
        role: msg.role,
        content: msg.content,
      }));

      // Call real /explore CLI via backend
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: content.trim(),
          conversationHistory,
        }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      const data = await response.json();

      // Add assistant response
      conversation.addMessage({
        role: 'assistant',
        content: data.response,
      });
    } catch (error) {
      console.error('Error calling API:', error);
      conversation.addMessage({
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please ensure the backend server is running (npm run server) and try again.',
      });
    } finally {
      conversation.setProcessing(false);
    }
  }
</script>

<div class="flex flex-col h-screen" style="background: #FAFBFC;">
  <!-- Header (only show when conversation started) -->
  {#if messages.length > 0}
    <Header {projectTitle} />
  {/if}

  <div class="flex-1 overflow-y-auto">
    {#if messages.length === 0}
      <WelcomeScreen />
    {:else}
      <MessageList {messages} />
    {/if}
  </div>

  <div class="flex-shrink-0">
    <ChatInput
      onSubmit={handleSubmit}
      disabled={isProcessing}
      placeholder="Type your message..."
    />
  </div>
</div>
