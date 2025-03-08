// ======== Google Maps API Initialization ========
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 28.6139, lng: 77.2090 }, // Default location (New Delhi)
        zoom: 14,
    });

    const trafficLayer = new google.maps.TrafficLayer();
    trafficLayer.setMap(map);
}

// ======== Fetch Real-time Traffic Data ========
async function fetchTrafficData() {
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ traffic_data: [30, 40, 50, 60, 70, 80] })
        });

        const data = await response.json();
        updateTrafficStatus(data.prediction);
    } catch (error) {
        console.error("Error fetching traffic data:", error);
    }
}

// ======== Update Traffic Status on Dashboard ========
function updateTrafficStatus(status) {
    document.getElementById("traffic-status").innerText = `Traffic: ${status}`;
}

// ======== Chart.js for Traffic Analysis ========
const ctx = document.getElementById("trafficChart").getContext("2d");
const trafficChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"],
        datasets: [{
            label: "Traffic Density",
            data: [30, 40, 50, 60, 70, 80],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 2,
        }]
    },
    options: {
        responsive: true,
        animation: { duration: 1000 },
    }
});

// ======== Manual Signal Control ========
function changeSignal(color) {
    document.getElementById("signal-status").innerText = `Signal: ${color.toUpperCase()}`;
}

// ======== Emergency Vehicle Detection (Simulated) ========
function detectEmergencyVehicle() {
    alert("🚨 Emergency Vehicle Detected! Changing Signal to GREEN 🚦");
    changeSignal("green");
}

// ======== Set Interval to Update Traffic Data Every 10 Seconds ========
setInterval(fetchTrafficData, 10000);

// ======== Load Google Maps on Window Load ========
window.onload = function () {
    initMap();
    fetchTrafficData();
};
