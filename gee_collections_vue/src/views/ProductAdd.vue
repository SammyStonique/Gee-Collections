<template>
    <div class="add-product">
        <h1>Products</h1>
        <form @submit.prevent="postProduct">
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
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<style>
    .row{
        margin:5px;
    }
</style>

<script>
export default {
    data(){
        return{
            image:null,
            thumbnail:null,
            name:'',
            description:'',
            price: 0
            
        }
    },
    methods:{
        onFileChange(e){
            this.image = e.target.files[0];
            console.log(this.image)
        },
        postProduct(){
            let formData = new FormData();
            formData.append('image', this.image);
            formData.append('name',this.name);
            formData.append('price',this.price);
            formData.append('description', this.description);
            console.log(formData)
            this.axios.post('http://127.0.0.1:8000/api/v1/latest-products/', formData)
            .then((response)=> {
                console.log(response)
            })
            .catch((error)=>{
                console.log(error)
            })
        },
    }
}
</script>
