var map = L.map('map').setView([20.5937, 78.9629], 5);

L.tileLayer(
'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
).addTo(map);

var marker;
var chart;

function searchCity() {

var city =
document.getElementById("cityInput").value;

fetch("/get_aqi/" + city)

.then(response => response.json())

.then(data => {

if (data.error) {

alert(data.error);
return;

}

document.getElementById("aqiValue")
.innerHTML =
"AQI: " + data.aqi;

document.getElementById("category")
.innerHTML =
"Category: " + data.category;

document.getElementById("advice")
.innerHTML =
"Health Advice: " + data.advice;

if (marker) {
map.removeLayer(marker);
}

marker = L.marker(
[data.lat, data.lon]
).addTo(map);

marker.bindTooltip(
"AQI: " + data.aqi
).openTooltip();

map.setView(
[data.lat, data.lon],
10
);

drawChart(data);

});

}

function drawChart(data) {

var ctx =
document.getElementById(
'pollutantChart'
).getContext('2d');

if (chart) {
chart.destroy();
}

chart = new Chart(ctx, {

type: 'bar',

data: {

labels: ["PM2.5","PM10","NO2","CO"],

datasets: [{

label: "Pollutant Levels",

data: [

data.pm25,
data.pm10,
data.no2,
data.co

]

}]

}

});

}