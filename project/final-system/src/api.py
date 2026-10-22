"""
Produktionssystem: Serving-API.

Stellt das trainierte Modell ueber einen /predict-Endpunkt bereit.
Voraussetzung: models/weight_model.joblib existiert (siehe train.py).

Starten aus final-system/:
    uvicorn src.api:app --reload --port 8000
"""
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = "models/weight_model.joblib"

app = FastAPI(title="Gewicht-Vorhersage-API")
model = joblib.load(MODEL_PATH)


class PredictionRequest(BaseModel):
    height: float
    age: float


class PredictionResponse(BaseModel):
    predicted_weight_kg: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    if request.height <= 0 or request.age <= 0:
        raise HTTPException(status_code=422, detail="height und age muessen positiv sein")
    row = pd.DataFrame([[request.height, request.age]], columns=["Height", "Age"])
    prediction = model.predict(row)
    return PredictionResponse(predicted_weight_kg=round(float(prediction[0]), 2))
