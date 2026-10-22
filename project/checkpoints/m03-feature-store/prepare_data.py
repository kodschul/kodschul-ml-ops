"""
Checkpoint: Lab 3.1 - Feature Stores, Vorbereitung der Parquet-Quelle.

Erzeugt feature_repo/data/people_stats_with_id.parquet aus
project/data/people_stats.csv (ergaenzt person_id und event_timestamp,
die Feast fuer jede Zeile benoetigt).

Ausfuehren aus dem project/-Ordner:
    python checkpoints/m03-feature-store/prepare_data.py
"""
import pandas as pd

df = pd.read_csv("data/people_stats.csv")
df["person_id"] = range(1, len(df) + 1)
df["event_timestamp"] = pd.Timestamp.now()
df = df.rename(columns={"Height": "height", "Age": "age", "Weight": "weight"})

out_path = "checkpoints/m03-feature-store/feature_repo/data/people_stats_with_id.parquet"
df[["person_id", "event_timestamp", "height", "age", "weight"]].to_parquet(out_path)
print(f"{len(df)} Zeilen geschrieben nach {out_path}")
