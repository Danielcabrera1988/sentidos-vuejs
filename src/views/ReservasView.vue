<template>
  <div>
    <FormularioReserva />
  </div>
</template>

<script>
import { defineComponent,computed } from "vue";
import { useStore } from "vuex";
import {useRouter} from 'vue-router';
import FormularioReserva from "../components/FormularioReserva.vue";

export default defineComponent({
  components: { FormularioReserva },
  setup() {
    const router = useRouter()
    const store = useStore()

    const usuario = computed(()=>(store.getters['getUsuario']))

    const verificarUsuario = ()=>{
      if (!usuario.value) {
        router.push('/login')
      }
    }

    verificarUsuario()

  },
});
</script>

<style scoped>
@import "../assets/Styles/StyleGral.css";
</style>