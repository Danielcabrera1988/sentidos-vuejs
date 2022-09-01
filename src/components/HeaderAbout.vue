<template>
  <div class="about__container">
    <h1>Seccion Nosotros</h1>
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import ScrollReveal from "scrollreveal";
export default defineComponent({
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".about__container", { delay: 200 });
    });
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleAbout.css";
</style>