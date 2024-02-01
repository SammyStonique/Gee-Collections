<template>
    <!-- Loading Animation for Printing Invoice -->
  <LoadingView
    :loader="loader"
    :showLoader="showLoader"
    :hideLoader="hideLoader"
  />

    <div :style="{zIndex: this.loaderIndex}">

        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
        <div class="container-fluid">
            <ul class="breadcrumb">
            <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
            <li class="breadcrumb-item"><router-link to="/cart">Receipts</router-link></li>
            <li class="breadcrumb-item active">New Receipt</li>
            </ul>
        </div>
        </div>
        <!-- Breadcrumb End -->
        <!-- Checkout Start -->
        <div class="receipt-add w-full px-16 py-10">
            <div class="bg-white py-10">
                <form action="" @submit.prevent="createReceipt">
                    <div class="flex">
                        <div class="basis-1/2 px-20">
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Customer :</strong></p>
                                </div>
                                <div class="basis-1/2">
                                    <select name="customer" ref="customerSelect" id="selectCustomer" class="form-control" @change="showOrders" onfocus="this.selectedIndex = -1;" v-model="customer">
                                        <option value="" disabled="true" selected>--Select Customer--</option>
                                        <option v-for="cust in customersArray">{{ cust.first_name }} {{ cust.last_name }}</option> 
                                    </select>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Payment Method :</strong></p>
                                </div>
                                <div class="basis-1/2">
                                    <select name="payment-method" id="" class="form-control" v-model="payment_method">
                                        <option value="" disabled="true">--Select Payment Method--</option>
                                        <option value="Cash">Cash</option>
                                        <option value="Mpesa">Mpesa</option>
                                        <option value="Cheque">Cheque</option>
                                        <option value="EFT">EFT</option>
                                    </select>
                                </div>
                                
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Receipt Date :</strong></p>
                                </div>
                                <div class="basis-1/2">
                                    <input type="date" name="" id="" class="form-control" v-model="receipt_date">
                                </div>
                            </div>
                            <div class="col-md-12 notification is-danger" v-if="errors.length">
                                <p style="color: red" v-for="error in errors" v-bind:key="error">
                                    {{ error }}
                                </p>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <button type="submit" class="save-button rounded w-24 px-3 py-2">Save</button>
                                </div>
                                <div class="basis-1/2">
                                    <button type="reset" class="reset-button rounded w-24 px-3 py-2">Reset</button>
                                </div>
                            </div>
                        </div>
                        <div class="basis-1/2 px-20">
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Customer Order:</strong></p>
                                </div>
                                <div class="basis-1/2">
                                    <select name="order" ref="orderSelect" id="" class="form-control" @change="setOrderID" onfocus="this.selectedIndex = -1;" v-model="customer_order">
                                        <option value="" disabled="true" selected>--Select Order--</option>
                                        <option v-for="ord in cstOrders">{{ ord.invoice_no }} [{{ord.id}} ({{ ord.order_total }})]</option> 
                                    </select>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Reference No:</strong></p>
                                </div>
                                <div class="basis-1/2">
                                <input type="text" class="form-control" v-model="reference_no">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <p><strong>Amount Received:</strong></p>
                                </div>
                                <div class="basis-1/2">
                                <input type="text" class="form-control" v-model="amount_received">
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<script>
import {ref, reactive} from "vue"
import LoadingView from "@/components/LoadingView.vue"

