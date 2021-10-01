console.log('Hello')

function buildPlot() {
    /* data route */
    const url = "/api/exchange";
    d3.json(url).then(function(response) {
  
      console.log(response);
    });
}

buildPlot();
