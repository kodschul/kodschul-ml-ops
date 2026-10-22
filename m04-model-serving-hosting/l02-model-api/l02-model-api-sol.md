# Lab 4.2 – Lösung: Gewichts-Modell als API bereitstellen

## Aufgabe 1: `serve.py`

```python
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("weight_model.joblib")


class PredictionRequest(BaseModel):
    height: float
    age: float


class PredictionResponse(BaseModel):
    predicted_weight_kg: float


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    row = pd.DataFrame([[request.height, request.age]], columns=["Height", "Age"])
    prediction = model.predict(row)
    return PredictionResponse(predicted_weight_kg=round(float(prediction[0]), 2))
```

## Aufgabe 2: API starten

```bash
uvicorn serve:app --reload --port 8000
```

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## Aufgabe 3: Endpunkt aufrufen

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"height": 180, "age": 35}'
```

Mit dem in Lab 1.2 trainierten Height+Age-Modell (Koeffizienten `[0.6352, 0.6445]`, Achsenabschnitt `-59.47`):

```json
{"predicted_weight_kg": 77.43}
```

## Aufgabe 4: Unrealistischer Wert

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"height": 180, "age": -5}'
```

Die API liefert trotzdem eine Zahl zurück (z. B. `{"predicted_weight_kg": 51.65}`), weil `age: -5` als gültige Zahl durchgeht – Pydantic prüft nur den Datentyp (`float`), nicht die fachliche Plausibilität. Das Modell selbst erkennt nicht, dass ein negatives Alter unsinnig ist.

## Erweiterung: Plausibilitätsprüfung ergänzen

```python
from fastapi import HTTPException


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    if request.height <= 0 or request.age <= 0:
        raise HTTPException(status_code=422, detail="height und age müssen positiv sein")
    row = pd.DataFrame([[request.height, request.age]], columns=["Height", "Age"])
    prediction = model.predict(row)
    return PredictionResponse(predicted_weight_kg=round(float(prediction[0]), 2))
```

## Grenzen

Diese Prüfung fängt nur offensichtlich unsinnige Werte ab (negativ oder null). Realistische, aber im Trainingsdatensatz nicht vorkommende Kombinationen (z. B. `height: 220`) lässt die API weiterhin durch – das Modell extrapoliert dann außerhalb des Bereichs, den es gelernt hat.
