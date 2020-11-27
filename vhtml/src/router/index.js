import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'django',
    component: () => import('../views/userlist.vue')
  },
  {
    path: '/userinfo',
    name: 'Userinfo',
    component: () => import('../views/Userinfo.vue')
  },
  {
    path: '/vue',
    name: 'vuecli',
    component: () => import('../views/vuecli.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
