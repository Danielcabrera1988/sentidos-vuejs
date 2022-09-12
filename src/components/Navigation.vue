<template>
  <nav class="nav__main">
    <div class="nav__title">Sentidos</div>

    <v-btn class="toggle__btn" @click="toggleBtn" style="color: black"><v-icon>mdi-menu</v-icon></v-btn>

    <div class="nav__links" :class="active ? 'active' : ''">
      <!-- NavBar -->
      <ul>
        <li>
          <router-link to="/">Home</router-link>
        </li>
        <li>
          <router-link to="/menu">Menu</router-link>
        </li>
        <li>
          <router-link to="/reservas">Reservas</router-link>
        </li>
        <li>
          <router-link to="/blog">Blog</router-link>
        </li>
        <li>
          <router-link to="/login">Login</router-link>
        </li>
        <li>
          <router-link to="/newUser">Sing in</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {

    const active = ref(false);
    const toggleBtn = () => {
      active.value = !active.value;
    };

    return {
      active,
      toggleBtn,
    };
  },
});
</script>




<style  scoped>
@import "../assets/Styles/StyleNav.css";
</style>s