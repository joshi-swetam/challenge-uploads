// Store our API endpoint as queryUrl.
let queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// A function to determine the marker size based on the population
function markerSize(magnitude) {
    return magnitude * 5;
}

function getColor(d) {
    return d > 90 ? '#ff5f65' :
        d > 70  ? '#fca35d' :
        d > 50  ? '#fdb72a' :
        d > 30  ? '#f7db11' :
        d > 10   ? '#dcf400' :
                '#a3f600';
}

var geojsonMarkerOptions = {
    radius: 8,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

// Perform a GET request to the query URL.
d3.json(queryUrl).then(function (data) {
    var earthquakes = data.features;
    console.log(earthquakes);

    // Create the base layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });

    // Create a baseMaps object to contain the streetmap and the darkmap.
    var baseMaps = {
        "Street Map": street,
        "Topographic Map": topo
    };
    
  
    // Modify the map so that it has the streetmap, states, and cities layers
    var map = L.map("map", {
        center: [37.09, -95.71],
        zoom: 4,
        layers: [street]
    });

    let earthquakesLayer = L.geoJSON(earthquakes, {
                pointToLayer: function(feature, latlng) {
                    return new 
                            L.CircleMarker(latlng, {radius: markerSize(feature.properties.mag), fillColor: getColor(feature.geometry.coordinates[2]), fillOpacity: 0.85, color: "#000", weight:1, opacity: 1})
                            .bindPopup(`<h3>Magnitude: ${feature.properties.mag.toFixed(2)}</h3><h3>Location: ${feature.properties.place}</h3><h3>Depth: ${feature.geometry.coordinates[2].toFixed(2)}</h3>`)
                }
            }
        ).addTo(map);

    let overlyMaps = {
        "Earthquakes": earthquakesLayer
    }

    // Create a layer control that contains our baseMaps and overlayMaps, and add them to the map.
    L.control.layers(baseMaps, overlyMaps, {
        collapsed: false
    }).addTo(map);

    const legend = L.control({position: 'bottomright'});

	legend.onAdd = function (map) {

		const div = L.DomUtil.create('div', 'info legend');
		const grades = [-10, 10, 30, 50, 70, 90];
		const labels = [];
		let from, to;

		for (let i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(`<i style="background:${getColor(from + 1)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
		}

		div.innerHTML = labels.join('<br>');
		return div;
	};

	legend.addTo(map);
    
    

});