<template>
    <div class="margin__navbar">
        <Comentario/>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import Comentario from '../components/Comentario.vue'

export default defineComponent({
    components: {Comentario},
    setup() {
        //
    },
})
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>