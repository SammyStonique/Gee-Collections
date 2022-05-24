<template>
    <div class="section"> 
        <div class="pull-right">
            <div class="pagination">
                <ul>
                    <!-- <li>
                        <a
                            class="btn"
                            @click.prevent="onClickFirstPage" 
                            :disabled="isInFirstPage"
                        >
                        First
                        </a>
                    </li> -->
                    <li>
                        <a
                            class="btn"
                            @click="onClickPreviousPage" 
                            :disabled="isInFirstPage"
                        >
                        Prev
                        </a>
                    </li>

                    <!-- visible as start -->
                    <li v-for="page in pages" :key="page.name">
                        <a
                            class="btn"
                            @click="onClickPage(page.name)"
                            :disabled="page.isDisabled"
                        >
                        {{page.name}}
                        </a>
                    </li>
                    <!-- visible as end -->

                    <li>
                        <a
                            class="btn"
                            @click="onClickNextPage" 
                            :disabled="isInLastPage"
                        >
                        Next
                        </a>
                    </li>
                    <!-- <li>
                        <a
                            class="btn"
                            @click="onClickLastPage" 
                            :disabled="isInLastPage"
                        >
                        Last
                        </a>
                    </li> -->
                </ul>
            </div>
        </div>                
    </div>
</template>

<script>
export default {
    props: {
        maxVisibleButtons: {
            type: Number,
            required: false,
            default: 5
        },
        totalPages: {
            type: Number,
            required: true,
        },
        totalItems: {
            type: Number,
            required: true
        },
        perPage: {
            type: Number,
            required: true,
        },
        currentPage: {
            type: Number,
            required: true
        }
    },

    data() 
    {
        return {
            
        }
    },

    computed: {
        startPage() 
        {
            if(this.currentPage === 1) // while on first page
            {
                return 1;
            }
            
            if(this.currentPage === this.totalPages) // while on last page
            {
                return this.totalPages - this.maxVisibleButtons + 1;
                // const start = this.totalPages - (this.maxVisibleButtons - 1);

                // if(start === 0) 
                // {
                //     return 1;
                // }
                // else 
                // {
                //     return start;
                // }
            }

            return this.currentPage - 1; // while in between fisrt and last
        },

        endPage() 
        {
            return Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);
        },

        pages() 
        {
            const pageRange = [];
            // Math.min(this.startPage + this.maxVisiblePages - 1, this.totalPages) / this.endPage;

            for(let i = this.startPage; i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages); i++)
            {
                pageRange.push({
                    name: i,
                    isDisabled: i === this.currentPage
                });
            }

            return pageRange;
        },

        // for event listeners
        isInFirstPage() 
        {
            return this.currentPage === 1;
        },
        isInLastPage() 
        {
            return this.currentPage === this.totalPages;
        }
    },

    methods: {
        onClickFirstPage() 
        {
            this.$emit('page-changed', 1);
        },
        onClickPreviousPage() 
        {
            this.$emit('page-changed', this.currentPage - 1);
        },
        onClickPage(page) 
        {
            this.$emit('page-changed', page);
        },
        onClickNextPage() 
        {
            this.$emit('page-changed', this.currentPage + 1);
        },
        onClickLastPage() 
        {
            this.$emit('page-changed', this.totalPages);
        },
    },
    mounted() 
    {
        // console.log(`on pages ::: pages are ::: ${this.totalPages}`)
    },

    updated() 
    {
        
    }

}
</script>