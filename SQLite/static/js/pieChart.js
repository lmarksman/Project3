function buildPieChart(year){
    console.log("PieChart");

    d3.json(`api/pie/${year}`).then((data) => {
        console.log(data);

        let trace = [{
        values: data["Volume"],
        labels: data["Index"],
        type: 'pie'        
      }];
      
      
      var layout = {
        height: 600,
        width: 800,
        title: `Volume For ${year}`
      };
      
      
      Plotly.newPlot('piechart', trace, layout);
    });
}

function buildPieChart2(stockIndex){
    console.log("PieChart2");

    d3.json(`api/pie2/${stockIndex}`).then((data) => {
        console.log(data);

        let trace = [{
        values: data["Volume"],
        labels: data["Year"],
        type: 'pie'        
      }];
      
      
      var layout = {
        height: 600,
        width: 800,
        title: `Volume For ${stockIndex}`
      };
      
      
      Plotly.newPlot('piechart2', trace, layout);
    });
}

buildPieChart(2021);
buildPieChart2("NYA");