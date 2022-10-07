<template>
  <div class="login__container">
    <h1 class="animate__animated animate__zoomIn">Sentidos</h1>
    <h3 class="animate__animated animate__zoomIn">Restaurante y casa de te</h3>
    <div class="login__form">
      <form ref="form" @submit.prevent="login" class="container__form">
        <v-text-field
          hide-details="false"
          class="ma-4"
          prepend-icon="mdi-account-outline"
          v-model="formUser.user"
          label="Usuario"
        /><span
          style="color: red"
          v-for="error in v$.user.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          hide-details="false"
          class="ma-4"
          prepend-icon="mdi-lock"
          type="password"
          v-model="formUser.password"
          label="Password"
        /><span
          style="color: red"
          v-for="error in v$.password.$errors"
          :key="error"
          >{{ error.$message }}</span
        >
        <br />
        <button class="form__btn">Login</button>
      </form>
    </div>
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
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { getAPI } from "../Ax-Api";
import useVuelidate from "@vuelidate/core";
import { required, helpers } from "@vuelidate/validators";

export default {
  setup() {
    //en vue 3 se desarrolla todo desde dentro del setup
    const router = useRouter();
    const store = useStore();
    const logged = ref(false);
    const dialog = ref(false);
    const message = ref("");
    const form = ref(null);
    const formUser = ref({
      user: "",
      password: "",
    });

    const cerrar = () => {
      if (logged.value) {
        //con router redirigimos al usuario logrado hascia la ruta que le indiquemos si todo está bien
        router.push("/");
      }
      dialog.value = false;
    };

    const rules = computed(() => {
      return {
        user: {
          required: helpers.withMessage("Username es requerido", required),
        },
        password: {
          required: helpers.withMessage("Contraseña es requerida", required),
        },
      };
    });

    const v$ = useVuelidate(rules, formUser);

    const login = async () => {
      const dataUser = {
        username: formUser.value.user,
        password: formUser.value.password,
      };
      try {
        const result = await v$.value.$validate();
        if (result) {
          const data = await getAPI.post("/api/login/", dataUser);
          if (data.status === 200) {
            store.commit("SET_USUARIO", data.data.user);
            store.commit("SET_TOKEN", data.data.token);
            localStorage.setItem("usuario", JSON.stringify(data.data.user));
            localStorage.setItem("token", JSON.stringify(data.data.token));
            message.value = "¡Usuario logeado con éxito!";
            dialog.value = true;
            logged.value = true;
          }
        }
      } catch (error) {
        dialog.value = true;
        message.value =
          "Ocurrio un error al ingresar, verifique usuario y contraseña";
        /*error.response.status forma de leer los errores*/
      }
    };
    return {
      form,
      formUser,
      dialog,
      message,
      v$,
      login,
      cerrar,
    };
  },
};
</script>
<style>
@import "@/assets/Styles/StyleLogin.css";
</style>
