import { createStore } from "vuex";

export default createStore({
  state: {
    usuario: null,
    token: null,
  },
  getters: {
    //los getters se llaman con store.getters['getUsuario']
    getUsuario(state) {
      return state.usuario;
    },
    getToken(state) {
      return state.token;
    },
  },
  mutations: {
    //las mutaciones se llaman con store.commit('SET_USUARIO')
    SET_USUARIO(state, payload) {
      state.usuario = payload;
    },
    SET_TOKEN(state, payload) {
      state.token = payload;
    },
  },
  actions: {
    //con el dispatch se llama a las acciones
  },
  modules: {},
});
