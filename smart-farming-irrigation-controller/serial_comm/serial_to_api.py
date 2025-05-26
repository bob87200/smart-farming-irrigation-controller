import serial
import requests

API_URL = "http://127.0.0.1:8000/predict"
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace with your COM port

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            temp, hum, soil, rain = map(float, line.split(','))
            data = {
                "temperature": temp,
                "humidity": hum,
                "soil_moisture": soil,
                "rainfall": rain
            }
            res = requests.post(API_URL, json=data)
            print("Prediction:", res.json())
    except Exception as e:
        print("Error:", e)
