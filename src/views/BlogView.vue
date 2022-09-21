<template>
  <div>
    <Blog />
  </div>
</template>

<script >
import { defineComponent } from "vue";
import Blog from "@/components/Blog.vue";
export default defineComponent({
  components: { Blog },
  setup() {
    //
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>