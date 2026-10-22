"""
Checkpoint: Lab 4.2 - Gewichts-Modell als API bereitstellen.

Finale Version inklusive der Plausibilitaetspruefung aus der Erweiterung.
Voraussetzung: weight_model.joblib existiert im project/-Wurzelordner
(siehe train_linreg.py).

Lokal starten (aus dem Ordner dieser Datei, da `uvicorn` keine Bindestriche
in Modulpfaden akzeptiert):
    cd project/checkpoints/m04-model-serving-hosting
    uvicorn serve:app --reload --port 8000
"""
import os

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "weight_model.joblib")

app = FastAPI()
model = joblib.load(MODEL_PATH)


class PredictionRequest(BaseModel):
    height: float
    age: float


class PredictionResponse(BaseModel):
    predicted_weight_kg: float


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    if request.height <= 0 or request.age <= 0:
        raise HTTPException(status_code=422, detail="height und age muessen positiv sein")
    row = pd.DataFrame([[request.height, request.age]], columns=["Height", "Age"])
    prediction = model.predict(row)
    return PredictionResponse(predicted_weight_kg=round(float(prediction[0]), 2))
