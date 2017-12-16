<template>
  <div class="m-card">
    <div class="m-card-title">
      {{ title }}
    </div>
    <div class="m-card-value">
      {{ value }}
    </div>
  </div>
</template>
<script>
  export default {
    props: ['title', 'value']
  }
</script>
<style scoped>
  .m-card {
    background: rgba(255, 255, 255, 0.35);
    border-radius: 3px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0);
    height: 100%;
    display: block;
    text-align: center;
  }

  .m-card:hover {
    background: rgba(255, 255, 255, 0.35);
    border-radius: 3px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 2);
    height: 100%;
    display: block;
    text-align: center;

  }
  .m-card-title {
    height: 30%;
    padding: 5px;
    font-size: 12px;
    font-family: 'Inconsolata';
  }

  .m-card-value {
    font-weight: bold;
    font-size: 15px;
    font-family: 'Inconsolata';
  }
</style>
