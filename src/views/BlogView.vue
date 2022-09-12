<template>
  <div>
    <HeaderBlog />
  </div>
</template>

<script >
import { defineComponent } from "vue";
import HeaderBlog from "@/components/HeaderBlog.vue";
export default defineComponent({
  components: { HeaderBlog },
  setup() {
    //
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>