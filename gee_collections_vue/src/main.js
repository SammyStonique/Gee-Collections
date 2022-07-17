import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueToast from 'vue-toast-notification';
import JwPagination from 'jw-vue-pagination';
import 'vue-toast-notification/dist/theme-sugar.css';
import '@/assets/styles/style.scss';
import '@/lib/easing/easing.js';
import '@/lib/slick/slick.js';
import '@/lib/slick/slick.min.js';
import '@/js/main.js';

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// axios.defaults.baseURL = 'https://d94b-197-248-34-79.ngrok.io/'

createApp(App).use(store).use(router).use(VueAxios,axios).component('jw-pagination', JwPagination).use(VueToast,{position:'top'}).mount('#app')
