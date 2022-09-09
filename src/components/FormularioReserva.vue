<template>
  <div class="reserva__container">
    <div class="reserva__img">
      <v-img class="reserva__img__logo" :src="require('../assets/Img/LogoSentidos2.png')"></v-img>
    </div>
    <div class="reserva__selection">
      <h2>Sentidos Casa de Te y Restaurant</h2>
      <p>
        Sleccione una fecha:
        <v-text-field type="date" variant="outlined" v-model="reservaUser.fecha" ></v-text-field>
      </p>
      <p>
        Ingrese la cantidad de mesas:<br />
        4P por mesas maximo
        <v-text-field type="number" variant="outlined" v-model="reservaUser.mesa"></v-text-field>
      </p>
    </div>
    <div class="reserva__selection__mesa">
      <!-- algo para sellecionar la mesa y que quede seleccionado o referencia a un numero de mesa para posteriormente guardar en el formulario de reserva -->
    </div>
    <div class="reserva__form">
      <h2>Datos de Reserva</h2>
      <v-form ref="form">

        <v-text-field
          variant="outlined"
          v-model="formUser.name"
          :rules="nameRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          variant="outlined"
          v-model="formUser.email"
          :rules="emailRules"
          label="E-mail"
        ></v-text-field>

        <v-text-field
          variant="outlined"
          v-model="formUser.tel"
          :rules="telRules"
          label="Teléfono"
        ></v-text-field>

        <button type="submit">Enviar</button>
      </v-form>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const form = ref(null);
    const reservaUser = ref({
      fecha: "",
      mesas: 0,

    })
    const formUser = ref({
      name: "",
      email: "",
      tel: "",
    });

    const nameRules = [(value) => !!value || "Nombre es requerido"];
    const telRules = [(value) => !!value || "Teléfono es requerido"];
    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) => /.+@.+/.test(value) || "E-mail debe ser válido",
    ];

    return {
      form,
      formUser,
      reservaUser,
      nameRules,
      emailRules,
      telRules,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleReserve.css";
</style>