export default{
    props: ["getAllCustomers", "customersArray", 'showClientOrders','myOrders','loader','showLoader','hideLoader','loaderIndex'],
    components:{
        LoadingView
    },
    // setup(){

    //     const selectedCustomer = ref(null)
    //     const state = reactive({
    //         customer: "",
    //         date: "",
    //         order: "",
    //         reference_no: "",
    //         payment_method: "",
    //         amount: 0,
    //         orders: [],
    //         customerOrders: [],
    //         email: "",
            
    //     });

    //     const showOrders = ()=>{
    //        state.email = this.customersArray[selectedCustomer.selectedIndex].email;
    //        console.log("The email is ", state.email)
    //        console.log("The selcted index is ",selectedCustomer.selectedIndex)

    //         // this.axios
    //         // .get(`api/v1/orders/${user}/`)
    //         // .then((response) => {
    //         //     state.orders = response.data;
    //         //     state.customerOrders = state.orders[selectedCustomer.selectedIndex];
    //         // })
    //         // .catch((error) => {
    //         // console.log(error);
    //         // });
    //     }
    //     return{
    //         selectedCustomer, showOrders
    //     }
    // },
    data(){
        return{
            email: "",
            customerID: "",
            selectedCust: 0,
            selectedOrd: 0,
            orders: [],
            cstOrders: [],
            errors: [],
            receipt_date: "",
            payment_method: "",
            reference_no: "",
            amount_received: 0,
            customer: "",
            customer_order: "",
            balance: 0,
            order_id: "",
            payment_status: false,
            order_first_name: "",
            order_last_name: "",
            order_email: "",
            order_phone_number: "",
            order_county: "",
            order_city: "",
            order_address: "",
            order_items: [],
            order_order_total: 0,
            order_delivery_fee: 0,
            order_coupon: [],
            generated_receipt: [],
            coupon_code : "",
            coupon_status: "Activated",
        }
    },
    methods :{
        showOrders(){
            this.cstOrders = [];
            this.selectedCust = this.$refs.customerSelect.selectedIndex - 1;
            this.email = this.customersArray[this.selectedCust].email;
            this.customerID = this.customersArray[this.selectedCust].id;
    
            this.axios
            .get(`api/v1/orders/?=${this.email}/`)
            .then((response) => {
                this.orders = response.data;
                for(let i=0; i<this.orders.length; i++){
                    if(this.orders[i].user == this.email && this.orders[i].paid == false){
                        this.cstOrders.push(this.orders[i]);
                    }
                }
            })
            .catch((error) => {
            console.log(error);
            });
        },
        setOrderID(){
            this.order_id = "";
            this.order_first_name = "";
            this.order_last_name = "";
            this.order_email = "";
            this.order_phone_number = "";
            this.order_county = "";
            this.order_city = "";
            this.order_address = "";
            this.order_order_total = 0;
            this.order_delivery_fee = 0;
            this.order_items = [];
            this.payment_status = false;
            this.selectedOrd = this.$refs.orderSelect.selectedIndex - 1;
            this.order_id = this.cstOrders[this.selectedOrd].id;
            this.payment_status = this.cstOrders[this.selectedOrd].paid;
            this.order_first_name = this.cstOrders[this.selectedOrd].first_name;
            this.order_last_name = this.cstOrders[this.selectedOrd].last_name;
            this.order_email = this.cstOrders[this.selectedOrd].email;
            this.order_phone_number = this.cstOrders[this.selectedOrd].phone_number;
            this.order_county = this.cstOrders[this.selectedOrd].county;
            this.order_city = this.cstOrders[this.selectedOrd].city;
            this.order_address = this.cstOrders[this.selectedOrd].address;
            this.order_order_total = this.cstOrders[this.selectedOrd].order_total;
            this.order_delivery_fee = this.cstOrders[this.selectedOrd].delivery_fee;
            this.order_items = this.cstOrders[this.selectedOrd].items;
            this.coupon_applied = this.cstOrders[this.selectedOrd].coupon_applied;
        },
        createReceipt(){
            this.showLoader();
            this.errors = [];
            if (
                this.customer === "" &&
                this.receipt_date === "" &&
                this.payment_method === "" &&
                this.customer_order === "" &&
                this.reference_no === "" &&
                this.amount_received === ""
            ) {
                this.errors.push("Please fill in the details!");
            } else {
                if (
                this.customer === "" ||
                this.receipt_date === "" ||
                this.payment_method === "" ||
                this.customer_order === "" ||
                this.reference_no === "" ||
                this.amount_received === "" 
                ) {
                this.errors.push("Some details are missing!");
                }
            }
            this.balance = this.cstOrders[this.selectedOrd].order_total - this.amount_received;
            if (!this.errors.length) {
                let formData = {
                    receipt_order: this.order_id,
                    receipt_user: this.customerID,
                    received_amount: Number(this.amount_received).toFixed(2),
                    payment_method: this.payment_method,
                    reference_no: this.reference_no,
                    created_at: this.receipt_date,
                    balance: Number(this.balance).toFixed(2)
                }
                this.axios
                .post('api/v1/generate-receipt/', formData)
                .then((response)=>{
                    this.generated_receipt = response.data;
  
                    this.$toast.success("Receipt Succesfully Added", {
                    duration: 5000,
                    dismissible: true,
                    });
                })
                .catch((error)=>{
                    console.log(error);
                })
                .finally(()=>{
                    this.payment_status = true;
                    let formData = {
                        first_name: this.order_first_name,
                        last_name: this.order_last_name,
                        email: this.order_email,
                        phone_number: this.order_phone_number,
                        county: this.order_county,
                        city: this.order_city,
                        address: this.order_address,
                        order_total: this.order_order_total,
                        delivery_fee: this.order_delivery_fee,
                        items: this.order_items,
                        paid : this.payment_status,
                        payment_reference : this.reference_no,
                        receipt_no : this.generated_receipt.receipt_no,
                        coupon_applied: this.coupon_applied,
                    }
                    
                    this.axios
                    .put("/api/v1/orders/" + this.order_id + "/", formData)
                    .then((response)=>{
                        console.log(response);
                    })
                    .catch((error)=>{
                        console.log(error.message);
                        // console.log(error.response.data);  
                        // console.log(error.response.status);  
                        // console.log(error.response.headers);
                    })
                    .finally(()=>{
                        this.axios
                        .get(`/api/v1/coupons/?=${ this.order_id }/`)
                        .then((response)=>{
                            this.order_coupon = response.data;
                            this.coupon_code = this.order_coupon[0].coupon_code;                          
                        })
                        .catch((error)=>{
                            console.log(error.message);
                        })
                        .finally(()=>{
                            let formData = {
                                coupon_amount : this.order_coupon[0].coupon_amount,
                                coupon_order : this.order_coupon[0].coupon_order,
                                status: this.coupon_status,
                            }
                            this.axios
                            .put(`/api/v1/coupons-list/${this.coupon_code}/`, formData)
                            .then((response)=>{

                            })
                            .catch((error)=>{
                                console.log(error.message);
                            })
                            .finally(()=>{
                                this.hideLoader();
                                this.customer = "";
                                this.customer_order = "";
                                this.amount_received = 0;
                                this.receipt_date = "";
                                this.payment_method = "";
                                this.reference_no = "";
                                this.payment_status = false;
                            })
                        })
                    
                    })
                    
                })
            }

        }

    },
    mounted(){
        this.getAllCustomers();
    }
}

</script>

<style scoped>
 .save-button{
    background-color: #ff6f61;
    color: white;
 }
 .reset-button{
    border: 1px solid;
    border-color: #ff6f61;
 }
 .save-button:hover{
    border: 1px solid;
    background-color: black;
    color: white;
 }
 .reset-button:hover{
    border: 1px solid;
    background-color: #ff6f61;
    color: white;
 }
</style>