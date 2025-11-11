<script lang="ts">
  export let currentVersion: number = 1;
  export let onVersionChange: (version: number) => void;

  const versions = [
    { id: 1, name: 'Teams Classic', desc: 'Right/left aligned, subtle backgrounds' },
    { id: 2, name: 'ChatGPT Modern', desc: 'Colored bubbles, minimal' },
    { id: 3, name: 'Centered Transcript', desc: 'Traditional chat, centered' },
  ];
</script>

<div style="
  position: fixed;
  top: 16px;
  right: 16px;
  background: white;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  z-index: 1000;
  min-width: 240px;
">
  <div style="
    font-size: 13px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 8px;
  ">
    UI Version
  </div>

  {#each versions as version}
    <button
      on:click={() => onVersionChange(version.id)}
      style="
        display: block;
        width: 100%;
        text-align: left;
        padding: 8px 12px;
        border: 1px solid {currentVersion === version.id ? 'var(--accent)' : 'var(--border)'};
        background: {currentVersion === version.id ? 'var(--accent-bg)' : 'white'};
        border-radius: 6px;
        margin-bottom: 6px;
        cursor: pointer;
        transition: all 150ms ease;
      "
      class="version-btn"
    >
      <div style="
        font-size: 14px;
        font-weight: {currentVersion === version.id ? '600' : '500'};
        color: {currentVersion === version.id ? 'var(--accent)' : 'var(--text-primary)'};
      ">
        {version.name}
      </div>
      <div style="
        font-size: 12px;
        color: var(--text-secondary);
        margin-top: 2px;
      ">
        {version.desc}
      </div>
    </button>
  {/each}
</div>

<style>
  .version-btn:hover {
    border-color: var(--accent);
  }
</style>
