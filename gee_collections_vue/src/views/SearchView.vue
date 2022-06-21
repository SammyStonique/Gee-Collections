<template>
    <div class="products">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Products</a></li>
                    <li class="breadcrumb-item active">Search Result</li>
                </ul>
            </div>
        </div>
        <!-- Breadcrumb End -->
        <!-- Product List Start -->
        <div class="product-view">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-9">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="product-view-top">
                                    <div class="row">
                                        <p style="font-size: 20px;">Showing Results for "<em style="font-weight: bold; font-size: 24px;">{{this.productSearch}}</em> "</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">   
                                <div class="col-md-4">
                                    <ProductCard
                                    :item="searchItem"
                                    :addToCart="addToCart"
                                    :getProductDetails="getProductDetails"
                                    :addToWishlist="addToWishlist"
                                    :buyNow="buyNow"

                                    />
                                </div>
                        </div>
                    </div>           
                    
                    <!-- Side Bar Start -->
                    <div class="col-lg-3 sidebar">
                        <div class="sidebar-widget category">
                            <h2 class="title">Category</h2>
                            <nav class="navbar bg-light">
                                <ul class="navbar-nav">
                                    <li class="nav-item">
                                        <a class="nav-link" href="#"><i class="fa fa-female"></i>Fashion & Beauty</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#"><i class="fa fa-child"></i>Kids & Babies Clothes</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#"><i class="fa fa-tshirt"></i>Men & Women Clothes</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#"><i class="fa fa-mobile-alt"></i>Gadgets & Accessories</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#"><i class="fa fa-microchip"></i>Electronics & Accessories</a>
                                    </li>
                                </ul>
                            </nav>
                        </div>
                        
                        <div class="sidebar-widget widget-slider">
                            <div class="swiper">
                                <div class="swiper-wrapper">
                                    <div class="swiper-slide" v-for="item,index in items" >
                                        <ProductCard
                                        :item="item"
                                        :key="item.id"
                                        :getProducts="getProducts"
                                        :index="index"
                                        :addToCart="addToCart"
                                        :getProductDetails="getProductDetails"
                                        :buyNow="buyNow"
                                        />
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="sidebar-widget brands">
                            <h2 class="title">Our Brands</h2>
                            <ul>
                                <li><a href="#">Nulla </a><span>(45)</span></li>
                                <li><a href="#">Curabitur </a><span>(34)</span></li>
                                <li><a href="#">Nunc </a><span>(67)</span></li>
                                <li><a href="#">Ullamcorper</a><span>(74)</span></li>
                                <li><a href="#">Fusce </a><span>(89)</span></li>
                                <li><a href="#">Sagittis</a><span>(28)</span></li>
                            </ul>
                        </div>
                    </div>
                    <!-- Side Bar End -->
                </div>
            </div>
        </div>
        <!-- Product List End --> 
    </div>
</template>

<style>
    
</style>

<script>
import {Swiper, Autoplay} from 'swiper';
import ProductCard from '@/components/ProductCard.vue';
import Pagination from '@/components/Pagination.vue'
export default {
    props:['getProducts','items','addToCart','addToWishlist','getProductDetails','totalItems','buyNow','scrollToTop'],
    components:{
        ProductCard,
        Swiper,
        Pagination
    },
    data(){
        return{
            pageOfItems: [],
            productSearch : '',
            searchItems: [],
            searchItem: []
        }
    },
    methods:{
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
        getSearchedProduct(){
            this.axios.get(`api/v1/latest-products/${this.productSearch}`)
            .then((response)=>{
                this.searchItem = response.data;
                this.searchItems.push(this.searchItem)
                console.log('the searched item is',this.searchItems[0])
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        searchAddToCart(){
            //Getting the index of the items in the cart
            let selectedItem = arguments[0];
            if(isNaN(this.quantity) || this.quantity<1){
                this.quantity = 1;
            }
            
            const cartItem={
                items : this.searchItems[selectedItem],
                quantity : this.quantity
            }
            this.$store.commit('addToCart',cartItem);
            this.$toast.success(`${this.searchItems[selectedItem].name} added to cart`);
        }
    },
    updated(){
        // this.getSearchedProduct()
    },
    mounted(){
        this.productSearch = this.$store.state.productSearch
        this.getSearchedProduct()
        Swiper.use(Autoplay);

        const swiper = new Swiper('.swiper',{
            loop:true,
            direction: 'horizontal',
            slidesPerView: 1,
            modules:[Autoplay],
            speed:700,
            autoplay:{
                delay: 3000,
                disableOnInteraction:false,
                pauseOnMouseEnter:true,
                el:'.swiper-slide',
            },
            on: {
                init() {
                this.el.addEventListener('mouseenter', () => {
                    this.autoplay.stop();
                });

                this.el.addEventListener('mouseleave', () => {
                    this.autoplay.start();
                });
                }
            },            
        })
        swiper.autoplay.start();
    },
}

</script>