const distinct = (value, index, self) => {
  return self.indexOf(value) === index;
}

function buildYearChart(year) {

    console.log(year);
    // const stockIndex = response.Index.filter(distinct);
  
    d3.json(`api/years/${year}`).then((data) => {
      

  
      var trace1 = {
        type: 'scatter',
        x: data['Date'],
        y: data['Open'],
      };
      
      var trace = [ trace1 ];
      
      var layout = { 
        title: 'Years',
      };
      
      var config = {responsive: true}
      
      Plotly.newPlot('compare_open', trace, layout, config );
    
    })
  }

  function optionYearChanged(newYear) {
    buildYearChart(newYear);
  }

  
  buildYearChart("2000")
  
