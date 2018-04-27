<template>
  <v-app>
    <div>
      <router-view/>
    </div>
  </v-app>
</template>

<script>
  export default {
    name: 'app'
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  @font-face {
    font-family: 'modeno';
    src: url('/static/modeno.ttf');
  }

  @font-face {
    font-family: 'Inconsolata';
    src: url('/static/Inconsolata.otf');
  }

  html {
    overflow: hidden;
  }


</style>
