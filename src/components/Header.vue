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
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates, quisquam inventore quos quia pariatur at dicta est doloribus laborum fugiat.
        </p>
      </div>
      <div class="home__body">
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
        <div class="home__about">
          <h2>Seccion Nosotros</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores, in
            repudiandae eligendi accusamus nobis mollitia ipsam sunt error ipsum
            praesentium non consequuntur aliquam voluptatibus soluta, quas
            deleniti, esse excepturi. Eligendi, numquam delectus. Alias nihil
            vero nemo ea fugiat culpa molestias, deleniti, earum nam laboriosam
            maiores autem esse tenetur harum ratione consectetur molestiae
            aliquid iste animi voluptatum aut rerum. Nihil odio dolore error ex,
            alias nam consequatur laboriosam magnam! Veritatis et eos provident
            optio praesentium dolores, magni alias illo delectus magnam, culpa
            quisquam natus voluptatem necessitatibus qui expedita? Maxime
            temporibus eligendi quia neque facere modi atque, aliquid nihil iure
            porro deleniti.
          </p>
        </div>
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