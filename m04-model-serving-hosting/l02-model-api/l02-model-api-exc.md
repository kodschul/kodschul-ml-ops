# Lab 4.2 – Übung: Gewichts-Modell als API bereitstellen

**Dauer:** ca. 45 Minuten
**Ändert die Gewicht-Projektbasis?** Ja – macht das in Lab 1.2 gespeicherte Modell über eine API nutzbar.

## Vorbereitung

`weight_model.joblib` aus Lab 1.2 (Erweiterung, Modell mit `Height` + `Age`) liegt im Arbeitsverzeichnis.

## Aufgaben

1. Lege eine Datei `serve.py` an, die das Modell lädt und eine FastAPI-App mit einem `/predict`-Endpunkt bereitstellt (Eingabe: `height`, `age`; Ausgabe: `predicted_weight_kg`).
2. Starte die API lokal mit `uvicorn`.
3. Rufe den Endpunkt mit der eigenen Größe und dem eigenen Alter auf (z. B. über `curl` oder `http://127.0.0.1:8000/docs`).
4. Rufe den Endpunkt ein zweites Mal mit einem unrealistischen Wert auf (z. B. `age: -5`) und beobachte, was passiert.

## Checkpoint

- Die API startet ohne Fehler und ist unter `http://127.0.0.1:8000/docs` erreichbar.
- Der `/predict`-Aufruf mit eigenen Werten liefert ein plausibles Gewicht in kg zurück.

## Abschlusskriterien

- Ein Satz, der beschreibt, was beim Aufruf mit `age: -5` passiert ist (z. B. ob das Modell trotzdem eine Zahl liefert, obwohl der Wert unrealistisch ist).

## Erweiterung

Ergänze eine einfache Prüfung im Endpunkt, die negative Werte für `height` oder `age` mit einer Fehlermeldung ablehnt, statt sie an das Modell weiterzugeben.
