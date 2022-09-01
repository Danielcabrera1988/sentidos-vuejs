<template>
  <div class="padding-navbar">
    <Menu />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Menu from "@/components/Menu.vue";

export default defineComponent({
  components: { Menu },
  setup() {
    //
  },
});
</script>