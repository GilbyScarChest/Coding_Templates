// Pie Chart
let trace = {
    labels: ["beer", "wine", "martini", "margarita", "ice tea", "rum & coke", "mai tai", "gin & tonic"],
    values: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
    type: "pie"
};

let data = [trace];

let layout = {
    title: "Pie Chart"
};

Plotly.newPlot("plot", data, layout); // you don't need to have a '#' on 'plot' even though it's an id




// // Bar Chart
// let trace = {
//     x: ["beer", "wine", "martini", "margarita", "ice tea", "rum & coke", "mai tai", "gin & tonic"],
//     y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
//     type: "bar"
// };

// let data = [trace];

// let layout = {
//     title: "Bar Chart"
// };

// Plotly.newPlot("plot", data, layout);




// // Multiple Line Plot
// function randomNumberGenerator(n) {
// 	let randomNumberArray = [];
// 	for (let i = 0; i < n; i++){
// 		randomNumberArray.push(Math.floor(Math.random() * 10));
// 	}
// 	return randomNumberArray;
// }

// console.log(randomNumberGenerator(6));

// let trace1 = {
// 	x: [1, 2, 3, 4, 5],
// 	y: randomNumberGenerator(5),
// 	type: "line"
// };

// let trace2 = {
// 	x: [1, 2, 3, 4, 5],
// 	y: randomNumberGenerator(5),
// 	type: "line"
// };

// let data = [trace1, trace2];

// Plotly.newPlot("plot", data);


// Scatter Plots
// const hiJumpData = {
// 	x: data.year,
// 	y: data.high_jump,
// 	mode: "markers",
// 	type: "scatter",
// 	name: "high jump",
// 	marker: {
// 		color: "#2077b4",
// 		symbol: "hexagram"
// 	}
// };

// const discThrowData = {
// 	x: data.year,
// 	y: data.discus_throw,
// 	mode: "markers",
// 	type: "scatter",
// 	name: "disk throw",
// 	marker: {
// 		color: "orange",
// 		symbol: "diamond-x"
// 	}
// };

// const longJumpData = {
// 	x: data.year,
// 	y: data.long_jump,
// 	mode: "markers",
// 	type: "scatter",
// 	name: "long jump",
// 	marker: {
// 		color: "blue",
// 		symbol: "cross"
// 	}
// };

// let chartData = [hiJumpData, discThrowData, longJumpData];

// let layout = {
// 	title: "Olympic trends over the years",
// 	xaxis: {title: "Year"},
// 	yaxis: {title: "Olympic Event"},
// };

// Plotly.newPlot("plot", chartData, layout);
