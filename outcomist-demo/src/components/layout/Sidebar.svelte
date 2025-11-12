<script lang="ts">
  export let showLogo: boolean = false;

  // Navigation items will be added here as we build out features
  let activeItem = 'home';
</script>

<div class="sidebar">
  <!-- Logo icon (only when conversation active) -->
  {#if showLogo}
    <div class="logo-icon">
      <img
        src="/src/assets/outcomist-icon.svg"
        alt="Outcomist"
        style="width: 32px; height: 32px; object-fit: contain;"
      />
    </div>
    <div class="divider"></div>
  {/if}

  <!-- Navigation items -->
  <nav class="nav-items">
    <!-- Home/New chat -->
    <button
      class="nav-item"
      class:active={activeItem === 'home'}
      on:click={() => activeItem = 'home'}
      title="New decision"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 5v14M5 12h14"/>
      </svg>
    </button>

    <!-- Recent conversations (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'recent'}
      on:click={() => activeItem = 'recent'}
      title="Recent decisions"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    </button>

    <!-- Search (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'search'}
      on:click={() => activeItem = 'search'}
      title="Search"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/>
        <path d="m21 21-4.35-4.35"/>
      </svg>
    </button>
  </nav>

  <!-- Bottom items -->
  <div class="bottom-items">
    <!-- Settings (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'settings'}
      on:click={() => activeItem = 'settings'}
      title="Settings"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="3"/>
        <path d="M12 1v6m0 6v6M3 12h6m6 0h6"/>
      </svg>
    </button>

    <!-- Help (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'help'}
      on:click={() => activeItem = 'help'}
      title="Help"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/>
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3m.08 4h.01"/>
      </svg>
    </button>
  </div>
</div>

<style>
  .sidebar {
    width: 60px;
    background: var(--bg-primary);
    border-right: 1px solid var(--border-default);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0;
    flex-shrink: 0;
  }

  .logo-icon {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: var(--space-4);
    margin-bottom: var(--space-2);
  }

  .divider {
    width: 32px;
    height: 1px;
    background: var(--border-default);
    margin: 0 0 var(--space-4) 0;
  }

  .nav-items {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    flex: 1;
  }

  .bottom-items {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    margin-top: auto;
    padding-bottom: var(--space-4);
  }

  .nav-item {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    background: transparent;
    color: var(--gray-500);
    cursor: pointer;
    border-radius: var(--radius-md);
    transition: all var(--duration-fast) var(--ease-out);
  }

  .nav-item:hover {
    background: var(--gray-100);
    color: var(--text-primary);
  }

  .nav-item.active {
    background: var(--blue-50);
    color: var(--blue-500);
  }

  .nav-item:active {
    transform: scale(0.95);
    transition: transform var(--duration-instant) var(--ease-in);
  }
</style>
