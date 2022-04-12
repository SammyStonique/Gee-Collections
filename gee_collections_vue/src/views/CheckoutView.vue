<template>
    <div class="checkout">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                    <li class="breadcrumb-item"><router-link to="/cart">Cart</router-link></li>
                    <li class="breadcrumb-item active">Checkout</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        
        <!-- Checkout Start -->
        <div class="checkout">
            <div class="container-fluid"> 
                <form action="" @submit.prevent="placeOrder">
                    <div class="row">
                            <div class="col-lg-8">
                                <div class="checkout-inner">
                                    <div class="billing-address">
                                        <h2>Billing Address</h2>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <label>First Name</label>
                                                    <input class="form-control" type="text" placeholder="First Name" v-model="first_name">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Last Name</label>
                                                    <input class="form-control" type="text" placeholder="Last Name" v-model="last_name">
                                            </div>
                                            <div class="col-md-6">
                                                <label>E-mail</label>
                                                    <input class="form-control" type="email" placeholder="Email" v-model="email" disabled="true">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Mobile No</label>
                                                    <input class="form-control" type="text" placeholder="Mobile" v-model="phone_number">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Gender</label>
                                                    <select name="gender" class="form-control" v-model="gender">
                                                        <option value="" disabled="true">--Select your Gender--</option>
                                                        <option>Male</option>
                                                        <option>Female</option>
                                                        <option>Other</option>
                                                    </select>
                                            </div>                                    
                                            <div class="col-md-6">
                                                <label>Address</label>
                                                    <input class="form-control" type="text" placeholder="Address" v-model="address">
                                            </div>
                                            <div class="col-md-6">
                                                <label>City</label>
                                                    <select name="city" class="form-control" v-model="city">
                                                        <option value="" disabled="true">--Select your City--</option>
                                                        <option>Nairobi</option>
                                                        <option>Kisumu</option>
                                                        <option>Mombasa</option>
                                                        <option>Nakuru</option>
                                                    </select>
                                            </div>
                                            <div class="col-md-6">
                                                <label>County</label>
                                                    <select name="county" class="form-control" v-model="county">
                                                        <option value="" disabled="true">--Select your County--</option>
                                                        <option>Siaya</option>
                                                        <option>Kisumu</option>
                                                        <option>Nairobi</option>
                                                        <option>Mombasa</option>
                                                    </select>
                                            </div>                                
                                            <div class="col-md-12">
                                                <div class="custom-control custom-checkbox">
                                                    <input type="checkbox" class="custom-control-input" id="newaccount">
                                                    <label class="custom-control-label" for="newaccount">Create an account</label>
                                                </div>
                                            </div>
                                            <div class="col-md-12">
                                                <div class="custom-control custom-checkbox">
                                                    <input type="checkbox" class="custom-control-input" id="shipto">
                                                    <label class="custom-control-label" for="shipto">Ship to different address</label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="shipping-address">
                                        <h2>Shipping Address</h2>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <label>First Name</label>
                                                <input class="form-control" type="text" placeholder="First Name">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Last Name</label>
                                                <input class="form-control" type="text" placeholder="Last Name">
                                            </div>
                                            <div class="col-md-6">
                                                <label>E-mail</label>
                                                <input class="form-control" type="text" placeholder="E-mail">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Mobile No</label>
                                                <input class="form-control" type="text" placeholder="Mobile No">
                                            </div>
                                            <div class="col-md-12">
                                                <label>Address</label>
                                                <input class="form-control" type="text" placeholder="Address">
                                            </div>
                                            <div class="col-md-6">
                                                <label>Country</label>
                                                <select class="custom-select">
                                                    <option selected>Kenya</option>
                                                    <option>Tanzania</option>
                                                    <option>Uganda</option>
                                                    <option>Rwanda</option>
                                                </select>
                                            </div>
                                            <div class="col-md-6">
                                                <label>City</label>
                                                <input class="form-control" type="text" placeholder="City">
                                            </div>
                                            <div class="col-md-6">
                                                <label>County</label>
                                                <input class="form-control" type="text" placeholder="County">
                                            </div>
                                            <div class="col-md-6">
                                                <label>ZIP Code</label>
                                                <input class="form-control" type="text" placeholder="ZIP Code">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4">
                                <div class="checkout-inner">
                                    <div class="checkout-summary">
                                        <h1>Cart Total</h1>
                                        <p class="sub-total">Sub Total<span>ksh. {{Number(cartSubTotal).toLocaleString()}}</span></p>
                                        <p class="ship-cost">Shipping Cost<span>ksh. {{Number(shippingCost).toLocaleString()}}</span></p>
                                        <h2>Grand Total<span>{{Number(cartGrandTotal).toLocaleString()}}</span></h2>
                                    </div>

                                    <div class="checkout-payment">
                                        <div class="payment-methods">
                                            <h1>Payment Methods</h1>
                                            <div class="payment-method">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="custom-control-input" id="payment-1" name="payment">
                                                    <label class="custom-control-label" for="payment-1">Paypal</label>
                                                </div>
                                                <div class="payment-content" id="payment-1-show">
                                                    <p>
                                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt orci ac eros volutpat maximus lacinia quis diam.
                                                    </p>
                                                </div>
                                            </div>
                                            <div class="payment-method">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="custom-control-input" id="payment-2" name="payment">
                                                    <label class="custom-control-label" for="payment-2">Payoneer</label>
                                                </div>
                                                <div class="payment-content" id="payment-2-show">
                                                    <p>
                                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt orci ac eros volutpat maximus lacinia quis diam.
                                                    </p>
                                                </div>
                                            </div>
                                            <div class="payment-method">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="custom-control-input" id="payment-3" name="payment">
                                                    <label class="custom-control-label" for="payment-3">Check Payment</label>
                                                </div>
                                                <div class="payment-content" id="payment-3-show">
                                                    <p>
                                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt orci ac eros volutpat maximus lacinia quis diam.
                                                    </p>
                                                </div>
                                            </div>
                                            <div class="payment-method">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="custom-control-input" id="payment-4" name="payment">
                                                    <label class="custom-control-label" for="payment-4">Direct Bank Transfer</label>
                                                </div>
                                                <div class="payment-content" id="payment-4-show">
                                                    <p>
                                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt orci ac eros volutpat maximus lacinia quis diam.
                                                    </p>
                                                </div>
                                            </div>
                                            <div class="payment-method">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="custom-control-input" id="payment-5" name="payment">
                                                    <label class="custom-control-label" for="payment-5">Cash on Delivery</label>
                                                </div>
                                                <div class="payment-content" id="payment-5-show">
                                                    <p>
                                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt orci ac eros volutpat maximus lacinia quis diam.
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="checkout-btn">
                                            <button>Place Order</button>
                                        </div>
                                    </div>
                                </div>
                            </div>   
                    </div>
                </form>
            </div>
        </div>
        <!-- Checkout End -->
    </div>
