<template>
  <div class="container__reservas">
    <div class="container__reserva__info">
      <h2>Mis Reservas</h2>
    </div>
    <div class="container__reservas__data">
      <v-table theme="dark">
        <thead>
          <tr>
            <th class="text-left">Fecha</th>
            <th class="text-left">Horario</th>
            <th class="text-left">Mesas</th>
            <th class="text-left">Pagos</th>
            <th class="text-left">Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="reserva in reservas" :key="reserva.id">
            <td>{{ reserva.date }}</td>
            <td>{{ reserva.schedule }}</td>
            <td>{{ reserva.selected_tables }}</td>
            <td>
              <v-btn @click="toPaid(reserva.id)">Pagar</v-btn>
            </td>
            <td>
              <v-btn @click="cancel(reserva.id)" v-model="reserva.id"
                >Cancelar</v-btn
              >
            </td>
          </tr>
        </tbody>
      </v-table>
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
import { defineComponent, ref, computed } from "vue";
import { getAPI } from "../Ax-Api";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
export default defineComponent({
  setup() {
    const router = useRouter();
    const parcial = ref(false);
    const total = ref(false);
    const dialog = ref(false);
    const message = ref("");
    const store = useStore();
    const user = computed(() => store.getters["getUsuario"]);
    const reservas = ref([]);

    /* metodo para abonar la reserva parcial o total */
    const toPaid = async (item) => {
      const updateDateUser = {
        id: item,
        paid: true,
        paid_parcial: true,
      };
      const updateReservation = await getAPI.put(
        "/api/paidReservation/",
        updateDateUser
      );
      try {
        if (updateReservation) {
          message.value = "¡Pago registrado correctamente!";
          dialog.value = true;
        }
      } catch (error) {
        message.value = "Error en el pago [ " + error + " ]";
      }
    };

    const cancel = async (item) => {
      const updateReservation = await getAPI.delete("/api/deleteReservation/", {
        params: {
          id: item,
        },
      });
      try {
        if (updateReservation) {
          message.value = "¡Reserva cancelada correctamente!";
          dialog.value = true;
          
        }
      } catch (error) {
        message.value = "Error en el pago [ " + error + " ]";
      }
    };

    /* metodo para traer todas las reservas realizadas por el usuario */
    const myReservation = async () => {
      reservas.value = [];
      const data = await getAPI.get("/api/myReservation/", {
        params: {
          user_id: user.value.id,
        },
      });
      data.data.forEach((reserva) => {
        reservas.value.push(reserva);
      });
    };
    myReservation();

    const imagenes = [
      require("@/assets/Img/entrada.jpg"),
      require("@/assets/Img/living-central.jpg"),
      require("@/assets/Img/c3b.jpg"),
      require("@/assets/Img/c4b.jpg"),
    ];
    const model = ref(0); //ref se utiliza para cuando tenemos variables reactivas, hay que importar de vue

    const cerrar = () => {
      if (user.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/misreservas");
      }
      dialog.value = false;
      window.location.reload();
    };

    return {
      imagenes,
      model,
      dialog,
      message,
      reservas,
      toPaid,
      cerrar,
      cancel,
    };
  },
});
</script>

<style scoped>
@import "@/assets/Styles/StyleMisReservas";
</style>
