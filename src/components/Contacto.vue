<template>
  <div class="comment__main">
    <div class="comment__message">
      <h3 class="animate__animated animate__bounce">¡Contactanos!</h3>
      <div class="comment__message__box">
        <v-textarea
          variant="outlined"
          name="msg"
          label="Dejanos tu mensaje"
          v-model="formUser.message"
          hide-details="false"
        ></v-textarea>
        <span
          style="color: red"
          v-for="error in v$.message.$errors"
          :key="error"
          >{{ error.$message }}</span
        >
      </div>
      <div class="comment__form">
        <form @submit.prevent="sendContact">
          <v-text-field
            class="ma-4"
            prepend-icon="mdi-account-outline"
            v-model="formUser.name"
            hide-details="false"
            label="Nombre y Apellido"
          /><span
            style="color: red; margin-left: 50px"
            v-for="error in v$.name.$errors"
            :key="error"
            >{{ error.$message }}</span
          >

          <v-text-field
            class="ma-4"
            prepend-icon="mdi-account-outline"
            v-model="formUser.email"
            hide-details="false"
            label="Email"
          /><span
            style="color: red; margin-left: 50px"
            v-for="error in v$.email.$errors"
            :key="error"
            >{{ error.$message }}</span
          >

          <v-text-field
            class="ma-4"
            prepend-icon="mdi-email-outline"
            type="number"
            v-model="formUser.telefono"
            label="Telefono"
            hide-details="false"
          /><span
            style="color: red; margin-left: 50px"
            v-for="error in v$.telefono.$errors"
            :key="error"
            >{{ error.$message }}</span
          >
          <br />
          <button class="btn__submit">Enviar</button>
        </form>
      </div>
    </div>
    <div class="main__img__covid">
      <v-img
        class="comment__main__img"
        :src="require('@/assets/Img/covid.jpg')"
      ></v-img>
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
import useVuelidate from "@vuelidate/core";
import { useRouter } from "vue-router";
import { getAPI } from "../Ax-Api";
import {
  required,
  email,
  maxLength,
  helpers,
  numeric,
} from "@vuelidate/validators";
export default {
  setup() {
    const dialog = ref(false);
    const message = ref("");
    const router = useRouter();
    const register = ref(false);
    const formUser = ref({
      name: "",
      email: "",
      message: "",
      telefono: "",
    });
    const cerrar = () => {
      if (register.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/");
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
        email: {
          required: helpers.withMessage("Email es requerido", required),
          email: helpers.withMessage("Formato incorrecto", email),
        },
        message: {
          required: helpers.withMessage(
            "Es obligatorio enviar un mensaje",
            required
          ),
          maxLength: helpers.withMessage(
            "Debe contener como maximo 50 caracteres",
            maxLength(50)
          ),
        },
        telefono: {
          required: helpers.withMessage("Telefono es requerido ", required),
          numeric: helpers.withMessage("Sólo números", numeric),
        },
      };
    });

    const v$ = useVuelidate(rules, formUser);

    const sendContact = async () => {
      const result = await v$.value.$validate();
      if (result) {
        const dataUser = {
          fullname: formUser.value.name,
          email: formUser.value.email,
          phone: formUser.value.telefono,
          message: formUser.value.message,
        };
        try {
          if (result) {
            const data = await getAPI.post("/api/contact/", dataUser);
            if (data.status === 200) {
              message.value =
                "Gracias por contactarte con nosotros! Nos pondremos en contacto a la brevedad";
              dialog.value = true;
              register.value = true;
            } else if (data.status != 200) {
              dialog.value = true;
              message.value =
                "Ocurrio un error al intentar enviar su consulta";
            }
          }
        } catch (error) {
          dialog.value = true;
          message.value = "Ocurrio un error inesperado, por favor intente mas tarde";
          /*error.response.status forma de leer los errores*/
        }
      }
    };
    return {
      formUser,
      cerrar,
      sendContact,
      rules,
      v$,
      dialog,
      message,
    };
  },
};
</script>

<style scoped>
@import "@/assets/Styles/StyleContacto.css";
</style>
