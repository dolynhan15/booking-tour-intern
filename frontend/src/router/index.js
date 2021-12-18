import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/pages/Home.vue'
import DetailTour from '@/pages/DetailTour.vue'
import BookingTour from '@/pages/BookingTour.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }, 
  {
    path: '/detail',
    name: 'Detail',
  
    component: DetailTour
  },
  {
    path: '/booking',
    name: 'BookingTour',
  
    component: BookingTour
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
