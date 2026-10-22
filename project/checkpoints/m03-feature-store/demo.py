"""
Checkpoint: Lab 3.1 - Feature Stores, Features abrufen.

Liegt bewusst ausserhalb von feature_repo/: `feast apply` importiert
jede .py-Datei in diesem Ordner, um Feature-Definitionen zu finden. Ein
Skript, das beim Import bereits Features abfragt, wuerde `feast apply`
zum Absturz bringen, bevor die Feature View uberhaupt registriert ist.

Voraussetzung: feature_repo/data/people_stats_with_id.parquet existiert
(siehe prepare_data.py) und `feast apply` + `feast materialize` wurden
im feature_repo/-Ordner ausgefuehrt (siehe README.md in diesem Ordner).

Ausfuehren aus dem m03-feature-store/-Ordner:
    python demo.py
"""
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")
result = store.get_online_features(
    features=["person_features:height", "person_features:age"],
    entity_rows=[{"person_id": 42}],
).to_dict()
print(result)
