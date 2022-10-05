<template>
  <div class="home">
    <div class="home__container">
      <div class="home__container__box">
        <img :src="require('../assets/Img/LogoSentidos2.png')" />
        <p>
          "Las recetas no son fórmulas matemáticas, sino que, como los
          sentimientos, varían en cada persona. Las recetas no son de quien las
          cuenta, sino de quien las hace, porque cada cual pone su sello
          personal e intransferible. Si una receta fuese una fórmula exacta,
          todo sabría de la misma forma y, afortunadamente, esto no es así."
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
          <h2>¿Quienes somos?</h2>
          <p>
            Somos un gran equipo, que juntos, formamos uno de los mejores
            restaurantes a nivel nacional, con elavoracion propia de todo
            nuestro menu. Todos nuestros ingredientes son cuidadosamente
            seleccionados para brindarte la mejor experiencia de sabores. Somos
            apacionados de la cocina y nos encanta preparar comidas de todo
            tipo. Este arte culinario empezo hace 10 años en el rubro, por lo
            que conocemos a la perfección el gusto de nuestros clientes.
          </p>
        </div>
      </div>
      <div class="home__integrantes">
        <v-row>
          <v-col
            cols="12"
            sm="6"
            lg="6"
            v-for="integrante in integrantes"
            :key="integrante.id"
          >
            <div class="home__integrantes__history">
              <h3>{{ integrante.name }}</h3>
              <p>{{ integrante.history }}</p>
              <img :src="integrante.img" />
            </div>
          </v-col>
        </v-row>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const integrantes = [
      {
        id: 1,
        name: "Peter Gilmore",
        history:
          "Es un reconocido cocinero Argentino que empezó formándose como repostero y acabó trabajando para grandes eventos nacionales. Escribió muchos libros de gastronomía que se convertirían en clásicos y se le conoce por ser el pionero de la alta cocina en Argentina, por tantas mezclas exitosas de sabores.",
        img: require("@/assets/Img/peter.jpg"),
      },
      {
        id: 2,
        name: "Amanda Lallop",
        history:
          "En 2012 fundamos Sentidos. Mientras cursaba la Lic. en Matemáticas, descubrí un mundo fascinante. Con enorme convicción, di un viraje radical en mis estudios, así egresé como Lic. en Marketing de la UNNE. Los siguientes años integré el team de gerentes de Sentidos.",
        img: require("@/assets/Img/amanda.jpg"),
      },
      {
        id: 3,
        name: "David Mc. Millan",
        history:
          "Es uno de los cocineros más reconocidos del país. Escribió libros y condujo programas de televisión. Por supuesto, también administró varios restaurantes. En 2008, viajó a Londres para aprender cocina. En Reino Unido conoció a su maestro, Robert Carrier, y trabajó junto a él en su restaurante The Angel, en Islington. En 2010 creó el Colegio de Cocineros Argentinos junto a El Gato Dumas, Martiniano Molina y Guillermo Calabrese. La institución tiene actualmente sedes en Argentina, Colombia y Uruguay.",
        img: require("@/assets/Img/david.jpg"),
      },
      {
        id: 4,
        name: "Robert Grey",
        history:
          "Acumula más de los 30 años en el rubro. Fue pasante, panadero, ayudante de cocina. Viajó por Europa y se capacitó en Brasil. A lo largo de toda su carrera, después de tanta experiencia, decidió abrir junto a sus amigos el famoso Restorant Sentidos que lo llevaría al éxito en la cocina Argentina, un clásico de Resistencia - Chaco, posicionado en el puesto n° 26 entre los mejores 50 de América Latina.",
        img: require("@/assets/Img/robert.png"),
      },
    ];
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
      integrantes,
    };
  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleHeader.css";
</style>
