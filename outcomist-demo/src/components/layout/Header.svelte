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
    { id: 'discover' as Phase, label: 'Discover' },
    { id: 'review' as Phase, label: 'Review' },
    { id: 'execute' as Phase, label: 'Execute' }
  ];
</script>

<header
  style="
    position: relative;
    background: white;
    border-bottom: 1px solid #E4E6E8;
    padding: 24px;
    display: flex;
    align-items: center;
  "
>
  <!-- Left: Phases breadcrumb -->
  {#if showPhases}
    <div style="display: flex; align-items: center; gap: 8px;">
      {#each phases as phase, i}
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 13px; color: {currentPhase === phase.id ? '#3B7FE8' : '#94969A'}; font-weight: {currentPhase === phase.id ? '600' : '500'};">
            {phase.label}
          </span>
          {#if i < phases.length - 1}
            <span style="color: #E4E6E8;">›</span>
          {/if}
        </div>
      {/each}
    </div>
  {/if}

  <!-- Center: Project title (absolutely positioned for true centering) -->
  <div
    style="
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      font-size: 15px;
      color: #3D4043;
      font-weight: 500;
    "
  >
    {projectTitle || 'New Decision'}
  </div>

  <!-- Profile button on right -->
  <button
    on:click={openProfile}
    style="
      position: absolute;
      right: 24px;
      top: 24px;
      padding: 6px 16px;
      border-radius: 8px;
      border: 1px solid #E4E6E8;
      background: white;
      color: #3D4043;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      transition: all 200ms ease-out;
    "
  >
    Profile
  </button>
</header>

<ProfileModal show={showProfile} onClose={closeProfile} />
