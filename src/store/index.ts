import { createStore } from "vuex";

export default createStore({
  state: {
    usuario: null,
  },
  getters: {
    //los getters se llaman con store.getters['getUsuario']
    getUsuario(state) {
      return state.usuario;
    },
  },
  mutations: {
    //las mutaciones se llaman con store.commit('SET_USUARIO')
    SET_USUARIO(state, payload) {
      state.usuario = payload;
    },
  },
  actions: {
    //con el dispatch se llama a las acciones
  },
  modules: {},
});
