<template>
    <div class="my-account">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                    <li class="breadcrumb-item active">My Account</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        
        <!-- My Account Start -->
        <div class="my-account">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-3">
                        <div class="nav flex-column nav-pills" role="tablist" aria-orientation="vertical">
                            <a class="nav-link active" id="dashboard-nav" data-toggle="pill" href="#dashboard-tab" role="tab"><i class="fa fa-tachometer-alt"></i>Dashboard</a>
                            <a class="nav-link" id="orders-nav" data-toggle="pill" href="#orders-tab" role="tab"><i class="fa fa-shopping-bag"></i>Orders</a>
                            <a class="nav-link" id="payment-nav" data-toggle="pill" href="#payment-tab" role="tab"><i class="fa fa-credit-card"></i>Payment Method</a>
                            <a class="nav-link" id="address-nav" data-toggle="pill" href="#address-tab" role="tab"><i class="fa fa-map-marker-alt"></i>Address</a>
                            <a class="nav-link" id="account-nav" data-toggle="pill" href="#account-tab" role="tab"><i class="fa fa-user"></i>Account Details</a>
                            <router-link to="/logout" class="nav-link"><i class="fa fa-sign-out-alt"></i>Logout</router-link>
                        </div>
                    </div>
                    <div class="col-md-9">
                        <div class="tab-content">
                            <div class="tab-pane fade show active" id="dashboard-tab" role="tabpanel" aria-labelledby="dashboard-nav">
                                <h4>Dashboard</h4>
                                <p>
                                Hello {{this.first_name}}, we're very excited to have you on board. Gee Collections appreciates your contribution towards 
                                assisting us grow us a brand. We could not make it this far without you, always feel free to leave a suggestion so that we can 
                                provide you with quality services. Thank you.
                                </p> 
                                <DoughnutChart/>
                            </div>
                            <div class="tab-pane fade" id="orders-tab" role="tabpanel" aria-labelledby="orders-nav">
                                <div class="table-responsive">
                                    <table class="table table-bordered">
                                        <thead class="thead-dark">
                                            <tr>
                                                <th>No</th>
                                                <th>#ID</th>
                                                <th>Date</th>
                                                <th>Order Total</th>
                                                <th>Status</th>
                                                <th>Payment Ref</th>
                                                <th>Action</th>
                                                <!-- <th></th> -->
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="order,index in pageOfItems" :key="index">
                                                <td>{{index + 1}}</td>
                                                <td>{{order.id.substring(0,7)}}</td>
                                                <td>{{order.created_at.substring(0,10)}}</td>
                                                <td>ksh {{Number(order.order_total).toLocaleString()}}</td>
                                                <td v-if="order.paid" style="color:green;">Paid</td>
                                                <td v-else style="color:red;">Not Paid</td>
                                                <td v-if="order.paid">{{order.payment_reference}}</td>
                                                <td v-else>N/A</td>
                                                <td v-if="order.paid"><button class="btn" @click="showModal(order.id)">View Order</button></td>
                                                <td v-else><button class="btn" @click="showPaymentModal(order.id)">Make Payment</button></td>
                                                <!-- <td><button class="btn" @click="printOrder(order.id)">Print</button></td> -->
                                            </tr>
                                        </tbody>
                                    </table>

                                    <p class="empty-order-list" v-if="!Object.keys(myOrders).length"><span class="emoji " role="img" aria-label="">😭</span><br/><em class="empty-cart-message">Ooops,You haven't placed any order yet</em></p>

                                    <!-- PAGINATION -->
                                    <div class="row">
                                        <Pagination
                                            :items="myOrders"
                                            @changePage="onChangePage"
                                            :pageSize=5
                                        />
                                    </div>
                                    <!-- pagination end -->
                                </div>
                            </div>
                            <!-- MODAL component for viewing order details -->
                            <Modal
                            v-show="isModalVisible"
                            @close="closeModal"
                            > 
                            <template v-slot:header>
                                My Order Details
                            </template>

                            <template v-slot:body>
                            <div class="myorders-page">
                                <div class="table-responsive">
                                    <table class="table table-bordered">
                                        <thead class="thead-dark">
                                            <tr>
                                                <th>Product</th>
                                                <th>Price</th>
                                                <th>Quantity</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody class="align-middle">
                                            <tr v-for="ordDet,index in myOrderDetails.items" :key="index">
                                                <td>
                                                    <div class="img">
                                                        <a href="#"><img :src="`${ordDet.product.image}`" alt="Image"></a>                                                     
                                                        <p>{{ordDet.product.name}}</p>
                                                    </div>
                                                </td>
                                                <td>ksh. {{Number(ordDet.product.price).toLocaleString()}}</td>
                                                <td>{{ordDet.quantity}}</td>
                                                <td>ksh. {{Number(orderItemTotal[index]).toLocaleString()}}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            </template>

                            <template v-slot:footer>
                                Thank you for doing business with us.
                            </template>
                            </Modal>

                            <!-- MODAL component for making payment -->
                            <Modal
                            v-show="paymentModalVisible"
                            @close="closeModal"
                            > 
                            <template v-slot:header>
                                Payment Methods
                            </template>

                            <template v-slot:body>
                                <div>
                                    <button type="button" class="lipanampesa" @click="showLipaNaMpesa">Lipa Na Mpesa</button>
                                    <div v-if="lipaNaMpesa">
                                    <p>To proceed to Lipa Na Mpesa, please enter the phone number you would like to make the payment with.</p>
                                    <label for="">Phone Number:</label>
                                    <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX" v-model="payment_number" :style="{borderColor: pStyle,borderWidth: bWidth+'px'}">
                                    <span v-if="watcherMsg.payment_number" :style="{color: pStyle, fontSize:10 + 'px'}">{{watcherMsg.payment_number}}</span>
                                    <div class="col-md-12 notification is-danger" v-if="errors.length">
                                        <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                    </div>
                                    <button type="button" class="procPayBtn" @click="payViaMpesa">Proceed to Pay</button>
                                    <p v-if="paymentConfirm">An mpesa prompt has been sent to the number entered above,enter your mpesa PIN then proceed to payment confirmation</p>
                                    <button type="button" class="procPayBtn" @click="getMpesaPayments" v-if="paymentConfirm">Confirm Payment</button>
                                    </div>
                                </div>
                                <!-- MODAL component for confirming payment -->
                                <Modal
                                v-show="isPayModalVisible"
                                @close="closeModal"
                                >
                                <template v-slot:header>
                                    M-Pesa Payment Confirmation
                                </template>

                                <template v-slot:body>
                                <div>
                                <p>Please confirm the details of your payments to succesfully place your order</p>
                                <label for="">Phone Number:</label>
                                <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX" v-model="payment_number2" :style="{borderColor: p2Style,borderWidth: bWidth+'px'}">
                                <span v-if="watcherMsg.payment_number2" :style="{color: p2Style, fontSize:10 + 'px'}">{{watcherMsg.payment_number2}}</span>
                                <label for="">Reference Number:</label>
                                <input type="text" class="form-control" placeholder="e.g QRYU0U***P1" v-model="mpesaRef" :style="{borderColor: rfStyle,borderWidth: bWidth+'px'}">
                                <span v-if="watcherMsg.mpesaRef" :style="{color: rfStyle, fontSize:10 + 'px'}">{{watcherMsg.mpesaRef}}</span>
                                <button type="button" class="procPayBtn" @click="confirmPayment">Confirm Payment</button>                                        
                                </div>
                                </template>

                                <template v-slot:footer>
                                    Thank you for doing business with us.
                                </template>

                                </Modal>
                                <div id="paypal-button-container"></div>
                            </template>

                            <template v-slot:footer>
                                Thank you for doing business with us.
                            </template>
                            </Modal>
                            <div class="tab-pane fade" id="payment-tab" role="tabpanel" aria-labelledby="payment-nav">
                                <h4>Payment Method</h4>
                                <div class="row payment-row">
                                    <div class="col-md-12">
                                        <h6 style="font-weight:700;">Select from our popular payment options below</h6>
                                    </div> 
                                    <div class="col-md-3 payment-card">
                                        <h6 style="font-weight:700;">Bank Payment</h6>
                                        <img src="@/assets/img/bank-icon.jpeg" alt="Bank Icon" class="bank-icon">
                                        <p>Make payments easily using your debit or credit card</p>
                                        <button class="btn btn-payment-option">Select Option</button>
                                    </div>
                                    <div class="col-md-3 payment-card">
                                        <h6 style="font-weight:700;">Lipa Na M-pesa</h6>
                                        <img src="@/assets/img/mpesa.jpeg" alt="M-Pesa"  class="mpesa-icon">
                                        <p>Make payments easily and efficiently using your M-pesa account</p>
                                        <button class="btn btn-payment-option">Select Option</button>
                                    </div>
                                    <div class="col-md-3 payment-card">
                                        <h6 style="font-weight:700;">PayPal</h6>
                                        <img src="@/assets/img/paypal-icon.png" alt="PayPal" class="paypal-icon">
                                        <p>Make payments easily and efficiently using your PayPal account</p>
                                        <button class="btn btn-payment-option">Select Option</button>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="address-tab" role="tabpanel" aria-labelledby="address-nav">
                                <h4>Address</h4>
                                <div class="row">
                                    <div class="col-md-6">
                                        <h5>Payment Address</h5>
                                        <p>123 Payment Street, Los Angeles, CA</p>
                                        <p>Mobile: 012-345-6789</p>
                                        <button class="btn">Edit Address</button>
                                    </div>
                                    <div class="col-md-6">
                                        <h5>Shipping Address</h5>
                                        <p>123 Shipping Street, Los Angeles, CA</p>
                                        <p>Mobile: 012-345-6789</p>
                                        <button class="btn" @click="showShippingAddress()">Edit Address</button>
                                    </div>
                                </div>
                                <br><br>
                                <div class="shipping-address" v-if="shippingAddress">
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
                                        <div class="col-md-12">
                                            <button class="btn">Save Changes</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="account-tab" role="tabpanel" aria-labelledby="account-nav">
                                <h4>Account Details</h4>
                                <form action="" @submit.prevent="postProfileData">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="First Name" v-model="first_name" :style="{borderColor: fnStyle,borderWidth: bWidth+'px'}">
                                            <span v-if="watcherMsg.first_name" :style="{color: fnStyle, fontSize:10 + 'px'}">{{watcherMsg.first_name}}</span>
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="Last Name" v-model="last_name" :style="{borderColor: lnStyle,borderWidth: bWidth+'px'}">
                                            <span v-if="watcherMsg.last_name" :style="{color: lnStyle, fontSize:10 + 'px'}">{{watcherMsg.last_name}}</span>
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="email" placeholder="Email" v-model="email" disabled="true">
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="Mobile" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px'}">
                                            <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                                        </div>
                                        <div class="col-md-6">
                                            <select name="gender" class="form-control" v-model="gender" :style="{borderColor: gStyle,borderWidth: bWidth+'px'}">
                                                <option value="" disabled="true">--Select your Gender--</option>
                                                <option value="Male">Male</option>
                                                <option value="Female">Female</option>
                                                <option value="Other">Other</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="date" placeholder="Date of Birth" v-model="birthdate" :style="{borderColor: dStyle,borderWidth: bWidth+'px'}">
                                        </div>
                                        <div class="col-md-6">
                                            <select name="city" class="form-control" v-model="city" :style="{borderColor: cStyle,borderWidth: bWidth+'px'}">
                                                <option value="" disabled="true">--Select your City--</option>
                                                <option value="Nairobi">Nairobi</option>
                                                <option value="Kisumu">Kisumu</option>
                                                <option value="Mombasa">Mombasa</option>
                                                <option value="Nakuru">Nakuru</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6">
                                            <select name="county" class="form-control" v-model="county" :style="{borderColor: ccStyle,borderWidth: bWidth+'px'}">
                                                <option value="" disabled="true">--Select your County--</option>
                                                <option value="Siaya">Siaya</option>
                                                <option value="Kisumu">Kisumu</option>
                                                <option value="Nairobi">Nairobi</option>
                                                <option value="Mombasa">Mombasa</option>
                                            </select>
                                        </div>
                                        <div class="col-md-12">
                                            <input class="form-control" type="text" placeholder="Address" v-model="address" :style="{borderColor: aStyle,borderWidth: bWidth+'px'}">
                                            <span v-if="watcherMsg.address" :style="{color: aStyle, fontSize:10 + 'px'}">{{watcherMsg.address}}</span>
                                        </div>
                                        <div class="col-md-12 notification is-danger" v-if="errors.length">
                                            <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                        </div>
                                        <div class="col-md-12">
                                            <button class="btn">Update Account</button>
                                            <br><br>
                                        </div>
                                    </div>
                                </form>
                                <h4>Password change</h4>
                            <form action="" @submit.prevent="changePassword">
                                <div class="row">
                                    <div class="col-md-12">
                                        <input class="form-control" type="password" placeholder="Current Password" v-model="currentPassword">
                                    </div>
                                    <div class="col-md-6">
                                        <input class="form-control" :type="passType ? 'text' : 'password'" placeholder="New Password" v-model="newPassword">
                                        <button type="button" class="show-password" @click="showPassword()">
                                        <i class="fa fa-eye-slash" v-if="!passType"></i>
                                        <i class="fa fa-eye" v-else></i>
                                        </button>
                                        <span v-if="watcherMsg.newPassword" style="color:red; font-size: 10px;">{{watcherMsg.newPassword}}</span>
                                    </div>
                                    <div class="col-md-6">
                                        <input class="form-control" :type="pass2Type ? 'text' : 'password'" placeholder="Confirm Password" v-model="newPassword2">
                                        <button type="button" class="show-password" @click="showPassword2()">
                                        <i class="fa fa-eye-slash" v-if="!pass2Type"></i>
                                        <i class="fa fa-eye" v-else></i>
                                        </button>
                                        <span v-if="watcherMsg.newPassword2" style="color:red; font-size: 10px;">{{watcherMsg.newPassword2}}</span>
                                    </div>
                                    <div class="col-md-12">
                                        <button class="btn">Save Changes</button>
                                    </div>
                                </div>
                            </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- My Account End -->
    </div>
