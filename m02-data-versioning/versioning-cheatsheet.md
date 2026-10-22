# Versionierungs-Cheatsheet (DVC + MLflow)

Schnellreferenz für die in Modul 2 verwendeten Befehle: DVC für Daten, MLflow für Modelle/Experimente.

## DVC (Daten)

| Befehl | Wirkung |
| --- | --- |
| `dvc init` | DVC in einem bestehenden Git-Repository einrichten |
| `dvc add <datei>` | Datei in den DVC-Cache verschieben, `.dvc`-Verweisdatei erzeugen |
| `git add <datei>.dvc` | Verweisdatei in Git aufnehmen (nicht die echten Daten) |
| `git log --oneline -- <datei>.dvc` | Versionsverlauf einer Datendatei anzeigen |
| `git checkout <commit> -- <datei>.dvc` | Verweisdatei auf einen früheren Stand zurücksetzen |
| `dvc checkout` | echte Daten passend zur aktuellen `.dvc`-Datei wiederherstellen |
| `dvc remote add <name> <url>` | Remote-Storage für Teamarbeit einrichten (in diesem Kurs nicht verwendet) |
| `dvc push` / `dvc pull` | Daten zu/von einem Remote synchronisieren (in diesem Kurs nicht verwendet) |

### Ablaufmuster für einen Daten-Rollback

1. `git log --oneline -- <datei>.dvc` → gewünschten Commit-Hash finden.
2. `git checkout <commit> -- <datei>.dvc` → Verweisdatei zurücksetzen.
3. `dvc checkout` → echte Datei passend dazu wiederherstellen.

## MLflow (Modelle/Experimente)

| Befehl/Code | Wirkung |
| --- | --- |
| `mlflow.set_tracking_uri("sqlite:///mlflow.db")` | Tracking-Backend festlegen (Dateiordner reicht seit MLflow 3.x nicht mehr für die Registry) |
| `mlflow.set_experiment("<name>")` | Experiment auswählen/anlegen, gruppiert zusammengehörige Runs |
| `mlflow.start_run()` | neuen Run öffnen, alles im `with`-Block gehört dazu |
| `mlflow.log_param(<name>, <wert>)` | einen Trainings-Parameter protokollieren |
| `mlflow.log_metric(<name>, <wert>)` | eine Metrik protokollieren (z. B. MAE, R²) |
| `mlflow.sklearn.log_model(model, name="model")` | trainiertes Modell als Teil des Runs speichern |
| `mlflow.register_model(<uri>, "<name>")` | Modell aus einem Run in die Model Registry aufnehmen |
| `client.set_registered_model_alias(<name>, "production", <version>)` | Version als aktuell produktiv markieren |
| `mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001` | Weboberfläche starten (Port 5001 statt 5000 wegen macOS-AirPlay-Konflikt) |

### Ablaufmuster für Tracking + Registry

1. Tracking-URI + Experiment setzen.
2. Je Trainingsvariante einen Run mit Parametern, Metriken und Modell protokollieren.
3. Beste Variante über `register_model` registrieren.
4. Registrierte Version mit `set_registered_model_alias` als `production` markieren.
5. In der MLflow-UI alle Runs vergleichen, bevor der Alias gesetzt wird.

