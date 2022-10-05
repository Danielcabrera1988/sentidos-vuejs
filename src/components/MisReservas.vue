<template>
  <div>
    <h1>Mis Reservas - ESTAMOS TRABAJANDO EN ELLO</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const drawer = ref(false);
    const items = [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" },
    ];

    return {
      items,
      drawer,
    };
  },
});
</script>

<style scoped>
@import "@/assets/Styles/StyleMisReservas";
</style>
