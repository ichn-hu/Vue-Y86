<template>
  <div id="dropZone" @dragover.stop.prevent="handleDragOver" @drop.stop.prevent="handleFileSelect">
    <div id="dropBackground"/>
    <v-container grid-list-md text-xs-center id="welcomePanel">
      <v-layout row wrap>
        <v-flex xs6 offset-xs3>
          <v-card>
            <v-card-text>
              <h1>The Modern Y86 Simulator</h1>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import $ from 'jquery'

var uploadUrl = 'http://localhost:5000/upload'
export default {
  name: 'Welcome',
  methods: {
    handleDragOver: function (evt) {
      evt.dataTransfer.dropEffect = 'copy' // Explicitly show this is a copy.
    },
    handleFileSelect: function (evt) {
      var self = this
      var files = evt.dataTransfer.files // FileList object.
      // files is a FileList of File objects. List some properties.
      for (var i = 0, f; (f = files[i]); i++) {
        var reader = new FileReader()
        reader.onload = function (e) {
          // console.log(e.target.result)
          $.post(
            uploadUrl,
            { instrCode: e.target.result },
            function (result) {
              //    console.log(result)
              window.result = result
            },
            'json'
          ).done(function () {
            self.$router.push({
              path: '/result'
            })
          })
        }
        reader.readAsText(f)
      }
    }
  }
}
</script>
<style scoped>
#welcomePanel {
  background: rgba(255, 255, 255, 0.35);
  border-radius: 3px;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.25);
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  top: 10%;
  left: 10%;
  right: 10%;
  position: fixed;
  z-index: 2;
}

#dropZone {
    position: fixed;
    width: 100%;
    height: 100%;
    background-size: cover;
    z-index: 100;
}
a {
  position: fixed;
  top: 500px;
}
h1 {
  position: relative;
  top: 10px;
  text-align: center;
  font-size: 50px;
  font-family: 'modeno'
}
#dropBackground {
  display: block;
  height: 99%;
  width: 99%;
  z-index: -1;
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  z-index: -1.00;
  background: url('/static/bkgd3.gif') no-repeat;
  /* background: url('/static/bg2.jpeg') no-repeat; */
  background-position: center;
  background-size: cover;
  -webkit-filter: blur(3px);
  -moz-filter: blur(3px);
  -o-filter: blur(3px);
  -ms-filter: blur(3px);
  filter: blur(3px);
}



</style>
