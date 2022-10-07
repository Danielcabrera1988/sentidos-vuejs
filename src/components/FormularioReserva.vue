<template>
  <div class="reserva__container">
    <!-- Captura de datos (img - encabezado - guia - fecha - hora - mesas)-->
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
        <h4 class="reserva__selection__title">
          INSTRUCCIONES PARA RESERVAR UNA MESA
        </h4>
        <p>PASO N°1: SELECCIONE UNA FECHA</p>
        <p>PASO N°2: SELECCIONE UN HORARIO</p>
        <p>PASO N°3: PRESIONE EL BOTON "Buscar"</p>
        <h4 class="reserva__selection__title">Sleccione una fecha 📅</h4>

        <v-text-field
          type="date"
          variant="outlined"
          v-model="reservaUser.fecha"
          :min="fechaMinima"
          :max="fechaMaxima"
        />

        <h4 class="reserva__selection__title">Seleccione un horario 🕰️</h4>
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
      <!-- Botones de Reservado y Libre -->
      <div class="reserva_selection_show">
        <button class="reserva_selected" disabled>Reservado</button>
        <button class="reserva_libre" disabled>Libre</button>
      </div>
      <!-- Cuadricula de selección de mesas -->
      <div class="reserva__selection__mesas">
        <h4 class="reserva__selection__title">Seleccione la/s mesas</h4>
        <div class="reserva__selection__locked" v-if="flagReserva">
          <v-row class="reserva__selection__table">
            <v-col cols="3" v-for="number in 20" v-bind:key="number">
              <v-btn disabled>{{ number }}</v-btn>
            </v-col>
          </v-row>
        </div>
        <div class="reserva__selection__free" v-else>
          <v-row class="reserva__selection__table">
            <v-col cols="3" v-for="number in 20" v-bind:key="number">
              <v-btn
                :disabled="reservas.includes(number.toString())"
                :color="reservas.includes(number.toString()) ? 'blue' : 'white'"
                @click="addTable(number)"
                >{{ number }}</v-btn
              >
            </v-col>
          </v-row>
        </div>
      </div>
    </div>
    <!-- Formulario del usuario (medios de pago - horario - form)-->
    <div class="container__reserva__form">
      <div class="reserva__form__pagos">
        <h2 style="margin: 20px auto">Medios de Pago 🪙</h2>
        <img
          :src="require('@/assets/Img/medios-de-pago.png')"
          alt="medios-de-pago"
          style="
            border: 3px solid gold;
            border-radius: 10px;
            max-width: 90%;
            margin: 0 auto;
          "
        />
      </div>
      <div class="reserva__form__horarios">
        <h2 style="margin-top: 30px">Horarios de Atención</h2>
        <p>Desayuno: 08:00hs a 11:00hs</p>
        <p>Almuerzo: 11:30hs a 14:30hs</p>
        <p>Merienda: 16:30hs a 19:00hs</p>
        <p>Cena: 20:30hs a 00:00hs</p>
        <h2 style="margin-top: 40px">Confirmación de Reserva</h2>
      </div>
      <form class="reserva__form__data" @submit.prevent="makeReservation">
        <v-text-field
          variant="outlined"
          v-model="reservaUser.tel"
          label="Teléfono"
          class="ma-3"
          :counter="maxTel"
          :rules="phoneRules"
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
import moment from "moment";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { getAPI } from "../Ax-Api";
import useVuelidate from "@vuelidate/core";
import { required, helpers, numeric, maxLength } from "@vuelidate/validators";
export default {
  setup() {
    const store = useStore();
    const user = computed(() => store.getters["getUsuario"]);
    const router = useRouter();
    const form = ref(null);
    const dialog = ref(false);
    const message = ref("");
    const reservas = ref([]);
    const flagReserva = ref(true);
    const fechaMinima = moment().add(1, "days").format("YYYY-MM-DD");
    const fechaMaxima = moment().add(30, "days").format("YYYY-MM-DD");
    const items = ["Desayuno", "Almuerzo", "Merienda", "Cena"];
    const maxTel = ref(12);
    const phoneRules = [
      (value) => value.length <= 12 || "No puede exceder los 12 caracteres",
    ];
    const reservaUser = ref({
      id: "",
      tel: "",
      fecha: fechaMinima,
      mesas: [],
      horario: "",
    });

    /* Verifico si existe un usuario logeado, sino te redirige al login */
    const verificarUsuario = () => {
      if (!user.value) {
        router.push("/login");
      }
    };
    verificarUsuario();

    /* metodo para agregar mesas al arreglo de mesas del usuario */
    const addTable = (idMesa) => {
      /* agrega y elimina mesas, si toca 2 veces la misma mesa la elimina*/
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
          numeric: helpers.withMessage("Solo números", numeric),
          maxLength: helpers.withMessage(
            "No se permiten las de 12 dígitos",
            maxLength
          ),
        },
      };
    });

    const v$ = useVuelidate(rules, reservaUser);

    /* metodo para cerrar el diagolo de exito o error, de comunicación con el usuario */
    const cerrar = () => {
      if (user.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/misreservas");
      }
      dialog.value = false;
    };

    /* Cargo todas las reservas filtradas por dia y horario */
    const allReserved = async () => {
      //pasar dia y horario para filtrar
      reservas.value = [];
      const data = await getAPI.get("/api/getReservation/", {
        params: {
          date: reservaUser.value.fecha,
          schedule: reservaUser.value.horario,
        },
      });
      data.data.forEach((reserva) => {
        reservas.value.push(...reserva.selected_tables.split(","));
      });
      flagReserva.value = false;
    };

    /* LLama a la función de AllReserved cuando se llenan los parametros */
    const find = () => {
      allReserved();
    };

    /* Metodo para realizar una reserva si todo está bien */
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
          } else if (data.status != 200) {
            dialog.value = true;
            message.value = "Ocurrio un error al intentar registrar su reserva";
          }
        }
      } catch (error) {
        dialog.value = true;
        message.value = "" + error;
        /*error.response.status forma de leer los errores*/
      }
    };

    return {
      find,
      cerrar,
      makeReservation,
      addTable,
      v$,
      items,
      form,
      reservaUser,
      dialog,
      message,
      reservas,
      fechaMinima,
      fechaMaxima,
      flagReserva,
      maxTel,
      phoneRules,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleReserve.css";
</style>
