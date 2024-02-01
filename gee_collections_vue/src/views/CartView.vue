<template>
  <div class="cart">
    <!-- Breadcrumb Start -->
    <div class="breadcrumb-wrap">
      <div class="container-fluid">
        <ul class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">Home</a></li>
          <li class="breadcrumb-item"><a href="#">Products</a></li>
          <li class="breadcrumb-item active">Cart</li>
        </ul>
      </div>
    </div>
    <!-- Breadcrumb End -->
    <!-- Cart Start -->
    <div class="cart-page">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8">
            <div class="cart-page-inner">
              <div class="table-responsive">
                <table class="table table-bordered">
                  <thead class="thead-dark">
                    <tr>
                      <th>Product</th>
                      <th>Price</th>
                      <th>Quantity</th>
                      <th>Total</th>
                      <th>Remove</th>
                    </tr>
                  </thead>
                  <tbody class="align-middle">
                    <tr v-for="(prod, index) in pageOfItems" :key="index">
                      <td>
                        <div class="img">
                          <a href="#"><img :src="`${prod.items.image}`" alt="Image" /></a>
                          <p>{{ prod.items.name }}</p>
                        </div>
                      </td>
                      <td>{{ Number(prod.items.price).toLocaleString() }}</td>
                      <td>
                        <div class="qty">
                          <button class="btn-minus" @click="decrementQuantity(index)">
                            <i class="fa fa-minus"></i>
                          </button>
                          <input type="text" :value="`${prod.quantity}`" />
                          <button class="btn-plus" @click="incrementQuantity(index)">
                            <i class="fa fa-plus"></i>
                          </button>
                        </div>
                      </td>
                      <td>{{ Number(prodCartItemTotal[index]).toLocaleString() }}</td>
                      <td>
                        <button @click="removeFromCart(index)">
                          <i class="fa fa-trash"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <p class="empty-cart" v-if="!Object.keys(cart).length">
                  <span class="emoji" role="img" aria-label="">😭</span><br /><em
                    class="empty-cart-message"
                    >Ooops,No items in cart</em
                  >
                </p>
                <!-- PAGINATION -->
                <div class="row">
                  <Pagination :items="cart" @changePage="onChangePage" :pageSize="5" />
                </div>
                <!-- pagination end -->
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="cart-page-inner">
              <div class="row">
                <div class="col-md-12">
                  <div class="coupon">
                    <input type="text" placeholder="Coupon Code" v-model="coupon_code" />
                    <button @click="applyCouponCode(coupon_code)">Apply Code</button>
                  </div>
                </div>
                <div class="col-md-12">
                  <div class="cart-summary">
                    <div class="cart-content">
                      <h1>Cart Summary</h1>
                      <p class="mb-4">
                        Sub Total<span
                          >ksh. {{ Number(cartSubTotal).toLocaleString() }}</span
                        >
                      </p>
                      <p class="mb-4">
                        Delivery Fee(varies)<span
                          >ksh. {{ Number(shippingCost).toLocaleString() }}</span
                        >
                      </p>
                      <p class="mb-2">
                        Coupon Applied<span
                          >ksh. {{ Number(coupon_applied).toLocaleString() }}</span
                        >
                      </p>
                      <h2>
                        Grand Total<span>{{
                          Number(cartTotal).toLocaleString()
                        }}</span>
                      </h2>
                    </div>
                    <div class="cart-btn">
                      <button>
                        <router-link to="/products" class="check-btn"
                          >Update Cart</router-link
                        >
                      </button>
                      <button v-if="cart.length">
                        <router-link to="/checkout" class="checkout"
                          >Checkout</router-link
                        >
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Cart End -->
  </div>
</template>

<script>
import swal from "sweetalert";
import Pagination from "@/components/Pagination.vue";

export default {
  data() {
    return {
      myEmoji: "\u{1F62D}",
      pageOfItems: [],
      // couponArr : [],
      coupon_code: "",
      // couponCodes: [],
      // coupon_amount: 0,
      // cartTotal: 0,
    };
  },
  props: [
    "cart",
    "items",
    "cartGrandTotal",
    "cartItemTotal",
    "cartSubTotal",
    "shippingCost",
    "couponArr",
    "couponCodes",
    "coupon_applied",
    "cartTotal",
    "applyCouponCode"
  ],
  components: {
    Pagination,
  },
  computed: {
    prodCartItemTotal() {
      let itemTotal = [];
      for (let i = 0; i < this.pageOfItems.length; i++) {
        let lineTotal = (
          this.pageOfItems[i].quantity * this.pageOfItems[i].items.price
        ).toFixed(2);
        itemTotal.push(lineTotal);
      }
      return itemTotal;
    },
  },
  methods: {
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    incrementQuantity() {
      let selectedItemQuantity = arguments[0];
      this.pageOfItems[selectedItemQuantity].quantity += 1;
      this.updateCart();
    },
    decrementQuantity() {
      let selectedItemQuantity = arguments[0];
      if (this.pageOfItems[selectedItemQuantity].quantity >= 2) {
        this.pageOfItems[selectedItemQuantity].quantity -= 1;
      } else {
        this.$store.commit("removeFromCart", selectedItemQuantity);
        this.$store.commit("reloadingPage");
      }
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart() {
      let selectedItem = arguments[0];
      swal({
        title: "Are you sure?",
        text: `Do you wish to remove ${this.pageOfItems[selectedItem].items.name} from your cart?`,
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((willDelete) => {
        if (willDelete) {
          this.$store.commit("removeFromCart", selectedItem);
          swal("Poof! Item removed succesfully!", {
            icon: "success",
          });
          this.$store.commit("reloadingPage");
        } else {
          swal("Your item is safely in the cart!");
        }
      });
    },
    
  },
  mounted() {},
};
</script>

<style scoped>
.empty-cart {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  margin: 20px;
}
.emoji {
  font-size: 36px;
  font-style: normal;
}
.checkout {
  color: white;
}
.checkout:hover {
  color: #ff6f61;
}
</style>
