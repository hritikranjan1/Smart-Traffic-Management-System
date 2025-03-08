#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "Your_SSID";      // Replace with your WiFi SSID
const char* password = "Your_PASSWORD";  // Replace with your WiFi Password
const char* serverUrl = "http://your-server-ip:5000/traffic"; // Replace with your Flask backend URL

WiFiClient client;
HTTPClient http;

// Sensor Pins
const int trafficSensor = A0;  // Analog pin for traffic density sensor
const int emergencyPin = D2;   // Digital pin for emergency vehicle detection

void setup() {
    Serial.begin(115200);
    
    // Connect to WiFi
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi");
    
    pinMode(emergencyPin, INPUT); // Set emergency sensor as input
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        http.begin(client, serverUrl);
        http.addHeader("Content-Type", "application/json");

        int trafficDensity = analogRead(trafficSensor); // Read traffic sensor data
        int emergencyStatus = digitalRead(emergencyPin); // Check for emergency vehicle

        // Prepare JSON payload
        String postData = "{ \"traffic_density\": " + String(trafficDensity) + 
                          ", \"emergency\": " + String(emergencyStatus) + " }";

        Serial.println("Sending Data: " + postData);

        int httpResponseCode = http.POST(postData);
        
        if (httpResponseCode > 0) {
            Serial.println("Response Code: " + String(httpResponseCode));
            String response = http.getString();
            Serial.println("Server Response: " + response);
        } else {
            Serial.println("Error in sending request");
        }

        http.end();
    } else {
        Serial.println("WiFi Disconnected! Reconnecting...");
        WiFi.begin(ssid, password);
    }

    delay(5000); // Send data every 5 seconds
}
