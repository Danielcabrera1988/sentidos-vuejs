<template>
  <div class="menu__container">
    <div class="menu__container__header">
      <v-img
        class="banner_img"
        :src="require('../assets/Img/banner-menu.jpg')"
      />
      <v-img class="qr_img" :src="require('../assets/Img/qr.svg')"></v-img>
      <h2 class="header__title">Download Menu</h2>
      <p class="header__description">
        "La mejor combinación de sabores la podes encontrar acá. Todos nuestros
        platos son elavorados con los mal altos estandares de cocina y por
        personal altamente capacitado. Lorem ipsum dolor sit, amet consectetur
        adipisicing elit. Voluptatum rem asperiores quod molestias amet
        molestiae deserunt magni illum, eum alias ratione est veniam esse atque
        sapiente quos vitae eius ad quibusdam neque."
      </p>
    </div>
    <div class="menu__cards">
      <h3 class="menu__title">¡Algunas de nuestas delicias! 😋</h3>
      <p class="menu__description">
        Si quieres saber más de estas exquisitas comidas, sólo descarga el menu
        completo desde el QR y a disfrutar de una lluvia de esquisitos sabores.
      </p>
      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="4"
          lg="3"
          v-for="(comida, i) in comidas"
          :key="i"
        >
          <v-card class="cards__conteiners">
            <v-img :src="require(`@/assets/Img/${comida.imagen}`)"></v-img>

            <v-card-title class="card__name">{{ comida.nombre }}</v-card-title>

            <v-card-subtitle class="card__price">
              {{ comida.price }}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn style="font-size: 10px; margin-left: 15px"  :icon="comida.show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="changeShow(comida)" color="orange lighten-2" text> Leer más... </v-btn>
              <v-spacer></v-spacer>
              <v-btn :icon="comida.show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="changeShow(comida)"></v-btn>
            </v-card-actions>
            <v-expand-transition>
              <div v-show="comida.show">
                <v-divider></v-divider>
                <v-card-text class="card__description">
                  {{ comida.description }}
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
export default defineComponent({
  setup() {
    /* Variables Reactivas */

    const changeShow = (item) => {
      item.show = !item.show;
    };
    const comidas = ref([
      {
        nombre: "Cangreburguer",
        description: "descripcion",
        price: "$150 pesitos",
        imagen: "menu1.jpg",
        show: false,
      },
      {
        nombre: "Sushilanga",
        description: "descripcion",
        price: "$350 pesitos",
        imagen: "menu2.jpg",
        show: false,
      },
      {
        nombre: "Brichesirijillo",
        description: "descripcion",
        price: "$200 pesitos",
        imagen: "menu3.jpg",
        show: false,
      },
      {
        nombre: "Pizzita",
        description: "descripcion",
        price: "$300 pesitos",
        imagen: "menu4.jpg",
        show: false,
      },
      {
        nombre: "Ensaladita",
        description: "descripcion",
        price: "$250 pesitos",
        imagen: "menu5.jpg",
        show: false,
      },
      {
        nombre: "Volcancirri",
        description: "descripcion",
        price: "$180 pesitos",
        imagen: "menu6.jpg",
        show: false,
      },
      {
        nombre: "Pimientirijillo",
        description: "descripcion",
        price: "$220 pesitos",
        imagen: "menu7.jpg",
        show: false,
      },
      {
        nombre: "Bastoncirri",
        description: "descripcion",
        price: "$310 pesitos",
        imagen: "menu8.jpg",
        show: false,
      },
    ]);
    return {
      comidas,
      changeShow,
    };
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleMenu.css";
</style>