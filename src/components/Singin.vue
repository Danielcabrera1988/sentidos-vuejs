<template>
  <div class="user__container">
    <h1 class="animate__animated animate__zoomInDown">Nuevo Usuario</h1>
    <div class="user__container__form">
      <form @submit.prevent="singIn">
        <v-text-field
          class="ma-2"
          v-model="formUser.name"
          prepend-icon="mdi-account"
          label="Nombre y Apellido"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.name.$errors"
          :key="error"
          >{{ error.$message }}</span
        >
        <v-text-field
          class="ma-2"
          v-model="formUser.dni"
          prepend-icon="mdi-account"
          type="number"
          label="DNI"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.dni.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          class="ma-2"
          v-model="formUser.userName"
          prepend-icon="mdi-account"
          label="Usuario"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.userName.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          class="ma-2"
          v-model="formUser.email"
          type="text"
          prepend-icon="mdi-email-outline"
          label="E-mail"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.email.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          class="ma-2"
          v-model="formUser.password"
          label="Password"
          prepend-icon="mdi-lock-outline"
          type="password"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.password.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          class="ma-2"
          v-model="formUser.confirmPassword"
          label="Verify Password"
          prepend-icon="mdi-lock-outline"
          type="password"
          hide-details="false"
        /><span
          style="color: red; margin-left: 50px"
          v-for="error in v$.confirmPassword.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <button class="form__btn">Enviar</button>
      </form>
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
import { ref, computed } from "vue";
import useVuelidate from "@vuelidate/core";
import { useRouter } from "vue-router";
import { getAPI } from "../Ax-Api";
import {
  required,
  email,
  minLength,
  sameAs,
  helpers,
  numeric,
} from "@vuelidate/validators";
export default {
  setup() {
    const router = useRouter();
    const dialog = ref(false);
    const register = ref(false);
    const message = ref("");
    const formUser = ref({
      name: "",
      dni: "",
      userName: "",
      email: "",
      password: "",
      confirmPassword: "",
    });
    const cerrar = () => {
      if (register.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/login");
      }
      dialog.value = false;
    };
    const rules = computed(() => {
      return {
        name: {
          required: helpers.withMessage(
            "Nombre y Apellido son requeridos",
            required
          ),
        },
        dni: {
          required: helpers.withMessage("DNI es requerido ", required),
          maxLength: helpers.withMessage(
            "Debe tener al menos 8 digitos ",
            minLength(8)
          ),
          numeric: helpers.withMessage("Sólo números", numeric),
        },
        userName: {
          required: helpers.withMessage("Username es requerido", required),
        },
        email: {
          required: helpers.withMessage("Email es requerido", required),
          email: helpers.withMessage("Formato incorrecto", email),
        },
        password: {
          required: helpers.withMessage("Contraseña es requerida", required),
          minLength: helpers.withMessage("Debe contener al menos 8 caracteres", minLength(8)),
        },
        confirmPassword: {
          required: helpers.withMessage("Confirmación es requerida ", required),
          sameAs: helpers.withMessage(
            "Deben coincidir",
            sameAs(formUser.value.password)
          ),
        },
      };
    });

    const v$ = useVuelidate(rules, formUser);//asociacion de datos input con las reglas establecidas

    const singIn = async () => {
      const dataUser = {
        username: formUser.value.userName,
        email: formUser.value.email,
        fullname: formUser.value.name,
        dni: formUser.value.dni,
        password: formUser.value.password,
      };
      try {
        const result = await v$.value.$validate();
        if (result) {
          const data = await getAPI.post("/api/register/", dataUser);
          if (data.status === 200) {
            message.value = "¡Usuario creado correctamente!";
            dialog.value = true;
            register.value = true;
          } else if (data.status != 200) {
            dialog.value = true;
            message.value = "Ocurrio un error al intentar registrar el usuario";
          }
        }
      } catch (error) {
        dialog.value = true;
        message.value = "El nombre del usuario se encuentra en uso";
        /*error.response.status forma de leer los errores*/
      }
    };

    return {
      formUser,
      singIn,
      v$,
      cerrar,
      dialog,
      message,
    };
  },
};
</script>
<style scoped>
@import "../assets/Styles/StyleSingin.css";
</style>
