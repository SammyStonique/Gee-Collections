<template>
  <div class="product-detail">
    <!-- Breadcrumb Start -->
    <div class="breadcrumb-wrap">
      <div class="container-fluid">
        <ul class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">Home</a></li>
          <li class="breadcrumb-item"><a href="#">Products</a></li>
          <li class="breadcrumb-item active">Product Detail</li>
        </ul>
      </div>
    </div>
    <!-- Breadcrumb End -->

    <!-- Product Detail Start -->
    <div class="product-detail">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8">
            <div class="product-detail-top">
              <div class="row align-items-center">
                <div class="col-md-5">
                  <div class="product-slider-single normal-slider">
                    <img :src="`${detailProducts.image}`" alt="Product Image" />
                  </div>
                </div>
                <div class="col-md-7">
                  <div class="product-content">
                    <div class="title">
                      <h2>{{ detailProducts.name }}</h2>
                    </div>
                    <div class="ratting">
                      <i class="fa fa-star"></i>
                      <i class="fa fa-star"></i>
                      <i class="fa fa-star"></i>
                      <i class="fa fa-star"></i>
                      <i class="fa fa-star"></i>
                    </div>
                    <div class="price">
                      <h4>Price:</h4>
                      <p>
                        ksh. {{ Number(detailProducts.price).toLocaleString() }}
                        <span
                          >ksh. {{ Number(productOriginalPrice).toLocaleString() }}</span
                        >
                      </p>
                    </div>
                    <div class="quantity">
                      <h4>Quantity:</h4>
                      <div class="qty">
                        <button class="btn-minus" @click="decrementQuantity()">
                          <i class="fa fa-minus"></i>
                        </button>
                        <input type="text" v-model="quantity" />
                        <button class="btn-plus" @click="incrementQuantity()">
                          <i class="fa fa-plus"></i>
                        </button>
                      </div>
                    </div>
                    <div class="p-size">
                      <h4>Size:</h4>
                      <div class="btn-group btn-group-sm">
                        <button type="button" class="btn">S</button>
                        <button type="button" class="btn">M</button>
                        <button type="button" class="btn">L</button>
                        <button type="button" class="btn">XL</button>
                      </div>
                    </div>
                    <div class="p-color">
                      <h4>Color:</h4>
                      <div class="btn-group btn-group-sm">
                        <button type="button" class="btn">White</button>
                        <button type="button" class="btn">Black</button>
                        <button type="button" class="btn">Blue</button>
                      </div>
                    </div>
                    <div class="action">
                      <a class="btn details-add-to-cart-btn" @click="detailsAddToCart()"
                        ><i class="fa fa-shopping-cart"></i>Add to Cart</a
                      >
                      <a class="btn details-add-to-cart-btn" @click="detailsBuyNow()"
                        ><i class="fa fa-shopping-bag"></i>Buy Now</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="row product-detail-bottom">
              <div class="col-lg-12">
                <ul class="nav nav-pills nav-justified">
                  <li class="nav-item">
                    <a class="nav-link active" data-toggle="pill" href="#description"
                      >Description</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" data-toggle="pill" href="#specification"
                      >Specification</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" data-toggle="pill" href="#reviews">Reviews (1)</a>
                  </li>
                </ul>

                <div class="tab-content">
                  <div id="description" class="container tab-pane active">
                    <h4>Product description</h4>
                    <p>{{ detailProducts.description }}</p>
                  </div>
                  <div id="specification" class="container tab-pane fade">
                    <h4>Product specification</h4>
                    <ul>
                      <li>Lorem ipsum dolor sit amet</li>
                      <li>Lorem ipsum dolor sit amet</li>
                      <li>Lorem ipsum dolor sit amet</li>
                      <li>Lorem ipsum dolor sit amet</li>
                      <li>Lorem ipsum dolor sit amet</li>
                    </ul>
                  </div>
                  <div id="reviews" class="container tab-pane fade">
                    <div class="reviews-submitted">
                      <div class="reviewer">
                        Phasellus Gravida - <span>01 Jan 2020</span>
                      </div>
                      <div class="ratting">
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                      </div>
                      <p>
                        Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                        accusantium doloremque laudantium, totam rem aperiam.
                      </p>
                    </div>
                    <div class="reviews-submit">
                      <h4>Give your Review:</h4>
                      <div class="ratting">
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                      </div>
                      <div class="row form">
                        <div class="col-sm-6">
                          <input type="text" placeholder="Name" />
                        </div>
                        <div class="col-sm-6">
                          <input type="email" placeholder="Email" />
                        </div>
                        <div class="col-sm-12">
                          <textarea placeholder="Review"></textarea>
                        </div>
                        <div class="col-sm-12">
                          <button>Submit</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="product">
              <div class="section-header">
                <h1>Related Products</h1>
              </div>
              <div class="related-products">
                <div class="swiper-related">
                  <div class="swiper-wrapper">
                    <div class="swiper-slide" v-for="(item, index) in items.slice(3, 6)">
                      <ProductCard
                        :item="item"
                        :getProducts="getProducts"
                        :key="item.id"
                        :index="index"
                        :addToCart="addToCart"
                        :getProductDetails="getProductDetails"
                        :buyNow="buyNow"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Side Bar Start -->
          <div class="col-lg-4 sidebar">
            <div class="sidebar-widget category">
              <h2 class="title">Category</h2>
              <nav class="navbar bg-light">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <a class="nav-link" href="#"
                      ><i class="fa fa-female"></i>Fashion & Beauty</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#"
                      ><i class="fa fa-child"></i>Kids & Babies Clothes</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#"
                      ><i class="fa fa-tshirt"></i>Men & Women Clothes</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#"
                      ><i class="fa fa-mobile-alt"></i>Gadgets & Accessories</a
                    >
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#"
                      ><i class="fa fa-microchip"></i>Electronics & Accessories</a
                    >
                  </li>
                </ul>
              </nav>
            </div>
            <div class="sidebar-widget widget-slider">
              <div class="swiper">
                <div class="swiper-wrapper">
                  <div class="swiper-slide" v-for="(item, index) in items.slice(0, 3)">
                    <ProductCard
                      :item="item"
                      :getProducts="getProducts"
                      :key="item.id"
                      :index="index"
                      :addToCart="addToCart"
                      :addToWishlist="addToWishlist"
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

            <div class="sidebar-widget tag">
              <h2 class="title">Tags Cloud</h2>
              <a href="#">Lorem ipsum</a>
              <a href="#">Vivamus</a>
              <a href="#">Phasellus</a>
              <a href="#">pulvinar</a>
              <a href="#">Curabitur</a>
              <a href="#">Fusce</a>
              <a href="#">Sem quis</a>
              <a href="#">Mollis metus</a>
              <a href="#">Sit amet</a>
              <a href="#">Vel posuere</a>
              <a href="#">orci luctus</a>
              <a href="#">Nam lorem</a>
            </div>
          </div>
          <!-- Side Bar End -->
        </div>
      </div>
    </div>
    <!-- Product Detail End -->
  </div>
