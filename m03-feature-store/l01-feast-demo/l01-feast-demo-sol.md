# Lab 3.1 – Lösung: Feature Stores – Konzept und Mini-Demo mit Feast

## Aufgabe 1: Parquet-Quelle erzeugen

```python
import pandas as pd

df = pd.read_csv("project/data/people_stats.csv")
df["person_id"] = range(1, len(df) + 1)
df["event_timestamp"] = pd.Timestamp.now()
df = df.rename(columns={"Height": "height", "Age": "age", "Weight": "weight"})

df[["person_id", "event_timestamp", "height", "age", "weight"]].to_parquet(
    "feature_repo/data/people_stats_with_id.parquet"
)
```

## Aufgaben 2-3: `feature_store.yaml` und `features.py`

```yaml
# feature_repo/feature_store.yaml
project: mlops_course
registry: data/registry.db
provider: local
online_store:
  type: sqlite
  path: data/online_store.db
entity_key_serialization_version: 3
```

```python
# feature_repo/features.py
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64
from feast.value_type import ValueType

person = Entity(name="person_id", join_keys=["person_id"], value_type=ValueType.INT64)

source = FileSource(
    path="data/people_stats_with_id.parquet",
    timestamp_field="event_timestamp",
)

person_features = FeatureView(
    name="person_features",
    entities=[person],
    schema=[
        Field(name="height", dtype=Float32),
        Field(name="age", dtype=Int64),
    ],
    source=source,
)
```

## Aufgaben 4-5: Anwenden und befüllen

```bash
cd feature_repo
feast apply
feast materialize 2025-01-01T00:00:00 2027-01-01T00:00:00
```

## Aufgabe 6: Features abrufen

```python
# demo.py – liegt eine Ebene ÜBER feature_repo/, nicht darin!
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")
result = store.get_online_features(
    features=["person_features:height", "person_features:age"],
    entity_rows=[{"person_id": 42}],
).to_dict()
print(result)
```

Getestet (`feast` 0.67.0): `{'person_id': [42], 'height': [171.0], 'age': [39]}` – identisch mit Zeile 42 in `people_stats.csv` (`171,72,39`).

## Grenzen

Dieser Durchlauf bleibt eine Demo ohne Anbindung an Lab 1.2/4.2 – `height`/`age` kommen in der realen Projektpipeline weiterhin direkt aus `people_stats.csv`, nicht aus Feast.
