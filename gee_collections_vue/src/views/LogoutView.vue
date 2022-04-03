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
                </div>     
            </div>
        </div> 
        
    </div>
</template>

<script>
export default {
    data(){
        return{
    
        }
    },
    beforeMount() {
        this.$store.commit('removeToken')
        const token = this.$store.state.token 
        localStorage.setItem('token',token)
        console.log('token is:',this.$store.state.token)
    },
}
</script>