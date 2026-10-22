# Lab 2.3 – Lösung: Modelle und Experimente versionieren mit MLflow

## Aufgabe 1: Tracking-URI und Experiment setzen

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("weight-prediction")
```

## Aufgaben 2+3: Beide Modelle als Runs protokollieren

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("project/data/people_stats.csv")

configs = [
    ("height_only", ["Height"]),
    ("height_age", ["Height", "Age"]),
]

run_ids = {}

for name, features in configs:
    X = df[features]
    y = df["Weight"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=60
    )

    with mlflow.start_run(run_name=name) as run:
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        mlflow.log_param("features", ",".join(features))
        mlflow.log_metric("mae_kg", mae)
        mlflow.log_metric("r2", r2)
        mlflow.sklearn.log_model(model, name="model")

        run_ids[name] = run.info.run_id
        print(f"{name}: MAE={mae:.2f} kg, R2={r2:.3f}")
```

Ausgabe:

```text
height_only: MAE=7.36 kg, R2=0.037
height_age: MAE=6.66 kg, R2=0.290
```

## Aufgaben 4+5: Modell registrieren und als „production" markieren

```python
best_run_id = run_ids["height_age"]
model_uri = f"runs:/{best_run_id}/model"
result = mlflow.register_model(model_uri, "weight-predictor")

client = mlflow.MlflowClient()
client.set_registered_model_alias("weight-predictor", "production", result.version)
print("Alias 'production' gesetzt auf Version", result.version)
```

## Aufgabe 6: MLflow UI öffnen

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001
```

Unter `http://127.0.0.1:5001` sind im Experiment `weight-prediction` beide Runs sichtbar; `height_age` hat den niedrigeren `mae_kg`-Wert. Unter „Models" → `weight-predictor` zeigt die registrierte Version den Alias `production`.

## Grenzen

Dieser Durchlauf registriert das Modell, ersetzt aber nicht den in Lab 4.2 gebauten FastAPI-Endpunkt – der lädt weiterhin direkt `weight_model.joblib`. In einem größeren Projekt würde die API das Modell stattdessen über die Registry laden (`models:/weight-predictor@production`), um immer automatisch die aktuell markierte Version zu bekommen.
