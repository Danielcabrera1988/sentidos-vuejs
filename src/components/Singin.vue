<template>
  <div class="user__container">
    <h1 class="animate__animated animate__zoomInDown">Nuevo Usuario</h1>
    <div class="user__container__form">
      <v-form ref="form" @submit.prevent="singIn">
        <v-text-field
          v-model="formUser.firstName"
          prepend-icon="mdi-account"
          :counter="maxName"
          :rules="firstNameRules"
          label="Nombre"
        ></v-text-field>

        <v-text-field
          v-model="formUser.lastName"
          prepend-icon="mdi-account"
          :counter="maxName"
          :rules="lastNameRules"
          label="Apellido"
        ></v-text-field>

        <v-text-field
          v-model="formUser.username"
          prepend-icon="mdi-account"
          :rules="userNameRules"
          label="Usuario"
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

        <button class="form__btn">Enviar</button>
      </v-form>
    </div>
    <h3>¡Gracias por formar parte de nosotros!</h3>
    <div class="text-center">
      <v-dialog v-model="dialog">
        <v-card>
          <v-card-text>
            {{ message }}
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="cerrar">Cerrar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { getAPI } from "../Ax-Api";
export default {
  setup() {
    const dialog = ref(false);
    const message = ref("");
    const form = ref(null);
    const formUser = ref({
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      password2: "",
    });

    const singIn = () => {
      const dataUser = {
        username: formUser.value.username,
        email: formUser.value.email,
        name: formUser.value.firstName,
        lastName: formUser.value.lastName,
        password: formUser.value.password,
      };
      getAPI
        .post("api/register/", dataUser)
        .then((data) => {
          if (data.status === 200) {
            message.value = "Usuario creado correctamente!";
            dialog.value = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    };
    singIn();

    const maxName = ref(20);
    const minCaracter = ref(8);

    const firstNameRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 20 || "Nombre debe tener maximo 10 caracteres",
    ];
    const lastNameRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 20 || "Nombre debe tener maximo 10 caracteres",
    ];
    const userNameRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 20 || "Nombre debe tener maximo 10 caracteres",
    ];
    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) =>
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
        "E-mail debe ser válido",
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
      firstNameRules,
      lastNameRules,
      userNameRules,
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
@import "../assets/Styles/StyleSingin.css";
</style>
