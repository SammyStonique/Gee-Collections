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
                                                    <input type="checkbox" class="custom-control-input" id="shipto" @click="showShippingDetails">
                                                    <label class="custom-control-label" for="shipto">Ship to different address</label>
                                                    <div class="shipping-address" v-if="checked" >
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
                                    <h1>Payment Methods</h1>
                                        <button type="button" class="lipanampesa" @click="showLipaNaMpesa">Lipa Na Mpesa</button>
                                        <div v-if="lipaNaMpesa">
                                            <p>To proceed to Lipa Na Mpesa, please enter the phone number you would like to make the payment with.</p>
                                            <label for="">Phone Number:</label>
                                            <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX" v-model="payment_number">
                                            <div class="col-md-12 notification is-danger" v-if="errors.length">
                                                <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                            </div>
                                            <button type="button" class="procPayBtn" @click="payViaMpesa">Proceed to Pay</button>
                                            <p v-if="paymentConfirm">An mpesa prompt has been sent to the number entered above,enter your mpesa PIN then proceed to payment confirmation</p>
                                            <button type="button" class="procPayBtn" @click="getMpesaPayments" v-if="paymentConfirm">Confirm Payment</button>
                                        </div>

                                         <!-- MODAL component for confirming payment -->
                                         <Modal
                                        v-show="isModalVisible"
                                        @close="closeModal"
                                        >
                                        <template v-slot:header>
                                            M-Pesa Payment Confirmation
                                        </template>

                                        <template v-slot:body>
                                        <div>
                                        <p>Please confirm the details of your payments to succesfully place your order</p>
                                        <label for="">Phone Number:</label>
                                        <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX">
                                        <label for="">Reference Number:</label>
                                        <input type="text" class="form-control" placeholder="e.g QRYU0U***P1" v-model="mpesaRef">
                                        <button type="button" class="procPayBtn" @click="confirmPayment">Confirm Payment</button>                                        
                                        </div>
                                        </template>

                                        <template v-slot:footer>
                                            Thank you for doing business with us.
                                        </template>

                                        </Modal>
                                        <div id="paypal-button-container"></div>
                                        <div class="checkout-btn" >
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
import Modal from "@/components/Modal.vue"
export default {
    props:['cartGrandTotal','cartItemTotal','cartSubTotal','shippingCost','cartTotalUSD'],
    el:'#selector',
    components:{
        Modal
    },
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
            errors:[],
            lipaNaMpesa: false,
            paymentConfirm: false,
            checked: false,
            errors:[],
            payment_number: '',
            transaction_id:'',
            isModalVisible: false,
            mpesaRefs: [],
            mpesaRef : '',
            is_paid : false,
            payment_ref: ''
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
        registerCallbackUrl(){
            this.axios.get('/api/v1/c2b/register')
            .then((response)=>{
                console.log(response.data)
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        payViaMpesa(){
            this.errors = []
            if(this.payment_number === ''){
                this.errors.push('Please enter phone number');
                this.$toast.error('Invalid phone number', {
                    duration: 3000
                })
            }
            if(!this.errors.length){
                this.axios.post('/api/v1/online/lipa/')
                .then((response)=>{
                    console.log(response.data)
                    this.paymentConfirm = true;
                })
                .catch((error)=>{
                    console.log(error)
                })
                .finally(()=>{
                    
                })
            }
        },
        getMpesaPayments(){
            this.mpesaRefs = []
            this.axios.get('api/v1/mpesa-payments/')
            .then((response)=>{
                // console.log(response.data[0].transaction_id)
                for(let i=0 ; i<response.data.length ; i++){
                    let trans_id = response.data[i].transaction_id
                    this.mpesaRefs.push(trans_id)
                    
                }
                console.log(this.mpesaRefs)
                this.isModalVisible = true;
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        confirmPayment(){
            if(this.mpesaRefs.includes(this.mpesaRef)){
               this.is_paid = true;
               this.payment_ref = this.mpesaRef;
               this.$toast.success('Payment Confirmation Succesful', {
                    duration: 3000
                }) 
                this.placeOrder();
            }
            else{
                this.$toast.error('Invalid Reference Number', {
                    duration: 3000
                })
            }
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
            let formData={
                first_name:this.first_name,
                last_name: this.last_name,
                address: this.address,
                county: this.county,
                city: this.city,   
                phone_number: this.phone_number,
                email: this.email,
                items: items,
                order_total: this.cartSubTotal,
                payment_reference: this.payment_ref,
                paid : this.is_paid
            }
            console.log(formData)
            this.axios.post('/api/v1/checkout/', formData)
            .then((response)=>{
                console.log(response.data)
                this.$store.commit('clearCart')
                this.$toast.success('Order succesfully placed')
                this.$router.push('/')
                this.$store.commit('reloadingPage')
                this.$router.push('/')
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        showLipaNaMpesa(){
            this.lipaNaMpesa = !this.lipaNaMpesa
        },
        showShippingDetails(){
            this.checked = !this.checked
            console.log(this.checked)
        },
        closeModal() {
            this.isModalVisible = false;
        },        
        mountPaypalButton(){

        }
    },
    beforeMount() {
        this.getProfileDetails();
        this.cart = this.$store.state.cart;
    },
    mounted(){
        this.registerCallbackUrl()
        paypal.Buttons({
            //Styling the paypal button
            style: {
                color: 'blue',
                shape: 'pill',
                label: 'pay',
                height: 40
            },
            // Sets up the transaction when a payment button is clicked
            createOrder: (data, actions) => {
            return actions.order.create({
                purchase_units: [{
                amount: {
                    // value: this.cartTotalUSD // Can also reference a variable or function
                    value: 0.01
                }
                }]
            });
            },
            // Finalize the transaction after payer approval
            onApprove: (data, actions) => {   
                const my_action = actions.order.capture().then(function(orderData) {
                    // Successful capture! For dev/demo purposes:
                    console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                    this.transaction_id = orderData.purchase_units[0].payments.captures[0].id
                    console.log('the transaction_id is:', this.transaction_id)
                    
                    const transaction = orderData.purchase_units[0].payments.captures[0];
                    alert(`Transaction ${transaction.status}: ${transaction.id}\n\nSee console for all available details`);
                    
                    
                    // this.placeOrder();
                    // When ready to go live, remove the alert and show a success message within this page. For example:
                    // const element = document.getElementById('paypal-button-container');
                    // element.innerHTML = '<h3>Thank you for your payment!</h3>';
                    // Or go to another URL:  actions.redirect('thank_you.html');
                });
                return my_action;
            }
        }).render('#paypal-button-container');
    }
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
    .lipanampesa{
        width: 100%;
        height: 40px;
        padding: 2px 10px;
        font-family: 'Source Code Pro', monospace;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        color: #000000;
        background: #228B22;
        border: none;
        transition: all .3s;
        margin-bottom: 20px;
        border-radius: 20px;
    }
    .lipanampesa:hover{
        background-color: black;
        color: green;
    }
    .procPayBtn{
        margin: 20px;
        color:#228B22;
        background-color: black;
        border: none;
        border-radius: 4px;
        transition: all .3s;
        font-weight: 700;
        font-size: 18px;
    }
    .procPayBtn:hover{
        color: white;
        background-color: green;
    }
</style>