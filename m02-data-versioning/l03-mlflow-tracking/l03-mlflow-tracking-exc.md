# Lab 2.3 – Übung: Modelle und Experimente versionieren mit MLflow

**Dauer:** ca. 45 Minuten
**Ändert die Gewicht-Projektbasis?** Ja – protokolliert die beiden Modelle aus Lab 1.2 als MLflow-Runs und registriert das bessere Modell.

## Vorbereitung

`mlflow` ist installiert (`pip install -r project/requirements.txt`). `project/data/people_stats.csv` liegt bereit.

## Aufgaben

1. Setze die MLflow-Tracking-URI auf `sqlite:///mlflow.db` und das Experiment auf `weight-prediction`.
2. Trainiere das Modell nur mit `Height` (wie in Lab 1.2) innerhalb eines `mlflow.start_run()`-Blocks; protokolliere Feature(s), MAE und R² sowie das Modell selbst.
3. Wiederhole Schritt 2 mit `Height`+`Age` als zweitem Run.
4. Registriere das Height+Age-Modell in der Model Registry unter dem Namen `weight-predictor`.
5. Markiere die registrierte Version mit dem Alias `production`.
6. Starte die MLflow-UI (`mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001`) und vergleiche beide Runs in der Oberfläche.

## Checkpoint

- Im Experiment `weight-prediction` sind zwei Runs sichtbar (`height_only`, `height_age`) mit jeweils eigenen Parametern und Metriken.
- Unter „Models" existiert `weight-predictor` mit mindestens einer Version und dem Alias `production`.

## Abschlusskriterien

- Beide Trainingsläufe sind in MLflow nachvollziehbar (Parameter + Metriken + Modell), und das bessere Modell trägt den Alias `production`.

## Fallback

Bei Zeitdruck wird Schritt 6 (UI-Vergleich) als Trainer-Demo gezeigt statt selbst geöffnet; die Schritte 1-5 (Protokollieren + Registrieren) werden in jedem Fall selbst ausgeführt.