</template>

<script>
import Modal from "@/components/Modal.vue"
import Pagination from "@/components/Pagination.vue"
import DoughnutChart from "@/components/DoughnutChart.vue"


export default {
    props: ["getUserDetails", "userDetails"],
    components:{
    Modal,
    Pagination,
    DoughnutChart,
},
    data() {
        return {
            id: "",
            first_name: "",
            last_name: "",
            email: "",
            phone_number: "",
            birthdate: "",
            address: "",
            county: "",
            city: "",
            gender: "",
            errors: [],
            myOrders: [],
            myOrderDetails:[],
            isModalVisible: false,
            isPayModalVisible: false,
            paymentModalVisible: false,
            lipaNaMpesa: false,
            currentPage: 1,
            totalItems: 0,
            itemsPerPage: 2,
            totalPages: 0,
            start: 1,
            limit: 2,
            watcherMsg: [],
            fnStyle : null,
            lnStyle : null,
            nStyle : null,
            gStyle : null,
            bWidth : null,
            dStyle: null,
            cStyle : null,
            ccStyle : null,
            aStyle : null,
            pStyle: null,
            p2Style: null,
            rfStyle : null,
            payment_number: '',
            payment_number2: '',
            mpesaRefs : [],
            mpesaRef : '',
            paymentConfirm : false,
            myOrderID: '',
            pageOfItems: [],
            shippingAddress: false,
            currentPassword: '',
            newPassword: '',
            newPassword2: '',
            showPass: false,
            passType: false,
            showPass2: false,
            pass2Type : false
        };
    },
    watch:{
        first_name(value){
            this.first_name = value;
            this.validateFirstName(value);
        },
        last_name(value){
            this.last_name = value;
            this.validateLastName(value);            
        },
        phone_number(value){
            this.phone_number = value;
            this.validatePhoneNumber(value)
        },
        gender(value){
            this.gender = value;
            this.validateGender(value)
        },    
        birthdate(value){
            this.birthdate = value;
            this.validateBirthdate(value)
        },
        city(value){
            this.city = value;
            this.validateCity(value)
        },
        county(value){
            this.county = value;
            this.validateCounty(value)
        },  
        address(value){
            this.address = value;
            this.validateAddress(value)
        },  
        payment_number(value){
            this.payment_number = value;
            this.validatePaymentNumber(value)
        },
         payment_number2(value){
            this.payment_number2 = value;
            this.confirmPaymentNumber(value)
        },
        mpesaRef(value){
            this.mpesaRef = value;
            this.validatePaymentRef(value)
        },
        newPassword2(value){
            this.newPassword2 = value;
            this.validatePassword2(value)
        },
         newPassword(value){
            this.newPassword = value;
            this.validateNewPassword(value)
        },                     
    },
    computed:{
        orderItemTotal(){
            let itemTotal = [];
            for(let i = 0; i<this.myOrderDetails.items.length; i++){
                let lineTotal = (this.myOrderDetails.items[i].quantity * this.myOrderDetails.items[i].product.price).toFixed(2)
                itemTotal.push(lineTotal);
            }
            return itemTotal
        },
    },
    methods: {
        validateFirstName(value){
            if(value.length == 0){
                this.watcherMsg['first_name'] = ''
                this.fnStyle = ''
                this.bWidth = 1
            }
            else{
                if(value.length >0 && value.length < 3){
                this.watcherMsg['first_name'] = 'Name is too short'
                this.fnStyle = 'red'
                this.bWidth = 2
                }
                else{
                    if(/\d/.test(value)){
                        this.watcherMsg['first_name'] = 'Name should not contain a number'
                        this.fnStyle = 'red'
                        this.bWidth = 2
                    }               
                    else{
                        this.watcherMsg['first_name'] = ''
                        this.fnStyle = 'green'
                        this.bWidth = 2
                    }
                }
            }    
        },
        validateLastName(value){
            if(value.length == 0){
                this.watcherMsg['last_name'] = ''
                this.lnStyle = ''
                this.bWidth = 1
            }
            else{
                if(value.length >0 && value.length < 3){
                this.watcherMsg['last_name'] = 'Name is too short'
                this.lnStyle = 'red'
                this.bWidth = 2
                }
                else{
                    if(/\d/.test(value)){
                        this.watcherMsg['last_name'] = 'Name should not contain a number'
                        this.lnStyle = 'red'
                        this.bWidth = 2
                    }                  
                    else{
                        this.watcherMsg['last_name'] = ''
                        this.lnStyle = 'green'
                        this.bWidth = 2
                    }
                }
            }    
        },
        validatePhoneNumber(value){
            if(value == ''){
                this.nStyle = '';
                this.watcherMsg['phone_number'] = ''                        
            }
            else{
                if ((/^(?:254|\+254|0)?((?:(?:7(?:(?:[01249][0-9])|(?:5[789])|(?:6[89])))|(?:1(?:[1][0-5])))[0-9]{6})$/.test(value))|| (/^(?:254|\+254|0)?((?:(?:7(?:(?:3[0-9])|(?:5[0-6])|(8[5-9])))|(?:1(?:[0][0-2])))[0-9]{6})$/.test(value))){
                    this.nStyle = 'green';
                    this.watcherMsg['phone_number'] = ''
                    this.bWidth = 2
                }
                else{
                    this.nStyle = 'red';
                    this.watcherMsg['phone_number'] = 'Invalid Phone Number'
                    this.bWidth = 2
                }
            }
        },
        validateGender(value){
            if(value != ''){
                this.gStyle = 'green';
                this.bWidth = 2
            }
        }, 
        validateBirthdate(value){
            if(value != ''){
                this.bStyle = 'green';
                this.bWidth = 2
            }
        },
        validateCity(value){
            if(value != ''){
                this.cStyle = 'green';
                this.bWidth = 2
            }
        },
        validateCounty(value){
            if(value != ''){
                this.ccStyle = 'green';
                this.bWidth = 2
            }
        },  
        validateAddress(value){
            if(value.length == 0){
                this.aStyle = '';
                this.watcherMsg['address'] = ''
            }
            else{
                if(value.length > 0 && value.length < 3){
                    this.watcherMsg['address'] = 'Address is too short'
                    this.aStyle = 'red';
                    this.bWidth = 2                    
                }
                else{
                    if(value != '' && value.length > 3){
                        this.aStyle = 'green';
                        this.bWidth = 2;
                        this.watcherMsg['address'] = ''
                    }
                }
            }
        },  
        validatePaymentNumber(value){
            if(value == ''){
                    this.watcherMsg['payment_number'] = '';
                    this.pStyle = '';
                    this.bWidth = 1
            }
            else{
                if(/^(?:254)?((?:(?:7(?:(?:[01249][0-9])|(?:5[789])|(?:6[89])))|(?:1(?:[1][0-5])))[0-9]{6})$/.test(value)){
                    this.watcherMsg['payment_number'] = '';
                    this.pStyle = 'green';
                    this.bWidth = 2
                }else{
                    this.watcherMsg['payment_number'] = 'Invalid Phone Number';
                    this.pStyle = 'red';
                    this.bWidth = 2
                    }
            }
        }, 
        confirmPaymentNumber(value){
            if(value == ''){
                this.watcherMsg['payment_number2'] = ''
                this.p2Style = ''
                this.bWidth = 1
            }
            else{
                if(value == this.payment_number){
                    this.watcherMsg['payment_number2'] = ''
                    this.p2Style = 'green'
                    this.bWidth = 2
                }
                else{
                    this.watcherMsg['payment_number2'] = 'Invalid Phone Number'
                    this.p2Style = 'red'
                    this.bWidth = 2
                }
            }
        },
        validatePaymentRef(value){
            if(value.length == 0){
                this.watcherMsg['mpesaRef'] = '';
                this.rfStyle = '';
                this.bWidth = 1;
            }
            else{
                if(value.length > 0 && value.length < 10){
                    this.rfStyle = 'red';
                    this.watcherMsg['mpesaRef'] = 'Incomplete Reference Number';
                    this.bWidth = 2;
                }
                else{
                    if(/^[A-Z0-9]$/.test(value)){
                        this.rfStyle = 'green';
                        this.watcherMsg['mpesaRef'] = '';
                        this.bWidth = 2;
                    }
                }
            }
        }, 
        validateNewPassword(value){
            if(value.length == ''){
                this.watcherMsg['newPassword'] = '';
            }else{
                if(value.length > 0 && value.length < 8){
                    this.watcherMsg['newPassword'] = 'Password is too short';
                }
                else{
                    this.watcherMsg['newPassword'] = '';
                }
            }
        },
        validatePassword2(value){
            if(value == this.newPassword){
                this.watcherMsg['newPassword2'] = '';
            }else{
                this.watcherMsg['newPassword2'] = 'Passwords do not match';
            }
        },        
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
        postProfileData() {
            this.errors = [];
            if (this.first_name === "" && this.last_name === "" && this.birthdate === "" && this.gender === "" && this.city === "" && this.county === "" && this.address === "") {
                this.errors.push("Please fill in the details!");
            }
            else {
                if (this.first_name === "" || this.last_name === "" || this.birthdate === "" || this.gender === "" || this.city === "" || this.county === "" || this.address === "") {
                    this.errors.push("Some details are missing!");
                }
            }
            if (!this.errors.length) {
                let formData = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    birthdate: this.birthdate,
                    address: this.address,
                    county: this.county,
                    city: this.city,
                    gender: this.gender,
                    phone_number: this.phone_number,
                    email: this.email
                };
                this.axios.put("/api/v1/user-list/" + this.id + "/", formData)
                    .then((response) => {
                    this.$toast.success("Profile Succesfully Updated", {
                        duration: 5000,
                        dismissible: true
                    });
                    this.fnStyle = ''
                    this.lnStyle = ''
                    this.gStyle = ''
                    this.cStyle = ''
                    this.ccStyle = ''
                    this.aStyle = ''
                    this.$router.push("/my-account");
                })
                    .catch((error) => {
                    console.log(error);
                });
            }
        },
        changePassword(){
            let formData = {
                password:this.newPassword
            }
            this.axios.patch("/api/v1/users/me/",formData)
            .then((response)=>{
                console.log(response.data)
                this.$toast.success('Password Changed Succesfully')
                this.newPassword = ''
                this.newPassword2 = ''
                this.curreentPassword = ''
                this.$store.commit('removeToken')
                const token = this.$store.state.token
                localStorage.setItem('token',token)
                this.$router.push('/login')
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        getProfileDetails() {
            this.axios.get("/api/v1/users/me/")
                .then((response) => {
                this.phone_number = response.data.phone_number;
                this.email = response.data.email;
                this.id = response.data.id;
                this.first_name = response.data.first_name;
                this.last_name = response.data.last_name;
                this.gender = response.data.gender;
                this.city = response.data.city;
                this.county = response.data.county;
                this.birthdate = response.data.birthdate;
                this.address = response.data.address;
                console.log(response.data.email)
                this.currentPassword = response.data.password;
            })
                .catch((error) => {
                    console.log(error)
            });
        },
        getMpesaPayments(){
            this.mpesaRefs = []
            this.axios.get('api/v1/mpesa-payments/')
            .then((response)=>{
                for(let i=0 ; i<response.data.length ; i++){
                    let trans_id = response.data[i].transaction_id
                    this.mpesaRefs.push(trans_id)
                    
                }
                console.log(this.mpesaRefs)
                this.isPayModalVisible = true;
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        confirmPayment(){
            if(this.mpesaRefs.includes(this.mpesaRef)){

                let formData = {
                    paid : true,
                    payment_reference : this.mpesaRef,
                }
               this.axios.patch(`/api/v1/my-orders/${this.myOrderID}/`,formData)
               .then((response)=>{
                    this.$toast.success('Payment Confirmation Succesful', {
                        duration: 3000
                    }) 
                    this.mpesaRef = ''
                    this.payment_number2 = ''
                    this.$router.push('/my-account')
                    this.$store.commit('reloadingPage')
               })
               .catch((error)=>{
                   console.log(error)
               })

            }
            else{
                this.$toast.error('Invalid Reference Number', {
                    duration: 3000
                })
            }
        },
        showClientOrders() {
            this.axios.get("api/v1/my-orders/")
                .then((response) => {
                this.myOrders = response.data;
            })
                .catch((error) => {
                console.log(error);
            });
        },
        showModal() {
            this.isModalVisible = true;

            let orderID = arguments[0];
            this.axios.get(`/api/v1/my-orders/${orderID}/`)
            .then((response)=>{
                this.myOrderDetails = response.data
                console.log(this.myOrderDetails)
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        showPaymentModal(){
            this.paymentModalVisible = true;
            let orderID = arguments[0];
            this.axios.get(`/api/v1/my-orders/${orderID}/`)
            .then((response)=>{
                this.myOrderID = orderID;
                console.log(this.myOrderID)
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        closeModal() {
            this.isModalVisible = false;
            this.paymentModalVisible = false
        },
        showLipaNaMpesa(){
            this.lipaNaMpesa = !this.lipaNaMpesa
        },
        showShippingAddress(){
            this.shippingAddress = true;
        },
        payViaMpesa(){
            this.paymentConfirm = true;
            this.errors = []
            if(this.payment_number === ''){
                this.errors.push('Please enter phone number');
                this.$toast.error('Invalid phone number', {
                    duration: 3000
                })
            }
            if(!this.errors.length && this.pStyle == 'green'){
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
        showPassword(){
            if(!this.showPass){
                this.showPass = true;
                this.passType = true;
            }
            else{
                this.showPass = false;
                this.passType = false;
            }
        }, 
        showPassword2(){
            if(!this.showPass2){
                this.showPass2 = true;
                this.pass2Type = true;
            }
            else{
                this.showPass2 = false;
                this.pass2Type = false;
            }
        },
        printOrder(){
            let orderID = arguments[0];
            this.axios.get(`api/v1/view_pdf/${orderID}/`)
            .then((response)=>{
                console.log(response)
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    beforeMount() {
    },
    mounted() {
        this.getProfileDetails();
        this.showClientOrders();
        
 
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
    .empty-order-list{
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin: 20px;
    }
    .emoji{
        font-size: 36px;
        font-style: normal;
    }
    .lipanampesa{
        width: 95%;
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
    .payment-card{
        background-color: white;
        margin-left:20px;
        margin-bottom: 30px;
        margin-top: 20px;
        align-items: center;
        padding-bottom: 20px;
    }
    .bank-icon{
        background-color: #f3f6ff;
        width: 100px;
        height: 100px;
        margin-bottom: 20px;
    }
    .paypal-icon{
        height: 100px;
        width: 100%;
        margin-bottom: 20px;
    }
    .mpesa-icon{
        height: 50px;
        margin-top: 50px;
        margin-bottom: 20px;
    }
    .payment-row{
        background-color: #f3f6ff;
        margin-top: 20px;
    }
    .btn-payment-option{
        margin-top: 30px;
    }
    .myorders-page .table .img {
    display: flex;
    align-items: center;
    }

    .myorders-page .table .img img {
        max-width: 60px;
        max-height: 60px;
        margin-right: 15px;
    }

    .myorders-page .table .img p {
        display: inline-block;
        text-align: left;
        margin: 0;
    }
    .show-password{
        float: right;
        margin-top: -50px;
        position: relative;
        z-index: 1;
        cursor:pointer;
        height: 35px;
        border:0px;
        background-color: inherit;
        color:grey;
    }
    .show-password:focus{
        outline: none;
    }
    .show-password:hover{
        color: black !important;
    }
</style>