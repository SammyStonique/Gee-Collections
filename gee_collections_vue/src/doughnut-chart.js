export const doughnutChartData = {
    type: "line",
    data: {
      labels: ["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"],
      datasets: [
        {
          label: "No of orders per Month",
          data: [2, 0, 5, 2, 7, 14, 27, 14],
          backgroundColor: "rgba(54,73,93,.5)",
          borderColor: "#36495d",
          borderWidth: 3
        },
        {
          label: "Amounts Purchased",
          data: [450,0,630,500,580,810,970,880],
          backgroundColor: "rgba(71, 183,132,.5)",
          borderColor: "#47b784",
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 1,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              padding: 25
            }
          }
        ]
      }
    }
  };
  
  export default doughnutChartData;