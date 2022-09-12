<template>
  <div>
    <Login />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Login from "@/components/Login.vue";
export default defineComponent({
  components: {
    Login,
  },
  setup() {
    //
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>