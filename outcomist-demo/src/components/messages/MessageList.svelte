<script lang="ts">
  import { afterUpdate, tick } from 'svelte';
  import type { Message, Phase } from '../../stores/conversation';
  import MessageBubble from './MessageBubble.svelte';
  import ThinkingIndicator from './ThinkingIndicator.svelte';

  export let messages: Message[];
  export let isProcessing: boolean = false;
  export let currentPhase: Phase = 'discover';
  export let onQuickReply: ((option: string) => void) | undefined = undefined;

  let messagesEnd: HTMLDivElement;

  async function scrollToBottom() {
    await tick(); // Wait for DOM updates
    messagesEnd?.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }

  afterUpdate(() => {
    scrollToBottom();
  });
</script>

<div class="messages-container">
  {#each messages as message (message.id)}
    <MessageBubble
      role={message.role}
      content={message.content}
      isStreaming={message.isStreaming}
      onQuickReply={onQuickReply}
    />
  {/each}

  {#if isProcessing}
    <ThinkingIndicator />
  {/if}

  <div bind:this={messagesEnd}></div>
</div>

<style>
  .messages-container {
    display: flex;
    flex-direction: column;
    padding: var(--space-6) var(--space-5);
    max-width: 900px;
    margin: 0 auto;
  }
</style>
