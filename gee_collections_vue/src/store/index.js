import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      cartItems:[]
    },
    token: '',
    isAuthenticated: false
  },
  getters: {

  },
  mutations: {
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

    },
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
    removeFromCart(state, cartItem){
        // let itemIndex = state.cart.cartItems.indexOf(cartItem)

        state.cart.cartItems.splice(cartItem,1)
        localStorage.setItem('cart',JSON.stringify(state.cart));
    },
    setToken(state,token){
      state.token = token;
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
