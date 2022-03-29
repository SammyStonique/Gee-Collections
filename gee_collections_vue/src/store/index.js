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
      //Add the cart to local storage if it doesn't exist
      }else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
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
    }
  },
  actions: {
  },
  modules: {
  }
})
