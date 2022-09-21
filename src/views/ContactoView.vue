<template>
    <div>
        <Contacto/>
    </div>
</template>

<script>
    import { defineComponent } from "vue";
    import Contacto from "@/components/Contacto.vue";
    export default defineComponent({
      components: { Contacto },
      setup() {
        //
      },
    });
    </script>
    <style scoped>
    @import "../assets/Styles/StyleContacto.css";
    </style>