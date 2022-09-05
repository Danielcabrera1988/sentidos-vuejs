<template>
  <div class="padding-navbar">
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
