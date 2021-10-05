console.log('Hello')

function buildPlot() {
    /* data route */
    const url = "/api/exchanges/New York";
    d3.json(url).then(function(response) {
  
      console.log(response);
      buildYearChart(response);
    });
}

function GetReults(form){
  console.log("GetResults")
    buildYearChart(form.year, form.stock);
    buildSingleCandlestick(form.year, form.stock);
}

function optionStockChanged(stockIndex) {
  buildYearChart(2021,stockIndex);
  console.log("OptionYearChanged")
  buildSingleCandlestick(2021, stockIndex);
}
// function buildCandlestick(year) {
//   /* data route */
//   const url = `/api/years/${year}`;
//   d3.json(url).then(function(response) {

//     console.log(response);
//     buildSingleCandlestick(response);
//   });
// }

//buildPlot();
//buildCandlestick();
