<template>
  <div class="home">
    <div class="home__container">
      <div class="home__container__box">
        <img :src="require('../assets/Img/LogoSentidos2.png')" />
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem, omnis necessitatibus beatae numquam enim, dolore
          tempore quas blanditiis, fuga ratione culpa tempora cumque! Expedita
          in incidunt eaque? Qui, consequatur sit!
        </p>
      </div>
      <div class="home__carousel__box">
        <v-carousel v-model="model" :cycle="true">
          <v-carousel-item
            :src="imagen"
            v-for="imagen in imagenes"
            :key="imagen"
          >
          </v-carousel-item>
        </v-carousel>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {

    const imagenes = [
      require("@/assets/Img/entrada.jpg"),
      require("@/assets/Img/living-central.jpg"),
      require("@/assets/Img/c3b.jpg"),
      require("@/assets/Img/c4b.jpg"),
    ];
    const model = ref(0); //ref se utiliza para cuando tenemos variables reactivas, hay que importar de vue
    return {
      imagenes,
      model,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleHeader.css";
</style>