</template>

<script>
import ProductCard from "@/components/ProductCard.vue";
import { Swiper, Autoplay } from "swiper";
import "swiper/scss";

export default {
  props: [
    "items",
    "index",
    "getProducts",
    "addToCart",
    "getProductDetails",
    "addToWishlist",
    "productDetails",
    "buyNow",
  ],
  components: {
    ProductCard,
    Swiper,
  },
  data() {
    return {
      quantity: 1,
      detailProducts: [],
    };
  },
  computed: {
    productOriginalPrice() {
      return this.detailProducts.price - -200;
    },
  },
  methods: {
    incrementQuantity() {
      this.quantity += 1;
    },
    decrementQuantity() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      } else {
        if (this.quantity > 1) {
          this.quantity -= 1;
        }
      }
    },
    detailsAddToCart() {
      //Getting the index of the items in the cart
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
      const cartItem = {
        items: this.productDetails,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", cartItem);
      this.$toast.success(`${this.productDetails.name} added to cart`);
    },
    detailsBuyNow() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const cartItem = {
        items: this.productDetails,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", cartItem);
      this.$router.push("/checkout");
      this.scrollToTop();
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
  },
  beforeMount() {},
  mounted() {
    this.getProducts();
    this.quantity = 1;
    let newVar = JSON.parse(localStorage.getItem("detailProducts"));
    let anotherVar = [];
    anotherVar.push(newVar[0]);
    this.detailProducts = anotherVar[0];

    Swiper.use(Autoplay);
    //Swiper for additional products
    const swiper = new Swiper(".swiper", {
      direction: "horizontal",
      loop: true,
      slidesPerView: 1,
      speed: 700,
      modules: [Autoplay],
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
    });
    swiper.autoplay.start();
    //Swiper for related products
    const swiper1 = new Swiper(".swiper-related", {
      direction: "horizontal",
      loop: false,
      slidesPerView: 3,
      spaceBetween: 20,
      speed: 700,
      modules: [Autoplay],
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
    });
    swiper1.autoplay.start();
  },
};
</script>

<style scoped>
.product-detail .product-slider-single-nav {
  margin: 15px 30px 30px 30px;
  border: 3px double #ff6f61;
}
.product-detail-slider {
  height: 421px;
}
.details-add-to-cart-btn {
  color: #ff6f61;
}
.details-add-to-cart-btn:hover {
  color: white;
}
</style>
