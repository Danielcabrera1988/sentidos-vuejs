<template>
  <div>
    <Header />
    <h1></h1>
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import Header from "@/components/Header.vue";
import ScrollReveal from "scrollreveal";
export default defineComponent({
  components: { Header },
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".padding-navbar", { delay: 200, reset: true });
    });
  },
});
</script>
