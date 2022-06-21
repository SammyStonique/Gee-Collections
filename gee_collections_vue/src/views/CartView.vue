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
                                <p class="empty-cart" v-if="!Object.keys(cart).length"><span class="emoji " role="img" aria-label="">😭</span><br/><em class="empty-cart-message">Ooops,No items in cart</em></p>
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
                                            <p>Sub Total<span>ksh. {{Number(cartSubTotal).toLocaleString()}}</span></p>
                                            <p>Shipping Cost(varies)<span>ksh. {{Number(shippingCost).toLocaleString()}}</span></p>
                                            <h2>Grand Total<span>{{Number(cartGrandTotal).toLocaleString()}}</span></h2>
                                        </div>
                                        <div class="cart-btn">
                                            <button><router-link to="/products" class="check-btn">Update Cart</router-link></button>                      
                                            <button v-if="cart.length"><router-link to="/checkout" class="checkout">Checkout</router-link></button>
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
import Pagination from "@/components/Pagination.vue"

export default {
    data(){
        return{
            myEmoji:'\u{1F62D}',
            pageOfItems: [],
        }
    },
    props:['cart','items','cartGrandTotal','cartItemTotal','cartSubTotal','shippingCost'],
    components:{
        Pagination
    },
    computed:{
        
    },
    methods:{
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
        incrementQuantity(){
            let selectedItemQuantity = arguments[0];
            this.cart[selectedItemQuantity].quantity += 1;
            this.updateCart();
        },
        decrementQuantity(){
            let selectedItemQuantity = arguments[0];
            if(this.cart[selectedItemQuantity].quantity >=2){
                this.cart[selectedItemQuantity].quantity -= 1;
            }
            else{
                this.$store.commit('removeFromCart',selectedItemQuantity);
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
        font-size: 20px;
        font-weight: bold;
        margin: 20px;
    }
    .emoji{
        font-size: 36px;
        font-style: normal;
    }
    .checkout{
        color: white;
    }
    .checkout:hover{
        color: #FF6F61;
    }
</style>