</template>

<script>
export default {
    props:['cartGrandTotal','cartItemTotal','cartSubTotal','shippingCost'],
    data(){
        return{
            cart:{
                cartItems:[]
            },
            id:'',
            first_name:'',
            last_name: '',
            email: '',
            phone_number: '',
            address: '',
            county: '',
            city: '',
            gender: '',
            errors:[]
        }
    },
    methods:{
        getProfileDetails(){
            this.axios.get('/api/v1/users/me/')
            .then((response)=>{
                this.phone_number = response.data.phone_number;
                this.email = response.data.email;
                this.id = response.data.id;
                this.first_name = response.data.first_name
                this.last_name = response.data.last_name
                this.gender = response.data.gender
                this.city = response.data.city
                this.county = response.data.county
                this.address = response.data.address
            })
            .catch((error)=>{

            })
        },
        placeOrder(){
            const items = []
            for (let i = 0; i < this.cart.cartItems.length; i++) {
            const item = this.cart.cartItems[i]
            const obj = {
                product: item.items.id,
                quantity: item.quantity,
                price: item.items.price * item.quantity
            }
            items.push(obj)
            
            } 
            //Daraja Authorisation API
            // let headers = new Headers();
            // headers.append("Authorization", "Bearer d0tXZk1Gb24wcTYwRmpQb3BBQVZseUZqU2xiNHJBM006OXZxNEhYWHBkNzZJUFRtaQ");

            this.axios.get("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")
            .then((response) =>{
                console.log(response.data)
            })
            .then((result)=>{
                console.log(result)
            })
            .catch((error)=>{
                console.log(error)
            });           
            // let formData={
            //     first_name:this.first_name,
            //     last_name: this.last_name,
            //     address: this.address,
            //     county: this.county,
            //     city: this.city,   
            //     phone_number: this.phone_number,
            //     email: this.email,
            //     items: items,
            //     order_total: this.cartSubTotal,
            // }
            // console.log(formData)
            // this.axios.post('/api/v1/checkout/', formData)
            // .then((response)=>{
            //     console.log(response.data)
            //     this.$store.commit('clearCart')
            //     this.$toast.success('Order succesfully placed')
            //     this.$router.push('/')
            // })
            // .catch((error)=>{
            //     console.log(error)
            // })
        }
    },
    beforeMount() {
        this.getProfileDetails();
        this.cart = this.$store.state.cart;
    },
}

</script>

<style scoped>
    input{
        font-weight: 300;
        color: black;
    }
    select{
        font-weight: 300;
        color: black;
    }
</style>