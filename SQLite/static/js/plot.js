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
// // USD -----------------------------------------------------------------------
//       //usd chart open
//       var trace_usd1 = {
//         type: 'scatter',
//         x: data['Date'],
//         y: data['Open_USD'],
//       };
      
//       var trace_openUSD = [ trace_usd1 ];
      
//       var layout = { 
//         tickformat: '%d/%m'
        
//       };
      
//       var config = {responsive: true}
      
//       Plotly.newPlot('openUSD', trace_openUSD, layout, config );

//       //usd chart close
//       var trace_usd2 = {
//         type: 'scatter',
//         x: data['Date'],
//         y: data['Close_USD'],
//       };
      
//       var trace_closeUSD = [ trace_usd2 ];
      
//       var layout = { 
//         tickformat: '%d/%m'
        
//       };
      
//       var config = {responsive: true}
      
//       Plotly.newPlot('closeUSD', trace_closeUSD, layout, config );


//       //usd chart high
//       var trace_usd3 = {
//         type: 'scatter',
//         x: data['Date'],
//         y: data['High_USD'],
//       };
      
//       var trace_highUSD = [ trace_usd3 ];
      
//       var layout = { 
//         tickformat: '%d/%m'
        
//       };
      
//       var config = {responsive: true}
      
//       Plotly.newPlot('highUSD', trace_highUSD, layout, config );


//       //usd chart low
//       var trace_usd4 = {
//         type: 'scatter',
//         x: data['Date'],
//         y: data['Low_USD'],
//       };
      
//       var trace_lowUSD = [ trace_usd4 ];
      
//       var layout = { 
//         tickformat: '%d/%m'
        
//       };
      
//       var config = {responsive: true}
      
//       Plotly.newPlot('lowUSD', trace_lowUSD, layout, config );
    
    })
  }

  buildYearChart(2021, "NYA");
  
  
