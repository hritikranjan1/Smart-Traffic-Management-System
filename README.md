# 🚦 Smart Traffic Management System

## 📖 About the Project
The **Smart Traffic Management System** is an **AI and IoT-powered solution** designed to reduce congestion, optimize traffic signals, and prioritize emergency vehicles. It integrates **machine learning, real-time sensor data, and cybersecurity** features to enhance road safety and efficiency.

## 🔹 Key Features
 ✔️ **Real-time Traffic Monitoring** (Google Maps API)
 
 ✔️ **AI-Based Traffic Prediction**
 ✔️ **IoT Sensor Integration** (NodeMCU, IR & Ultrasonic Sensors)
 ✔️ **Smart Traffic Light Control 🚦**
 ✔️ **Emergency Vehicle Detection 🚑**
 ✔️ **Cybersecurity with Data Encryption 🔐**

## 📂 Project Structure
```
Smart_Traffic_Management/
├── Backend/
│   ├── app.py                 # Flask Backend API
│   ├── model.py               # AI-based Traffic Prediction
│   ├── encryption.py          # Data Encryption
│   ├── requirements.txt       # Dependencies
├── IoT_Device/
│   ├── nodemcu_code.ino       # ESP8266 NodeMCU Code
│   ├── sensors.py             # Sensor Data Processing
├── Frontend/
│   ├── index.html             # Main Dashboard
│   ├── style.css              # Styling
│   ├── script.js              # Frontend Logic & API Calls
│   ├── dashboard.html         # Advanced Dashboard UI
└── README.md                  # Project Documentation
```

## 🛠️ Tech Stack Used
| **Component** | **Technologies Used** |
|--------------|----------------------|
| **Frontend** | HTML, CSS, JavaScript, Chart.js, Google Maps API |
| **Backend** | Python, Flask |
| **Machine Learning** | NumPy, Scikit-learn |
| **IoT Devices** | NodeMCU ESP8266, Sensors (IR, Ultrasonic, Vibration) |
| **Security** | Cryptography (Fernet Encryption) |

## 🚀 Installation Guide

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/hritikranjan1/Smart-Traffic-Management-System.git
cd Smart-Traffic-Management-System
```

### 🔹 2. Install Backend Dependencies
```sh
cd Backend
pip install -r requirements.txt
```

### 🔹 3. Run the Backend Server
```sh
python app.py
```
_Server runs at_ **http://127.0.0.1:5000**

### 🔹 4. Set Up IoT Device
- Upload **nodemcu_code.ino** to **ESP8266/NodeMCU**.
- Connect sensors:
  - **IR Sensor** – Counts vehicles
  - **Ultrasonic Sensor** – Measures traffic density
  - **Vibration Sensor** – Monitors road conditions
- Run **sensors.py** to send real-time data.

### 🔹 5. Start the Frontend
- Open **dashboard.html** in a browser.
- Ensure **script.js** fetches data from **http://127.0.0.1:5000**.

## 📡 API Endpoints

### 🚦 Traffic Prediction API
**Method:** `POST`
**Endpoint:** `/predict`
**Description:** Predicts traffic congestion.

#### 📌 Example Request
```json
{
  "traffic_data": [20, 45, 60, 80]
}
```

#### 📌 Response
```json
{
  "prediction": "Heavy Traffic"
}
```

## 🗺️ Live Dashboard Features
✔️ **Google Maps API for Live Traffic**
✔️ **Smart Traffic Signal Control 🚦**
✔️ **Emergency Vehicle Detection 🚑**
✔️ **Traffic Density Visualization (Chart.js) 📊**

## 🔐 Security Features
✔️ **Fernet Encryption** for Secure Data Transfer
✔️ **Authentication for API Endpoints**

## 🎯 Future Enhancements
✅ **AI-Driven Traffic Optimization**
✅ **Image Processing for Vehicle Detection**
✅ **Voice-Controlled Traffic Commands**

## 🤝 Contributing 🚀
Contributions are **welcome**! Follow these steps to contribute:

1. **Fork** the repo
2. **Create a new branch** (`feature-branch`)
3. **Commit changes** (`git commit -m "Added a new feature"`)
4. **Push to GitHub** (`git push origin feature-branch`)
5. **Submit a Pull Request 🎉**

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
📩 **Email:** hritikranjan1408@gmail.com  
🌐 **GitHub:** [hritikranjan1](https://github.com/hritikranjan1)  
💡 **Issues/Suggestions?** Open an issue in this repository!

## 📌 Show Your Support!
⭐ **Star this repository** if you found it useful!  
🐞 **Report issues** in the Issues tab!  
🚀 **Follow me on GitHub** for more cool projects!
