<template>
    <div class="products">
        <!-- Breadcrumb Start -->
        <div class="breadcrumb-wrap">
            <div class="container-fluid">
                <ul class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Products</a></li>
                    <li class="breadcrumb-item active">Product List</li>
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
                                        <div class="col-md-4">
                                            <div class="product-search">
                                                <input type="email" value="Search">
                                                <button><i class="fa fa-search"></i></button>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <div class="product-short">
                                                <div class="dropdown">
                                                    <div class="dropdown-toggle" data-toggle="dropdown" style="color:black !important;">Product sort by</div>
                                                    <div class="dropdown-menu dropdown-menu-right">
                                                        <a href="#" class="dropdown-item">Newest</a>
                                                        <a href="#" class="dropdown-item">Popular</a>
                                                        <a href="#" class="dropdown-item">Most sale</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <div class="product-price-range">
                                                <div class="dropdown">
                                                    <div class="dropdown-toggle" data-toggle="dropdown" style="color:black !important;">Product price range</div>
                                                    <div class="dropdown-menu dropdown-menu-right">
                                                        <a href="#" class="dropdown-item">$0 to $50</a>
                                                        <a href="#" class="dropdown-item">$51 to $100</a>
                                                        <a href="#" class="dropdown-item">$101 to $150</a>
                                                        <a href="#" class="dropdown-item">$151 to $200</a>
                                                        <a href="#" class="dropdown-item">$201 to $250</a>
                                                        <a href="#" class="dropdown-item">$251 to $300</a>
                                                        <a href="#" class="dropdown-item">$301 to $350</a>
                                                        <a href="#" class="dropdown-item">$351 to $400</a>
                                                        <a href="#" class="dropdown-item">$401 to $450</a>
                                                        <a href="#" class="dropdown-item">$451 to $500</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">   
                                <div class="col-md-4" v-for="(item,index) in pageOfItems">                                       
                                    <ProductCard
                                    :item="item"
                                    :getProducts="getProducts"
                                    :key="item.id"
                                    :index="index"
                                    :addToCart="addToCart"
                                    :getProductDetails="getProductDetails"
                                    :addToWishlist="addToWishlist"
                                    :buyNow="buyNow"
                                    />
                                    </div>
                        </div>
                        <Pagination
                        :items="exampleItems"
                        @changePage="onChangePage"
                        :pageSize=6
                        />
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
            exampleItems: [],
            pageOfItems: []
        }
    },
    methods:{
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        }
    },
    mounted(){
        this.getProducts();
        this.exampleItems = this.items
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
    }
}

</script>