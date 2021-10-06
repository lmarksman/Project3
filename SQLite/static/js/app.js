console.log('Hello')

function buildPlot() {
    /* data route */
    const url = "/api/exchanges/New York";
    d3.json(url).then(function(response) {
  
      console.log(response);
      buildYearChart(response);
    });
}

function GetResults(){
  console.log("GetResults");
  let year = document.getElementById("year");
  console.log(year.value);
  let stock = document.getElementById("stock");
  console.log(stock.value);

  buildYearChart(year.value, stock.value);
  buildSingleCandlestick(year.value, stock.value);
  buildPieChart(year.value);
  buildPieChart2(stock.value);
}

// function optionStockChanged(stockIndex) {
//   buildYearChart(2021,stockIndex);
//   console.log("OptionYearChanged")
//   buildSingleCandlestick(2021, stockIndex);
// }

