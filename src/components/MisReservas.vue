<template>
  <div class="container__reservas">
    <div class="container__reserva__info">
      <h2 class="animate__animated animate__zoomIn">Mis Reservas</h2>
    </div>
    <div class="container__reservas__data">
      <v-table>
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
          <tr v-for="reserva in reservas" :key="reserva.id" >
            <td>{{ reserva.date }}</td>
            <td>{{ reserva.schedule }}</td>
            <td>{{ reserva.selected_tables }}</td>
            <td>
              <v-menu>
                <template v-slot:activator="{ props }">
                  <v-btn v-bind="props" 
                  >
                    Pagar
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="paid in items"
                    :key="paid.id"
                    @click="toPaid(reserva.id, paid.valor)"
                  >
                    <v-list-item-title>{{ paid.valor }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
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
    const items = [{ valor: "Seña" }, { valor: "Total" }];
    const router = useRouter();
    const parcial = ref(false);
    const total = ref(false);
    const dialog = ref(false);
    const message = ref("");
    const store = useStore();
    const user = computed(() => store.getters["getUsuario"]);
    const reservas = ref([]);
    const pago_total = ref("false");
    const colorToPaid = ref("");

    /* metodo para abonar la reserva parcial o total y actualizar BD*/
    const toPaid = async (id_reserved, valor) => {
      if (valor === "Seña") {
        parcial.value = true;
      } else if (valor === "Total") {
        pago_total.value = true;
      }
      const updateDateUser = {
        id: id_reserved,
        paid: total.value,
        paid_parcial: parcial.value,
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
    /* metodo para cancelar las reservas y actualizar BD */
    const cancel = async (id_reserved) => {
      const updateReservation = await getAPI.delete("/api/deleteReservation/", {
        params: {
          id: id_reserved,
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

    const cerrar = () => {
      if (user.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/misreservas");
      }
      dialog.value = false;
      window.location.reload();
    };

    return {
      dialog,
      items,
      message,
      reservas,
      colorToPaid,
      pago_total,
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
