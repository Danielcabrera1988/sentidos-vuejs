<template>
  <div>
    <NewUser />
  </div>
</template>

<script>
import NewUser from "../components/NewUser.vue";
import { defineComponent  } from "vue";
export default defineComponent({
  components: { NewUser },
  setup() {
    //
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>