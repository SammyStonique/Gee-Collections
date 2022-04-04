<template>
    <div class="product-item">
        <div class="product-title">
            <a href="#">{{item.name}}</a>
            <div class="ratting">
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
            </div>
        </div>
        <div class="product-image">
            <a href="product-detail.html">
                <img :src="`${item.image}`" alt="Product Image" class="prod-img">
            </a>
            <div class="product-action">
                <a class="btn" @click="addToCart(index)" title="Add to Cart"><i class="fa fa-cart-plus"></i></a>
                <a href="#" title="Add to Wishlist"><i class="fa fa-heart"></i></a>
                <a href="#" title="View Product Details"><i class="fa fa-search"></i></a>
            </div>
        </div>
        <div class="product-price">
            <h3 class="prod-price"><span>ksh</span>{{Number(item.price).toLocaleString()}}</h3>
            <button class="btn btn-cart" @click="addToCart"><i class="fa fa-shopping-cart"></i>Buy Now</button>
        </div>
    </div>
</template>

<style>
    .prod-img{

        max-width: inherit;
        min-height:275px;
        max-height:275px;
    }
    .prod-price{
        font-size: 16px;
    }
    .btn-cart{
        font-size: 12px;
    }
</style>


<script>
export default {
    props:['item','getProducts','index','addToCart']
}
</script>