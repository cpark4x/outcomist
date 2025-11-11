<script lang="ts">
  import { marked } from 'marked';
  import { MessageSquare } from 'lucide-svelte';
  import StreamingIndicator from './StreamingIndicator.svelte';
  import { colors } from '../../design/tokens';

  export let role: 'user' | 'assistant';
  export let content: string;
  export let isStreaming: boolean = false;

  $: htmlContent = marked(content);
</script>

<!-- Version 2: ChatGPT Modern - User no avatar, colored bubble -->
<div
  class="message-bubble"
  style="
    padding: var(--spacing-lg) 0;
  "
>
  {#if role === 'user'}
    <!-- User message: Right-aligned bubble, no avatar -->
    <div class="flex justify-end px-6">
      <div
        style="
          max-width: 580px;
          background-color: var(--accent);
          color: white;
          padding: 12px 16px;
          border-radius: 18px;
          line-height: 1.5;
          white-space: pre-wrap;
        "
      >
        {content}
      </div>
    </div>
  {:else}
    <!-- Assistant message: Left-aligned with avatar -->
    <div class="flex gap-3 px-6 max-w-[800px]">
      <div
        class="avatar"
        style="
          width: 32px;
          height: 32px;
          min-width: 32px;
          background-color: {colors.accent};
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-shrink: 0;
          color: white;
        "
      >
        <MessageSquare size={16} strokeWidth={2.5} />
      </div>

      <div class="flex-1" style="min-width: 0; padding-top: 4px;">
        <div class="prose">
          {@html htmlContent}
        </div>

        {#if isStreaming}
          <StreamingIndicator />
        {/if}
      </div>
    </div>
  {/if}
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
