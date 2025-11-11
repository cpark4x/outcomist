<script lang="ts">
  export let options: string[] = [];
  export let onSelect: (option: string) => void;

  function handleClick(option: string) {
    onSelect(option);
  }
</script>

{#if options.length > 0}
  <div
    class="quick-replies"
    style="
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    "
  >
    {#each options as option}
      <button
        type="button"
        on:click={() => handleClick(option)}
        style="
          padding: 8px 16px;
          background: #3B7FE8;
          color: white;
          border: none;
          border-radius: 20px;
          font-size: 14px;
          font-weight: 500;
          cursor: pointer;
          transition: all 150ms ease-out;
          box-shadow: 0 1px 3px rgba(59, 127, 232, 0.15);
        "
        on:mouseenter={(e) => {
          e.currentTarget.style.background = '#2E6DC9';
          e.currentTarget.style.transform = 'translateY(-1px)';
          e.currentTarget.style.boxShadow = '0 2px 6px rgba(59, 127, 232, 0.25)';
        }}
        on:mouseleave={(e) => {
          e.currentTarget.style.background = '#3B7FE8';
          e.currentTarget.style.transform = 'translateY(0)';
          e.currentTarget.style.boxShadow = '0 1px 3px rgba(59, 127, 232, 0.15)';
        }}
      >
        {option}
      </button>
    {/each}
  </div>
{/if}
