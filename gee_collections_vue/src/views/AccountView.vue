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
                            </div>
                            <div class="tab-pane fade" id="orders-tab" role="tabpanel" aria-labelledby="orders-nav">
                                <div class="table-responsive">
                                    <table class="table table-bordered">
                                        <thead class="thead-dark">
                                            <tr>
                                                <th>#</th>
                                                <th>Date</th>
                                                <th>Order Total</th>
                                                <th>Status</th>
                                                <th>Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="order,index in myOrders" :key="index">
                                                <td>{{order.id}}</td>
                                                <td>{{order.created_at.substring(0,10)}}</td>
                                                <td>ksh {{Number(order.order_total).toLocaleString()}}</td>
                                                <td v-if="order.paid">Paid</td>
                                                <td v-else>Not Paid</td>
                                                <td v-if="order.paid"><button class="btn" @click="showModal(order.id)">View Order</button></td>
                                                <td v-else><button class="btn" @click="showPaymentModal(order.id)">Make Payment</button></td>
                                            </tr>
                                        </tbody>
                                    </table>

                                    <p class="empty-order-list" v-if="!Object.keys(myOrders).length"><span class="emoji " role="img" aria-label="">😭</span><br/><em class="empty-cart-message">Ooops,You haven't placed any order yet</em></p>

                                    <!-- PAGINATION -->
                                    <div class="row">
                                        <Pagination
                                            :totalPages="totalPages"
                                            :perPage="itemsPerPage"
                                            :currentPage="currentPage"
                                            :totalItems="totalItems"
                                            @page-changed="onPageChange"
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
                                                        <!-- <a href="#"><img :src="`${ordDet.product.image}`" alt="Image"></a> -->
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
                            </template>

                            <template v-slot:footer>
                                This is a new modal footer.
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
                                    <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX">
                                    <!-- <input type="text" class="form-control" placeholder="e.g 2547XXXXXXXX" v-model="payment_number"> -->
                                    <div class="col-md-12 notification is-danger" v-if="errors.length">
                                        <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                    </div>
                                    <button type="button" class="procPayBtn" @click="payViaMpesa">Proceed to Pay</button>
                                    </div>
                                </div>
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
                                        <button class="btn">Edit Address</button>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="account-tab" role="tabpanel" aria-labelledby="account-nav">
                                <h4>Account Details</h4>
                                <form action="" @submit.prevent="postProfileData">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="First Name" v-model="first_name">
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="Last Name" v-model="last_name">
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="email" placeholder="Email" v-model="email" disabled="true">
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="text" placeholder="Mobile" v-model="phone_number">
                                        </div>
                                        <div class="col-md-6">
                                            <select name="gender" class="form-control" v-model="gender">
                                                <option value="" disabled="true">--Select your Gender--</option>
                                                <option>Male</option>
                                                <option>Female</option>
                                                <option>Other</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6">
                                            <input class="form-control" type="date" placeholder="Date of Birth" v-model="birthdate">
                                        </div>
                                        <div class="col-md-6">
                                            <select name="city" class="form-control" v-model="city">
                                                <option value="" disabled="true">--Select your City--</option>
                                                <option>Nairobi</option>
                                                <option>Kisumu</option>
                                                <option>Mombasa</option>
                                                <option>Nakuru</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6">
                                            <select name="county" class="form-control" v-model="county">
                                                <option disabled="true">--Select your County--</option>
                                                <option>Siaya</option>
                                                <option>Kisumu</option>
                                                <option>Nairobi</option>
                                                <option>Mombasa</option>
                                            </select>
                                        </div>
                                        <div class="col-md-12">
                                            <input class="form-control" type="text" placeholder="Address" v-model="address">
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
                                <div class="row">
                                    <div class="col-md-12">
                                        <input class="form-control" type="password" placeholder="Current Password">
                                    </div>
                                    <div class="col-md-6">
                                        <input class="form-control" type="text" placeholder="New Password">
                                    </div>
                                    <div class="col-md-6">
                                        <input class="form-control" type="text" placeholder="Confirm Password">
                                    </div>
                                    <div class="col-md-12">
                                        <button class="btn">Save Changes</button>
                                    </div>
                                </div>
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

export default {
    props: ["getUserDetails", "userDetails"],
    components:{
        Modal,
        Pagination,
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
            paymentModalVisible: false,
            lipaNaMpesa: false,
            currentPage: 1,
            totalItems: 0,
            itemsPerPage: 2,
            totalPages: 0,
            start: 1,
            limit: 2,
        };
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
        onPageChange(page){
            this.currentPage = page
            this.start += this.limit;

            this.axios.get(`api/v1/my-orders-pagination/`)
                .then((response)=>{
                    this.myOrders = response.data;
                    console.log(this.myOrders)
                })
                .catch((error)=>{
                    console.log(error)
                })
        },
        showClientOrders() {
            this.axios.get("api/v1/my-orders-pagination/")
                .then((response) => {
                this.myOrders = response.data;
                this.totalItems = response.data.length;
                
                const pages = ~~(this.totalItems / this.itemsPerPage);
                this.totalPages = pages;
            })
                .catch((error) => {
                console.log(error);
            });
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
                    console.log(response.data)
                    this.$toast.success("Profile Succesfully Updated", {
                        duration: 5000,
                        dismissible: true
                    });
                    this.$router.push("/my-account");
                })
                    .catch((error) => {
                    console.log(error);
                });
            }
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
            })
                .catch((error) => {
                    console.log(error)
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
            this.paymentModalVisible = true
        },
        closeModal() {
            this.isModalVisible = false;
            this.paymentModalVisible = false
        },
        showLipaNaMpesa(){
            this.lipaNaMpesa = !this.lipaNaMpesa
        },
        payViaMpesa(){
            const formData = {
                    "BusinessShortCode": 174379,
                    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNDIxMTcxODIy",
                    "Timestamp": "20220421171822",
                    "TransactionType": "CustomerPayBillOnline",
                    "Amount": 1,
                    "PartyA": 254795968217,
                    "PartyB": 174379,
                    "PhoneNumber": 254795968217,
                    "CallBackURL": "https://478f-197-248-34-79.ngrok.io/api/v1/c2b/callback",
                    "AccountReference": "Gee Collections",
                    "TransactionDesc": "Payment of X"
                }
                this.axios.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',formData)
                .then((response)=>{
                    console.log(response.data)
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
        width: 60%;
        height: 40px;
        padding: 2px 10px;
        font-family: 'Source Code Pro', monospace;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        color: #000000;
        background: #228B22;
        border: none;
        border-radius: 4px;
        transition: all .3s;
        margin-bottom: 20px;
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
</style>