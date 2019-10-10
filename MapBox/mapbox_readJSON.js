// Creating map object
var map = L.map("map", {
  center: [40.7128, -74.0059],
  zoom: 11
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "MyID",
  accessToken: API_KEY
}).addTo(map);

// Link to JSON data
var link = "http://myURL"

// Grabbing our GeoJSON data..
d3.json(link, function(data) {

	// Creating a geoJSON layer with the retrieved data
	L.geoJson(data, {

		// Style each feature (in this case a neighborhood)
	    style: function(x) {
	      	return {
				color: "white",
				// Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
				fillColor: chooseColor(x.properties.borough),
				fillOpacity: 0.5,
				weight: 1.5
	    	};
    	},
	}).addTo(map);
});