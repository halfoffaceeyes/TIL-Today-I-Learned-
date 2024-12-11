import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SearchView from '@/views/SearchView.vue'
import LaterView from '@/views/LaterView.vue'
import ChannelView from '@/views/ChannelView.vue'
import DetailView from '@/views/DetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'home',
      component : HomeView
    },
    {
      path : '/search',
      name : 'search',
      component : SearchView
    },  
    {
      path : '/later',
      name : 'later',
      component : LaterView
    },
    {
      path : '/channel',
      name : 'channel',
      component : ChannelView
    },
    {
      path : '/video/:videoId',
      name : 'detail',
      component : DetailView
    },
  ]
})

export default router
