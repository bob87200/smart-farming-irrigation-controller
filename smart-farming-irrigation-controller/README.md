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
