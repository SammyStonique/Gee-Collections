import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import ProductAdd from '../views/ProductAdd.vue'
import ProductDetail from '../views/ProductDetail.vue'
import CartView from '../views/CartView.vue'
import CheckoutView from '../views/CheckoutView.vue'
import AccountView from '../views/AccountView.vue'
import LoginView from '../views/LoginView.vue'
import WishlistView from '../views/WishlistView.vue'
import ContactView from '../views/ContactView.vue'
import RegisterView from '../views/RegisterView.vue'
import LogoutView from '../views/LogoutView.vue'
import SearchView from '../views/SearchView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta:{
      isIdle: true,
    }
  },
  {
    path: '/products',
    name: 'products',
    component: ProductView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/add-product',
    name: 'add-product',
    component: ProductAdd
  },
  {
    path: '/product-detail',
    name: 'product-detail',
    component: ProductDetail
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView,
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutView,
    meta:{
      emptyCart: true,
      requireLogin: true
    }    
  },
  {
    path: '/my-account',
    name: 'my-account',
    component: AccountView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta:{
      alreadyAuthenticated : true,
    }
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/wishlist',
    name: 'wishlist',
    component: WishlistView
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.emptyCart) && !store.state.cart.cartItems.length) {
    next({ name: 'cart', query: { to: to.path } });
  } else {
    next()
  }
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.alreadyAuthenticated) && store.state.isAuthenticated) {
    next({ name: 'home', query: { to: to.path } });
  } else {
    next()
  }
})

// VUE IDLE
// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.isIdle) && store.state.idleVue.isIdle) {
//     next({ name: 'login', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router
