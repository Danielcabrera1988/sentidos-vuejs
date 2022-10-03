<template>
  <div class="reserva__container">
    <!-- Captura de datos -->
    <div class="container__reserva__data">
      <div class="reserva__img__text">
        <img
          class="reserva__img__logo"
          :src="require('../assets/Img/LogoSentidos2.png')"
        />
        <p>
          Desde 1985, nos ha encantado tener la oportunidad de servir excelente
          comida a nuestros maravillosos huéspedes en Resistencia Chaco. Gracias
          a todos por el privilegio de organizar sus cenas de negocios,
          celebraciones de cumpleaños, banquetes de bodas y noches tranquilas.
          Nos sentimos honrados de que haya elegido pasar tiempo con nosotros.
          Siempre trabajaremos para ganarnos ese privilegio.
        </p>
      </div>
      <div class="reserva__selection">
        <p class="reserva__selection__title">Sleccione una fecha</p>

        <v-text-field
          type="date"
          variant="outlined"
          v-model="reservaUser.fecha"
          hide-details="false"
          :min="fechaMinima"
        />

        <p class="reserva_horario_title">Seleccione un horario</p>
        <v-select
          :items="items"
          label="Horarios"
          variant="outlined"
          hide-details="false"
          v-model="reservaUser.horario"
        /><span
          style="color: red"
          v-for="error in v$.horario.$errors"
          :key="error"
          >{{ error.$message }}</span
        >
        <button class="form__btn" @click="find">Buscar</button>
      </div>
      <div class="reserva_selection_show">
        <button class="reserva_selected" disabled>Reservado</button>
        <button class="reserva_libre" disabled>Libre</button>
      </div>
      <div class="reserva__selection__mesas">
        <p class="reserva_mesas_title">Seleccione las mesas</p>
        <v-row class="reserva__selection__table">
          <v-col cols="3" v-for="number in 20" v-bind:key="number">
            <v-btn
              class="selection__table"
              style="color: black"
              :color="reservaUser.mesas.includes(number) ? 'blue' : 'white'"
              @click="addTable(number)"
              >{{ number }}</v-btn
            >
          </v-col>
        </v-row>
      </div>
    </div>
    <!-- Formulario del usuario -->
    <div class="container__reserva__form">
      <h2>Confirmación de Reserva</h2>
      <form class="reserva__form__data" @submit.prevent="makeReservation">
        <v-text-field
          variant="outlined"
          v-model="reservaUser.tel"
          label="Teléfono"
          hide-details="false"
          class="ma-3"
        /><span
          style="color: red"
          v-for="error in v$.tel.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <v-text-field
          variant="outlined"
          readonly
          v-model="reservaUser.mesas"
          label="Mesas Seleccionadas"
          hide-details="false"
          class="ma-3"
        /><span
          style="color: red"
          v-for="error in v$.mesas.$errors"
          :key="error"
          >{{ error.$message }}</span
        >

        <button class="form__btn">Enviar</button>
      </form>
    </div>
    <!-- Mensajes para el usuario -->
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
import { useStore } from "vuex";
import moment from "moment";
import { useRouter } from "vue-router";
import { getAPI } from "../Ax-Api";
import useVuelidate from "@vuelidate/core";
import { required, helpers, numeric } from "@vuelidate/validators";
export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const register = ref(false);
    const reservado = ref(true);
    const form = ref(null);
    const dialog = ref(false);
    const message = ref("");
    const reservas = ref([]);
    const fechaMinima = moment().add(1, "days").format("YYYY-MM-DD");
    const user = computed(() => store.getters["getUsuario"]);
    const items = ["Desayuno", "Almuerzo", "Merienda", "Cena"];
    const reservaUser = ref({
      fecha: fechaMinima,
      mesas: [],
      horario: "",
      user_id: "",
      tel: "",
    });

    const verificarUsuario = () => {
      if (!user.value) {
        router.push("/login");
      }
    };
    verificarUsuario();
    const addTable = (idMesa) => {
      /* agregacion de mesas y eliminacion si toca 2 veces la misma mesa */
      if (reservaUser.value.mesas.includes(idMesa)) {
        reservaUser.value.mesas = reservaUser.value.mesas.filter(
          (item) => item != idMesa
        );
      } else {
        reservaUser.value.mesas.push(idMesa);
      }
    };

    const rules = computed(() => {
      return {
        fecha: {
          required: helpers.withMessage("Debe seleccionar una fecha", required),
        },
        mesas: {
          required: helpers.withMessage("Debe eligir las mesas", required),
        },
        horario: {
          required: helpers.withMessage(
            "Debe seleccionar un horario",
            required
          ),
        },
        tel: {
          required: helpers.withMessage(
            "Debe introducir su número de teléfono ",
            required
          ),
          numeric: helpers.withMessage("Sólo números", numeric),
        },
      };
    });

    const v$ = useVuelidate(rules, reservaUser);
    /* metodo para cerrar el diagolo de exito o error, de comunicación con el usuario */
    const cerrar = () => {
      if (register.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/");
      }
      dialog.value = false;
    };
    /* Cargo todas las reservas filtradas por dia y horario */
    /* const allReserved = async () => {
      const dataFilter = {
        date: reservaUser.value.fecha,
        schedule: reservaUser.value.horario,
      }
      const { data } = await getAPI.get("/api/getReservation", dataFilter);//pasar dia y horario para filtrar
      reservas.value = data;
    };
    allReserved(); */

    const makeReservation = async () => {
      const dataUser = {
        user_id: user.value.id,
        phone: reservaUser.value.tel,
        schedule: reservaUser.value.horario,
        date: reservaUser.value.fecha,
        selected_tables: reservaUser.value.mesas.toString(),
      };
      try {
        const result = await v$.value.$validate();
        if (result) {
          const data = await getAPI.post("/api/reservation/", dataUser);
          if (data.status === 200) {
            message.value = "¡Reserva realizada correctamente!";
            dialog.value = true;
            register.value = true;
          } else if (data.status != 200) {
            dialog.value = true;
            message.value = "Ocurrio un error al intentar registrar el usuario";
          }
        }
      } catch (error) {
        dialog.value = true;
        message.value = "" + error;
        /*error.response.status forma de leer los errores*/
      }
    };

    return {
      cerrar,
      makeReservation,
      addTable,
      v$,
      items,
      form,
      reservaUser,
      reservado,
      dialog,
      message,
      user,
      reservas,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleReserve.css";
</style>
