from flask import Flask, jsonify, request
from model import predict_traffic
from encryption import encrypt_data, decrypt_data
import json
from datetime import datetime

app = Flask(__name__)

# Sample database to store real-time traffic data
traffic_data_db = []

@app.route('/')
def home():
    """
    Root API endpoint.
    Returns a welcome message for API testing.
    """
    return jsonify({"message": "Welcome to the Smart Traffic Management System "})


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to predict traffic conditions based on real-time sensor data.
    
    Request JSON format:
    {
        "traffic_data": [30, 40, 50, 60]
    }
    
    Returns:
    {
        "prediction": "Heavy Traffic"
    }
    """
    try:
        data = request.get_json()
        if 'traffic_data' not in data:
            return jsonify({"error": "Missing traffic_data in request"}), 400
        
        prediction = predict_traffic(data['traffic_data'])
        response = {"prediction": prediction}
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    API endpoint to encrypt messages for secure transmission.

    Request JSON format:
    {
        "message": "Emergency vehicle detected at Sector 45"
    }
    
    Returns:
    {
        "encrypted_message": "<encrypted_string>"
    }
    """
    try:
        data = request.get_json()
        if 'message' not in data:
            return jsonify({"error": "Missing message in request"}), 400

        encrypted_message = encrypt_data(data['message'])
        return jsonify({"encrypted_message": encrypted_message})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    API endpoint to decrypt messages.

    Request JSON format:
    {
        "encrypted_message": "<encrypted_string>"
    }

    Returns:
    {
        "decrypted_message": "Emergency vehicle detected at Sector 45"
    }
    """
    try:
        data = request.get_json()
        if 'encrypted_message' not in data:
            return jsonify({"error": "Missing encrypted_message in request"}), 400

        decrypted_message = decrypt_data(data['encrypted_message'])
        return jsonify({"decrypted_message": decrypted_message})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_traffic_data', methods=['POST'])
def add_traffic_data():
    """
    API endpoint to collect real-time traffic sensor data.

    Request JSON format:
    {
        "location": "Intersection A",
        "vehicle_count": 45,
        "timestamp": "2025-03-08T10:00:00"
    }
    
    Returns:
    {
        "message": "Traffic data added successfully"
    }
    """
    try:
        data = request.get_json()
        if not all(k in data for k in ["location", "vehicle_count"]):
            return jsonify({"error": "Missing fields in request"}), 400

        data["timestamp"] = datetime.now().isoformat()  # Add server timestamp
        traffic_data_db.append(data)
        return jsonify({"message": "Traffic data added successfully", "data": data})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_traffic_data', methods=['GET'])
def get_traffic_data():
    """
    API endpoint to retrieve the latest collected traffic data.
    
    Returns:
    {
        "traffic_data": [
            {
                "location": "Intersection A",
                "vehicle_count": 45,
                "timestamp": "2025-03-08T10:00:00"
            }
        ]
    }
    """
    try:
        return jsonify({"traffic_data": traffic_data_db})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
