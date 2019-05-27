//Get the data from data.js
let tableData = data;

// Get a reference to the table body
let tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);

// // Loop Through `data` and console.log each weather report object
tableData.forEach(function(item) {
  console.log(item);
});

// // Use d3 to update each cell's text with
// // weather report values (weekday, date, high, low)
tableData.forEach(function(item) {
  console.log(item);
  let row = tbody.append("tr");
  Object.entries(item).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    let cell = row.append("td");
    cell.text(value);
  });
});

// BONUS: Refactor to use Arrow Functions!
// data.forEach((item) => {
//   var row = tbody.append("tr");
//   Object.entries(item).forEach(([key, value]) => {
//     var cell = row.append("td");
//     cell.text(value);
//   });
// });