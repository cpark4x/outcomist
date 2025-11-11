<script lang="ts">
  import { onMount, onDestroy } from 'svelte';

  const thinkingStates = [
    'Analyzing your question...',
    'Exploring the decision space...',
    'Considering patterns...',
    'Forming insights...',
  ];

  let currentStateIndex = 0;
  let interval: number;

  onMount(() => {
    // Cycle through thinking states every 2 seconds
    interval = setInterval(() => {
      currentStateIndex = (currentStateIndex + 1) % thinkingStates.length;
    }, 2000);
  });

  onDestroy(() => {
    if (interval) {
      clearInterval(interval);
    }
  });
</script>

<div
  class="thinking-indicator"
  style="
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 18px 22px;
    border-radius: 12px 12px 12px 4px;
    background-color: #F5F7F9;
    max-width: 90%;
    animation: fadeIn 300ms ease-out;
  "
>
  <!-- Animated dots -->
  <div
    class="dots"
    style="
      display: flex;
      gap: 6px;
    "
  >
    {#each [0, 1, 2] as i}
      <div
        style="
          width: 8px;
          height: 8px;
          background-color: #3B7FE8;
          border-radius: 50%;
          animation: bounce 1.2s ease-in-out {i * 0.15}s infinite;
        "
      ></div>
    {/each}
  </div>

  <!-- Thinking text -->
  <div
    style="
      font-size: 14px;
      color: #64676B;
      font-style: italic;
    "
  >
    {thinkingStates[currentStateIndex]}
  </div>
</div>

<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes bounce {
    0%, 60%, 100% {
      transform: translateY(0);
    }
    30% {
      transform: translateY(-8px);
    }
  }
</style>
