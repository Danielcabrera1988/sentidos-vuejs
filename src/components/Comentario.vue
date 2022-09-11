<template>
  <div class="comment__main">
    <h3 class="animate__animated animate__bounce">¡Gracias por dejar tu comentario!</h3>
    <div class="comment__msg">
      <v-textarea
        :counter="maxCaracter"
        variant="outlined"
        name="msg"
        label="Mensaje"
        :rules="rulesMsg"
      ></v-textarea>
    </div>
    <div class="comment__calification">
      <div class="calification">
        <h3>Atencion</h3>
        <!-- atention -->
        <v-rating
          v-model="rating.atention"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Lugar</h3>
        <!-- place -->
        <v-rating
          v-model="rating.place"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Comida</h3>
        <!-- Food -->
        <v-rating
          v-model="rating.food"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
      <div class="calification">
        <h3>Precio</h3>
        <!-- price -->
        <v-rating
          v-model="rating.price"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
      </div>
    </div>
    <div class="comment__btn__action">
      <v-btn class="btn__back" to="/blog">Volver</v-btn>
      <v-btn class="btn__submit" type="submit" action="metodoParaCalificar">Enviar</v-btn>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const maxCaracter = 50;
    const rulesMsg = [
      (value) =>
        value.length <= 50 || "El msj no puede exceder los 50 caracteres",
    ];

    const rating = ref({
      atention: 3,
      place: 3,
      food: 3,
      price: 3,
    });
    return {
      rating,
      rulesMsg,
      maxCaracter,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleComentario.css";
</style>