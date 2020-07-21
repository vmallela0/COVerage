// NULL CODE

var long = 37.4275;
var lat = 122.1697;

window.onload = function getLocation() { // retrieves the client location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
};

function showPosition(position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
    var map = new ol.Map({
        target: 'map',
        layers: [
            // include county boundaries here
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            // centers map at user location and zooms
            center: ol.proj.fromLonLat([long, lat]),
            zoom: 12
        })
    });
}
