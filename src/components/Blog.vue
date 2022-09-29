<template>
  <div class="blog__container">
    <div class="blog__container__main">
      <div class="main__comment__points">
        <div class="blog__comments__container">
          <h2>Seccion Comentarios ✍</h2>
          <!-- cards comments -->
          <div
            class="comments__cards"
            v-for="(data, i) in dataUser"
            :key="i"
          >
            <p class="comments__user">{{ data.user.username }}</p>
            <p class="comments__text">{{ data.comment }}</p>
          </div>
        </div>
        <div class="blog__calification__container">
          <h2>⭐ ¡Puntuaciones! 🤩</h2>
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
            <v-btn class="btn__calification" to="/calification"
              >¡Califícanos aquí!</v-btn
            >
          </div>
        </div>
      </div>
      <div class="main__articles">
        <div class="articles__container">
          <h2>SECCION DE ARTICULOS</h2>
          <p>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Voluptatibus quo explicabo error amet? Laboriosam, blanditiis eum
            aliquam similique incidunt fugiat facilis, omnis asperiores sequi
            eius totam assumenda tenetur esse aut. Rem aspernatur iure dolorem
            modi ipsum id consequatur exercitationem sed fuga voluptatem,
            adipisci omnis inventore ex obcaecati, deserunt distinctio ab
            laboriosam enim facere porro error esse ut! Nostrum natus distinctio
            sed ratione molestiae doloremque qui eius at totam inventore
            corporis ab fugit deserunt, saepe ea rem! Vero doloribus rem
            officiis. Asperiores illo quae odit explicabo! Fugiat maxime non
            maiores! Inventore saepe iste accusamus eum minima sint reiciendis
            laboriosam vel! Molestiae.
          </p>
          <!-- Articulos informativos, recetas, experiencias, etc -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { getAPI }  from "../Ax-Api";
export default defineComponent({
  setup() {

    const dataUser = ref([]);
    const fetchComentarios = async () => {
      const { data } = await getAPI.get("/api/listOpinions/");
      dataUser.value = data;
    };

    fetchComentarios();

    return {
      dataUser,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleBlog.css";
</style>
