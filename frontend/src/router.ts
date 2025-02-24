import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Services from './views/Services.vue'
import Contact from './views/Contact.vue'
import Products from './views/Products.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/services', name: 'Services', component: Services },
  { path: '/contact', name: 'Contact', component: Contact },
  { path: '/products', name: 'Products', component: Products }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
