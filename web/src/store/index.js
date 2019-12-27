import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/plugins/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    fornecedores: []
  },
  mutations: {
    setFornecedores (state, lista) {
      state.fornecedores = lista
    }
  },
  actions: {
    loadFornecedores: async context => {
      const { data } = await axios.get('/financeiro/fornecedores/')
      context.commit('setFornecedores', data)
      return data
    }
  },
  modules: {
  }
})
