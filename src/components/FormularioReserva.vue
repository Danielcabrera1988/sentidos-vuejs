<template>
  <div class="reserva__container">
    <!-- Captura de datos -->
    <div class="container__reserva__data">
      <div class="reserva__img">
        <img
          class="reserva__img__logo"
          :src="require('../assets/Img/LogoSentidos2.png')"
        />
      </div>
      <div class="reserva__selection">
        <p>
          Sleccione una fecha:
          <v-text-field
            type="date"
            variant="outlined"
            :rules="fechaRules"
            v-model="reservaUser.fecha"
            :min="fechaMinima"
          ></v-text-field>
        </p>
        <p class="selection__table">Seleccione las mesas</p>
      </div>
      <!-- Seleccion de mesas class="reserva__selection__mesa"-->
      <v-row class="reserva__selection__table">
        <v-col cols="3" v-for="number in 20" v-bind:key="number">
          <v-btn
            class="selection__table"
            style="color: black"
            @click="addTable(number)"
            >{{ number }}</v-btn
          >
        </v-col>
      </v-row>
    </div>
    <!-- Formulario del usuario -->
    <div class="container__reserva__form">
      <h2>Datos de Reserva</h2>
      <v-form class="reserva__form__data" ref="form">
        <v-text-field
          variant="outlined"
          v-model="reservaUser.name"
          :rules="nameRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          variant="outlined"
          v-model="reservaUser.email"
          :rules="emailRules"
          label="E-mail"
        ></v-text-field>

        <v-text-field
          variant="outlined"
          v-model="reservaUser.tel"
          :rules="telRules"
          label="Teléfono"
        ></v-text-field>

        <v-text-field
          variant="outlined"
          readonly
          :rules="mesasRules"
          v-model="reservaUser.mesas"
          label="Mesas Seleccionadas"
        ></v-text-field>

        <button  class="form__btn" type="submit">Enviar</button>
      </v-form>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import moment from 'moment';

export default {
  setup() {
    const form = ref(null);
    const fechaMinima = moment().add(2,'days').format("YYYY-MM-DD")
    const reservaUser = ref({
      fecha: fechaMinima,
      mesas: [],
      name: "",
      email: "",
      tel: "",
    });
  
    const addTable = (idMesa)=>{
      /* agregacion de mesas y eliminacion si toca 2 veces la misma mesa */
      if (reservaUser.value.mesas.includes(idMesa)) {
        reservaUser.value.mesas = reservaUser.value.mesas.filter((item) => item != idMesa) 

      }else{
        reservaUser.value.mesas.push(idMesa)
      }
    }
    const mesasRules = [(value) => value.length > 0 || "La cantidad de mesas es requerida"];
    const fechaRules = [(value) => !!value || "La fecha es requerida"];
    const nameRules = [(value) => !!value || "Nombre es requerido"];
    const telRules = [(value) => !!value || "Teléfono es requerido"];
    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) =>
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
        "E-mail debe ser válido",
    ];

    return {
      form,
      reservaUser,
      nameRules,
      emailRules,
      telRules,
      addTable,
      mesasRules,
      fechaRules,
      fechaMinima
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleReserve.css";
</style>
