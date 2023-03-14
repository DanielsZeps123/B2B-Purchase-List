var marker = null;
var map;

function createMap(target, property = true) {
    var mapOptions = {
        center: [56.947561, 24.099315],
        zoom: 6
    }
    
    map = new L.map(target, mapOptions);
    
    var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    map.addLayer(layer);

    try {
        marker = L.marker([document.getElementById('lat').value, document.getElementById('lng').value]);
        marker.addTo(map);
    } catch {}
    if (!property) {
        map.on("click", function(e){
            if (marker != null) {
                map.removeLayer(marker);
            }
            marker = L.marker([e.latlng.lat, e.latlng.lng]);
            marker.addTo(map);
            document.getElementById('longitude').value = Math.round(e.latlng.lng * 100000) / 100000;
            document.getElementById('latitude').value = Math.round(e.latlng.lat * 100000) / 100000;
        })
        long = Number(document.getElementById('longitude').value);
        lat = Number(document.getElementById('latitude').value);
        marker = L.marker([lat, long]);
        marker.addTo(map);
    } else {
        long = Number(document.getElementById('longitude').innerHTML);
        lat = Number(document.getElementById('latitude').innerHTML);
        marker = L.marker([lat, long]);
        marker.addTo(map);
    }
}
