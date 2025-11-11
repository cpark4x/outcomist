<script lang="ts">
  import SendButton from './SendButton.svelte';

  export let onSubmit: (content: string) => void;
  export let disabled: boolean = false;
  export let placeholder: string = 'Type your message...';

  let value: string = '';

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (value.trim() && !disabled) {
      onSubmit(value.trim());
      value = '';
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  }
</script>

<div
  class="input-container"
  style="
    width: 100%;
    background: var(--background);
    border-top: 1px solid var(--border);
    padding: var(--spacing-lg) 0;
  "
>
  <div style="max-width: var(--max-width); margin: 0 auto; padding: 0 var(--spacing-lg);">
    <form on:submit={handleSubmit}>
      <div
        class="input-wrapper"
        style="
          display: flex;
          align-items: center;
          gap: var(--spacing-md);
          padding: var(--spacing-md) var(--spacing-lg);
          border: 1px solid var(--border);
          border-radius: 8px;
          background: var(--background);
          transition: all var(--duration-fast) var(--easing-out);
        "
      >
        <input
          type="text"
          bind:value
          on:keydown={handleKeydown}
          {disabled}
          {placeholder}
          style="
            flex: 1;
            outline: none;
            border: none;
            font-size: var(--font-size-base);
            color: var(--text-primary);
            background: transparent;
          "
        />
        <SendButton
          {disabled}
          canSubmit={value.trim().length > 0}
          on:click={handleSubmit}
        />
      </div>
    </form>
  </div>
</div>
