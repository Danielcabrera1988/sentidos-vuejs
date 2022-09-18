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
  </div>
</template>

<script>
import { ref } from "vue";
import {getAPI} from "../Ax-Api";
export default {
  setup() {
    const form = ref(null);
    const formUser = ref({
      user: "",
      password: "",
    });
    const userRules = [(value) => !!value || "User es requerido"];
    const passwordlRules = [(value) => !!value || "Contraseña es requerida"];
    return {
      form,
      formUser,
      userRules,
      passwordlRules,
    };
  },
  methods: {
    login() {
      const dataUser = {
        "username": this.formUser.user,
        "password": this.formUser.password,
      };
      getAPI.post("/api/login/", dataUser).then((data) => {
        if(data.status === 200){
          console.log(data)
        }
      });
    },
  },
};
</script>
<style scoped>
@import "@/assets/Styles/StyleLogin.css";
</style>