function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  // YOUR CODE HERE
  // Use `Plotly.restyle` to update the pie chart with the newdata array
  Plotly.restyle("pie", "values", [newdata]);
}

function getData(dataset) {
  // YOUR CODE HERE
  // create a select statement to select different data arrays (YOUR CHOICE)
  // whenever the dataset parameter changes. This function will get called
  // from the dropdown event handler.
 let data = [];


  switch(dataset) {
    case "US":
      data = [34, 46, 87, 90];
      break;
    case "UK":
      data = [120, 26, 27, 65];
      break;
    case "CA":
      data = [23, 78, 54, 88];
      break;
    default:
      data = [19, 26, 55, 88];
      break;
  }

  updatePlotly(data);
}

init();
