🌾 Smart Farming with AI and IoT – Virtual Irrigation System
This project simulates a smart farming system that uses AI to decide whether irrigation is needed, based on virtual sensor data (Temperature, Humidity, Soil Moisture, and Rainfall). It's deployed using Streamlit Cloud and trained with a Random Forest Classifier.

🚀 Features
Virtual sensor sliders for real-time control
AI model predicts irrigation needs
Interactive UI built with Streamlit
Deployable on Streamlit Cloud
Simulated data for testing ML pipeline



# Smart Farming: Virtual Irrigation Controller

An end-to-end IoT + ML project to predict irrigation needs using:
- Arduino Uno + Soil Sensor + DHT22
- Serial communication to Python
- FastAPI ML backend
- Streamlit frontend

## Run Instructions

1. Upload `arduino/smart_farming.ino` to Arduino Uno
2. Train your model or use `irrigation_model.pkl`
3. Start FastAPI:
   ```bash
   cd backend
   uvicorn app:app --reload
   ```
4. Run Serial Reader:
   ```bash
   cd serial_comm
   python serial_to_api.py
   ```
5. Run Streamlit UI:
   ```bash
   cd frontend
   streamlit run app_ui.py
   ```
🧠 Tech Stack
Python

Streamlit

Scikit-learn (RandomForestClassifier)

Pandas

Joblib

GitHub + Streamlit Cloud
