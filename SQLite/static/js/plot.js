function buildYearChart(year, stockIndex) {

    console.log(year);
    // const stockIndex = response.Index.filter(distinct);
  
    d3.json(`api/years/${year}/${stockIndex}`).then((data) => {
      

  
      var trace1 = {
        type: 'scatter',
        x: data['Date'],
        y: data['Open'],
      };
      
      var trace = [ trace1 ];
      
      var layout = { 
        tickformat: '%d/%m'
        
      };
      
      var config = {responsive: true}
      
      Plotly.newPlot('compare_open', trace, layout, config );

    })
  }

  buildYearChart(2021, "NYA");
  
  
