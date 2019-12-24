import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/fornecedores',
    name: 'Fornecedores',
    component: () => import('@/views/Fornecedores.vue')
  },
  {
    path: '/contas',
    name: 'Contas',
    component: () => import('@/views/Contas.vue')
  },
  {
    path: '/titulos',
    name: 'Títulos',
    component: () => import('@/views/Titulos.vue')
  },
  {
    path: '/pagamentos',
    name: 'Pagamentos',
    component: () => import('@/views/Pagamentos.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
