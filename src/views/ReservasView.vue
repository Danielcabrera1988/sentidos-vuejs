<template>
  <div>
    <FormularioReserva />
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import ScrollReveal from 'scrollreveal'
import FormularioReserva from "../components/FormularioReserva.vue";

export default defineComponent({
  components: { FormularioReserva },
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".padding-navbar", { delay: 200, reset: true });
    });
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleFormReserve.css";
</style>