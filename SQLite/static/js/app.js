console.log('Hello')

function buildPlot() {
    /* data route */
    const url = "/api/exchanges/New York";
    d3.json(url).then(function(response) {
  
      console.log(response);
      buildCandlestick(response);
    });
}

buildPlot();
