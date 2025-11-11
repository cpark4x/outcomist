<div
  class="streaming-indicator"
  style="
    display: inline-block;
    width: 8px;
    height: 16px;
    background-color: var(--accent);
    margin-left: 2px;
    animation: pulse-once 600ms ease-in-out infinite;
  "
></div>

<style>
  @keyframes pulse-once {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }
</style>
