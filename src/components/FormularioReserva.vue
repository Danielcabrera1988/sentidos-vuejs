<template>
  <div class="reserva__container">
    <h1 class="reserva__container__titulo">Formulario Reserva</h1>
    <div class="reserva__container__form">
      <v-form ref="form" @submit.prevent="submit">
        <v-text-field
          v-model="formUser.name"
          :counter="maxName"
          :rules="nameRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          v-model="formUser.email"
          :rules="emailRules"
          label="E-mail"
        ></v-text-field>

        <textarea name="Mensaje" cols="30" rows="10">Mensaje</textarea>

        <button type="submit">Enviar</button>
      </v-form>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import ScrollReveal from "scrollreveal";

export default {
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".reserva__container", { delay: 200 });
    });
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

    return {
      form,
      formUser,
      nameRules,
      emailRules,
      maxName,
      minCaracter,
    };
  },
};
</script>

<style scoped>
@import '../assets/Styles/StyleFormReserve.css'
</style>
