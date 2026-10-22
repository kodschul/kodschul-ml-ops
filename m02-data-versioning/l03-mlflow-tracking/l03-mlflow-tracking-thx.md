# Lab 2.3: Modelle und Experimente versionieren mit MLflow

**Leitfragen:**

<details>
<summary>Was unterscheidet Datenversionierung (DVC) von Modell-/Experiment-Versionierung (MLflow)?</summary>

DVC versioniert die Eingabedaten (welche Zeilen, welcher Stand). MLflow versioniert, was beim Training daraus entsteht: welche Parameter wurden genutzt, welche Metriken kamen heraus, welches Modell wurde gespeichert – pro Trainingslauf (Run), nicht pro Datei.

</details>

<details>
<summary>Warum reicht eine gespeicherte Modell-Datei (`weight_model.joblib`) allein nicht aus?</summary>

Eine `.joblib`-Datei enthält nur das fertige Modell, aber nicht, mit welchen Features, welchem Datenstand oder welcher Güte (MAE, R²) es trainiert wurde. Ohne diese Angaben lässt sich ein Modell später nicht mit einer Alternative vergleichen oder nachvollziehen, warum gerade diese Version produktiv ist.

</details>

<details>
<summary>Was bedeutet es, ein Modell in der Model Registry mit dem Alias „production" zu markieren?</summary>

Es zeigt, welche von mehreren registrierten Versionen aktuell die produktiv genutzte ist – ohne Dateien umzubenennen. Eine Anwendung fragt immer „das Modell mit Alias production" ab; welche Versionsnummer dahintersteckt, kann sich ändern, ohne dass der aufrufende Code angepasst werden muss.

</details>

- MLflow Tracking protokolliert zu jedem Trainingslauf (Run) die genutzten Parameter, die gemessenen Metriken und das Modell selbst – nachvollziehbar und vergleichbar, auch wenn mehrere Varianten ausprobiert werden.
- Die Model Registry verwaltet durchnummerierte Versionen eines benannten Modells und erlaubt es, eine bestimmte Version per Alias als aktuell produktiv zu markieren.
- Dieses Lab nutzt dieselben zwei Modellvarianten aus Lab 1.2 (`Height` allein vs. `Height`+`Age`) – diesmal wird aber jeder Lauf mitprotokolliert statt nur das Endergebnis zu sehen.

## MLflow Tracking einrichten

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("weight-prediction")
```

Neuere MLflow-Versionen (ab 3.x) unterstützen den klassischen reinen Dateiordner (`file:./mlruns`) nicht mehr als Tracking-Backend für die Model Registry – eine lokale SQLite-Datenbank reicht für eine Einzelperson/einen Kurstag vollständig aus und wird beim ersten Lauf automatisch angelegt.

## Zwei Trainingsläufe protokollieren

```python
with mlflow.start_run(run_name="height_age") as run:
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mlflow.log_param("features", "Height,Age")
    mlflow.log_metric("mae_kg", mean_absolute_error(y_test, y_pred))
    mlflow.log_metric("r2", r2_score(y_test, y_pred))
    mlflow.sklearn.log_model(model, name="model")
```

- `mlflow.start_run()` öffnet einen Run; alles, was innerhalb des `with`-Blocks protokolliert wird, gehört zu genau diesem Trainingslauf.
- `log_param` hält fest, womit trainiert wurde (hier: welche Features); `log_metric` hält fest, wie gut das Ergebnis war; `log_model` speichert das trainierte Modell selbst als Teil des Runs.

Getestet (`mlflow` 3.17.2), beide Varianten aus Lab 1.2 als eigene Runs protokolliert:

```text
height_only: MAE=7.36 kg, R2=0.037
height_age:  MAE=6.66 kg, R2=0.290
```

## Modell registrieren und als „production" markieren

```python
model_uri = f"runs:/{best_run_id}/model"
result = mlflow.register_model(model_uri, "weight-predictor")

client = mlflow.MlflowClient()
client.set_registered_model_alias("weight-predictor", "production", result.version)
```

Das Height+Age-Modell (niedrigerer MAE) wird registriert und erhält den Alias `production`. Ältere MLflow-Tutorials verwenden stattdessen „Stages" (`Staging`/`Production`) – das ist mittlerweile veraltet; Aliase sind die aktuelle, empfohlene Variante.

## MLflow UI öffnen

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001
```

Unter `http://127.0.0.1:5001` zeigt die UI alle Runs des Experiments `weight-prediction` nebeneinander (Parameter, Metriken, Dauer) sowie unter „Models" die registrierte `weight-predictor` mit ihren Versionen und Aliasen. Port `5001` statt des MLflow-Standardports `5000`, weil Port `5000` auf macOS häufig bereits vom AirPlay-Empfänger belegt ist.

## Plattform-Vergleich: MLflow, Kubeflow, Metaflow

MLflow deckt heute Tracking + Model Registry ab. Größere Teams/Projekte nutzen teils umfassendere Plattformen, die zusätzlich Pipeline-Orchestrierung und Infrastruktur bündeln:

| Plattform | Fokus | Auswahlkriterium |
| --- | --- | --- |
| MLflow | Tracking, Model Registry, optional Serving | einzelne/kleine Teams, einfacher Einstieg, wenig Infrastruktur nötig |
| Kubeflow | komplette ML-Pipelines auf Kubernetes (Training, Serving, Orchestrierung) | größere Teams, bereits vorhandene Kubernetes-Infrastruktur |
| Metaflow | Workflow-Orchestrierung für Data-Science-Pipelines, Fokus auf Entwicklerfreundlichkeit | Teams mit komplexen, mehrstufigen Pipelines, weniger Infrastruktur-Overhead als Kubeflow |

Für dieses Projekt (1 Person, ein Modell) ist MLflow allein ausreichend – der Vergleich dient der Einordnung für größere Vorhaben, nicht als Entscheidung für heute.

## Fazit

- MLflow Tracking macht Trainingsläufe nachvollziehbar und vergleichbar – es ergänzt DVC (Datenversionierung) um die Modell-/Experiment-Seite.
- Die Model Registry trennt „ein Modell existiert" von „ein Modell ist aktuell produktiv" über Versionen und Aliase statt manuellem Dateiumbenennen.
- Damit ist für das Gewicht-Projekt ab jetzt nachvollziehbar, welcher Datenstand (DVC), welcher Code (Git) und welches trainierte Modell mit welchen Metriken (MLflow) zusammengehören.

Modul 3 zeigt als Nächstes, wie Features statt ganzer Dateien konsistent zwischen Training und Produktivbetrieb bereitgestellt werden.
