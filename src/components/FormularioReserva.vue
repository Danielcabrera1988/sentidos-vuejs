<template>
  <div class="reserva__main">
    <h1>Formulario Reservas</h1>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import ScrollReveal from "scrollreveal";

export default {
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".reserva__main", { delay: 200 });
    });
  },
};
</script>

<style scoped>
@import '../assets/Styles/StyleFormReserve.css'
</style>
