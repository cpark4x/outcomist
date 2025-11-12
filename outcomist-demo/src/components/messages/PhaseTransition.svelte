<script lang="ts">
  import type { Phase } from '../../stores/conversation';

  export let fromPhase: Phase;
  export let toPhase: Phase;

  const phaseData = {
    discover: {
      label: 'Explore Options',
      icon: '🔍',
      description: 'Understanding the landscape',
    },
    review: {
      label: 'Decide Path',
      icon: '⚖️',
      description: 'Evaluating alternatives',
    },
    execute: {
      label: 'Take Action',
      icon: '🚀',
      description: 'Moving forward',
    },
  };

  $: from = phaseData[fromPhase];
  $: to = phaseData[toPhase];
</script>

<div class="phase-transition">
  <div class="transition-line"></div>

  <div class="transition-content">
    <div class="phase-from">
      <span class="phase-icon">{from.icon}</span>
      <span class="phase-label">{from.label}</span>
    </div>

    <div class="transition-arrow">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M5 12h14M12 5l7 7-7 7"/>
      </svg>
    </div>

    <div class="phase-to">
      <span class="phase-icon">{to.icon}</span>
      <div class="phase-info">
        <span class="phase-label">{to.label}</span>
        <span class="phase-description">{to.description}</span>
      </div>
    </div>
  </div>
</div>

<style>
  .phase-transition {
    position: relative;
    margin: var(--space-8) 0;
    padding: 0 var(--space-5);
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
  }

  .transition-line {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 1px;
    background: linear-gradient(
      to right,
      var(--border-default) 0%,
      var(--blue-200) 50%,
      var(--border-default) 100%
    );
  }

  .transition-content {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--space-6);
    background: var(--bg-primary);
    padding: var(--space-6);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-default);
    box-shadow: var(--shadow-sm);
    animation: fadeSlideIn var(--duration-slow) var(--ease-out);
  }

  @keyframes fadeSlideIn {
    from {
      opacity: 0;
      transform: translateY(-8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .phase-from,
  .phase-to {
    display: flex;
    align-items: center;
    gap: var(--space-3);
  }

  .phase-from {
    opacity: 0.6;
  }

  .phase-icon {
    font-size: var(--font-size-xl);
    line-height: 1;
  }

  .phase-label {
    font-size: var(--font-size-sm);
    font-weight: var(--font-weight-medium);
    color: var(--text-secondary);
  }

  .phase-to .phase-label {
    color: var(--blue-500);
    font-weight: var(--font-weight-semibold);
  }

  .phase-info {
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
  }

  .phase-description {
    font-size: var(--font-size-xs);
    color: var(--text-tertiary);
  }

  .transition-arrow {
    color: var(--blue-500);
    flex-shrink: 0;
  }

  /* Mobile responsive */
  @media (max-width: 640px) {
    .phase-transition {
      margin: var(--space-6) 0;
    }

    .transition-content {
      flex-direction: column;
      gap: var(--space-4);
      padding: var(--space-5);
    }

    .phase-from {
      opacity: 1;
    }

    .transition-arrow {
      transform: rotate(90deg);
    }
  }
</style>
