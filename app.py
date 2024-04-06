import requests
import onnxruntime as ort
import numpy as np
from flask import Flask, request, render_template, jsonify
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
def predict_pump_status(soil_moisture, temperature, humidity):
    ort_session = ort.InferenceSession('models/model1.onnx')
    input_features = np.array([[soil_moisture, temperature, humidity]], dtype=np.float32)
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    prediction = ort_session.run([output_name], {input_name: input_features})[0]
    return prediction[0]

def predict_soil_moisture(temperature, humidity):
    ort_session = ort.InferenceSession('models/model2.onnx')
    input_features = np.array([[temperature, humidity, 0]], dtype=np.float32)
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    prediction = ort_session.run([output_name], {input_name: input_features})[0]
    return prediction[0]

ESP32_SERVER_IP = "192.168.104.210"  # Replace with the IP address of your ESP32 server

def get_timer(data):
    soil_moisture = data['moisture']
    temperature = data['temperature']
    humidity = data['humidity']
    pump_status = predict_pump_status(soil_moisture, temperature, humidity)

    if pump_status == 1:
        req_moisture = predict_soil_moisture(temperature, humidity)
        deficit = req_moisture - soil_moisture
        rate_of_restoration = 100
        timer = np.round(deficit / rate_of_restoration, 0)
        timer = str(timer[0])
        return timer, pump_status
    else:
        return '0', pump_status  # Returning '0' instead of 0 to maintain consistency with string representation

@app.route('/')
def index():
    return render_template('new_index.html')

@app.route('/sensor_data')
def get_sensor_data():
    try:
        response = requests.get(f"http://{ESP32_SERVER_IP}/data")
        sensor_data = response.json()
        timer, pump_status = get_timer(sensor_data)  # Get timer data and pump status
        sensor_data['timer'] = timer  # Add timer data to sensor data
        sensor_data['pump_status'] = int(pump_status)  # Convert pump_status to integer
        # Send pump_status back to ESP32 server
        requests.post(f"http://{ESP32_SERVER_IP}/pump_status", json={'pump_status': int(pump_status)})
    except Exception as e:
        print(f"Error fetching data from ESP32 server: {e}")
        sensor_data = {'humidity': 'N/A', 'moisture': 'N/A', 'temperature': 'N/A', 'timer': 'N/A', 'pump_status': 'N/A'}
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


