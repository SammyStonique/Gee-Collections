<template>
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
            <form action="" @submit.prevent="">
                <div class="flex">
                    <div class="basis-1/2 px-20">
                        <div class="flex">
                            <div class="basis-1/2">
                                <p><strong>Customer :</strong></p>
                            </div>
                            <div class="basis-1/2">
                                <!-- <select name="customer" ref="customerSelect" id="selectCustomer" class="form-control" onchange="showOrders" onfocus="this.selectedIndex = -1;"> -->
                                <select name="customer" ref="customerSelect" id="selectCustomer" class="form-control" @change="showOrders" onfocus="this.selectedIndex = -1;">
                                    <option value="" disabled="true" selected>--Select Customer--</option>
                                    <option v-for="cust in customersArray">{{ cust.first_name }} {{ cust.last_name }}</option> 
                                </select>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="basis-1/2">
                                <p><strong>Receipt Date :</strong></p>
                            </div>
                            <div class="basis-1/2">
                                <input type="date" name="" id="" class="form-control">
                            </div>
                        </div>
                        <div class="flex">
                            <div class="basis-1/2">
                                <p><strong>Payment Method :</strong></p>
                            </div>
                            <div class="basis-1/2">
                                <select name="payment-method" id="" class="form-control" aria-placeholder="Select Payment Method">
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
                                <select name="customer" id="" class="form-control" aria-placeholder="Select Customer Order">
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
                            <input type="text" class="form-control">
                            </div>
                        </div>
                        <div class="flex">
                            <div class="basis-1/2">
                                <p><strong>Amount Received:</strong></p>
                            </div>
                            <div class="basis-1/2">
                            <input type="text" class="form-control">
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>

</template>

<script>
import {ref, reactive} from "vue"
export default{
    props: ["getAllCustomers", "customersArray", 'showClientOrders','myOrders'],
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
            selectedCust: 0,
            orders: [],
            cstOrders: []
        }
    },
    methods :{
        showOrders(){
            this.cstOrders = [];
            this.selectedCust = this.$refs.customerSelect.selectedIndex - 1;
            this.email = this.customersArray[this.selectedCust].email;
    
            this.axios
            .get(`api/v1/orders/?=${this.email}/`)
            .then((response) => {
                this.orders = response.data;
                for(let i=0; i<this.orders.length; i++){
                    if(this.orders[i].user == this.email){
                        this.cstOrders.push(this.orders[i]);
                    }
                }
                console.log("The customer orders are ", this.cstOrders)
            })
            .catch((error) => {
            console.log(error);
            });
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