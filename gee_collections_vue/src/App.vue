<template>
        
        <!-- Top bar Start -->
        <div class="top-bar">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-6">
                        <i class="fa fa-envelope"></i>
                        otisamueloti@gmail.com
                    </div>
                    <div class="col-sm-6">
                        <i class="fa fa-phone-alt"></i>
                        +254-717-423-651
                    </div>
                </div>
            </div>
        </div>
        <!-- Top bar End -->
        
        <!-- Nav Bar Start -->
        <div class="nav">
            <div class="container-fluid">
                <nav class="navbar navbar-expand-md bg-dark navbar-dark">
                    <router-link to="#" class="navbar-brand">MENU</router-link>
                    <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse justify-content-between" id="navbarCollapse">
                        <div class="navbar-nav mr-auto">
                            <router-link to="/" class="nav-item nav-link">Home</router-link>
                            <router-link to="/products" class="nav-item nav-link">Products</router-link>
                            <router-link to="product-detail" class="nav-item nav-link" v-if="productDetails.length">Product Detail</router-link>
                            <router-link to="/cart" class="nav-item nav-link">Cart</router-link>
                            <router-link to="/checkout" class="nav-item nav-link" v-if="this.cart.cartItems.length">Checkout</router-link>
                            <router-link to="/my-account" class="nav-item nav-link">My Account</router-link>
                            <div class="nav-item dropdown">
                                <router-link to="#" class="nav-link dropdown-toggle" data-toggle="dropdown">More Pages</router-link>
                                <div class="dropdown-menu">
                                    <router-link to="/wishlist" class="dropdown-item">Wishlist</router-link>
                                    <router-link to="/contact" class="dropdown-item">Contact Us</router-link>
                                </div>
                            </div>
                        </div>
                        <div class="navbar-nav ml-auto" v-if="!isAuthenticated">
                            <div class="nav-item dropdown">
                                <router-link to="#" class="nav-link dropdown-toggle" data-toggle="dropdown">User Account</router-link>
                                <div class="dropdown-menu">
                                    <router-link to="/login" class="dropdown-item">Login</router-link>
                                    <router-link to="/register" class="dropdown-item">Register</router-link>
                                    <!-- <router-link to="/logout" class="dropdown-item">Log Out</router-link> -->
                                </div>
                            </div>
                        </div>
                        <div class="navbar-nav ml-auto" v-if="isAuthenticated">
                            <div class="nav-item dropdown">
                                <router-link to="#" class="nav-link dropdown-toggle" data-toggle="dropdown">WELCOME,{{userDetails.email}}</router-link>
                                <div class="dropdown-menu">
                                    <router-link to="/logout" class="dropdown-item">Logout</router-link>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
        <!-- Nav Bar End -->      
        
        <!-- Bottom Bar Start -->
        <div class="bottom-bar">
            <div class="container-fluid">
                <div class="row align-items-center">
                    <div class="col-md-3">
                        <div class="logo">
                            <router-link to="/">
                                <img src="@/assets/img/new-logo.png" alt="Logo" class="new-logo">
                            </router-link>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="search">
                            <input type="text" placeholder="Search">
                            <button><i class="fa fa-search"></i></button>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="user">
                            <router-link to="/wishlist" class="btn wishlist">
                                <i class="fa fa-heart"></i>
                                <span>({{totalWishlistQuantity}})</span>
                            </router-link>
                            <router-link to="/cart" class="btn cart">
                                <i class="fa fa-shopping-cart"></i>
                                <span>({{totalQuantity}})</span>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Bottom Bar End -->
        <router-view
        :getProducts="getProducts"
        :items="items"
        :productDetails="productDetails"
        :wishlist="wishlist.wishlistItems"
        :cart="cart.cartItems"
        :addToCart="addToCart"
        :addToWishlist="addToWishlist"
        :totalQuantity="totalQuantity"
        :totalWishlistQuantity="totalWishlistQuantity"
        :cartSubTotal="cartSubTotal"
        :wishlistSubTotal="wishlistSubTotal"
        :cartItemTotal="cartItemTotal"
        :wishlistItemTotal="wishlistItemTotal"
        :cartGrandTotal="cartGrandTotal"
        :cartTotalUSD="cartTotalUSD"
        :wishlistGrandTotal="wishlistGrandTotal"
        :shippingCost="shippingCost"
        :token="token"
        :isAuthenticated="isAuthenticated"
        :getUserDetails="getUserDetails"
        :getProductDetails="getProductDetails"
        :userDetails="userDetails"
        />

        <!-- Footer Start -->
        <div class="footer">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-3 col-md-6">
                        <div class="footer-widget">
                            <h2>Get in Touch</h2>
                            <div class="contact-info">
                                <p><i class="fa fa-map-marker"></i>Opposite Jamia Mosque, Siaya</p>
                                <p><a href="http://www.gmail.com" target="blank"><i class="fa fa-envelope"></i>otisamueloti@gmail.com</a></p>
                                <p><i class="fa fa-phone"></i>+254-717-423-651</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-lg-3 col-md-6">
                        <div class="footer-widget">
                            <h2>Follow Us</h2>
                            <div class="contact-info">
                                <div class="social">
                                    <a href="http://www.twitter.com" target="blank" ><i class="fab fa-twitter"></i></a>
                                    <a href="http://www.facebook.com" target="blank"><i class="fab fa-facebook-f"></i></a>
                                    <a href="http://www.linkedin.com" target="blank"><i class="fab fa-linkedin-in"></i></a>
                                    <a href="http://www.instagram.com" target="blank"><i class="fab fa-instagram"></i></a>
                                    <a href="http://www.youtube.com" target="blank"><i class="fab fa-youtube"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6">
                        <div class="footer-widget">
                            <h2>Company Info</h2>
                            <ul>
                                <li><router-link to="#">About Us</router-link></li>
                                <li><router-link to="#">Privacy Policy</router-link></li>
                                <li><router-link to="#">Terms & Conditions</router-link></li>
                            </ul>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6">
                        <div class="footer-widget">
                            <h2>Purchase Info</h2>
                            <ul>
                                <li><router-link to="#">Payment Policy</router-link></li>
                                <li><router-link to="#">Shipping Policy</router-link></li>
                                <li><router-link to="#">Return Policy</router-link></li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="row payment align-items-center">
                    <div class="col-md-6">
                        <div class="payment-method">
                            <h2>We Accept:</h2>
                            <img src="@/assets/img/payment-method.png" style="width: inherit;" alt="Payment Method"/>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="payment-security">
                            <h2>Secured By:</h2>
                            <img src="@/assets/img/godaddy.svg" style="width: inherit;" alt="Payment Security" />
                            <img src="@/assets/img/norton.svg" style="width: inherit;" alt="Payment Security" />
                            <img src="@/assets/img/ssl.svg" style="width: inherit;" alt="Payment Security" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->
        
        <!-- Footer Bottom Start -->
        <div class="footer-bottom">
            <div class="container">
                <div class="row">
                    <div class="col-md-6 copyright">
                        <p>Copyright &copy; <router-link to="#" style="color: white !important;">SammyB</router-link>. All Rights Reserved</p>
                    </div>

                    <div class="col-md-6 template-by">
                        <p>Template By <router-link to="#" style="color: white !important;">SammyB</router-link></p>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer Bottom End -->       
        
        <!-- Back to Top -->
        <router-link to="#" @click="scrollToTop()" class="back-to-top"><i class="fa fa-chevron-up"></i></router-link>

