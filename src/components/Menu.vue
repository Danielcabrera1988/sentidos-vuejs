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
        personal altamente capacitado."
      </p>
    </div>
    <div class="menu__cards">
      <h3 class="menu__title">¡Algunas de nuestas delicias! 😋</h3>
      <p class="menu__description">
        Si quieres saber más de estas exquisitas comidas, sólo descarga el menu
        completo desde el QR y a disfrutar de una lluvia de exquisitos sabores.
      </p>
      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="4"
          lg="3"
          v-for="(producto, i) in productos"
          :key="i"
        >
          <v-card class="cards__conteiners">
            <v-img :src="`/media/food/Pizza${producto.img}`"></v-img>

            <v-card-title class="card__name">{{ producto.name }}</v-card-title>

            <v-card-subtitle class="card__price">
              {{ producto.price }}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn
                style="font-size: 10px; margin-left: 15px"
                :icon="producto.state ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                @click="changeShow(producto)"
                color="orange lighten-2"
                text
              >
                Leer más...
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                :icon="producto.state ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                @click="changeShow(producto)"
              ></v-btn>
            </v-card-actions>
            <v-expand-transition>
              <div v-show="producto.state">
                <v-divider></v-divider>
                <v-card-text class="card__description">
                  {{ producto.detail_food }}
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
import { getAPI } from "../Ax-Api";
export default defineComponent({
  setup() {
    const productos = ref([]);
    const changeShow = (item) => {
      item.state = !item.state;
    };
    const fetchProductos = async () => {
      const { data } = await getAPI.get("food/");
      productos.value = data;
    };

    fetchProductos();
    return {
      productos,
      changeShow,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleMenu.css";
</style>