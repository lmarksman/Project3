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
        // height: 375,
        // width: 600,
        title: `Volume For ${year}`
        
      };
      
      
      
      Plotly.newPlot('piechart', trace, layout);
    });
}

function buildPieChart2(stockIndex, stockName){
    console.log("PieChart2");

    d3.json(`api/pie2/${stockIndex}`).then((data) => {
        console.log(data);

        let trace = [{
        values: data["Volume"],
        labels: data["Year"],
        type: 'pie',
        sort:false   ,
        rotation: 180     
      }];
      
      
      var layout = {
        // height: 375,
        // width: 600,
        title: `${stockName}`
      };
      
      
      Plotly.newPlot('piechart2', trace, layout);
    });
}

buildPieChart(2021);
buildPieChart2("NYA", "New York Stock Exchange");