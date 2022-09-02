<template>
  <div class="menu__container">
    <div class="menu__container__header">
      <p>
        La mejor combinación de sabores la podes encontrar acá. Todos nuestros
        platos son elavorados con los mal altos estandares de cocina y por
        personal altamente capacitado
      </p>
      <v-img :src="require('../assets/Img/banner-menu.jpg')" />      
    </div>
    <div class="menu__cards">
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
            <p>{{ comida.nombre }}</p>
            <v-img :src="require(`@/assets/Img/${comida.imagen}`)" />
          </v-card>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import ScrollReveal from "scrollreveal";
export default defineComponent({
  setup() {
    onMounted(() => {
      ScrollReveal().reveal(".menu__cards", { delay: 200 });
    });

    const comidas = [
      {
        nombre: "Cangreburguer",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu1.jpg",
      },
      {
        nombre: "Sushilanga",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu2.jpg",
      },
      {
        nombre: "Brichesirijillo",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu3.jpg",
      },
      {
        nombre: "Pizzita",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu4.jpg",
      },
      {
        nombre: "Ensaladita",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu5.jpg",
      },
      {
        nombre: "Volcancirri",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu6.jpg",
      },
      {
        nombre: "Pimientirijillo",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu7.jpg",
      },
      {
        nombre: "Bastoncirri",
        descripcion: "descripcion",
        precio: "$",
        imagen: "menu8.jpg",
      },
    ];

    return {
      comidas,
    };
  },
});
</script>
<style scoped>
@import "../assets/Styles/StyleMenu.css";
</style>