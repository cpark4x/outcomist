<script lang="ts">
  import { conversation } from '../stores/conversation';
  import MessageList from '../components/messages/MessageList.svelte';
  import ChatInput from '../components/input/ChatInput.svelte';
  import WelcomeScreen from '../components/empty-states/WelcomeScreen.svelte';
  import Header from '../components/layout/Header.svelte';
  import Sidebar from '../components/layout/Sidebar.svelte';

  const API_URL = 'http://localhost:3001/api/explore';
  const TITLE_API_URL = 'http://localhost:3001/api/generate-title';

  $: messages = $conversation.messages;
  $: isProcessing = $conversation.isProcessing;
  $: projectTitle = $conversation.projectTitle;
  $: currentPhase = $conversation.currentPhase;

  // Generate AI-powered project title
  async function generateProjectTitle(userMessage: string, conversationContext?: string): Promise<string> {
    try {
      const response = await fetch(TITLE_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          userMessage,
          conversationContext
        }),
      });

      if (!response.ok) {
        throw new Error(`Title generation failed: ${response.statusText}`);
      }

      const data = await response.json();
      return data.title;
    } catch (error) {
      console.error('Error generating title:', error);
      // Fallback: simple truncation
      return userMessage.substring(0, 50) + (userMessage.length > 50 ? '...' : '');
    }
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
      // First message - generate AI title asynchronously
      generateProjectTitle(content.trim()).then(title => {
        conversation.setProjectTitle(title);
      });
    } else if (isTopicShift(content.trim())) {
      // Topic shifted - generate new title with context
      const conversationSummary = messages.slice(-2).map(m => `${m.role}: ${m.content.substring(0, 100)}`).join('\n');
      generateProjectTitle(content.trim(), conversationSummary).then(title => {
        conversation.setProjectTitle(title);
      });
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

  function handleQuickReply(option: string) {
    // When user clicks a quick reply button, submit that as their message
    handleSubmit(option);
  }
</script>

<div class="flex h-screen" style="background: var(--bg-page);">
  <!-- Left sidebar (narrow icons) -->
  <Sidebar showLogo={messages.length > 0} />

  <!-- Main content area -->
  <div class="flex flex-col flex-1">
    <!-- Header (only show when conversation started) -->
    {#if messages.length > 0}
      <Header {projectTitle} {currentPhase} showPhases={true} />
    {/if}

    <div class="flex-1 overflow-y-auto">
      {#if messages.length === 0}
        <WelcomeScreen onSubmit={handleSubmit} disabled={isProcessing} />
      {:else}
        <MessageList {messages} {isProcessing} {currentPhase} onQuickReply={handleQuickReply} />
      {/if}
    </div>

    <!-- Only show bottom input when conversation started -->
    {#if messages.length > 0}
      <div class="flex-shrink-0">
        <ChatInput
          onSubmit={handleSubmit}
          disabled={isProcessing}
          placeholder="Type your message..."
        />
      </div>
    {/if}
  </div>
</div>
