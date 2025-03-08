import random
import time
import requests
import json

# Server API Endpoint (Replace with your Flask backend URL)
SERVER_URL = "http://your-server-ip:5000/traffic"

def get_traffic_density():
    """
    Simulates reading traffic density from a sensor.
    Replace this with actual sensor data retrieval code if using real sensors.
    """
    return random.randint(10, 100)  # Simulating traffic density in percentage (10% - 100%)

def get_vibration_data():
    """
    Simulates reading vibration data (used for detecting potholes or road conditions).
    Replace this with real accelerometer or vibration sensor data.
    """
    return random.uniform(0.1, 2.5)  # Simulating vibration levels (G-force)

def detect_emergency_vehicle():
    """
    Simulates emergency vehicle detection using sound sensors, RFID, or other methods.
    """
    return random.choice([0, 1])  # 0 = No emergency vehicle, 1 = Emergency vehicle detected

def collect_sensor_data():
    """
    Collects sensor data and prepares it for sending to the backend.
    """
    traffic_density = get_traffic_density()
    vibration_level = get_vibration_data()
    emergency_status = detect_emergency_vehicle()

    sensor_data = {
        "traffic_density": traffic_density,
        "vibration_level": round(vibration_level, 2),
        "emergency_detected": emergency_status
    }

    return sensor_data

def send_data_to_server(data):
    """
    Sends sensor data to the Flask backend via an HTTP POST request.
    """
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(SERVER_URL, data=json.dumps(data), headers=headers)
        
        if response.status_code == 200:
            print(f"Data Sent Successfully: {data}")
        else:
            print(f"Failed to send data: {response.status_code}, {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        sensor_data = collect_sensor_data()
        send_data_to_server(sensor_data)
        time.sleep(5)  # Sends data every 5 seconds
