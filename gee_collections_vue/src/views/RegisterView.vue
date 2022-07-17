<template>
    <div class="register">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                    <li class="breadcrumb-item active">Register</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        
        <!-- Login Start -->
        <div class="login">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <form @submit.prevent="createUser">    
                            <div class="register-form">
                            <h1 style="text-align: center; margin-bottom: 20px;">Sign Up</h1>
                                <div class="row">
                                    <div class="col-md-6">
                                        <label>E-mail<em>*</em></label>
                                        <input class="form-control" type="email" placeholder="E-mail" v-model="email" :style="{borderColor: eStyle,borderWidth: bWidth+'px' }" required>
                                        <span v-if="watcherMsg.email" :style="{color: eStyle, fontSize:10 + 'px'}">{{watcherMsg.email}}</span>
                                    </div>
                                    <div class="col-md-6">
                                        <label>Mobile No<em>*</em></label>
                                        <input class="form-control" type="text" placeholder="e.g 07XXXXXXXX" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px' }" required>
                                        <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                                    </div>
                                    <div class="col-md-6">
                                        <label>Password<em>*</em></label>
                                        <input class="form-control" :type="passType ? 'text' : 'password'" placeholder="Password" v-model="password" :style="{borderColor: pStyle,borderWidth: bWidth+'px' }" required>
                                        <button type="button" class="show-password" @click="showPassword()">
                                        <i class="fa fa-eye-slash" v-if="!passType"></i>
                                        <i class="fa fa-eye" v-else></i>
                                        </button>
                                        <span v-if="watcherMsg.password" :style="{color: pStyle, fontSize:10 + 'px' }">{{watcherMsg.password}}</span>
                                    </div>
                                    <div class="col-md-6">
                                        <label>Confirm Password<em>*</em></label>
                                        <input class="form-control" :type="pass2Type ? 'text' : 'password'" placeholder="Password" v-model="password2" :style="{borderColor: passStyle,borderWidth: bWidth+'px' }" required>
                                        <button type="button" class="show-password" @click="showPassword2()">
                                        <i class="fa fa-eye-slash" v-if="!pass2Type"></i>
                                        <i class="fa fa-eye" v-else></i>
                                        </button>
                                        <span v-if="watcherMsg.password2" :style="{color: passStyle , fontSize:10 + 'px' }">{{watcherMsg.password2}}</span>
                                    </div>
                                    <div class="col-md-12 notification is-danger" v-if="errors.length">
                                        <p class="capitalize-first" style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                    </div>
                                    <div class="col-md-12 btn-submit">
                                        <button class="btn submit-btn">Sign Up</button>
                                    </div>
                                </div>
                            </div>
                        </form>
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
            email: '',
            password: '',
            password2: '',
            phone_number: '',
            errors:[],
            watcherMsg:[],
            eStyle: null,
            nStyle: null,
            pStyle: null,
            passStyle: null,
            bWidth : null, 
            showPass: false,
            passType: false,
            showPass2: false,
            pass2Type : false          
        }
    },
    watch: {
        email(value){
        // binding this to the data value in the email input  
        this.email = value; 
        this.validateEmail(value);
        },
        phone_number(value){
            this.phone_number = value;
            this.validatePhoneNumber(value)
        },
        password(value){
            this.password = value;
            this.validatePassword(value)
        },
        password2(value){
            this.password2 = value;
            this.validatePasswordConfirmation(value)
        }
    },
    methods:{
        validateEmail(value){  
            if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value)){ 
                this.watcherMsg['email'] = '';
                this.eStyle = 'green';
                this.bWidth = 2

            } else{
                if(value == ''){
                    this.watcherMsg['email'] = ''; 
                    this.eStyle = ''

                }
                else{
                    this.watcherMsg['email'] = 'Invalid Email Address'; 
                    this.eStyle = 'red'
                    this.bWidth = 2
                }
            }  
        }, 
        validatePhoneNumber(value){
            if ((/^(?:254|\+254|0)?((?:(?:7(?:(?:[01249][0-9])|(?:5[789])|(?:6[89])))|(?:1(?:[1][0-5])))[0-9]{6})$/.test(value))|| (/^(?:254|\+254|0)?((?:(?:7(?:(?:3[0-9])|(?:5[0-6])|(8[5-9])))|(?:1(?:[0][0-2])))[0-9]{6})$/.test(value))){
                    this.nStyle = 'green';
                    this.watcherMsg['phone_number'] = ''
                    this.bWidth = 2

            }else{
                if(value == ''){
                    this.nStyle = '';
                    this.watcherMsg['phone_number'] = ''                        
                }
                else{
                    this.nStyle = 'red';
                    this.watcherMsg['phone_number'] = 'Invalid Phone Number'
                    this.bWidth = 2
                }
            }
        },
        validatePassword(value){
            if (value.length > 0 && value.length < 8){
                this.watcherMsg['password'] = 'Must be a minimum of 8 characters!'
                this.pStyle = 'red'
                this.bWidth = 2
            }else{
                if(value.length == 0){
                   this.watcherMsg['password'] = ''
                   this.pStyle = ''
                }
            else{
                    this.pStyle = 'green'
                    this.watcherMsg['password'] = ''
                    this.bWidth = 2
                }
            }
        }, 
        validatePasswordConfirmation(value){
            if (value === this.password){
                this.passStyle = 'green'
                this.watcherMsg['password2'] = ''
                this.bWidth = 2
            }else{
                this.watcherMsg['password2'] = 'The passwords do not match'
                this.passStyle = 'red'
                this.bWidth = 2
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
        createUser(){
            this.errors = []
            if(this.email === ''&&this.password === ''&&this.password2 === ''&& this.phone_number===''){
                this.errors.push('Please fill in the details!')
            }else{
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
                    this.password2 = ''
                }
            }

            if(!this.errors.length){
                let formData = new FormData();
                formData.append('email', this.email);
                formData.append('password', this.password);
                formData.append('phone_number', this.phone_number)

                this.axios.post('/api/v1/users/', formData)
                .then((response)=>{
                    this.$toast.success('Account Created Succesfully',{
                        duration: 10000,
                        dismissible: true
                    })
                    this.$router.push('/login');
                })
                .catch((error)=>{
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push((`${error.response.data[property]}`).toLowerCase().split(' ').map((s) => s.charAt(0).toUpperCase() + s.substring(1)).join(' '))
                            this.$toast.error((`${error.response.data[property]}`).toLowerCase().split(' ').map((s) => s.charAt(0).toUpperCase() + s.substring(1)).join(' '),{
                                duration: 5000,
                                dismissible: true
                            })
                        }
                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })
            }
            
        }
    }
}
</script>

<style scoped>
    .container-fluid{
        width:80%;
    }
    .btn-submit{
        text-align: center;
    }
    .submit-btn{
        width: 30%;
    }
    em{
        color: red;
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
</style>