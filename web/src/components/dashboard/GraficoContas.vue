<template>
  <DxChart
    id="chart"
    :data-source="$store.state.graficoSaldoContas"
    title="Saldos de Contas"
  >
    <DxTooltip
      :enabled="true"
      :shared="true"
      :customize-tooltip="customizeTooltip"
    />
    <DxSeries type="bar"/>
    <DxLegend :visible="false"/>
  </DxChart>
</template>

<script>

import DxChart, {
  DxLegend,
  DxSeries,
  DxTooltip
} from 'devextreme-vue/chart'

export default {
  components: {
    DxChart,
    DxLegend,
    DxSeries,
    DxTooltip
  },
  mounted () {
    this.$store.dispatch('loadGraficoSaldoContas')
  },
  methods: {
    customizeTooltip (pointInfo) {
      return {
        html: `
        <div>
          <div class='tooltip-header'>
          ${pointInfo.argumentText}
          </div>
          <div class='tooltip-body'>
          <div class='series-name'>Saldo: </div>
          <div class='value-text'>${pointInfo.points[0].valueText}
        </div>
        `
      }
    }
  }
}
</script>
<style>

.tooltip-header {
    margin-bottom: 5px;
    font-size: 16px;
    font-weight: 500;
    padding-bottom: 5px;
    border-bottom: 1px solid #c5c5c5;
}

.tooltip-body {
    width: 170px;
}

.tooltip-body .series-name {
    font-weight: normal;
    opacity: 0.6;
    display: inline-block;
    line-height: 1.5;
    padding-right: 10px;
    width: 126px;
}

.tooltip-body .value-text {
    display: inline-block;
    line-height: 1.5;
    width: 30px;
}
</style>
