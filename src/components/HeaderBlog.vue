<template>
  <div class="blog__container">
    <h1>Seccion Blog</h1>
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import ScrollReveal from "scrollreveal";
export default defineComponent({
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".blog__container", { delay: 200 });
    });
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleBlog.css";
</style>