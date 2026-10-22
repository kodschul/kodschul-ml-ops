"""
Produktionssystem: Modell-/Experiment-Versionierung mit MLflow.

Trainiert dieselben zwei Gewicht-Modell-Varianten wie train.py (Height-only,
Height+Age), protokolliert beide als MLflow-Runs (Parameter, Metriken,
Modell) und registriert die bessere Variante in der Model Registry mit dem
Alias "production".

Ausfuehren aus final-system/:
    python src/track.py
"""
import mlflow
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = "../data/people_stats.csv"

# Neuere MLflow-Versionen (ab 3.x) unterstuetzen den reinen Dateiordner
# ("file:./mlruns") nicht mehr als Tracking-Backend fuer die Model Registry.
# Eine lokale SQLite-Datenbank reicht fuer dieses System vollstaendig aus.
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("weight-prediction")

df = pd.read_csv(DATA_PATH)

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
        print(f"{name}: MAE={mae:.2f} kg, R2={r2:.3f}, run_id={run.info.run_id}")

# das Height+Age-Modell schneidet besser ab -> wird registriert
best_run_id = run_ids["height_age"]
model_uri = f"runs:/{best_run_id}/model"
result = mlflow.register_model(model_uri, "weight-predictor")
print("Registrierte Modellversion:", result.version)

client = mlflow.MlflowClient()
client.set_registered_model_alias("weight-predictor", "production", result.version)
print("Alias 'production' gesetzt auf Version", result.version)
