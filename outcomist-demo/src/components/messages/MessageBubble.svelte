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

<!-- Enhanced styling inspired by Manus -->
<div
  class="message"
  style="
    display: flex;
    justify-content: {role === 'user' ? 'flex-end' : 'flex-start'};
    margin-bottom: 24px;
    animation: slideIn 250ms ease-out;
  "
>
  <div class="message-content" style="
    padding: {role === 'user' ? '14px 18px' : '18px 22px'};
    border-radius: {role === 'user' ? '12px 12px 4px 12px' : '12px 12px 12px 4px'};
    background-color: {role === 'user' ? '#3B7FE8' : '#F5F7F9'};
    color: {role === 'user' ? 'white' : '#1A1D21'};
    max-width: {role === 'user' ? '75%' : '90%'};
    font-size: {role === 'user' ? '15px' : '15px'};
    line-height: 1.6;
    box-shadow: {role === 'user' ? '0 1px 2px rgba(0, 0, 0, 0.05)' : '0 1px 3px rgba(0, 0, 0, 0.05)'};
  ">
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
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  :global(.prose) {
    font-size: 15px;
    line-height: 1.6;
    color: #1A1D21;
  }

  :global(.prose p) {
    margin-bottom: 1.1em;
  }

  :global(.prose p:last-child) {
    margin-bottom: 0;
  }

  /* Enhanced bold text - more prominent like Manus */
  :global(.prose strong) {
    font-weight: 600;
    color: #0D0F11;
  }

  /* Italic text for emphasis */
  :global(.prose em) {
    font-style: italic;
    color: #2C3036;
  }

  /* Headings */
  :global(.prose h1), :global(.prose h2), :global(.prose h3) {
    font-weight: 600;
    color: #0D0F11;
    margin-top: 1.5em;
    margin-bottom: 0.75em;
    line-height: 1.3;
  }

  :global(.prose h1) {
    font-size: 1.5em;
  }

  :global(.prose h2) {
    font-size: 1.25em;
  }

  :global(.prose h3) {
    font-size: 1.1em;
  }

  /* Enhanced list styling - clearer hierarchy like Manus */
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
    line-height: 1.6;
  }

  :global(.prose li:last-child) {
    margin-bottom: 0;
  }

  :global(.prose ul li::before) {
    content: "•";
    position: absolute;
    left: 0.6em;
    color: #3B7FE8;
    font-weight: 700;
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
    color: #3B7FE8;
    font-weight: 700;
    font-size: 0.95em;
  }

  /* Strong text in lists - acts as labels like Manus */
  :global(.prose li strong) {
    display: inline-block;
    margin-bottom: 0.3em;
    color: #0D0F11;
    font-weight: 600;
  }

  /* Nested lists */
  :global(.prose li ul), :global(.prose li ol) {
    margin-top: 0.6em;
    margin-bottom: 0.6em;
  }

  /* Code blocks */
  :global(.prose code) {
    background: #EDF0F3;
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: 'Courier New', monospace;
    color: #2C3036;
  }

  /* Blockquotes */
  :global(.prose blockquote) {
    border-left: 3px solid #3B7FE8;
    padding-left: 1em;
    margin: 1.2em 0;
    color: #4A4E55;
    font-style: italic;
  }
</style>
