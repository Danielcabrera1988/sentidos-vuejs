<template>
  <div class="blog__container">
    <div class="blog__container__main">
      <div class="main__comment__points">
        <div class="blog__comments__container">
          <h2>Seccion Comentarios ✍</h2>
          <!-- cards comments -->
          <div class="comments__cards" v-for="(data, i) in dataUser" :key="i">
            <p class="comments__user">{{ data.user.username }}:</p>
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
                v-model="rating.atencion"
                bg-color="orange-lighten-1"
                color="blue"
                readonly=""
              ></v-rating>
            </div>
            <div class="calification">
              <h3>Lugar</h3>
              <!-- calificacion -->
              <v-rating
                v-model="rating.lugar"
                bg-color="orange-lighten-1"
                color="blue"
                readonly=""
              ></v-rating>
            </div>
            <div class="calification">
              <h3>Comida</h3>
              <!-- calificacion -->
              <v-rating
                v-model="rating.comida"
                bg-color="orange-lighten-1"
                color="blue"
                readonly=""
              ></v-rating>
            </div>
            <div class="calification">
              <h3>Precio</h3>
              <!-- calification -->
              <v-rating
                v-model="rating.precio"
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
      
      <h1>Articulos que pueden interesarte...</h1>
      <hr style="width: 100%"/>
      <section class="blog__container__articles">
        <article class="articles__container">
          <h3>Dieta Keto</h3>
          <p>
            La dieta cetogénica (o dieta keto, en su forma abreviada) es un plan
            de alimentación bajo en carbohidratos y rico en grasas que ofrece
            muchos beneficios para la salud. De hecho, alrededor de unos 20
            estudios demuestran que este tipo de dieta puede ayudar a perder
            peso y mejorar la salud. Las dietas cetogénicas pueden tener
            beneficios incluso contra la diabetes, el cáncer, la epilepsia y el
            Alzheimer.
          </p>
          <img :src="require('@/assets/Img/keto.jpg')" alt="keto" />
          <ul>
            <li>¿Qué es una dieta cetogénica?</li>
            <li>¿Qué puedo comer en la dieta Keto?</li>
            <li>¿Qué comer en una semana Keto?</li>
            <li>¿Cuales son los alimentos prohibidos?</li>
            <li>¿Cómo hacer la dieta Keto paso a paso?</li>
          </ul>
          <a
            href="https://www.healthline.com/health/es/dieta-cetogenica"
            target="blank"
            >Leer mas...</a
          >
          <!-- Articulos informativos, recetas, experiencias, etc -->
        </article>
        <article class="articles__container">
          <h3>Dieta Perricone</h3>
          <p>
            La dieta Perricone ganó popularidad después de que la reina Letizia
            la popularizara. Consiste en reducir las calorías diarias hasta las
            1.200 para conseguir perder peso estableciendo un plan de 3 o 28
            días con menús concretos. Los alimentos permitidos son muy
            limitados, basados en verduras, frutas y aquellos ricos en omega 3.
          </p>
          <img :src="require('@/assets/Img/perricone.jpg')" alt="perricone" />
          <ul>
            <li>¿Qué puedo comer en la dieta Perricone?</li>
            <li>¿Cuales es la dieta disociada?</li>
            <li>¿Cómo hacer la dieta Perricone paso a paso?</li>
          </ul>
          <a
            href="https://www.mundodeportivo.com/uncomo/belleza/articulo/como-hacer-la-dieta-perricone-32599.html"
            target="blank"
            >Leer mas...</a
          >
          <!-- Articulos informativos, recetas, experiencias, etc -->
        </article>
      </section>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { getAPI } from "../Ax-Api";
export default defineComponent({
  setup() {
    const dataUser = ref([]);
    const rating = ref({
      atencion: "",
      lugar: "",
      comida: "",
      precio: "",
    });
    const fetchComentarios = async () => {
      const { data } = await getAPI.get("/api/listOpinions/");
      dataUser.value = data;
    };
    fetchComentarios();

    const average = async () => {
      const averageProm = await getAPI.get("/api/getAverage");
      if (averageProm) {
        rating.value.atencion = averageProm.data.Atencion;
        rating.value.lugar = averageProm.data.Lugar;
        rating.value.comida = averageProm.data.Comida;
        rating.value.precio = averageProm.data.Precio;
      }
    };
    average();
    return {
      dataUser,
      rating,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleBlog.css";
</style>
