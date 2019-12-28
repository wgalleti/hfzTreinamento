<template>
  <div class="titulos">
    <app-crud
      url="/financeiro/titulos/"
      :colunas="colunas"
      :formulario="formulario"
    />
  </div>
</template>

<script>
export default {
  async created () {
    await this.$store.dispatch('loadFornecedores')
  },
  methods: {
    getFornecedores (options) {
      return {
        store: this.$store.state.fornecedores,
        paginate: true
      }
    }
  },
  computed: {
    colunas () {
      return [
        {
          dataField: 'id',
          caption: '#',
          width: 50
        },
        {
          dataField: 'data',
          dataType: 'date'
        },
        {
          dataField: 'numero_documento'
        },
        {
          dataField: 'vencimento',
          dataType: 'date'
        },
        {
          dataField: 'valor',
          format: {
            type: 'fixedPoint',
            precision: 2
          }
        },
        {
          dataField: 'fornecedor',
          lookup: {
            dataSource: this.getFornecedores,
            displayExpr: 'nome',
            valueExpr: 'id'
          }
        }
      ]
    },
    formulario () {
      return [
        {
          dataField: 'data',
          editorOptions: {
            dateSerializationFormat: 'yyyy-MM-dd'
          },
          validationRules: [
            { type: 'required', message: 'A data é obrigatória' }
          ]
        },
        {
          dataField: 'numero_documento',
          validationRules: [
            { type: 'required', message: 'O documento é obrigatório' }
          ]
        },
        {
          dataField: 'vencimento',
          editorOptions: {
            dateSerializationFormat: 'yyyy-MM-dd'
          },
          validationRules: [
            { type: 'required', message: 'O vencimento é obrigatório' }
          ]
        },
        {
          dataField: 'valor',
          editorOptions: {
            format: {
              type: 'fixedPoint',
              precision: 2
            }
          },
          validationRules: [
            { type: 'required', message: 'O valor é obrigatório' }
          ]
        },
        {
          dataField: 'fornecedor',
          validationRules: [
            { type: 'required', message: 'O fornecedor é obrigatório' }
          ],
          colSpan: 2
        }
      ]
    }
  }
}
</script>
