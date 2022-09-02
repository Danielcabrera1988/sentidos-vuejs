<template>
  <div class="padding-navbar">
    <HeaderBlog />
  </div>
</template>

<script >
import { defineComponent, onMounted } from "vue";
import HeaderBlog from "@/components/HeaderBlog.vue";
import ScrollReveal from "scrollreveal";
export default defineComponent({
  components: { HeaderBlog },
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".padding-navbar", { delay: 200, reset: true });
    });
  },
});
</script>