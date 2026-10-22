#!/usr/bin/env python3
"""
Checkpoint: Lab 6.1 - MLOps Best Practices, Metrikvergleich vor dem Promoten.

Operationalisiert die Kernregel aus Modul 6 ("Tun: ein neues Modell erst nach
Metrikvergleich als production markieren"): liest beide Runs aus dem
MLflow-Experiment von Lab 2.3 (mlflow_tracking.py), vergleicht ihre MAE und
entscheidet erst danach, welche registrierte Version den Alias "production"
behalten soll - statt das zuletzt trainierte Modell blind zu uebernehmen.

Voraussetzung: checkpoints/m02-data-versioning/mlflow_tracking.py wurde
bereits einmal ausgefuehrt (erzeugt project/mlflow.db mit beiden Runs und
der registrierten "weight-predictor").

Ausfuehren aus project/:
    python checkpoints/m06-mlops-best-practices/compare_before_promote.py
"""
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
client = mlflow.MlflowClient()

experiment = client.get_experiment_by_name("weight-prediction")
if experiment is None:
    raise SystemExit(
        "Kein Experiment 'weight-prediction' gefunden - zuerst "
        "checkpoints/m02-data-versioning/mlflow_tracking.py ausfuehren."
    )

runs = client.search_runs(experiment.experiment_id, order_by=["start_time ASC"])
if len(runs) < 2:
    raise SystemExit("Weniger als 2 Runs gefunden - mlflow_tracking.py liefert beide Varianten.")

print("Gefundene Runs:")
for run in runs:
    name = run.data.tags.get("mlflow.runName", run.info.run_id)
    mae = run.data.metrics.get("mae_kg")
    print(f"  {name}: mae_kg={mae:.2f}, run_id={run.info.run_id}")

best_run = min(runs, key=lambda r: r.data.metrics["mae_kg"])
best_name = best_run.data.tags.get("mlflow.runName", best_run.info.run_id)
print(f"\nBester Run nach Metrikvergleich: {best_name} (mae_kg={best_run.data.metrics['mae_kg']:.2f})")

model_name = "weight-predictor"
current_prod_version = None
try:
    current_prod = client.get_model_version_by_alias(model_name, "production")
    current_prod_version = current_prod.version
    current_prod_run = client.get_run(current_prod.run_id)
    current_prod_mae = current_prod_run.data.metrics.get("mae_kg")
    print(f"Aktuell als 'production' markiert: Version {current_prod_version} (mae_kg={current_prod_mae:.2f})")
except mlflow.exceptions.MlflowException:
    print("Noch keine Version mit Alias 'production' markiert.")

if current_prod_version is not None and current_prod_run.info.run_id == best_run.info.run_id:
    print("Entscheidung: aktuelle 'production'-Version ist bereits die beste - keine Aenderung noetig.")
else:
    versions = client.search_model_versions(f"name='{model_name}'")
    target_version = next(
        (v for v in versions if v.run_id == best_run.info.run_id), None
    )
    if target_version is None:
        print(
            "Entscheidung: bester Run ist noch nicht registriert - erst "
            "mlflow.register_model() aufrufen, dann diesen Vergleich erneut laufen lassen."
        )
    else:
        client.set_registered_model_alias(model_name, "production", target_version.version)
        print(f"Entscheidung: Alias 'production' auf Version {target_version.version} gesetzt (nach Metrikvergleich, nicht blind).")
