import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/pages/Home.vue'
import DetailTour from '@/pages/DetailTour.vue'
import BookingTour from '@/pages/BookingTour.vue'
import Login from "@/pages/Login/Login";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
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
