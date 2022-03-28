import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      cartItems:[]
    }
  },
  getters: {

  },
  mutations: {
    initializeStore(state){
      //Check if the cart exists in the local storage
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
        // console.log(state.cart.cartItems[0])
      //Add the cart to local storage if it doesn't exist
      }else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
      }
    },
    addToCart(state, cartItem){
      if(state.cart.cartItems.length > 0){
        console.log("Hello, this worked!")
        const exist = state.cart.cartItems.filter((i) => {
          
          return i.items.id === cartItem.items.id;
        })
        if(exist.length > 0){
          exist[0].quantity = parseInt(exist[0].quantity) + parseInt(cartItem.quantity)
        }else{
          state.cart.cartItems.push(cartItem)
        }

        localStorage.setItem('cart',JSON.stringify(state.cart));
      }
      else {
        console.log("This caused item to be added!")
        state.cart.cartItems.push(cartItem)
        localStorage.setItem('cart',JSON.stringify(state.cart));
      }
    }
  },
  actions: {
  },
  modules: {
  }
})
