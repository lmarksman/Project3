const distinct = (value, index, self) => {
    return self.indexOf(value) === index;
}

function buildMultipleCandlestick(response)
{
    //Not currently functioning completely
    console.log("Candlestick");
    
    const stockIndex = response.Index.filter(distinct);
    console.log(stockIndex);

    let highDate=new Date(Math.max.apply(null,response.Date.map(date => new Date(date))));
    let lowDate=new Date(Math.min.apply(null,response.Date.map(date => new Date(date))));

    console.log(lowDate);
    console.log(highDate);

    let minLow = Math.min.apply(null, response.Low.map(Number));
    let maxHigh = Math.max.apply(null, response.High.map(Number));
    
    let data = [];
    for (let i=0; i<stockIndex.length; i++)
    {
        let candlestickData = [response].filter(response.Index == stockIndex);
        console.log(candlestickData[0]);
        let dates = candlestickData[i].Date.map(date => new Date(date));
        let openValues = candlestickData[i].Open.map(Number);
        let closeValues = candlestickData[i].Close.map(Number);
        let highValues = candlestickData[i].High.map(Number);
        let lowValues = candlestickData[i].Low.map(Number);

        //future enhancement for multiple color traces
        // let r = Math.round (Math.random () * 255);
        // let g = Math.round (Math.random () * 255);
        // let b = Math.round (Math.random () * 255);

        // let r2 = Math.round (Math.random () * 255);
        // let g2 = Math.round (Math.random () * 255);
        // let b2 = Math.round (Math.random () * 255);

        var trace1 = {
            x:dates,
            close:closeValues,
            decreasing: {line: {color: 'red'}}, //{color: `rgb (${r}, ${g}, ${b})`}},  
            high: highValues,
            increasing: {line: {color: 'green'}}, //{color: `rgb (${r2}, ${g2}, ${b2})`}}, 
            low: lowValues,
            open: openValues,
            type: "candlestick",
            xaxis: "x",
            yaxis: "y",
            name: stockIndex[i]
        };
        console.log(trace1);
        data.push(trace1);
    }
    // console.log(data);
    var layout = {
        dragmode: "zoom",
        margin:{
            r:10,
            t: 25,
            b: 40,
            l: 60
        },
        showlegend: true,
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
    // console.log(data);
    // console.log(layout);
    
    Plotly.newPlot("candlestick", data, layout);
}

function buildSingleCandlestick(response)
{
    const stockIndex = response.Index.filter(distinct);
    let dates = response.Date.map(date => new Date(date));
    let openValues = response.Open.map(Number);
    let closeValues = response.Close.map(Number);
    let highValues = response.High.map(Number);
    let lowValues = response.Low.map(Number);

    let highDate=new Date(Math.max.apply(null,response.Date.map(date => new Date(date))));
    let lowDate=new Date(Math.min.apply(null,response.Date.map(date => new Date(date))));

    console.log(lowDate);
    console.log(highDate);

    let minLow = Math.min.apply(null, response.Low.map(Number));
    let maxHigh = Math.max.apply(null, response.High.map(Number));

    var trace1 = {
        x:dates,
        close:closeValues,
        decreasing: {line: {color: 'red'}}, //{color: `rgb (${r}, ${g}, ${b})`}},  
        high: highValues,
        increasing: {line: {color: 'green'}}, //{color: `rgb (${r2}, ${g2}, ${b2})`}}, 
        low: lowValues,
        open: openValues,
        type: "candlestick",
        xaxis: "x",
        yaxis: "y",
        name: stockIndex
    };
    console.log(trace1);
    let data =[trace1];

    // console.log(data);
    var layout = {
        dragmode: "zoom",
        margin:{
            r:10,
            t: 25,
            b: 40,
            l: 60
        },
        showlegend: true,
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
    // console.log(data);
    // console.log(layout);

    Plotly.newPlot("candlestick", data, layout);
}
