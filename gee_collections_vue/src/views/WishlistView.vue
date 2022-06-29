<template>
    <div class="wishlist">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Products</a></li>
                    <li class="breadcrumb-item active">Wishlist</li>
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
                                        <tr v-for="prod,index in wishlist" :key="index">
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
                                            <td>{{Number(wishlistItemTotal[index]).toLocaleString()}}</td>
                                            <td><button @click="removeFromWishlist(index)"><i class="fa fa-trash"></i></button></td>
                                        </tr>
                                    </tbody>
                                </table>
                                <p class="empty-wishlist" v-if="!Object.keys(wishlist).length"><span class="emoji " role="img" aria-label="">😭</span><br/><em class="empty-cart-message">Ooops,No items in wishlist</em></p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="cart-page-inner">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="cart-summary">
                                        <div class="cart-content">
                                            <h1>Wishlist Summary</h1>
                                            <p>Sub Total<span>ksh. {{Number(wishlistSubTotal).toLocaleString()}}</span></p>
                                            <p>Delivery Fee(varies)<span>ksh. {{Number(shippingCost).toLocaleString()}}</span></p>
                                            <h2>Grand Total<span>{{Number(wishlistGrandTotal).toLocaleString()}}</span></h2>
                                        </div>
                                        <div class="cart-btn">
                                            <button v-if="wishlist.length"><router-link to="/checkout" class="checkout">Proceed To Checkout</router-link></button>
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
export default {
    props:['wishlist','items','wishlistGrandTotal','wishlistItemTotal','wishlistSubTotal','shippingCost'],
    methods:{
        incrementQuantity(){
            let selectedItemQuantity = arguments[0];
            this.wishlist[selectedItemQuantity].quantity += 1;
            this.updateWishlist();
        },
        decrementQuantity(){
            let selectedItemQuantity = arguments[0];
            if(this.wishlist[selectedItemQuantity].quantity >=2){
                this.wishlist[selectedItemQuantity].quantity -= 1;
            }
            else{
                this.$store.commit('removeFromWishlist',selectedItemQuantity);
            }
            this.updateWishlist();
        },
        updateWishlist() {
            localStorage.setItem('wishlist', JSON.stringify(this.$store.state.wishlist))
        },
        removeFromWishlist(){
            let selectedItem = arguments[0];
            swal({
                title: "Are you sure?",
                text: `Do you wish to remove ${this.wishlist[selectedItem].items.name} from your wishlist?`,
                icon: "warning",
                buttons: true,
                dangerMode: true,
                })
            .then((willDelete) => {
                if (willDelete) {
                    this.$store.commit('removeFromWishlist',selectedItem);
                    swal("Poof! Item removed succesfully!", {
                    icon: "success",
                    });
                } else {
                    swal("Your item is safely in the wishlist!");
                }
            });
        },

    },
}
</script>

<style scoped>
    .empty-wishlist{
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
        color:#FF6F61;
        font-size: 20px;
        font-weight: bold;
        font-family: 'Source Code Pro', monospace;
    }
    .checkout:hover{
        color: black;
    }
    .cart-btn:hover{
        color:black !important;
    }
    .cart-btn{
        width: 600px;
    }
</style>