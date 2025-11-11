<script lang="ts">
  export let projectTitle: string = '';
</script>

<header
  style="
    background: white;
    border-bottom: 1px solid #E4E6E8;
    padding: 16px 24px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  "
>
  <!-- Logo on left -->
  <div
    style="
      position: absolute;
      left: 24px;
      top: 50%;
      transform: translateY(-50%);
    "
  >
    <img
      src="/src/assets/outcomist-logo-web.svg"
      alt="Outcomist"
      style="height: 24px; width: auto; display: block;"
    />
  </div>

  <!-- Project title centered -->
  <div
    style="
      font-size: 15px;
      color: #3D4043;
      font-weight: 500;
      max-width: 400px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    "
  >
    {projectTitle || 'New Decision'}
  </div>
</header>
