<script lang="ts">
  import { afterUpdate, tick } from 'svelte';
  import type { Message } from '../../stores/conversation';
  import MessageBubble from './MessageBubble.svelte';

  export let messages: Message[];

  let messagesEnd: HTMLDivElement;

  async function scrollToBottom() {
    await tick(); // Wait for DOM updates
    messagesEnd?.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }

  afterUpdate(() => {
    scrollToBottom();
  });
</script>

<div
  class="messages-container"
  style="
    display: flex;
    flex-direction: column;
    padding: 24px 20px;
    max-width: 900px;
    margin: 0 auto;
  "
>
  {#each messages as message (message.id)}
    <MessageBubble
      role={message.role}
      content={message.content}
      isStreaming={message.isStreaming}
    />
  {/each}
  <div bind:this={messagesEnd}></div>
</div>
