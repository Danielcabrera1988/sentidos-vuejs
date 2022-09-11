<template>
  <div class="login__container">
    <h1 class="animate__animated animate__zoomIn">Sentidos</h1>
    <img :src="require('../assets/Img/fondoLogin.jpg')"/>
    <div class="login__form">
      <v-form ref="form">
        <v-text-field
          class="form__input"
          prepend-icon="mdi-email-outline"
          v-model="formUser.email"
          :rules="emailRules"
          label="Email"
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

export default {
  setup() {
    const form = ref(null);
    const formUser = ref({
      email: "",
      password: "",
    });
    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) => /.+@.+/.test(value) || "E-mail debe ser válido",
    ];
    const passwordlRules = [(value) => !!value || "Contraseña es requerida"];
    return {
      form,
      formUser,
      emailRules,
      passwordlRules,
    };
  },
};
</script>
<style scoped>
@import "@/assets/Styles/StyleLogin.css";                
</style>