import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/plugins/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    fornecedores: [],
    contas: [],
    titulos: [],
    titulosPendentes: []
  },
  mutations: {
    setFornecedores (state, lista) {
      state.fornecedores = lista
    },
    setContas (state, lista) {
      state.contas = lista
    },
    setTitulos (state, lista) {
      state.titulos = lista
    },
    setTitulosPendentes (state, lista) {
      state.titulosPendentes = lista
    }
  },
  actions: {
    loadFornecedores: ({ commit }) => axios
      .get('/financeiro/fornecedores/')
      .then(res => {
        commit('setFornecedores', res.data)
      }),
    loadContas: ({ commit }) => axios
      .get('/financeiro/contas/')
      .then(res => {
        commit('setContas', res.data)
      }),
    loadTitulos: ({ commit }) => axios
      .get('/financeiro/titulos/')
      .then(res => {
        commit('setTitulos', res.data)
      }),
    loadTitulosPendentes: ({ commit }) => axios
      .get('/financeiro/titulos/pendentes/')
      .then(res => {
        commit('setTitulosPendentes', res.data)
      })
  },
  modules: {
  }
})
