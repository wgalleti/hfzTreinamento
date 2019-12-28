<template>
  <DxDataGrid
    ref="grid"
    :data-source="dataSource"
    :selection="selecao"
    :editing="edicao"
    :search-panel="pesquisa"
    :columns="columns"
    :show-borders="true"
  />
</template>

<script>
import DxDataGrid from 'devextreme-vue/data-grid'
import CustomStore from 'devextreme/data/custom_store'
import notify from 'devextreme/ui/notify'

export default {
  components: {
    DxDataGrid
  },
  props: {
    url: {
      type: String,
      required: true
    },
    carregarDados: {
      type: Function
    },
    colunas: {
      type: Array,
      required: true
    },
    formulario: {
      type: Array,
      required: true
    },
    qtdCamposFormulario: {
      type: Number,
      default: 3
    }
  },
  data () {
    return {
      fornecedores: [],
      selecao: {
        mode: 'multiple'
      },
      pesquisa: {
        visible: true,
        width: 300
      },
      edicao: {
        allowAdding: true,
        allowUpdating: true,
        allowDeleting: true,
        useIcons: true,
        mode: 'form',
        form: {
          labelLocation: 'top',
          colCount: this.qtdCamposFormulario,
          showValidationSummary: true,
          items: this.formulario
        }
      },
      columns: this.colunas
    }
  },
  methods: {
    atualizar () {
      const grid = this.$refs.grid.instance
      grid.refresh()
    }
  },
  computed: {
    dataSource () {
      return new CustomStore({
        key: 'id',
        load: async options => {
          if (this.carregarDados) {
            await this.carregarDados()
          }
          let dados = []
          try {
            const { data } = await this.axios.get(this.url)
            dados = data
          } catch {
            notify('Erro ao executar a requisição', 'error', 3000)
          }
          return {
            data: dados,
            totalCount: dados.length
          }
        },
        insert: values => this.axios.post(this.url, values),
        update: (key, values) => this.axios.patch(`${this.url}${key}/`, values),
        remove: async key => {
          try {
            await this.axios.delete(`${this.url}${key}/`)
          } catch {
            notify('Erro ao excluir o registro. Verifique se não existe registros filhos.', 'error', 3000)
          }
        }
      })
    }
  }
}
</script>
