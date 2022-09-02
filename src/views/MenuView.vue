<template>
  <div>
    <Menu />
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import Menu from "@/components/Menu.vue";
import ScrollReveal from 'scrollreveal'
export default defineComponent({
  components: { Menu },
  setup() {
     onMounted(() => {
      ScrollReveal().reveal(".padding-navbar", { delay: 200, reset: true });
    });
  },
});
</script>