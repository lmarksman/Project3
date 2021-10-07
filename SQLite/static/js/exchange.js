

//Europe - expected range 0.60-1.30
var trace1 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };
  
  //Hong Kong - expected range 7.60-7.90
  var trace2 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //China - expected range 6.00-8.30
  var trace3 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //Japan - expected range 75.50-134.90
  var trace4 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //Canada - expected range 0.90-1.70
  var trace5 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //India - expected range 44-77
  var trace6 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //Korea - expected range 900.40-1583
  var trace7 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //Swiss - expected range 0.70-1.90
  var trace8 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  //South Africa - expected range 5.60-19.10
  var trace9 = {
    x: ['Date'],
    y: [],
    type: 'scatter'
  };

  var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9];
  
  
  Plotly.newPlot('exchange', data);