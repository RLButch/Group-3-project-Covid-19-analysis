// Base url for the data
let url = "/api/covid";

// Retrieve data using d3
d3.json(url).then(function(data) {
  console.log(data);
  createFeatures(data.features);
});

// Function to decide the size of the marker
function markerSize(cumulative_cases) {
  return cumulative_cases/5000000000;
}

// Function to decide the color of the marker
function selectColour(cumulative_deaths) {
  if (cumulative_deaths <= 100000) return "#00FFEA";
  else if (cumulative_deaths <= 300000) return "#00C8FF";
  else if (cumulative_deaths <= 500000) return "#0066FF";
  else if (cumulative_deaths <= 700000) return "#000DFF";
  else if (cumulative_deaths <= 900000) return "#2F255E";
  else return "#1A162B";
}

// Function to create features for the map
function createFeatures(geoData) {
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>Country: ${feature.properties.Country}</h3><hr><p>Cumulative_cases: ${feature.properties.Cumulative_cases}</p><hr><p>Cumulative_deaths: ${feature.properties.Cumulative_deaths}</p>`);
  }

  let covid_data = L.geoJSON(geoData, {
    onEachFeature: onEachFeature,

    // Features
    pointToLayer: function(feature, coordinate) {
      let markers = {
        radius: markerSize(feature.properties.Cumulative_cases),
        fillColor: selectColour(feature.properties.Cumulative_deaths),
        fillOpacity: 0.75,
        color: selectColour(feature.properties.Cumulative_deaths),
        weight: 1,
      };
      return L.circleMarker(coordinate, markers);
    }
  });

  createMap(covid_data);
}

function createMap(covid_data) {
  // Create the base layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Create a baseMaps object.
  let baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

  // Create an overlay object to hold our overlay.
  let overlayMaps = {
    Covid: covid_data
  };

  // Create our map, giving it the streetmap and covid_data layers to display on load.
  let myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5,
    layers: [street, covid_data]
  });

  // Create a layer control.
  // Pass it our baseMaps and overlayMaps.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);


  let legend = L.control({position: "bottomright"});

  legend.onAdd = function () {
  let div = L.DomUtil.create("div", "info legend"),
    cumulative_deaths = [0, 100000, 300000, 500000, 700000, 900000];

      //div.innerHTML += "<h3 style='text-align: center'>Depth</h3>"

  // loop through density intervals
  for (let i = 0; i < depth.length; i++) {
      div.innerHTML +=
          '<i style="background:' + selectColour(cumulative_deaths[i] + 1) + '"></i> ' +
          cumulative_deaths[i] + (cumulative_deaths[i + 1] ? '&ndash;' + cumulative_deaths[i + 1] + '<br>' : '+');
  }
  return div;
 };

 legend.addTo(myMap);

}


