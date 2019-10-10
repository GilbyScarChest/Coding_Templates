

// select an element
d3.select('ul')

// select all of one type of element
d3.select('ul').selectAll('li')

// declaring and assigning data to element 
var arr = [30, 25, 18];
d3.select('ul').selectAll('li').data(arr)


// .each() //
// .each() is similar to forEach() in vanilla javascript
d3.select('ul').selectAll('li').each(function(d,i) {
	console.log('element', this),
	console.log('index', i),
	console.log('data', d)
})

// .text //
// function that changes the text inside each element it iterated through
d3.select('ul').selectAll('li').data(arr).text(function(d){
	return d;
})

// Or
d3.select('ul').selectAll('li').data(arr).text(d => d)


// Remove/Replace //
// replace the value of the li element to the data in arr.
// Also add any new "li" elements to complete data in arr.
d3.select('ul')
	.selectAll('li')
	.data(arr)
	.enter()
	.append('li')
	.text(function(d) {
		return d;
	})

// remove values
d3.select('ul')
	.selectAll('li')
	.data(arr)
	.exit() // removes values specified in arr.
	.remove(); // remove anything not removed by exit. 


// .HTML //
// creating 3 divs to hold 3 different gifs
var complexData = [{
  title: "javascript",
  url: "https://media.giphy.com/media/10bdAP4IOmoN7G/giphy.gif"
},
{
  title: "python",
  url: "https://media.giphy.com/media/2yP1jNgjNAkvu/giphy.gif"
},
{
  title: "css",
  url: "https://media.giphy.com/media/TsxMkIKHpvFaU/giphy.gif"
}
];

d3.select(".img-gallery").selectAll("div") 
  .data(complexData)
  .enter() // creates placeholder for new data
  .append("div") // appends a div to placeholder
  .classed("col-md-4 thumbnail", true) // sets the class of the new div
  .html(function(d) {
    return `<img src="${d.url}">`;
 }); // sets the html in the div to an image tag with the link


 d3.select(".table-striped").select("tbody").selectAll("tr")
  .data(austinWeather)
  .enter() // creates placeholder for new data
  .append("tr") // appends a div to placeholde
  .html(function(d) {
    return `<td>${d.date}</td> <td>${d.low}</td> <td>${d.high}</td>`
 });











 var austinTemps = [76, 59, 59, 73, 71];

/** *********************************************************
 * 1. Basic Data Bind
 ********************************************************** */

// Basic Bind - Updates current elements
var austinTemps = [76, 59, 59, 73, 71];
d3.selectAll("#content").selectAll(".temps")
    .data(austinTemps)
    .style("height", function(d) {
      return d + "px";
    });


/** *********************************************************
 * 2. Updates only the new elements
 ********************************************************** */
// Enter - Updates New Elements
var austinTemps = [76, 59, 59, 73, 71];
d3.select("#content").selectAll(".temps")
    .data(austinTemps)
    .enter()
    .append("div")
    .classed("temps", true)
    .style("height", function(d) {
      return d + "px";
    });


/** *********************************************************
 * 3. Enter - Updates Only Old Elements
 ********************************************************** */
var austinTemps = [76, 59, 59, 73, 71];
var selection = d3.select("#content").selectAll(".temps")
    .data(austinTemps);

selection.enter()
    .append("div")
    .classed("temps", true);

selection.style("height", function(d) {
  return d + "px";
});


/** *********************************************************
 * 4. Enter - Updates All Elements
 ********************************************************** */
var austinTemps = [76, 59, 59, 73, 71];
var selection = d3.select("#content").selectAll(".temps")
    .data(austinTemps);

selection.enter()
    .append("div")
    .classed("temps", true)
    .merge(selection)
    .style("height", function(d) {
      return d + "px";
    });


/** *********************************************************
// 5. Exit Pattern
********************************************************** */
var austinTemps = [76];

var selection = d3.select("#content").selectAll(".temps")
    .data(austinTemps);

selection.enter()
    .append("div")
    .classed("temps", true)
    .merge(selection)
    .style("height", function(d) {
      return d + "px";
    });

selection.exit().remove();

/** *********************************************************
 * 6. Enter - Update - Exit Pattern Function
 * https://bl.ocks.org/mbostock/3808218
 ********************************************************** */

function update(data) {

  var selection = d3.select("#content").selectAll(".temps")
        .data(data);

  selection.enter()
        .append("div")
        .classed("temps", true)
        .merge(selection)
        .style("height", function(d) {
          return d + "px";
        });

  selection.exit().remove();
}

/* Test 1 */
var austinTemps = [100, 103, 105, 110, 100, 98];
update(austinTemps);

/* Test 2 */
austinTemps = [80];
update(austinTemps);



// Scale Linearly
// Scales the domain to fit the range.
var yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([0, 1000]);

// Or
var testScores = [50, 90, 95, 75, 85];

var svgHeight = 1000;

var yScale = d3.scaleLinear()
  .domain([0, d3.max(testScores)])
  .range([0, svgHeight]);


// .extent() gives you the min and max of an array.
d3.extent()