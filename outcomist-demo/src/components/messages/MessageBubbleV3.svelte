<script lang="ts">
  import { marked } from 'marked';
  import { User, MessageSquare } from 'lucide-svelte';
  import StreamingIndicator from './StreamingIndicator.svelte';
  import { colors } from '../../design/tokens';

  export let role: 'user' | 'assistant';
  export let content: string;
  export let isStreaming: boolean = false;

  $: htmlContent = marked(content);
  $: avatarColor = role === 'user' ? colors.textPrimary : colors.accent;
</script>

<!-- Version 3: Centered Conversation - Traditional transcript style -->
<div
  class="message-bubble"
  style="
    padding: var(--spacing-lg);
    background-color: {role === 'user' ? 'var(--surface)' : 'white'};
  "
>
  <div class="flex gap-4 max-w-[680px] mx-auto px-4">
    <!-- Avatar always on left -->
    <div
      class="avatar"
      style="
        width: 40px;
        height: 40px;
        min-width: 40px;
        background-color: {avatarColor};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        color: white;
      "
    >
      {#if role === 'user'}
        <User size={20} strokeWidth={2.5} />
      {:else}
        <MessageSquare size={20} strokeWidth={2.5} />
      {/if}
    </div>

    <!-- Content -->
    <div class="flex-1" style="min-width: 0; padding-top: 2px;">
      <!-- Role label -->
      <div style="
        font-size: 13px;
        font-weight: 600;
        color: {avatarColor};
        margin-bottom: 6px;
      ">
        {role === 'user' ? 'You' : 'Outcomist'}
      </div>

      {#if role === 'assistant'}
        <div class="prose">
          {@html htmlContent}
        </div>
      {:else}
        <p style="
          color: var(--text-primary);
          line-height: 1.5;
          white-space: pre-wrap;
        ">
          {content}
        </p>
      {/if}

      {#if isStreaming}
        <StreamingIndicator />
      {/if}
    </div>
  </div>
</div>

<style>
  :global(.prose) {
    font-size: 15px;
    line-height: 1.6;
    color: var(--text-primary);
  }
  :global(.prose p) {
    margin-bottom: 1em;
  }
  :global(.prose p:last-child) {
    margin-bottom: 0;
  }
  :global(.prose strong) {
    font-weight: 600;
    color: var(--text-primary);
  }

  /* Enhanced list styling */
  :global(.prose ul), :global(.prose ol) {
    margin-top: 1em;
    margin-bottom: 1em;
    padding-left: 0;
    list-style: none;
  }

  :global(.prose li) {
    margin-bottom: 0.75em;
    padding-left: 1.75em;
    position: relative;
  }

  :global(.prose li:last-child) {
    margin-bottom: 0;
  }

  :global(.prose ul li::before) {
    content: "•";
    position: absolute;
    left: 0.5em;
    color: var(--accent);
    font-weight: 600;
    font-size: 1.1em;
  }

  :global(.prose ol) {
    counter-reset: item;
  }

  :global(.prose ol li::before) {
    content: counter(item) ".";
    counter-increment: item;
    position: absolute;
    left: 0.5em;
    color: var(--accent);
    font-weight: 600;
  }

  :global(.prose li strong) {
    display: inline-block;
    margin-bottom: 0.25em;
    color: var(--text-primary);
  }
</style>
