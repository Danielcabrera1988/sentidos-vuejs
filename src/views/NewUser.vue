<template>
  <div class="padding-navbar">
    <NewUser />
  </div>
</template>

<script>
import NewUser from "../components/NewUser.vue";
import { defineComponent, onMounted } from "vue";
import ScrollReveal from 'scrollreveal'
export default defineComponent({
  components: { NewUser },
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".padding-navbar", { delay: 200, reset: true });
    });
  },
});
</script>
