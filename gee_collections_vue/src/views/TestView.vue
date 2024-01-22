<template>
    <div class="name">
        <button @click="decreaseCount()" class="rounded border bg-slate-500 text-lg p-3 text-white">-</button>
        <p>{{ count }}</p>
        <button @click="increaseCount()" class="rounded border bg-slate-500 text-lg p-3 text-white">+</button>
    </div>
</template>
 
<script>
import { ref} from "vue"

export default{
    setup(){
        const count = ref(0);
        const increaseCount = ()=> count.value++;
        function decreaseCount(){
            count.value--;
        }
        return{
            count, increaseCount, decreaseCount
        }
    },
    
}

</script>

<style>
</style>