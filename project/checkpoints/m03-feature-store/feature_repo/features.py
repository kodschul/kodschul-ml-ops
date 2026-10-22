"""
Checkpoint: Lab 3.1 - Feature Stores, Entity- und Feature-View-Definition.

Getestet mit feast 0.67.0.
"""
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
