import Vue from 'vue'
import Crud from '@/components/Crud.vue'
import TituloPagamento from '@/components/titulos/Pagamento.vue'
import DetalhePagamento from '@/components/titulos/Detalhes.vue'
import GraficoContas from '@/components/dashboard/GraficoContas.vue'
import GraficoGastoFornecedor from '@/components/dashboard/GraficoGastoFornecedor.vue'
import AgendaPagamento from '@/components/dashboard/AgendaPagamento.vue'

Vue.component('app-crud', Crud)
Vue.component('app-titulo-pagamento', TituloPagamento)
Vue.component('app-detalhe-pagamento', DetalhePagamento)
Vue.component('dash-grafico-contas', GraficoContas)
Vue.component('dash-grafico-gasto-fornecedor', GraficoGastoFornecedor)
Vue.component('dash-agenda-pagamento', AgendaPagamento)
