// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);

// // Loop Through `data` and console.log each weather report object
data.forEach(function(weatherReport) {
  console.log(weatherReport);
});

// // Use d3 to update each cell's text with
// // weather report values (weekday, date, high, low)
data.forEach(function(weatherReport) {
  console.log(weatherReport);
  var row = tbody.append("tr");
  Object.entries(weatherReport).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = row.append("td");
    cell.text(value);
  });
});

// BONUS: Refactor to use Arrow Functions!
// data.forEach((weatherReport) => {
//   var row = tbody.append("tr");
//   Object.entries(weatherReport).forEach(([key, value]) => {
//     var cell = row.append("td");
//     cell.text(value);
//   });
// });