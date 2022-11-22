<template>
  <nav class="nav__main">
    <div class="nav__title">Sentidos</div>

    <v-btn class="toggle__btn" @click="toggleBtn" style="color: black"
      ><v-icon>mdi-menu</v-icon></v-btn
    >

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
          <router-link to="/Contacto">Contacto</router-link>
        </li>
        <li v-if="!user">
          <router-link to="/login">Ingresar</router-link>
        </li>
        <li v-if="!user">
          <router-link to="/singin">Registrarse</router-link>
        </li>
        <li v-if="user" @click="show" class="mdi mdi-view-list">
          {{ user }}
          <v-navigation-drawer
            v-model="drawer"
            location="right"
            style="background-color: #2f3640"
            :temporary="true"
          >
            <v-list-item
              prepend-avatar="https://randomuser.me/api/portraits/men/7.jpg"
              :title="user.username"
              color="white"
            ></v-list-item>

            <v-divider></v-divider>

            <v-list density="compact" nav>
              <v-list-item
                prepend-icon="mdi-view-dashboard"
                to="/misreservas"
                title="Mis Reservas"
                color="goldenrod"
              ></v-list-item>
              <v-list-item
                prepend-icon=""
                to="/calification"
                title="Califícanos"
                color="goldenrod"
              ></v-list-item>
              <v-list-item
                prepend-icon="mdi-comment-account"
                to="/contacto"
                title="Contacto Directo"
                color="goldenrod"
              ></v-list-item>
              <v-list-item
                prepend-icon="mdi-star"
                href="https://drive.google.com/file/d/1bQrTAT522C60PvXny4D_L3Bsfr2ry7Uo/view?usp=sharing"
                title="Descarga la App"
                color="goldenrod"
                target="_blank"
              ></v-list-item>
            </v-list>
          </v-navigation-drawer>
        </li>
        <li
          class="nav__close"
          style="cursor: pointer"
          @click="cerrarSesion"
          v-if="user"
        >
          <router-link to="/">Cerrar Sesión</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { defineComponent, ref, computed } from "vue";
import { useStore } from "vuex";
export default defineComponent({
  setup() {
    const drawer = ref(false);
    const store = useStore();
    //la función computed esta constantemente analizando si hay cambios para actualizarlos
    const user = computed(() => store.getters["getUsuario"]);
    const show = () => {
      drawer.value = !drawer.value;
    };
    const verificarLocalStorage = () => {
      if (localStorage.getItem("usuario")) {
        store.commit(
          "SET_USUARIO",
          JSON.parse(localStorage.getItem("usuario"))
        );
      }
    };
    verificarLocalStorage();

    const active = ref(false);
    const toggleBtn = () => {
      active.value = !active.value;
    };
    const cerrarSesion = () => {
      store.commit("SET_USUARIO", null);
      localStorage.removeItem("usuario");
      window.location.reload();
    };
    return {
      active,
      user,
      drawer,
      toggleBtn,
      cerrarSesion,
      show,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleNav.css";
</style>
