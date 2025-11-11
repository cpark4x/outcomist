<script lang="ts">
  import { Send } from 'lucide-svelte';

  export let disabled: boolean = false;
  export let canSubmit: boolean = false;
</script>

<button
  type="submit"
  disabled={disabled || !canSubmit}
  style="
    padding: var(--spacing-sm);
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all var(--duration-fast) var(--easing-out);
    opacity: {disabled || !canSubmit ? 0.3 : 1};
  "
  class:hover={!disabled && canSubmit}
>
  <Send size={20} strokeWidth={2} />
</button>

<style>
  button.hover:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
  }
  button.hover:active {
    transform: translateY(0);
  }
</style>
