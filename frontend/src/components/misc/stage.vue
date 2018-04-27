<template>
  <div class="stage-tile" v-bind:class="{bubble: bubble | stat === 5, stall: stall}">
    <div class="m-stage-title">
      {{ name }}
    </div>
    <div class="m-stage-content">
      <div class="m-stage-addr">
        {{ ins.addr }}
      </div>
      <div class="m-stage-code">
        {{ ins.code }}
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['name', 'ins', 'bubble', 'stall', 'operation', 'stat']
  }
</script>
<style>
  .stage-tile {
    height: 100%;
    width: 100%;
  }

  .m-stage-title {
    font-weight: bold;
    font-size: 22px;
    font-family: 'modeno';
    float: left;
    height: auto;
    width: 20%;
    text-align: center;
  }

  .m-stage-content {
    position: relative;
    float: left;
    height: auto;
    text-align: left;
    width: 80%;
  }

  .m-stage-addr {
    height: 20px;
    font-size: 12px;
    font-family: 'Inconsolata';
    height: 40%;
  }

  .m-stage-code {
    font-weight: bold;
    font-size: 12px;
    font-family: 'Inconsolata';
    height: 60%;
  }
</style>
