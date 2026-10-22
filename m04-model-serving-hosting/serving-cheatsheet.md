# Serving-Cheatsheet

Schnellreferenz für die in Modul 4 verwendeten Befehle und Bausteine.

| Befehl/Baustein | Wirkung |
| --- | --- |
| `joblib.dump(model, "datei.joblib")` | trainiertes Modell speichern |
| `joblib.load("datei.joblib")` | gespeichertes Modell laden |
| `class X(BaseModel): ...` | Eingabe-/Ausgabeformat für FastAPI definieren (Pydantic) |
| `@app.post("/pfad")` | HTTP-Endpunkt für eingehende Anfragen definieren |
| `uvicorn datei:app --reload --port 8000` | FastAPI-App lokal starten |
| `http://127.0.0.1:8000/docs` | automatisch erzeugte, interaktive API-Dokumentation |
| `curl -X POST <url> -d '<json>'` | Endpunkt von der Kommandozeile aus testen |

## Serving-Optionen im Überblick

| Option | Wann |
| --- | --- |
| Modell im Code laden | eine einzelne Anwendung |
| Einfache REST-API (FastAPI) | kleine Projekte, wenige Nutzer:innen |
| MLflow Model Serving | mehrere Modellversionen, Teamnutzung |
| TFServe / KServe | hohe Last, produktive Skalierung |
