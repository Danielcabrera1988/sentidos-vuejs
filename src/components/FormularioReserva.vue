<template>
  <div class="reserva__container">
    <h1>Sentidos Casa de Te y Restaurant</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum aut accusantium cumque? Doloremque blanditiis maxime iure dolorum minima, expedita nihil aspernatur esse ipsa voluptatum cupiditate accusamus nam autem quaerat, facilis quas sit, molestiae tempora architecto nesciunt laudantium error reprehenderit fugiat. Repudiandae dolores perferendis quod et id a ipsum, cumque soluta expedita voluptates quaerat non temporibus necessitatibus repellat eum assumenda aspernatur beatae sapiente, adipisci qui, provident minima corporis? Facere quidem, officiis repudiandae ipsam, cum deleniti, porro deserunt iusto voluptatibus accusantium delectus architecto magnam. Cupiditate ea vero dignissimos eum incidunt iste itaque perspiciatis obcaecati nostrum assumenda est, voluptatem, eius velit, consequatur praesentium autem. Sed magnam ipsam voluptates voluptate perspiciatis quos alias reprehenderit expedita? Consequatur deserunt molestias reprehenderit aperiam incidunt facilis quaerat, enim iste quos repudiandae dolor aspernatur a dignissimos eligendi accusantium minima eaque nobis dolores nulla quisquam quam delectus earum iure. Ullam dolores reiciendis distinctio. Ipsum iste distinctio, vitae corrupti inventore aliquid quibusdam tempora aut voluptate tenetur minima eum praesentium optio hic impedit natus molestiae totam nemo dicta quas, veniam eaque rem blanditiis. Dicta placeat tenetur ducimus inventore aliquid distinctio ipsa iste, cum animi saepe pariatur quisquam eveniet. Hic sit, at ratione animi ad quibusdam architecto eum necessitatibus adipisci. Ex, alias iste!</p>
    <h2>Reservas</h2>
    <v-img :src="require('../assets/Img/banner-reserva2.jpg')"></v-img>
    <div class="reserva__container__form">
      <v-form ref="form" @submit.prevent="submit">
        <v-text-field
          v-model="formUser.name"
          :counter="maxName"
          :rules="nameRules"
          label="Nombre y Apellido"
        ></v-text-field>

        <v-text-field
          v-model="formUser.email"
          :rules="emailRules"
          label="E-mail"
        ></v-text-field>

        <v-textarea
          outlined
          label="Escribe tu mensaje"
          v-model="formUser.msg"
        ></v-textarea>

        <button type="submit">Enviar</button>
      </v-form>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const form = ref(null);
    const formUser = ref({
      name: "",
      email: "",
      msg: "",
      password: "",
      password2: "",
    });
    const maxName = ref(10);
    const minCaracter = ref(8);

    const nameRules = [
      (value) => !!value || "Nombre es requerido",
      (value) => value.length <= 10 || "Nombre debe tener maximo 10 caracteres",
    ];

    const emailRules = [
      (value) => !!value || "E-mail es requerido",
      (value) => /.+@.+/.test(value) || "E-mail debe ser válido",
    ];

    return {
      form,
      formUser,
      nameRules,
      emailRules,
      maxName,
      minCaracter,
    };
  },
};
</script>

<style scoped>
@import "../assets/Styles/StyleFormReserve.css";
</style>
