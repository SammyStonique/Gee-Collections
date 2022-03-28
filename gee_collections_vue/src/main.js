import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import '@/assets/styles/style.scss'
import '@/lib/easing/easing.js'
import '@/lib/slick/slick.js'
import '@/lib/slick/slick.min.js'
import '@/js/main.js'


createApp(App).use(store).use(router).use(VueAxios,axios).mount('#app')
