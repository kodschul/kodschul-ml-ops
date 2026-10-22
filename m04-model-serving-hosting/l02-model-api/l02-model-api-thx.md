# Lab 4.2: Gewichts-Modell als API bereitstellen

**Leitfragen:**

<details>
<summary>Welche Informationen braucht die API zusätzlich zum Modell selbst?</summary>

Ein definiertes Eingabeformat (welche Felder, welcher Typ – hier `height`, `age`) und ein definiertes Ausgabeformat (hier: vorhergesagtes Gewicht). Ohne diese Vereinbarung weiß ein aufrufendes System nicht, wie es Anfragen stellen und Antworten lesen soll.

</details>

<details>
<summary>Wie würde dieser Endpunkt in einer echten Anwendung genutzt?</summary>

Eine andere Anwendung (z. B. eine Web-Oberfläche) schickt einen HTTP-Request mit Größe und Alter an die API und erhält die Vorhersage zurück, ohne selbst Python oder scikit-learn zu benötigen.

</details>

- Eine REST-API macht ein trainiertes Modell für beliebige Anwendungen über HTTP erreichbar.
- FastAPI übernimmt Validierung der Eingaben und Dokumentation der Schnittstelle automatisch.

## Endpunkt mit FastAPI

```python
# serve.py
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

- `BaseModel` (Pydantic) beschreibt Eingabe- und Ausgabeformat; FastAPI validiert eingehende Anfragen automatisch dagegen.
- `model.predict(row)` erwartet dieselben Spaltennamen (`Height`, `Age`), mit denen trainiert wurde; eine `DataFrame`-Zeile statt einer rohen Liste vermeidet eine scikit-learn-Warnung über fehlende Feature-Namen.

## API lokal starten

```bash
uvicorn serve:app --reload --port 8000
```

- `serve:app` verweist auf die Datei `serve.py` und das darin erzeugte `app`-Objekt.
- `--reload` startet die API bei Codeänderungen neu (nur für die Entwicklung).

## Request/Response-Format

| Teil | Format |
| --- | --- |
| Request (`POST /predict`) | JSON-Body: `{"height": 180, "age": 35}` |
| Response | JSON-Body: `{"predicted_weight_kg": 77.43}` |

## API testen

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"height": 180, "age": 35}'
```

FastAPI erzeugt unter `http://127.0.0.1:8000/docs` automatisch eine interaktive Dokumentationsseite, über die sich derselbe Request auch ohne `curl` ausprobieren lässt.

## Fazit

- Ein `BaseModel` definiert Eingabe- und Ausgabeformat einmal zentral.
- `uvicorn serve:app` startet die API lokal; `/docs` bietet eine Testoberfläche ohne zusätzliche Tools.
- Dasselbe Muster (Modell laden, Endpunkt definieren, Request/Response typisieren) funktioniert für jedes serialisierte scikit-learn-Modell.

Modul 5 prüft, ob die Daten, mit denen ein Modell läuft, noch zu den Trainingsdaten passen.
