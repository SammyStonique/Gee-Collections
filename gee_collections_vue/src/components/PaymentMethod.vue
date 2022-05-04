<template>
    <div>
        <b-card
            title="Card Title"
            img src="../assets/img/product-1.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style= "max-width: 20rem;"
            class="mb-2"
        >
            <b-card-text>
            Some quick example text to build on the card title and make up the bulk of the card's content.
            </b-card-text>

            <b-button href="#" variant="primary" class="btn-primary">Go somewhere</b-button>
        </b-card>
    </div>
</template>

<style scoped>
    .mb-2{
        max-width: 20rem;
    }
    .btn-primary{
        border-radius: 5%;
        padding: 5px;
    }
</style>