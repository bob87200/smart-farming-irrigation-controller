from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("backend/irrigation_model.pkl")

class SensorData(BaseModel):
    temperature: float
    humidity: float
    soil_moisture: float
    rainfall: float

app = FastAPI()

@app.post("/predict")
def predict(data: SensorData):
    features = [[data.temperature, data.humidity, data.soil_moisture, data.rainfall]]
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
