<template>
  <div class="padding-navbar">
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