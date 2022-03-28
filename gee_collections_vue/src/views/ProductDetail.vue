<template>
    <div class="product-detail">
        <h1>Product Detail</h1>
        <div class="row">
                <div class="col-md-6">
                    <label for="">Name</label>
                    <input type="text" v-model="name">
                </div>
                <div class="col-md-6">
                <label for="">Price</label>
                    <input type="number" v-model="price">
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="">Image</label>
                    <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg">
                </div>
                <div class="col-md-6">
                <label for="">Thumbnail</label>
                <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg">
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="">Description</label>
                    <textarea v-model="description"></textarea>
                </div>
            </div>
            <button @click="getProduct">Get Product</button>
    
    </div>
</template>

<script>
export default {
    data(){
        return{
           name:null, 
           price:null,
           description:null,
           image:null
        }
    },
    methods:{
        getProduct(){
            this.axios.get('http://127.0.0.1:8000/api/v1/latest-products/1/')
            .then((response)=>{
                console.log(response);
                this.name = response.data.name;
                this.price = response.data.price;
                this.description = response.data.description;
            })
            .catch((error)=>{
                console.log(error);
            })
        },
        onChangeFile(){

        }
    },
    mounted(){
        this.getProduct();
    }
}
</script>