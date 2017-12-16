// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import Router from 'vue-router'
import App from './App'
import router from './router'
Vue.use(Vuetify)
Vue.use(Router)

Vue.config.productionTip = false

/* eslint-disable no-new */
var myVue = new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

document.onkeyup = function (evt) {
  var e = evt || window.evt
  if (e && !myVue.$data.uploadAllowed) {
    if (e.keyCode === 13 || e.keyCode === 82) {
      myVue.renderInit()
    } else if (e.keyCode === 37 || e.keyCode === 80) {
      myVue.renderPrevious()
    } else if (e.keyCode === 39 || e.keyCode === 78) {
      myVue.renderNext()
    } else if (e.keyCode === 32) {
      myVue.$data.stopped = !myVue.$data.stopped
      if (!myVue.$data.stopped) {
        myVue.runThis()
      }
    }
  }
}
