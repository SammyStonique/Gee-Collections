<template>
  <div class="home">
    <!-- Main Slider Start -->
    <div class="header">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-3">
            <nav class="navbar bg-light">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link" href="#"><i class="fa fa-home"></i>Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#"
                    ><i class="fa fa-shopping-bag"></i>Best Selling</a
                  >
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#"
                    ><i class="fa fa-plus-square"></i>New Arrivals</a
                  >
                </li>
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
          <div class="col-md-6">
            <div class="swiper">
              <div class="swiper-wrapper">
                <div class="pt-48"></div>
                <div class="swiper-slide">
                  <div class="z-50">
                    <img
                      src="@/assets/img/main1.jpg"
                      alt="Slider Image"
                      style="width: 500px; height: 400px"
                    />
                  </div>
                </div>
                <div class="swiper-slide">
                  <div class="relative">
                    <img
                      src="@/assets/img/main2.jpg"
                      alt="Slider Image"
                      style="width: 500px; height: 400px"
                    />
                  </div>
                  <div class="absolute top-40">
                    <button
                      class="transition ease-in-out delay-150 rounded-full w-20 h-20 hover:-translate-y-1 hover:scale-110 duration-300"
                    >
                      <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
                    </button>
                  </div>
                </div>
                <div class="swiper-slide">
                  <div class="relative">
                    <img
                      src="@/assets/img/main3.jpg"
                      alt="Slider Image"
                      style="width: 500px; height: 400px"
                    />
                  </div>
                  <div class="absolute top-40">
                    <button
                      class="transition ease-in-out delay-150 rounded-full w-20 h-20 hover:-translate-y-1 hover:scale-110 duration-300"
                    >
                      <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="header-img">
              <div class="img-item">
                <img
                  src="@/assets/img/sleeping-net.jpg"
                  style="width: 280px; height: 200px"
                />
                <a class="img-text" href="">
                  <p>
                    Try out our modern sleeping net that come in a wide range of colors
                  </p>
                </a>
              </div>
              <div class="img-item">
                <img
                  src="@/assets/img/coffee-maker.jpg"
                  style="width: 280px; height: 200px"
                />
                <a class="img-text" href="">
                  <p>
                    It's always a good time to have a cup of coffee, we got you covered.
                  </p>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Main Slider End -->

    <!-- Brand Start -->
    <div class="container-fluid-brand">
      <div class="swiper-brand">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <img src="@/assets/img/brand-1.png" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="@/assets/img/brand-2.png" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="@/assets/img/brand-3.png" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="@/assets/img/brand-4.png" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="@/assets/img/brand-5.png" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="@/assets/img/brand-6.png" alt="" />
          </div>
        </div>
      </div>
    </div>
    <!-- Brand End -->

    <!-- Feature Start-->
    <div class="feature">
      <div class="container-fluid">
        <div class="row align-items-center">
          <div class="col-lg-3 col-md-6 feature-col">
            <div class="feature-content">
              <i class="fab fa-cc-mastercard"></i>
              <h2>Secure Payment</h2>
              <p>We offer a wide range of safe and secure payment methods.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 feature-col">
            <div class="feature-content">
              <i class="fa fa-truck"></i>
              <h2>Nationwide Delivery</h2>
              <p>We offer delivery services to all counties at a favourable price.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 feature-col">
            <div class="feature-content">
              <i class="fa fa-sync-alt"></i>
              <h2>30 Days Return</h2>
              <p>We give a 30 days warranty for all our products.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 feature-col">
            <div class="feature-content">
              <i class="fa fa-comments"></i>
              <h2>24/7 Support</h2>
              <p>We have a reliable support team that is at your full disposal.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Feature End-->

    <!-- Category Start-->
    <div class="category">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-3">
            <div class="category-item ch-400">
              <img src="@/assets/img/gee6.jpg" style="width: 400px; height: 420px" />
              <a class="category-name" href="">
                <p>Gold coated serving spoons for you and your guests</p>
              </a>
            </div>
          </div>
          <div class="col-md-3">
            <div class="category-item ch-250">
              <img src="@/assets/img/gee25.jpg" style="width: 450px; height: 300px" />
              <a class="category-name" href="">
                <p>A state of the art amazing rounded wall mirror</p>
              </a>
            </div>
            <div class="category-item ch-150">
              <img src="@/assets/img/category-5.jpg" />
              <a class="category-name" href="">
                <p>Some text goes here that describes the image</p>
              </a>
            </div>
          </div>
          <div class="col-md-3">
            <div class="category-item ch-150">
              <img src="@/assets/img/gee3.jpg" style="width: 400px; height: 150px" />
              <a class="category-name" href="">
                <p>Brand new imported cups and bowls</p>
              </a>
            </div>
            <div class="category-item ch-250">
              <img src="@/assets/img/gee32.jpg" style="width: 450px; height: 300px" />
              <a class="category-name" href="">
                <p>Quality table mats that come in a wide range of colors</p>
              </a>
            </div>
          </div>
          <div class="col-md-3">
            <div class="category-item ch-400">
              <img src="@/assets/img/gee30.jpg" style="width: 400px; height: 400px" />
              <a class="category-name" href="">
                <p>Baby towels printed with their favourite cartoon character</p>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Category End-->

    <!-- Call to Action Start -->
    <div class="call-to-action">
      <div class="container-fluid">
        <div class="row align-items-center">
          <div class="col-md-6">
            <h1>call us for any queries</h1>
          </div>
          <div class="col-md-6">
            <a href="tel:0717423651">+254-717-423-651</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Call to Action End -->

    <!-- Featured Product Start -->
    <div class="featured-product product">
      <div class="container-fluid">
        <div class="section-header">
          <h1>Featured Product</h1>
        </div>
        <div class="swiper-featured">
          <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="(item, index) in items">
              <ProductCard
                :item="item"
                :getProducts="getProducts"
                :index="index"
                :key="item.id"
                :addToCart="addToCart"
                :getProductDetails="getProductDetails"
                :addToWishlist="addToWishlist"
                :buyNow="buyNow"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Featured Product End -->

    <!-- Newsletter Start -->
    <div class="newsletter">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-6">
            <h1>Subscribe Our Newsletter</h1>
          </div>
          <div class="col-md-6">
            <form action="" @submit.prevent="newsSubscription">
              <div class="form">
                <input type="email" placeholder="Enter your email" v-model="newsEmail" />
                <button type="submit">Submit</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Newsletter End -->

    <!-- Recent Product Start -->
    <div class="recent-product product">
      <div class="container-fluid-review-wrapper">
        <div class="section-header">
          <h1>New Arrivals</h1>
        </div>
        <div class="swiper-recent">
          <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="(item, index) in items.slice(0, 6)">
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
        </div>
      </div>
    </div>
    <!-- Recent Product End -->

    <div class="review">
      <div class="container-fluid-review-wrapper">
        <div class="review-slider">
          <div class="swiper-wrapper">
            <div class="swiper-slide review-slider-item">
              <div class="review-img">
                <img
                  src="@/assets/img/sammyb-review.jpg"
                  alt="Image"
                  class="review-img"
                />
              </div>
              <div class="review-text">
                <h2>SammyB</h2>
                <h3>Software engineer</h3>
                <div class="ratting">
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                </div>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae
                  nunc eget leo finibus luctus et vitae lorem
                </p>
              </div>
            </div>
            <div class="swiper-slide review-slider-item">
              <div class="review-img">
                <img src="@/assets/img/mary-review.jpg" alt="Image" class="review-img" />
              </div>
              <div class="review-text">
                <h2>Mary</h2>
                <h3>Financial Analyst</h3>
                <div class="ratting">
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                </div>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae
                  nunc eget leo finibus luctus et vitae lorem
                </p>
              </div>
            </div>
            <div class="swiper-slide review-slider-item">
              <div class="review-img">
                <img src="@/assets/img/mike-review.jpg" alt="Image" class="review-img" />
              </div>
              <div class="review-text">
                <h2>Mike Bavon</h2>
                <h3>C.E.O - Ezen</h3>
                <div class="ratting">
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                  <i class="fa fa-star"></i>
                </div>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae
                  nunc eget leo finibus luctus et vitae lorem
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "@/components/ProductCard.vue";
import { Swiper, Autoplay, Pagination } from "swiper";
import "swiper/scss";
import "swiper/scss/navigation";
export default {
  data() {
    return {
      newsEmail: null,
    };
  },
  components: {
    ProductCard,
    Swiper,
  },
  props: [
    "items",
    "getProducts",
    "addToCart",
    "addToWishlist",
    "getProductDetails",
    "buyNow",
    "subscribedEmails",
    "getSubscribedEmails",
  ],
  methods: {
    newsSubscription() {
      let emailArray = [];
      for (let i = 0; i < this.subscribedEmails.length; i++) {
        emailArray.push(this.subscribedEmails[i].email);
        console.log(emailArray);
      }

      if (emailArray.includes(this.newsEmail)) {
        this.$toast.warning("You're already subscribed", {
          duration: 5000,
          dismissible: true,
        });
      } else {
        let formData = {
          email: this.newsEmail,
        };
        this.axios
          .post("api/v1/newsletter-subscription/", formData)
          .then((response) => {
            console.log(response.data);
            if (response.data != "No email provided") {
              this.$toast.success("You have succesfully subscribed to our newsletter", {
                duration: 5000,
                dismissible: true,
              });
              this.newsEmail = "";
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  mounted() {
    this.getSubscribedEmails();
    this.getProducts();
    Swiper.use(Autoplay, Pagination);
    const swiper = new Swiper(".swiper", {
      direction: "horizontal",
      loop: true,
      speed: 700,
      modules: [Autoplay, Pagination],
      autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
      },
      pagination: {
        el: ".swiper-pagination",
        type: "bullets",
      },
      on: {
        init() {
          this.el.addEventListener("mouseenter", () => {
            this.autoplay.stop();
          });

          this.el.addEventListener("mouseleave", () => {
            this.autoplay.start();
          });
        },
      },
    });
    swiper.autoplay.start();
    const swiper1 = new Swiper(".swiper-brand", {
      direction: "horizontal",
      loop: true,
      slidesPerView: 6,
      spaceBetween: 50,
      // speed: 10000,
      cssMode: "linear",
      modules: [Autoplay],
      autoplay: {
        speed: 200,
        delay: 800,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
        on: {
          init() {
            this.el.addEventListener("mouseenter", () => {
              this.autoplay.stop();
            });

            this.el.addEventListener("mouseleave", () => {
              this.autoplay.start();
            });
          },
        },
      },
    });
    swiper1.autoplay.start();
    const swiper2 = new Swiper(".swiper-featured", {
      direction: "horizontal",
      loop: true,
      slidesPerView: 4,
      spaceBetween: 30,
      speed: 700,
      cssMode: "linear",
      modules: [Autoplay],
      autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
      },
      on: {
        init() {
          this.el.addEventListener("mouseenter", () => {
            this.autoplay.stop();
          });

          this.el.addEventListener("mouseleave", () => {
            this.autoplay.start();
          });
        },
      },
    });
    swiper2.autoplay.start();

    const swiper3 = new Swiper(".swiper-recent", {
      direction: "horizontal",
      loop: true,
      slidesPerView: 4,
      spaceBetween: 30,
      speed: 700,
      cssMode: "linear",
      modules: [Autoplay],
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
      },
      on: {
        init() {
          this.el.addEventListener("mouseenter", () => {
            this.autoplay.stop();
          });

          this.el.addEventListener("mouseleave", () => {
            this.autoplay.start();
          });
        },
      },
    });
    swiper3.autoplay.start();

    const swiper4 = new Swiper(".review-slider", {
      direction: "horizontal",
      loop: true,
      speed: 700,
      slidesPerView: 2,
      spaceBetween: 30,
      modules: [Autoplay],
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
      },
      on: {
        init() {
          this.el.addEventListener("mouseenter", () => {
            this.autoplay.stop();
          });

          this.el.addEventListener("mouseleave", () => {
            this.autoplay.start();
          });
        },
      },
    });
  },
};
</script>

<style scoped>
.container-fluid-brand {
  padding-left: 60px;
  padding-right: 60px;
  background-color: white;
}
.review-img {
  height: 200px;
  width: 200px;
}
.container-fluid-review-wrapper {
  margin-left: 50px;
  margin-right: 50px;
  overflow-x: hidden;
}
.swiper {
  z-index: -1;
}
</style>
