<template>
  <div class="fornecedores">
    <DxDataGrid
      ref="grid"
      :data-source="dataSource"
      :selection="selecao"
      :editing="edicao"
      :search-panel="pesquisa"
      :columns="columns"
      :show-borders="true"
    />
  </div>
</template>

<script>
import DxDataGrid from 'devextreme-vue/data-grid'
import CustomStore from 'devextreme/data/custom_store'
import notify from 'devextreme/ui/notify'

export default {
  components: {
    DxDataGrid
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
          colCount: 3,
          showValidationSummary: true,
          items: [
            {
              dataField: 'nome',
              validationRules: [
                { type: 'required', message: 'O nome é obrigatório' }
              ]
            },
            {
              dataField: 'cpf_cnpj',
              validationRules: [
                { type: 'required', message: 'O CPF/CNPJ é obrigatório' }
              ]
            },
            {
              dataField: 'email',
              validationRules: [
                { type: 'required', message: 'O email é obrigatório' },
                { type: 'email', message: 'Informe um email válido' }
              ]
            }
          ]
        }
      },
      columns: [
        {
          dataField: 'id',
          caption: '#',
          width: 50
        },
        {
          dataField: 'nome'
        },
        {
          dataField: 'cpf_cnpj',
          caption: 'CPF / CNPJ'
        },
        {
          dataField: 'email'
        }
      ]
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
      const url = '/financeiro/fornecedores/'
      return new CustomStore({
        key: 'id',
        load: async options => {
          let dados = []
          try {
            const { data } = await this.axios.get(url)
            dados = data
          } catch {
            notify('Erro ao executar a requisição', 'error', 3000)
          }
          return {
            data: dados,
            totalCount: dados.length
          }
        },
        insert: values => this.axios.post(url, values),
        update: (key, values) => this.axios.patch(`${url}${key}/`, values),
        remove: async key => {
          try {
            await this.axios.delete(`${url}${key}/`)
          } catch {
            notify('Erro ao excluir o registro. Verifique se não existe registros filhos.', 'error', 3000)
          }
        }
      })
    }
  }
}
</script>
