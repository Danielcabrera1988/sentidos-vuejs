<template>
  <v-app class="general">
    <NavBar />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import { defineComponent } from "vue";
import Footer from "./components/Footer.vue";
import NavBar from "./components/NavBar.vue";

export default defineComponent({
  components: { Footer, NavBar },
  name: "App",
  data() {
    return {
      //
    };
  },
});
</script>
<style>
@import "../src/assets/Styles/StyleGral.css";
</style>
