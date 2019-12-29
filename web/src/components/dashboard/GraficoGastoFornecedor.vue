<template>
  <DxChart
    id="chart"
    :data-source="$store.state.graficoGastoFornecedor"
    title="Gastos e Pagamentos por Fornecedor"
    @pointClick="onPointClick"
  >
    <DxCommonSeriesSettings
      argument-field="fornecedor"
      type="bar"
      hover-mode="allArgumentPoints"
      selection-mode="allArgumentPoints"
    >
      <DxLabel :visible="true">
        <DxFormat
          :precision="0"
          type="fixedPoint"
        />
      </DxLabel>
    </DxCommonSeriesSettings>
    <DxSeries
      value-field="gasto"
      name="Gastos"
    />
    <DxSeries
      value-field="pago"
      name="Pagamentos"
    />
    <DxLegend
      vertical-alignment="bottom"
      horizontal-alignment="center"
    />
    <DxExport :enabled="true"/>
  </DxChart>
</template>
<script>
import {
  DxChart,
  DxSeries,
  DxCommonSeriesSettings,
  DxLabel,
  DxFormat,
  DxLegend,
  DxExport
} from 'devextreme-vue/chart'

export default {
  components: {
    DxChart,
    DxSeries,
    DxCommonSeriesSettings,
    DxLabel,
    DxFormat,
    DxLegend,
    DxExport
  },
  mounted () {
    this.$store.dispatch('loadGraficoGastoFornecedor')
  },
  data () {
    return {
      dataSource: [{
        fornecedor: 'Illinois',
        pago: 476.851,
        gasto: 528.904
      }, {
        fornecedor: 'Indiana',
        pago: 195.769,
        gasto: 227.271
      }, {
        fornecedor: 'Michigan',
        pago: 335.793,
        gasto: 372.576
      }, {
        fornecedor: 'Ohio',
        pago: 374.771,
        gasto: 418.258
      }, {
        fornecedor: 'Wisconsin',
        pago: 182.373,
        gasto: 211.727
      }]
    }
  },
  methods: {
    onPointClick ({ target }) {
      target.select()
    }
  }
}
</script>
<style>
#chart {
    height: 440px;
}
</style>
