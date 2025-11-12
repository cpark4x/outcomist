<script lang="ts">
  import ProfileModal from '../profile/ProfileModal.svelte';
  import type { Phase } from '../../stores/conversation';

  export let projectTitle: string = '';
  export let currentPhase: Phase = 'discover';
  export let showPhases: boolean = false;

  let showProfile = false;

  function openProfile() {
    showProfile = true;
  }

  function closeProfile() {
    showProfile = false;
  }

  const phases = [
    { id: 'discover' as Phase, label: 'Explore' },
    { id: 'review' as Phase, label: 'Review' },
    { id: 'execute' as Phase, label: 'Build' }
  ];
</script>

<header class="header">
  <!-- Left: Phases breadcrumb -->
  {#if showPhases}
    <div class="phases-breadcrumb">
      {#each phases as phase, i}
        <div class="phase-item">
          <div class="phase-content">
            <span
              class="phase-label"
              class:active={currentPhase === phase.id}
            >
              {phase.label}
            </span>
            <div class="phase-indicator">
              <div
                class="indicator-dot"
                class:active={currentPhase === phase.id}
              ></div>
            </div>
          </div>
          {#if i < phases.length - 1}
            <span class="phase-separator">›</span>
          {/if}
        </div>
      {/each}
    </div>
  {/if}

  <!-- Center: Project title -->
  <div class="project-title">
    {projectTitle || 'New Decision'}
  </div>

  <!-- Profile button on right -->
  <button class="profile-button" on:click={openProfile}>
    Profile
  </button>
</header>

<ProfileModal show={showProfile} onClose={closeProfile} />

<style>
  .header {
    position: relative;
    background: var(--bg-primary);
    border-bottom: 1px solid var(--border-default);
    padding: var(--space-6);
    display: flex;
    align-items: center;
  }

  .phases-breadcrumb {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }

  .phase-item {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }

  .phase-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-1);
  }

  .phase-label {
    font-size: var(--font-size-sm);
    color: var(--text-tertiary);
    font-weight: var(--font-weight-medium);
    transition: color var(--duration-fast) var(--ease-out);
  }

  .phase-label.active {
    color: var(--blue-500);
    font-weight: var(--font-weight-semibold);
  }

  .phase-indicator {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .indicator-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--gray-300);
    transition: background var(--duration-fast) var(--ease-out);
  }

  .indicator-dot.active {
    background: var(--blue-500);
  }

  .phase-separator {
    color: var(--border-default);
  }

  .project-title {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    font-size: var(--font-size-base);
    color: var(--text-secondary);
    font-weight: var(--font-weight-medium);
  }

  .profile-button {
    position: absolute;
    right: var(--space-6);
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-md);
    border: 1px solid var(--border-default);
    background: var(--bg-primary);
    color: var(--text-secondary);
    font-size: var(--font-size-sm);
    font-weight: var(--font-weight-medium);
    cursor: pointer;
    transition: all var(--duration-fast) var(--ease-out);
  }

  .profile-button:hover {
    background: var(--gray-50);
    border-color: var(--border-emphasis);
  }

  .profile-button:active {
    transform: scale(0.98);
  }
</style>
