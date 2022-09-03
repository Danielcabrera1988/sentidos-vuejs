<template>
  <div class="blog__container">
    <div class="blog__container__main">
      <div class="blog__comments__container">
        <!-- cards comments -->
        <div :class="i % 2==0 ? 'comments__cards': 'comments__cards__inverse' " v-for="(comment, i) in comments" :key="i"
        
        >
          <v-card >
            <p>{{ comment.name }}</p>
            <p>{{ comment.comment }} </p>
          </v-card>
        </div>
      </div>
      <div class="blog__calification__container">
        <div class="calification__container">
          <div class="calification">
            <h3>Atencion</h3>
            <!-- calificacion-->
            <v-rating
              v-model="rating"
              bg-color="orange-lighten-1"
              color="blue"
              readonly=""
            ></v-rating>
          </div>
          <div class="calification">
            <h3>Lugar</h3>
            <!-- calificacion -->
            <v-rating
              v-model="rating"
              bg-color="orange-lighten-1"
              color="blue"
              readonly=""
            ></v-rating>
          </div>
          <div class="calification">
            <h3>Comida</h3>
            <!-- calificacion -->
            <v-rating
              v-model="rating"
              bg-color="orange-lighten-1"
              color="blue"
              readonly=""
            ></v-rating>
          </div>
          <div class="calification">
            <h3>Precio</h3>
            <!-- calification -->
            <v-rating
              v-model="rating"
              bg-color="orange-lighten-1"
              color="blue"
              readonly=""
            ></v-rating>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  setup() {
    const comments = [
      {
        name: "Messi",
        comment: "descripcion",
      },
      {
        name: "De Paul",
        comment: "descripcion",
      },
      {
        name: "Kun",
        comment: "descripcion",
      },
      {
        name: "Dibu",
        comment: "descripcion",
      },
      {
        name: "Messi",
        comment: "descripcion",
      },
      {
        name: "De Paul",
        comment: "descripcion",
      },
      {
        name: "Kun",
        comment: "descripcion",
      },
      {
        name: "Dibu",
        comment: "descripcion",
      },
    ];
    return {
      comments,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleBlog.css";
</style>