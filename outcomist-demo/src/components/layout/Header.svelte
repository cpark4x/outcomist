<script lang="ts">
  import ProfileModal from '../profile/ProfileModal.svelte';

  export let projectTitle: string = '';

  let showProfile = false;

  function openProfile() {
    showProfile = true;
  }

  function closeProfile() {
    showProfile = false;
  }
</script>

<header
  style="
    background: white;
    border-bottom: 1px solid #E4E6E8;
    padding: 24px 24px 16px 24px;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    position: relative;
    min-height: 26.4px;
  "
>
  <!-- Logo on left -->
  <div
    style="
      position: absolute;
      left: 24px;
      top: 24px;
    "
  >
    <img
      src="/src/assets/outcomist-wordmark.png"
      alt="Outcomist"
      style="height: 26.4px; width: auto; display: block;"
    />
  </div>

  <!-- Project title centered, aligned with logo -->
  <div
    style="
      font-size: 15px;
      color: #3D4043;
      font-weight: 500;
      max-width: 400px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      line-height: 26.4px;
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
