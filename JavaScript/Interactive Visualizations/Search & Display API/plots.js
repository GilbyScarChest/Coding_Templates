const apiKey = "xgrTN11ANdPrJDavGTDL";

/* global Plotly */
const url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} data
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(data, index) {
  return data.map(function(row) {
    return row[index];
  });
}

/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {
  // @TODO: YOUR CODE HERE
  d3.json(url).then(function(data){
  	let name = data.dataset.name;
  	let stock = data.dataset.dataset_code;
  	let startDate = data.dataset.start_date;
  	let endDate = data.dataset.end_date;
  	let dates = unpack(data.dataset.data, 0);
  	let closingPrices = unpack(data.dataset.data, 1);

  	let trace1 = {
  		type: "scatter",
  		mode: "lines",
  		name: name,
  		x: dates,
  		y: closingPrices,
  		line: {
  			color: "#17BECF"
  		}
  	};

  	let chartData = [trace1];
  
	let layout = {
		title: `${stock} Closing Prices`,
		xaxis: {
			range: [startDate, endDate],
			type: 'date'
		},
		yaxis: {
			autorange: true,
			type: "linear"
		}
	};

	Plotly.newPlot("plot", chartData, layout);
  })
}

buildPlot();
