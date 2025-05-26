import streamlit as st
import requests

st.set_page_config(page_title="Smart Farming", layout="centered")
st.title("🌿 Smart Farming: Virtual Irrigation Controller")

temperature = st.slider("Temperature (°C)", 15, 45, 30)
humidity = st.slider("Humidity (%)", 20, 100, 50)
soil = st.slider("Soil Moisture (%)", 0, 100, 30)
rainfall = st.slider("Rainfall (mm)", 0, 20, 1)

if st.button("Predict"):
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": soil,
        "rainfall": rainfall
    }
    res = requests.post("http://127.0.0.1:8000/predict", json=data)
    st.success(f"Prediction: {'Irrigate' if res.json()['prediction'] else 'No Irrigation'}")
