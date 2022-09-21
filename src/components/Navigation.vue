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
          <router-link to="/Contacto">Contacto</router-link>
        </li>
        <li  v-if="!user">
          <router-link to="/login">Login</router-link>
        </li>
        <li v-if="!user">
          <router-link to="/singin">Sing in</router-link>
        </li>
        <li v-if="user">
          <router-link to="/">{{user.username}}</router-link>
        </li>
        <li style="cursor:pointer;" @click="cerrarSesion" v-if="user">
           Cerrar
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { defineComponent, ref,computed } from "vue";
import {useStore} from 'vuex';
export default defineComponent({
  setup() {
    
    const store = useStore()
    //la función computed esta constantemente analizando si hay cambios par aactualizarlos
    const user = computed(() => (store.getters['getUsuario']))

    const  verificarLocalStorage = () =>{
      if (localStorage.getItem('usuario')) {
        store.commit('SET_USUARIO',{username:JSON.parse(localStorage.getItem('usuario')),password:'*****'})
      }
    }

    verificarLocalStorage()

    const active = ref(false);
    const toggleBtn = () => {
      active.value = !active.value;
    };
    const cerrarSesion = ()=>{
      //commit se usa para llamar a las mutaciones dentro del store
      store.commit('SET_USUARIO',null)
      localStorage.removeItem('usuario')
    }
    return {
      active,
      toggleBtn,
      user,
      cerrarSesion
    };
  },
});
</script>




<style  scoped>
@import "../assets/Styles/StyleNav.css";
</style>s