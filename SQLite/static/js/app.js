console.log('Hello')

function buildPlot() {
    /* data route */
    const url = "/api/exchanges/New York";
    d3.json(url).then(function(response) {
  
      console.log(response);
      buildYearChart(response);
    });
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
