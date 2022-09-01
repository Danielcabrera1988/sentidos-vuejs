<!--Acá se arma toda la magia-->
<template>
  <v-app class="general">
    <Navigation />
    <v-main  >
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Footer from "./components/Footer.vue";
import Navigation from "./components/Navigation.vue";


export default defineComponent({
  components: { Footer, Navigation},
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
