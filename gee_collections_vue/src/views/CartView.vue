<template>
    <div class="cart">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Products</a></li>
                    <li class="breadcrumb-item active">Cart</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        <!-- Cart Start -->
        <div class="cart-page">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="cart-page-inner">
                            <div class="table-responsive">
                                <table class="table table-bordered">
                                    <thead class="thead-dark">
                                        <tr>
                                            <th>Product</th>
                                            <th>Price</th>
                                            <th>Quantity</th>
                                            <th>Total</th>
                                            <th>Remove</th>
                                        </tr>
                                    </thead>
                                    <tbody class="align-middle">
                                        <tr v-for="prod,index in cart" :key="index">
                                            <td>
                                                <div class="img">
                                                    <a href="#"><img :src="`${prod.items.image}`" alt="Image"></a>
                                                    <p>{{prod.items.name}}</p>
                                                </div>
                                            </td>
                                            <td>{{Number(prod.items.price).toLocaleString()}}</td>
                                            <td>
                                                <div class="qty">
                                                    <button class="btn-minus" @click="decrementQuantity(index)"><i class="fa fa-minus"></i></button>
                                                    <input type="text" :value="`${prod.quantity}`">
                                                    <button class="btn-plus" @click="incrementQuantity(index)"><i class="fa fa-plus"></i></button>
                                                </div>
                                            </td>
                                            <td>{{Number(cartItemTotal[index]).toLocaleString()}}</td>
                                            <td><button @click="removeFromCart(index)"><i class="fa fa-trash"></i></button></td>
                                        </tr>
                                    </tbody>
                                </table>
                                <p class="empty-cart" v-if="!Object.keys(cart).length"><em style="font-size: 24px;">{{myEmoji}}</em><em>Ooops,No items in cart</em></p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="cart-page-inner">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="coupon">
                                        <input type="text" placeholder="Coupon Code">
                                        <button>Apply Code</button>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="cart-summary">
                                        <div class="cart-content">
                                            <h1>Cart Summary</h1>
                                            <p>Sub Total<span>$99</span></p>
                                            <p>Shipping Cost<span>$1</span></p>
                                            <h2>Grand Total<span>$100</span></h2>
                                        </div>
                                        <div class="cart-btn">
                                            <button>Update Cart</button>
                                            <button>Checkout</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Cart End -->
    </div>
</template>

<script>
import swal from 'sweetalert';
export default {
    data(){
        return{
            myEmoji:'\u{1F62D}',
        }
    },
    props:['cart','items'],
    computed:{
        cartItemTotal(){
            let itemTotal = [];
            for(let i = 0; i<this.cart.length; i++){
                let lineTotal = (this.cart[i].quantity * this.cart[i].items.price).toFixed(2)
                itemTotal.push(lineTotal);
            }
            return itemTotal
        }
        
    },
    methods:{
        incrementQuantity(){
            let selectedItemQuantity = arguments[0];
            this.cart[selectedItemQuantity].quantity += 1;
            this.updateCart();
        },
        decrementQuantity(){
            let selectedItemQuantity = arguments[0];
            if(this.cart[selectedItemQuantity].quantity >=2){
                this.cart[selectedItemQuantity].quantity -= 1;
                console.log('Item quantity reduced')
            }
            else{
                this.$store.commit('removeFromCart',selectedItemQuantity);
                console.log('item removed from cart')
            }
            this.updateCart();
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(){
            let selectedItem = arguments[0];
            swal({
                title: "Are you sure?",
                text: `Do you wish to remove ${this.cart[selectedItem].items.name} from your cart?`,
                icon: "warning",
                buttons: true,
                dangerMode: true,
                })
            .then((willDelete) => {
                if (willDelete) {
                    this.$store.commit('removeFromCart',selectedItem);
                    swal("Poof! Item removed succesfully!", {
                    icon: "success",
                    });
                } else {
                    swal("Your item is safely in the cart!");
                }
            });
        },

    },
    mounted() {
        
    },
    
}
</script>

<style scoped>
    .empty-cart{
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        margin: 20px;
    }
</style>