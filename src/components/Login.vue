<template>
  <div class="login__container">
    <h1 class="animate__animated animate__zoomIn">Sentidos</h1>
    <h3 class="animate__animated animate__zoomIn">Restaurante y casa de te</h3>
    <div class="login__form">
      <v-form ref="form" v-on:submit.prevent="login">
        <v-text-field
          class="form__input"
          prepend-icon="mdi-account-outline"
          v-model="formUser.user"
          :rules="userRules"
          label="Usuario"
        ></v-text-field>

        <v-text-field
          class="form__input"
          prepend-icon="mdi-lock"
          type="password"
          v-model="formUser.password"
          :rules="passwordlRules"
          label="Password"
        ></v-text-field>

        <button class="form__btn" type="submit">Login</button>
      </v-form>
    </div>
    <div class="text-center">
      <v-dialog v-model="dialog">
        <v-card>
          <v-card-text>
            {{message}}
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="cerrar"
              >Cerrar</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import {useRouter} from 'vue-router';
import {useStore} from 'vuex';
import { getAPI } from "../Ax-Api";

export default {
  setup() {
    const router = useRouter()
    const store = useStore()
    const logged = ref(false)
    const dialog = ref(false);
    const form = ref(null);
    const formUser = ref({
      user: "",
      password: "",
    });

    const message = ref('');
    const userRules = [(value) => !!value || "Usuario es requerido"];
    const passwordlRules = [(value) => !!value || "Contraseña es requerida"];
    

    const cerrar = ()=>{
      if (logged.value) {
        router.push('/')
      }
      dialog.value =false

    }

    const login = ()=> {
      const dataUser = {
        username: formUser.value.user,
        password: formUser.value.password,
      }
      try {
        getAPI.post("/api/login/", dataUser).then((data) => {
          if (data.status === 200) {
            message.value='Usuario logeado'
            dialog.value=true;
            logged.value = true;
            store.commit('SET_USUARIO',dataUser)
            localStorage.setItem('usuario',JSON.stringify(dataUser.username))
          }
        })
      } catch (error) {
        dialog.value=true;
         message.value='Ocurrio un error al ingresar, verifique usuario y contraseña'
         
      }
    }
    return {
      form,
      formUser,
      userRules,
      passwordlRules,
      dialog,
      message,
      login,cerrar
    }
  }
};
</script>
<style scoped>
@import "@/assets/Styles/StyleLogin.css";
</style>


