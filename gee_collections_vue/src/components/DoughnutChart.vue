<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import doughnutChartData from '@/doughnut-chart'

export default {
  name: 'DoughnutChart',
   data() {
    return {
      doughnutChartData: doughnutChartData
    }
   },
   mounted() {
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, this.doughnutChartData);
  }
}
</script>