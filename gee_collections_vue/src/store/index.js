import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    cart:{
      cartItems:[]
    },
    wishlist:{
      wishlistItems:[]
    },
    token: '',
    isAuthenticated: false,
    loggedInUser: [],
    reloaded: false,
    productSearch: '',
    isProductSearched: false,
    searchItem: [],
    detailProducts: []
    
  },
  getters: {

  },
  mutations: {
    searchForItem(state){
      localStorage.setItem('productSearch',state.productSearch)
    },
    setSearchItem(state){
      localStorage.setItem('searchItem',JSON.stringify(state.searchItem))
    },
    setProductDetails(state){
      localStorage.setItem('detailProducts',JSON.stringify(state.detailProducts))
    },
    clearSearch(state){
      state.searchItem = []
      state.productSearch = ''
      localStorage.setItem('productSearch',state.productSearch)
      localStorage.setItem('searchItem',JSON.stringify(state.searchItem))
    },
    clearProductDetails(state){
      state.detailProducts = []
      localStorage.setItem('detailProducts',JSON.stringify(state.detailProducts))
    },
    reloadingPage(state){
      if (localStorage.getItem('reloaded')) {
        // The page was just reloaded. Clear the value from local storage
        // so that it will reload the next time this page is visited.
        localStorage.removeItem('reloaded', false);
        console.log('Value of reload in store set to false')
        } else {
            // Set a flag so that we know not to reload the page twice.
            localStorage.setItem('reloaded', true);
            console.log(state.reloaded,'Reload')
            window.location.reload();
        }
    },
    initializeStore(state){
      //Check if the cart exists in the local storage
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      //Add the cart to local storage if it doesn't exist
      }else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
      }
      //Checks if an authentication token is available in local storage
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token');
        state.isAuthenticated = true;
      }else{
        state.token = '';
        state.isAuthenticated = false;
      }

      //Check if the wishlist exists in the local storage
      if(localStorage.getItem('wishlist')){
        state.wishlist = JSON.parse(localStorage.getItem('wishlist'))
      //Add the wishlist to local storage if it doesn't exist
      }else{
        localStorage.setItem('wishlist',JSON.stringify(state.wishlist))
      }

    },
    //ADDING AN ITEM TO THE CART
    addToCart(state, cartItem){
      //Checking if the cart has an item
      if(state.cart.cartItems.length > 0){
        //Checking if an item exists in a cart
        const exist = state.cart.cartItems.filter((i) => {
          return i.items.id === cartItem.items.id;
        })
        //If the item exists, increment its quantity in the cart
        if(exist.length > 0){
          exist[0].quantity = parseInt(exist[0].quantity) + parseInt(cartItem.quantity)
        //If the item doesn't exist, push it to the cart
        }else{
          state.cart.cartItems.push(cartItem)
        }
        //Save the cart to the local storage
        localStorage.setItem('cart',JSON.stringify(state.cart));
      }
      //Adding a new item to the cart and saving it to the local storage
      else {
        state.cart.cartItems.push(cartItem)
        localStorage.setItem('cart',JSON.stringify(state.cart));
      }
    },
    //REMOVING AN ITEM FROM THE CART
    removeFromCart(state, cartItem){
        // let itemIndex = state.cart.cartItems.indexOf(cartItem)

        state.cart.cartItems.splice(cartItem,1)
        localStorage.setItem('cart',JSON.stringify(state.cart));
    },
    //ADD ITEM TO WISHLIST
    addToWishlist(state, wishlistItem){
      //Checking if the wishlist has an item
      if(state.wishlist.wishlistItems.length > 0){
        //Checking if an item exists in a wishlist
        const exist = state.wishlist.wishlistItems.filter((i) => {
          return i.items.id === wishlistItem.items.id;
        })
        //If the item exists, increment its quantity in the wishlist
        if(exist.length > 0){
          exist[0].quantity = parseInt(exist[0].quantity) + parseInt(wishlistItem.quantity)
        //If the item doesn't exist, push it to the wishlist
        }else{
          state.wishlist.wishlistItems.push(wishlistItem)
        }
        //Save the wishlist to the local storage
        localStorage.setItem('wishlist',JSON.stringify(state.wishlist));
      }
      //Adding a new item to the wishlist and saving it to the local storage
      else {
        state.wishlist.wishlistItems.push(wishlistItem)
        localStorage.setItem('wishlist',JSON.stringify(state.wishlist));
      }
    },
    //REMOVING ITEM FROM THE WISHLIST
    removeFromWishlist(state, wishlistItem){
      // let itemIndex = state.cart.cartItems.indexOf(cartItem)

      state.wishlist.wishlistItems.splice(wishlistItem,1)
      localStorage.setItem('wishlist',JSON.stringify(state.wishlist));
  },
    //SETTING AUTHENTICATION TOKEN
    setToken(state,token){
      state.token = token;
      state.isAuthenticated = true
    },
    //REMOVING AUTHENTICATION TOKEN
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    //CLEARING THE CART
    clearCart(state) {
      state.cart = { cartItems: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    }, 
    //CLEARING THE WISHLIST
    clearCart(state) {
      state.cart = { cartItems: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    setLoggedInUser(state, payload){
      state.loggedInUser = payload
    },
  },
  actions: {
    getUserDetails({commit}){
      axios.get('/api/v1/users/me/')
      .then((response)=>{
          commit('setLoggedInUser',response.data);
      })
      .catch((error)=>{
        console.log(error)
      })
    },
  },
  modules: {
  }
})
