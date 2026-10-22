# Lab 6.1 – Übung: MLOps Best Practices & Anti-Patterns

**Dauer:** ca. 25 Minuten
**Ändert die Gewicht-Projektbasis?** Nein – reine Reflexionsübung zum gesamten Tag.

## Vorbereitung

Keine zusätzliche Installation; die Übung baut auf allen bisherigen Modulen des Tages auf.

## Aufgaben

Für jede der folgenden Aussagen: Tun (Best Practice) oder Nicht tun (Anti-Pattern) – und warum?

1. „Ich trainiere ein neues Modell und setze es direkt als `production`-Alias, ohne die Metriken mit der alten Version zu vergleichen."
2. „Ich committe `people_stats.csv.dvc` zusammen mit dem Code-Commit, der das Modell darauf trainiert."
3. „Ich installiere Pakete ohne Versionsangabe (`pip install evidently`), weil es schneller geht."
4. „Ich starte die API und teste sie zuerst selbst mit `curl`, bevor ich sie für andere freigebe."
5. „Ich überschreibe `people_stats.csv` mit neuen Daten, ohne vorher `dvc add` für den alten Stand auszuführen."
6. „Ich prüfe einmal im Monat mit Evidently, ob sich die Eingabedaten gegenüber dem Trainingsstand verändert haben."

## Checkpoint

- Für jede Aussage liegt eine Einordnung (Tun/Nicht tun) mit einer kurzen Begründung vor, die auf ein konkretes Modul des Tages verweist.

## Abschlusskriterien

- Alle sechs Aussagen sind eingeordnet und die Begründung verweist auf das jeweils passende Prinzip (Versionierung, Validierung, Reproduzierbarkeit, Monitoring).

## Erweiterung: Aussage 1 in Code nachvollziehen

Aussage 1 lässt sich direkt am eigenen MLflow-Stand aus Lab 2.3 praktisch nachvollziehen:

```bash
python checkpoints/m06-mlops-best-practices/compare_before_promote.py
```

Das Skript liest beide Runs (`height_only`, `height_age`) aus `mlflow.db`, vergleicht ihre MAE und setzt den Alias `production` erst danach – statt das zuletzt trainierte Modell blind zu übernehmen. Voraussetzung: Lab 2.3 (`mlflow_tracking.py`) wurde bereits einmal ausgeführt.

## Fallback

Bei Zeitdruck werden die Aussagen im Plenum besprochen statt einzeln schriftlich beantwortet; die Erweiterung entfällt dann ganz.
