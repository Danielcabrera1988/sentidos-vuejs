<template>
  <div class="user__container">
    <h1 class="animate__animated animate__zoomInDown">Nuevo Usuario</h1>
    <img :src="require('../assets/Img/fondoregistro.jpg')" alt="" />
    <div class="user__container__form">
      <v-form ref="form" @submit.prevent="submit">
        <v-text-field
          v-model="formUser.name"
          prepend-icon="mdi-account"
          :counter="maxName"
          :rules="nameRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          v-model="formUser.email"
          prepend-icon="mdi-email-outline"
          :rules="emailRules"
          label="E-mail"
        ></v-text-field>

        <v-text-field
          v-model="formUser.password"
          label="Password"
          prepend-icon="mdi-lock-outline"
          type="password"
          :rules="passwordlRules"
          :counter="minCaracter"
        >
        </v-text-field>

        <v-text-field
          v-model="formUser.password2"
          label="Verify Password"
          prepend-icon="mdi-lock-outline"
          type="password"
          :rules="confirmPasswordRules"
          :counter="minCaracter"
        >
        </v-text-field>

        <button class="form__btn" type="submit">Enviar</button>
      </v-form>
    </div>
  </div>
</template>

<script >
import { ref } from "vue";
export default {
  setup() {
    const form = ref(null);
    const formUser = ref({
      name: "",
      email: "",
      password: "",
      password2: "",
    });
    const maxName = ref(10);
    const minCaracter = ref(8);

    const nameRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 10 || "Nombre debe tener maximo 10 caracteres",
    ];

    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) => /.+@.+/.test(value) || "E-mail debe ser válido",
    ];

    const passwordlRules = [
      (value) => !!value || "Contraseña es requerida",
      (value) =>
        value.length >= 8 || "La contraseña debe tener al menos 8 caracteres",
      (value) =>
        /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/.test(value) ||
        "Debe contener al menos 1 minuscula, 1 MAYUSCULA, 1 numero",
    ];

    const confirmPasswordRules = [
      (value) => !!value || "Contraseña es requerida",
      (value) =>
        value.length >= 8 || "La contraseña debe tener al menos 8 caracteres",
      (value) =>
        value === formUser.value.password || "Las contraseñas deben coincidir",
      (value) =>
        /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/.test(value) ||
        "Debe contener al menos 1 minuscula, 1 MAYUSCULA, 1 numero",
    ];

    return {
      form,
      formUser,
      nameRules,
      emailRules,
      passwordlRules,
      confirmPasswordRules,
      maxName,
      minCaracter,
    };
  },
};
</script>
<style scoped>
@import "../assets/Styles/StyleNewUser.css";
</style>