<template>
  <div class="autocomplete">
    <input
      v-model="search"
      @input="onChange"
      @keydown.down="onArrowDown"
      @keydown.up="onArrowUp"
      @keydown.enter="onEnter"
      type="text"
      placeholder="Search"
    />
    <ul
      class="absolute w-full shadow shadow-gray-500 autocomplete-results"
      v-show="isOpen"
    >
      <li
        class="autocomplete-result"
        v-for="(result, i) in results"
        :key="i"
        @click="setResult(result)"
        :class="{ 'is-active': i === arrowCounter }"
      >
        {{ result }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SearchAutocomplete",
  props: {
    items: {
      type: Array,
      required: false,
      default: () => [],
    },
  },
  data() {
    return {
      search: "",
      results: [],
      isOpen: false,
      arrowCounter: -1,
    };
  },
  beforeMount() {
    this.search = this.$store.state.productSearch;
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  updated() {
    this.$nextTick(() => {
      this.$store.state.productSearch = this.search;
      this.$store.commit("searchForItem");
    });
  },
  destroyed() {
    document.removeEventListener("click", this.handleClickOutside);
  },
  methods: {
    filterResults() {
      let newArray = [];
      for (let i = 0; i < this.items.length; i++) {
        newArray.push(this.items[i].name);
      }
      this.results = newArray.filter(
        (item) => item.toLowerCase().indexOf(this.search.toLowerCase()) > -1
      );
    },
    onChange() {
      this.filterResults();
      this.isOpen = true;
      this.$store.state.isProductSearched = false;
    },
    setResult(result) {
      this.search = result;
      this.isOpen = false;
      this.$store.state.isProductSearched = true;
      // this.$store.state.productSearch = result;
      // this.$tore.commit("searchForItem");
      this.$router.push("/products");
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.arrowCounter = -1;
        this.isOpen = false;
      }
    },
    onArrowDown() {
      if (this.arrowCounter < this.results.length) {
        this.arrowCounter = this.arrowCounter + 1;
      }
    },
    onArrowUp() {
      if (this.arrowCounter > 0) {
        this.arrowCounter = this.arrowCounter - 1;
      }
    },
    onEnter() {
      this.search = this.results[this.arrowCounter];
      this.arrowCounter = -1;
      this.isOpen = false;
      this.$store.state.isProductSearched = true;
    },
  },
};
</script>

<style>
/* .autocomplete {
  width: 100%;
} */

.autocomplete-results {
  padding: 0;
  margin: 0;
  border: 1px solid #eeeeee;
  height: 120px;
  min-height: 1em;
  max-height: 12em;
  overflow: auto;
  display: block;
}

.autocomplete-result {
  list-style: none;
  text-align: left;
  padding: 4px 2px;
  cursor: pointer;
  /* background-color: #ff6f61; */
  background-color: white;
  z-index: 1000;
}

.autocomplete-result.is-active,
.autocomplete-result:hover {
  background-color: #4aae9b;
  color: white;
}
</style>
