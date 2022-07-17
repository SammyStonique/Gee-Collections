<template>
    <div class="logout">
        <div class="breadcrumb-wrap">
            <div class="container-fluid login-breadcrumb">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                    <li class="breadcrumb-item active">Logout</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        <div class="login">
            <div class="container-fluid user-login-container">
                <div class="user-login-form">
                    <h1>You have been logged out</h1>
                    <p>You have been logged out. Do you want to log back in?</p>
                    <router-link to="/login"><button class="btn login-btn">Login</button></router-link>
                </div>     
            </div>
        </div> 
        
    </div>
</template>

<script>
export default {
    props:['loggedOut'],
    data(){
        return{
    
        }
    },
    beforeMount() {
        this.$store.commit('removeToken')
        this.$store.commit('clearCart')
        console.log(this.$store.state.reloaded)
        const token = this.$store.state.token
        localStorage.setItem('token',token)
    },
    mounted(){
        if (this.$store.state.reloaded == false){
            // this.$store.commit('reloadingPage')
            this.$store.state.reloaded = true
        }
    }
}
</script>

<style scoped>
    .user-login-form{
        background-color: white;
        height: 250px;
        margin-bottom: 20px;
        text-align: center;
        max-width: 80%;
    }
    p{
        margin:20px;
    }
</style>