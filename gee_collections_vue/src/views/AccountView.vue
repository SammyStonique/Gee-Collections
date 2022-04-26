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
                                                <td>{{order.created_at}}</td>
                                                <td>ksh {{order.order_total}}</td>
                                                <td>Approved</td>
                                                <td><button class="btn">View</button></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="payment-tab" role="tabpanel" aria-labelledby="payment-nav">
                                <h4>Payment Method</h4>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In condimentum quam ac mi viverra dictum. In efficitur ipsum diam, at dignissim lorem tempor in. Vivamus tempor hendrerit finibus. Nulla tristique viverra nisl, sit amet bibendum ante suscipit non. Praesent in faucibus tellus, sed gravida lacus. Vivamus eu diam eros. Aliquam et sapien eget arcu rhoncus scelerisque.
                                </p> 
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

export default {
    props:['getUserDetails','userDetails'],
    data(){
        return{
            id:'',
            first_name:'',
            last_name: '',
            email: '',
            phone_number: '',
            birthdate: '',
            address: '',
            county: '',
            city: '',
            gender: '',
            errors:[],
            myOrders: []
        }
    },
    methods:{
        showClientOrders(){
            this.axios.get('api/v1/my-orders/')
            .then((response)=>{
                this.myOrders = response.data
                console.log(this.myOrders)
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        postProfileData(){
            this.errors = []
            if(this.first_name ===''&&this.last_name ===''&&this.birthdate ===''&&this.gender ===''&&this.city ===''&&this.county ===''&&this.address ===''){
                this.errors.push('Please fill in the details!')
            }else{
                if(this.first_name ===''||this.last_name ===''||this.birthdate ===''||this.gender ===''||this.city ===''||this.county ===''||this.address ===''){
                this.errors.push('Some details are missing!')
                }
                // if(this.first_name ===''){
                //     this.errors.push('First Name is missing')
                // }
                // if(this.last_name ===''){
                //     this.errors.push('Last Name is missing')
                // }
                // if(this.birthdate ===''){
                //     this.errors.push('Date of birth missing')
                // }
                // if(this.gender ===''){
                //     this.errors.push('Please select your gender')
                // }
                // if(this.city ===''){
                //     this.errors.push('Please select your gender')
                // }
                // if(this.county ===''){
                //     this.errors.push('Please select your gender')
                // }
                // if(this.address ===''){
                //     this.errors.push('Address details missing')
                // }
            }
            if(!this.errors.length){
                let formData = {
                    first_name:this.first_name,
                    last_name: this.last_name,
                    birthdate: this.birthdate,
                    address: this.address,
                    county: this.county,
                    city: this.city,
                    gender: this.gender,    
                    phone_number: this.phone_number,
                    email: this.email               
                }
                this.axios.put('/api/v1/user-list/'+this.id+'/', formData)
                .then((response)=>{
                    console.log(response.data);
                    this.$toast.success('Profile Succesfully Updated',{
                        duration: 5000,
                        dismissible: true
                    })
                    this.$router.push('/my-account');
                })
                .catch((error)=>{
                    console.log(error);
                })
            }    
        },
        getProfileDetails(){
            this.axios.get('/api/v1/users/me/')
            .then((response)=>{
                console.log(response.data)
                this.phone_number = response.data.phone_number;
                this.email = response.data.email;
                this.id = response.data.id;
                this.first_name = response.data.first_name
                this.last_name = response.data.last_name
                this.gender = response.data.gender
                this.city = response.data.city
                this.county = response.data.county
                this.birthdate = response.data.birthdate
                this.address = response.data.address
            })
            .catch((error)=>{

            })
        },    
    },
    mounted(){
        this.getProfileDetails()
        this.showClientOrders()
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
</style>