<template>
  <div class="pagamentos">
    <app-crud
      url="/financeiro/pagamentos/"
      :colunas="colunas"
      :formulario="formulario"
      :carregar-dados="carregar"
    />
  </div>
</template>

<script>
export default {
  methods: {
    async carregar () {
      await this.$store.dispatch('loadContas')
      await this.$store.dispatch('loadTitulos')
    },
    getTitulos (options) {
      return {
        store: this.$store.state.titulos,
        paginate: true
      }
    },
    getContas (options) {
      return {
        store: this.$store.state.contas,
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
          dataField: 'valor',
          format: {
            type: 'fixedPoint',
            precision: 2
          }
        },
        {
          dataField: 'titulo',
          lookup: {
            dataSource: this.getTitulos,
            valueExpr: 'id',
            displayExpr: v => `${v.fornecedor_display.nome}, ${v.numero_documento}`
          }
        },
        {
          dataField: 'conta',
          lookup: {
            dataSource: this.getContas,
            valueExpr: 'id',
            displayExpr: 'descricao'
          }
        }
      ]
    },
    formulario () {
      return [
        {
          dataField: 'titulo',
          validationRules: [
            { type: 'required', message: 'O título é obrigatório' }
          ],
          colSpan: 2
        },
        {
          dataField: 'data',
          editorOptions: {
            dateSerializationFormat: 'yyyy-MM-dd'
          },
          validationRules: [
            { type: 'required', message: 'A data é obrigatória' }
          ],
          colSpan: 1
        },
        {
          dataField: 'valor',
          editorType: 'dxNumberBox',
          editorOptions: {
            format: {
              type: 'fixedPoint',
              precision: 2
            }
          },
          validationRules: [
            { type: 'required', message: 'O valor é obrigatório' }
          ],
          colSpan: 1
        },
        {
          dataField: 'conta',
          validationRules: [
            { type: 'required', message: 'A conta é obrigatório' }
          ],
          colSpan: 1
        }
      ]
    }
  }
}
</script>
