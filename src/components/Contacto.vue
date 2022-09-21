<template>
  <div class="comment__main">
    <h3 class="animate__animated animate__bounce">¡Contactanos!</h3>
    <div class="comment__msg">
      <v-textarea
        :counter="maxCaracter"
        variant="outlined"
        name="msg"
        label="Mensaje"
        :rules="rulesMsg"
      ></v-textarea>
      <v-form @submit.prevent="sendContact">
        <v-text-field
          class="form__input"
          prepend-icon="mdi-account-outline"
          v-model="formUser.user"
          :rules="userRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          class="form__input"
          prepend-icon="mdi-account-outline"
          v-model="formUser.email"
          :rules="emailRules"
          label="Email"
        ></v-text-field>

        <v-text-field
          class="form__input"
          prepend-icon="mdi-email-outline"
          type="number"
          v-model="formUser.telefono"
          label="Telefono"
        ></v-text-field>
        <v-btn class="btn__submit" type="submit" action="metodoParaCalificar"
          >Enviar</v-btn
        >
      </v-form>
    </div>
    <v-img class="comment__main__img" :src="require('@/assets/Img/covid.jpg')"></v-img>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const maxName = ref(20);
    const minCaracter = ref(8);
    const maxCaracter = 50;
    const rulesMsg = [
      (value) =>
        value.length <= 50 || "El msj no puede exceder los 50 caracteres",
    ];
    const sendContact = () => {
      alert("Formulario enviado con éxito!")
    }
    const formUser = ref({
      user: "",
      password: "",
      telefono: "",
    });

    const userRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 20 || "Nombre debe tener maximo 10 caracteres",
    ];

    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) =>
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
        "E-mail debe ser válido",
    ];
    return {
      formUser,
      userRules,
      emailRules,
      rulesMsg,
      maxCaracter,
      maxName,
      minCaracter,
      sendContact
    };
  },
});
</script>

<style scoped>
@import '@/assets/Styles/StyleContacto.css';
</style>
