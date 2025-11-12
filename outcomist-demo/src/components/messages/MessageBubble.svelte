<script lang="ts">
  import { marked } from 'marked';
  import StreamingIndicator from './StreamingIndicator.svelte';
  import QuickReply from './QuickReply.svelte';

  export let role: 'user' | 'assistant';
  export let content: string;
  export let isStreaming: boolean = false;
  export let onQuickReply: ((option: string) => void) | undefined = undefined;

  // Configure marked to be synchronous and return HTML string
  let htmlContent = '';
  let quickReplyOptions: string[] = [];

  $: {
    if (role === 'assistant') {
      // marked.parse() is the synchronous method in v17
      htmlContent = marked.parse(content, { async: false }) as string;

      // Parse quick reply options from content
      quickReplyOptions = parseQuickReplyOptions(content);
    }
  }

  function parseQuickReplyOptions(text: string): string[] {
    const options: string[] = [];

    // Look for numbered options like "1) option text" or "1. option text"
    const numberedPattern = /^\s*\d+[\)\.]\s+([^\n]+)/gm;
    const matches = text.matchAll(numberedPattern);

    for (const match of matches) {
      const option = match[1].trim();
      // Only include if it's short enough (< 40 chars) and looks like a selectable option
      if (option.length < 40 && !option.endsWith('?')) {
        options.push(option);
      }
    }

    // Limit to 4 options max
    return options.slice(0, 4);
  }

  function handleQuickReplySelect(option: string) {
    if (onQuickReply) {
      onQuickReply(option);
    }
  }
</script>

<!-- Enhanced styling using design tokens -->
<div
  class="message"
  class:user-message={role === 'user'}
  class:assistant-message={role === 'assistant'}
>
  <div class="message-content">
    {#if role === 'assistant'}
      <div class="prose">
        {@html htmlContent}
      </div>
    {:else}
      <div style="white-space: pre-wrap;">
        {content}
      </div>
    {/if}

    {#if isStreaming}
      <StreamingIndicator />
    {/if}

    {#if role === 'assistant' && !isStreaming && quickReplyOptions.length > 0}
      <QuickReply options={quickReplyOptions} onSelect={handleQuickReplySelect} />
    {/if}
  </div>
</div>

<style>
  /* Message container styling */
  .message {
    display: flex;
    margin-bottom: var(--space-6);
    animation: slideIn var(--duration-base) var(--ease-out);
  }

  .user-message {
    justify-content: flex-end;
  }

  .assistant-message {
    justify-content: flex-start;
  }

  /* Message bubble styling */
  .message-content {
    padding: var(--space-4) var(--space-5);
    border-radius: var(--radius-lg);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    box-shadow: var(--shadow-sm);
    max-width: 85%;
  }

  .user-message .message-content {
    background-color: var(--blue-500);
    color: white;
    border-bottom-right-radius: var(--radius-sm);
    max-width: 75%;
  }

  .assistant-message .message-content {
    background-color: var(--gray-50);
    color: var(--text-primary);
    border-bottom-left-radius: var(--radius-sm);
    max-width: 90%;
  }

  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(12px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Prose styling using design tokens */
  :global(.prose) {
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    color: var(--text-primary);
  }

  :global(.prose p) {
    margin-bottom: 1.1em;
  }

  :global(.prose p:last-child) {
    margin-bottom: 0;
  }

  /* Enhanced bold text */
  :global(.prose strong) {
    font-weight: var(--font-weight-semibold);
    color: var(--gray-900);
  }

  /* Italic text for emphasis */
  :global(.prose em) {
    font-style: italic;
    color: var(--gray-700);
  }

  /* Headings using design tokens */
  :global(.prose h1), :global(.prose h2), :global(.prose h3) {
    font-weight: var(--font-weight-semibold);
    color: var(--gray-900);
    margin-top: 1.5em;
    margin-bottom: 0.75em;
    line-height: var(--line-height-tight);
  }

  :global(.prose h1) {
    font-size: var(--font-size-xl);
  }

  :global(.prose h2) {
    font-size: var(--font-size-lg);
  }

  :global(.prose h3) {
    font-size: var(--font-size-md);
  }

  /* Enhanced list styling */
  :global(.prose ul), :global(.prose ol) {
    margin-top: 1.2em;
    margin-bottom: 1.2em;
    padding-left: 0;
    list-style: none;
  }

  :global(.prose li) {
    margin-bottom: 0.9em;
    padding-left: 2em;
    position: relative;
    line-height: var(--line-height-base);
  }

  :global(.prose li:last-child) {
    margin-bottom: 0;
  }

  :global(.prose ul li::before) {
    content: "•";
    position: absolute;
    left: 0.6em;
    color: var(--blue-500);
    font-weight: var(--font-weight-bold);
    font-size: 1.15em;
  }

  :global(.prose ol) {
    counter-reset: item;
  }

  :global(.prose ol li::before) {
    content: counter(item) ".";
    counter-increment: item;
    position: absolute;
    left: 0.4em;
    color: var(--blue-500);
    font-weight: var(--font-weight-bold);
    font-size: 0.95em;
  }

  /* Strong text in lists */
  :global(.prose li strong) {
    display: inline-block;
    margin-bottom: 0.3em;
    color: var(--gray-900);
    font-weight: var(--font-weight-semibold);
  }

  /* Nested lists */
  :global(.prose li ul), :global(.prose li ol) {
    margin-top: 0.6em;
    margin-bottom: 0.6em;
  }

  /* Code blocks using design tokens */
  :global(.prose code) {
    background: var(--gray-100);
    padding: 0.15em 0.4em;
    border-radius: var(--radius-sm);
    font-size: var(--font-size-sm);
    font-family: 'Courier New', monospace;
    color: var(--gray-700);
  }

  /* Blockquotes using design tokens */
  :global(.prose blockquote) {
    border-left: 3px solid var(--blue-500);
    padding-left: 1em;
    margin: 1.2em 0;
    color: var(--gray-600);
    font-style: italic;
  }
</style>
