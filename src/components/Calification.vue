<template>
  <div class="comment__main">
    <div class="comment__msg">
      <h3 class="animate__animated animate__bounce">
        ¡Gracias por dejar tu comentario!
      </h3>
      <v-textarea
        class="comment__area"
        variant="outlined"
        label="Comentario"
        v-model="userData.message"
        :rules="rulesMsg"
        :counter="maxCaracter"
      ></v-textarea>
    </div>
    <div class="comment__calification">
      <div class="calification">
        <h3>Atencion</h3>
        <!-- atention -->
        <v-rating
          v-model="userData.atention"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Lugar</h3>
        <!-- place -->
        <v-rating
          v-model="userData.place"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Comida</h3>
        <!-- Food -->
        <v-rating
          v-model="userData.food"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Precio</h3>
        <!-- price -->
        <v-rating
          v-model="userData.price"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
    </div>
    <div class="comment__btn__action">
      <button class="btn__effect" to="/blog">Volver</button>
      <button class="btn__effect" @click="userCalification">Enviar</button>
    </div>
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
</template>

<script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { getAPI } from "../Ax-Api";
export default {
  setup() {
    const router = useRouter();
    const store = useStore();
    const dialog = ref(false);
    const message = ref("");
    const register = ref(false);
    const user = computed(() => store.getters["getUsuario"]);
    const userData = ref({
      user: "",
      message: "",
      atention: 3,
      place: 3,
      food: 3,
      price: 3,
    });

    const maxCaracter = 50;
    const rulesMsg = [
      (value) =>
        value.length <= 50 || "El msj no puede exceder los 50 caracteres",
    ];

    const cerrar = () => {
      if (register.value) {
        //con router redirigimos al usuario logeado hascia la ruta que le indiquemos si todo está ben
        router.push("/blog");
      }
      dialog.value = false;
    };

    const verificarUsuario = () => {
      if (!user.value) {
        router.push("/login");
      }
    };
    verificarUsuario();

    const userCalification = async () => {
      const dataComment = {
        user: user.value.id,
        comment: userData.value.message,
        attention: userData.value.atention,
        place: userData.value.place,
        food: userData.value.food,
        price: userData.value.price,
      };
      try {
        const data = await getAPI.post("/api/opinions/", dataComment);
        if (data.status === 200) {
          message.value =
            "¡Gracias por dejarnos tus comentario! ¡Nos ayuda a mejorar cada día!";
          dialog.value = true;
          register.value = true;
        } else if (data.status != 200) {
          dialog.value = true;
          message.value = "Ocurrio un error al intentar registrar el usuario";
        }
      } catch (error) {
        dialog.value = true;
        message.value =
          "Ocurrio un error inesperado, vuelva a intentarlo mas tarde, disculpe las molestias ocasionadas";
        /*error.response.status forma de leer los errores*/
      }
    };
    return {
      userCalification,
      cerrar,
      userData,
      message,
      dialog,
      user,
      rulesMsg,
      maxCaracter,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleCalification.css";
</style>
