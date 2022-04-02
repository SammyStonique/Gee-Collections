<template>
    <div class="login">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Products</a></li>
                    <li class="breadcrumb-item active">Login & Register</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        
        <!-- Login Start -->
        <div class="login">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-6">
                        <form @submit.prevent="createUser">    
                            <div class="register-form">
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
                                        <input class="form-control" type="email" placeholder="E-mail" v-model="email">
                                    </div>
                                    <div class="col-md-6">
                                        <label>Mobile No</label>
                                        <input class="form-control" type="text" placeholder="Mobile No" v-model="phone_number">
                                    </div>
                                    <div class="col-md-6">
                                        <label>Password</label>
                                        <input class="form-control" type="password" placeholder="Password" v-model="password">
                                    </div>
                                    <div class="col-md-6">
                                        <label>Confirm Password</label>
                                        <input class="form-control" type="password" placeholder="Password" v-model="password2">
                                    </div>
                                    <div class="col-md-12 notification is-danger" v-if="errors.length">
                                        <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                    </div>
                                    <div class="col-md-12">
                                        <button class="btn">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-6">
                        <div class="login-form">
                            <div class="row">
                                <div class="col-md-6">
                                    <label>E-mail</label>
                                    <input class="form-control" type="email" placeholder="E-mail">
                                </div>
                                <div class="col-md-6">
                                    <label>Password</label>
                                    <input class="form-control" type="password" placeholder="Password">
                                </div>
                                <div class="col-md-12">
                                    <div class="custom-control custom-checkbox">
                                        <input type="checkbox" class="custom-control-input" id="newaccount">
                                        <label class="custom-control-label" for="newaccount">Keep me signed in</label>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <button class="btn">Submit</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Login End -->
    </div>
</template>

<script>
export default {
    data(){
        return{
            first_name:'',
            last_name:'',
            email: '',
            password: '',
            password2: '',
            phone_number: '',
            errors:[]
        }
    },
    methods:{
        createUser(){
            this.errors = []
            if(this.first_name === ''&& this.last_name === ''&&this.email === ''&&this.password === ''&&this.password2 === ''){
                this.errors.push('Please fill in the details!')
            }else{
                if(this.first_name === ''){
                    this.errors.push('First Name is missing')
                }
                if(this.last_name === ''){
                    this.errors.push('Last Name is missing')
                }
                if(this.email === ''){
                    this.errors.push('Email is missing')
                }
                if(this.phone_number === ''){
                    this.errors.push('Phone number required')
                }
                if(this.password === ''){
                    this.errors.push('Password is too short')
                }
                if(this.password2 === ''){
                    this.errors.push('Please confirm your password')
                }
                if(this.password !== this.password2){
                    this.errors.push('Passwords do not match')
                }
            }

            if(!this.errors.length){
                let formData = new FormData();
                formData.append('username', this.email);
                formData.append('password', this.password);

                this.axios.post('http://127.0.0.1:8000/api/v1/users/', formData)
                .then((response)=>{
                    console.log(response);
                    this.$toast.success('Account created succesfully, verification link sent to your email. Please verify',{
                        duration: 10000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error);
                })
            }
            
        }
    }
}
</script>

<style scoped>
</style>