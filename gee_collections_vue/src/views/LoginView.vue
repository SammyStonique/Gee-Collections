<template>

     <!-- Loading Animation for Printing Invoice -->
    <LoadingView
        :loader="loader"
        :showLoader="showLoader"
        :hideLoader="hideLoader"
    />

    <div class="login">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid login-breadcrumb">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                    <li class="breadcrumb-item active">Login</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        <div class="login">
            <div class="container-fluid user-login-container">
                <div class="user-login-form">
                    <form action="" @submit.prevent="userLogin">
                        <div class="col-md-6">
                            <label>Email</label>
                            <input class="form-control" type="email" placeholder="Enter your email" v-model="email" required>
                        </div>
                        <div class="col-md-6">
                            <label>Password</label>
                            <input class="form-control" :type="passType ? 'text' : 'password'" placeholder="Password" v-model="password" required>
                            <button type="button" class="show-password" @click="showPassword()">
                            <i class="fa fa-eye-slash" v-if="!passType"></i>
                            <i class="fa fa-eye" v-else></i>
                            </button>
                        </div>
                        <div class="col-md-12 notification is-danger" v-if="errors.length">
                            <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                        <div class="col-md-12">
                            <div class="custom-control custom-checkbox">
                                <input type="checkbox" class="custom-control-input" id="newaccount">
                                <label class="custom-control-label" for="newaccount">Keep me signed in</label>
                            </div>
                        </div>
                        <div class="col-md-12" style="font-size: 12px;">
                            <label for="">Don't have an account? </label>
                            <router-link to="/register"> Register</router-link>
                        </div>
                        <div class="col-md-12">
                            <button class="btn login-btn">Login</button>
                        </div>
                    </form>
                </div>     
            </div>
        </div>    
    </div>
</template>

<script>
import axios from 'axios'
import LoadingView from "@/components/LoadingView.vue"
export default {
    props:['token','isAuthenticated','loader','showLoader','hideLoader','loaderIndex'],
    data(){
        return{
            email:'',
            password: '',
            errors: [],
            showPass: false,
            passType: false
        }
    },
    components:{
        LoadingView
    },
    methods:{ 
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
        userLogin(){
            this.errors = [];
            if(this.email === '' && this.password === ''){
                this.errors.push('Please fill in the details')
                this.$toast.error('Invalid email and password', {
                    duration: 5000
                })
            }else{
                if(this.email ===''){
                    this.errors.push('Please enter your email')
                }
                if(this.password === ''){
                    this.errors.push('Please enter your password')
                }
            }

            if(!this.errors.length){
                const formData = {
                    email: this.email,
                    password: this.password
                }

                this.axios
                    .post('/api/v1/token/login/', formData)
                    .then((response)=>{
                        const token = response.data.auth_token;        
                        this.$store.commit('setToken', token);
                        axios.defaults.headers.common['Authorization'] = "Token " + token
                        localStorage.setItem('token',token)
                        this.$toast.success('Login Succesful',{
                            duration: 5000
                        })
                        this.$router.push('/');
                        this.$store.commit('reloadingPage');
                    })    
                    .catch((error)=>{
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data));
                            this.$toast.error('Invalid Login Credentials!',{
                                duration:5000
                            })
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again');
                            console.log(JSON.stringify(error))
                        }
                    })
                    .finally(()=>{
                        
                    })
            }
            
        }
    }
}
</script>

<style scoped> 
    input{
        font-weight: 300;
        color: black;
    }
    .user-login-container{
        width: 80%;
    }
    .login-breadcrumb{
        width: 80%;
    }
    .login-btn{
        width: 20%;
    }
    .login-form{
        max-width: 80%;
    }
    input{
        font-weight: 300;
        color: black;
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
    .user-login-form{
        background-color: white;
        margin-bottom: 50px;
        padding: 30px;
    }
</style>