</template>

<script>
import axios from 'axios'
import ProductCard from './components/ProductCard.vue'
export default {
    components:{
        ProductCard
    },
    data(){
        return{
            items:[],
            cart:{
                cartItems:[]
            },
            wishlist:{
                wishlistItems:[]
            },
            quantity: 1,
            shippingCost: 200,
            token: '',
            isAuthenticated: false,
            productDetails : [],
        }
    },
    beforeMount() {
        this.$store.commit('initializeStore');
        this.$store.commit('reloadingPage');
        
        const token = this.$store.state.token
        if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
        } else {
        axios.defaults.headers.common['Authorization'] = ""
        }
        this.cart = this.$store.state.cart;
        this.wishlist = this.$store.state.wishlist;
        this.isAuthenticated = this.$store.state.isAuthenticated;
    },
    mounted(){
        this.getUserDetails()
        console.log('login Auth is:',this.isAuthenticated)
    },
    computed: {
        totalQuantity() {
            let itemQuantity = 0

            for(let i = 0; i<this.cart.cartItems.length; i++ ){
                itemQuantity += this.cart.cartItems[i].quantity
            }
            return itemQuantity
        },
        totalWishlistQuantity() {
            let itemQuantity = 0

            for(let i = 0; i<this.wishlist.wishlistItems.length; i++ ){
                itemQuantity += this.wishlist.wishlistItems[i].quantity
            }
            return itemQuantity
        },
        cartItemTotal(){
            let itemTotal = [];
            for(let i = 0; i<this.cart.cartItems.length; i++){
                let lineTotal = (this.cart.cartItems[i].quantity * this.cart.cartItems[i].items.price).toFixed(2)
                itemTotal.push(lineTotal);
            }
            return itemTotal
        },
        wishlistItemTotal(){
            let itemTotal = [];
            for(let i = 0; i<this.wishlist.wishlistItems.length; i++){
                let lineTotal = (this.wishlist.wishlistItems[i].quantity * this.wishlist.wishlistItems[i].items.price).toFixed(2)
                itemTotal.push(lineTotal);
            }
            return itemTotal
        },
        cartSubTotal(){
            let itemTotal = [];
            let cartTotal = 0
            for(let i = 0; i<this.cart.cartItems.length; i++){
                let lineTotal = (this.cart.cartItems[i].quantity * this.cart.cartItems[i].items.price).toFixed(2)
                itemTotal.push(parseFloat(lineTotal));
                cartTotal = itemTotal.reduce(function(a,b){
                    return (a+ b);
                })
            }
            return cartTotal
        },
        wishlistSubTotal(){
            let itemTotal = [];
            let wishlistTotal = 0
            for(let i = 0; i<this.wishlist.wishlistItems.length; i++){
                let lineTotal = (this.wishlist.wishlistItems[i].quantity * this.wishlist.wishlistItems[i].items.price).toFixed(2)
                itemTotal.push(parseFloat(lineTotal));
                wishlistTotal = itemTotal.reduce(function(a,b){
                    return (a+ b);
                })
            }
            return wishlistTotal
        },
        cartGrandTotal(){
            return parseFloat(this.cartSubTotal) + this.shippingCost
        },
        cartTotalUSD(){
            return (parseFloat(this.cartGrandTotal) / 110).toFixed(2)
        },
        wishlistGrandTotal(){
            return parseFloat(this.wishlistSubTotal) + this.shippingCost
        },
        userDetails(){
            return this.$store.state.loggedInUser;
        }
        
    },
    methods:{
        getProducts(){                  
            this.axios.get('/api/v1/latest-products/')
            .then((response)=>{
                this.items = response.data;
                for(let i = 0; i<this.items.length; i++){
                    this.prodID = this.items[i].id
                }
                return this.prodID
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        addToCart(){
            //Getting the index of the items in the cart
            let selectedItem = arguments[0];
            if(isNaN(this.quantity) || this.quantity<1){
                this.quantity = 1;
            }
            
            const cartItem={
                items : this.items[selectedItem],
                quantity : this.quantity
            }
            this.$store.commit('addToCart',cartItem);
            this.$toast.success(`${this.items[selectedItem].name} added to cart`);
            
        },
        addToWishlist(){
            //Getting the index of the items in the wishlist
            let selectedItem = arguments[0];
            if(isNaN(this.quantity) || this.quantity<1){
                this.quantity = 1;
            }
            
            const wishlistItem={
                items : this.items[selectedItem],
                quantity : this.quantity
            }
            this.$store.commit('addToWishlist',wishlistItem);
            this.$toast.success(`${this.items[selectedItem].name} added to wishlist`);
            
        },
        getUserDetails(){
            this.$store.dispatch('getUserDetails')
            .then((response)=>{

            })
            .catch((error)=>{
                console.error(error)
            })
        },  
        getProductDetails(productID){
            this.axios.get(`/api/v1/latest-products/${productID}/`)
            .then((response)=>{
                this.productDetails = response.data;
                this.$router.push("/product-detail");
                this.scrollToTop()
            })
            .catch((error)=>{
                console.log(error)
            })
        },     
        scrollToTop(){
            window.scrollTo({top:0,behavior:"smooth"})
        }
    },
}
</script>


<style lang="scss">
    .router-link-exact-active{
        color: black !important;
    }
    .dropdown-toggle{
        color: white !important;
    }
    .new-logo{
        width: 212px;
        height: 53px;
    }
</style>