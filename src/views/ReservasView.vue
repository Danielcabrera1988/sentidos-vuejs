<template>
  <div class="padding-navbar">
    <FormularioReserva />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import FormularioReserva from "../components/FormularioReserva.vue";

export default defineComponent({
  components: { FormularioReserva },
  setup() {
    //
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleFormReserve.css";
</style>