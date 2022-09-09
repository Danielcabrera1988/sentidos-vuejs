<template>
  <div class="margin__navbar">
    <Header />
    <h1></h1>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Header from "@/components/Header.vue";
export default defineComponent({
  components: { Header },
  setup() {
    //
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>