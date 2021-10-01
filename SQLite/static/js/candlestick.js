function buildCandlestick(response)
{
    console.log("Candlestick");
    let dates = response.Date.map(date => new Date(date));
    let openValues = response.Open.map(Number);
    let closeValues = response.Close.map(Number);
    let highValues = response.High.map(Number);
    let lowValues = response.Low.map(Number);

    let highDate=new Date(Math.max.apply(null,dates));
    let lowDate=new Date(Math.min.apply(null,dates));

    console.log(lowDate);
    console.log(highDate);

    let minLow = Math.min.apply(null, lowValues);
    let maxHigh = Math.max.apply(null, highValues);
    
    var trace1 = {
        x:dates,
        close:closeValues,
        decreasing: {line: {color: 'red'}}, 
        high: highValues,
        increasing: {line: {color: 'green'}}, 
        low: lowValues,
        open: openValues,
        type: "candlestick",
        xaxis: "x",
        yaxis: "y"
    };
    console.log(trace1);
    var data = [trace1];

    var layout = {
        dragmode: "zoom",
        margin:{
            r:10,
            t: 25,
            b: 40,
            l: 60
        },
        showlegend: false,
        xaxis: {
            autorange: true,
            domain: [0,1],
            range: [lowDate, highDate],
            rangeslider: {range: [lowDate, highDate]},
            title: "Date",
            type: "date"
        },
        yaxis: {
            autorange: true,
            domain: [0,1],
            range: [minLow, maxHigh],
            type: "linear"
        }
    };
    console.log(data);
    console.log(layout);
    
    Plotly.newPlot("candlestick", data, layout);

    // buildCandlestick2(response);
}

function buildCandlestick2(response)
{
    console.log("Candlestick2");
    let dates = response.Date.map(date => new Date(date));
    let openValues = response.Open.map(Number);
    let closeValues = response.Close.map(Number);
    let highValues = response.High.map(Number);
    let lowValues = response.Low.map(Number);

    let highDate=new Date(Math.max.apply(null,dates));
    let lowDate=new Date(Math.min.apply(null,dates));

    console.log(lowDate);
    console.log(highDate);

    let minLow = Math.min.apply(null, lowValues);
    let maxHigh = Math.max.apply(null, highValues);
    
    var trace1 = {
        x:dates,
        close:closeValues,
        high: highValues,
        low: lowValues,
        open: openValues,

        decreasing: {line: {color: '#7F7F7F'}}, 
        increasing: {line: {color: '#17BECF'}}, 
        
        type: "candlestick",
        xaxis: "x",
        yaxis: "y"
    };
    // console.log(trace1);
    let data = [trace1];

    let layout = {
        dragmode: 'zoom',
        showlegend: false,
        xaxis: {
          rangeslider: {
               visible: false
           }
        }
      };
    console.log(data);
    console.log(layout);
    
    Plotly.newPlot("candlestick2", data, layout);
}

