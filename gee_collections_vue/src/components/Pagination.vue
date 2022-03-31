<template>
    <div>
        <!-- Pagination Start -->
        <div class="col-md-12">
            <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center">
                    <li class="page-item">
                        <a class="page-link" @click="onClickFirstPage" :disabled="isInFirstPage" href="#">First</a>
                    </li>
                    <li class="page-item disabled">
                        <a class="page-link" @click="onClickPreviousPage" :disabled="isInFirstPage" href="#" tabindex="-1">Previous</a>
                    </li>
                    <li class="page-item" v-for="page in pages" :key="page.name">
                        <a class="page-link" type="button" @click="onClickPage(page.name)" :disabled="page.isDisabled" :class="{ active: isPageActive(page.name) }">{{ page.name }}</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" @click="onClickNextPage" :disabled="isInLastPage" href="#">Next</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" @click="onClickLastPage" :disabled="isInLastPage" href="#">Last</a>
                    </li>
                </ul>
            </nav>
        </div>
        <!-- Pagination Start -->
    </div>
</template>

<script>
export default {
  props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 3
    },    
    totalPages: {
      type: Number,
      required: true
    },
    perPage: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    startPage() {
      // When on the first page
      if (this.currentPage === 1) {
        return 1;
      }
      // When on the last page
      if (this.currentPage === this.totalPages) {
        return this.totalPages - this.maxVisibleButtons;
      }
      // When inbetween
      return this.currentPage - 1;
    },
    pages() {
      const range = [];
      for (let i = this.startPage;i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);i++) {
        range.push({
          name: i,
          isDisabled: i === this.currentPage
        });
      }
      return range;
    },
    isInFirstPage() {
      return this.currentPage === 1;
    },
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
  },
  methods: {
    onClickFirstPage() {
      this.$emit('pagechanged', 1);
    },
    onClickPreviousPage() {
      this.$emit('pagechanged', this.currentPage - 1);
    },
    onClickPage(page) {
      this.$emit('pagechanged', page);
    },
    onClickNextPage() {
      this.$emit('pagechanged', this.currentPage + 1);
    },
    onClickLastPage() {
      this.$emit('pagechanged', this.totalPages);
    },
    isPageActive(page) {
      return this.currentPage === page;
    }
  }
};
</script>