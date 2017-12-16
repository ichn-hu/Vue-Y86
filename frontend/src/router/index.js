import Router from 'vue-router'
const routerOptions = [
  { path: '/', component: 'Welcome' },
  { path: '/result', component: 'Result' },
  { path: '/about', component: 'About' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

export default new Router({
  routes,
  mode: 'history'
})
