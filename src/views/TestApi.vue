<template>
  <div>
    <h1>TEST API</h1>
    <div>
      <p>{{ productos }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { getAPI } from "../Ax-Api";
export default defineComponent({
  setup() {
    const productos = ref([]);

    const fetchProductos = async () => {
      const { data } = await getAPI.get("/applications/food/");
      productos.value = data;
    };

    fetchProductos();
    return {
      productos,
    };
  },
});
</script>
