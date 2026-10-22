# Lab 3.1: Feature Stores – Konzept und Mini-Demo mit Feast

**Leitfragen:**

<details>
<summary>Welches Problem löst ein Feature Store, das einzelne Dateien nicht lösen?</summary>

Ein Feature Store stellt sicher, dass dieselbe Berechnung eines Features (z. B. `height` in cm) beim Training und beim Live-Betrieb verwendet wird. Einzelne CSV-Dateien oder Code-Kopien laufen sonst leicht auseinander, wenn die Berechnung an zwei Stellen gepflegt werden muss.

</details>

<details>
<summary>Wo würden `height`/`age` sonst doppelt berechnet oder inkonsistent abgelegt werden?</summary>

Im Trainingsskript (Lab 1.2) werden `Height`/`Age` direkt aus der CSV gelesen. In einer produktiven API (Lab 4.2) müssten dieselben Werte erneut irgendwo herkommen – ohne Feature Store oft aus einer zweiten, separat gepflegten Quelle, die von der Trainingsdatei abweichen kann.

</details>

- Ein Feature Store ist eine zentrale Quelle für Features, die sowohl beim Training als auch beim Live-Betrieb (Serving) dieselben Werte liefert.
- Dieses Lab ist eine Trainer-Demo – Feast wird gezeigt, nicht selbst installiert.

## Das Problem ohne Feature Store

In diesem Kurs liegen `height` und `age` bislang nur in `people_stats.csv`. Lab 1.2 liest sie direkt aus der Datei zum Training. Lab 4.2 müsste dieselben Werte für eine Vorhersage erneut irgendwoher bekommen – in der Praxis oft durch eine zweite, unabhängig gepflegte Implementierung (z. B. eine andere Berechnung in der Anwendung), die mit der Zeit von der Trainingslogik abweicht.

## Grundbegriffe von Feast

| Begriff | Bedeutung |
| --- | --- |
| Entity | der Schlüssel, zu dem Features gehören (hier: eine Person, identifiziert über `person_id`) |
| Feature View | eine Gruppe zusammengehöriger Features für eine Entity (hier: `height`, `age`) |
| Feature Store | die zentrale Komponente, die Feature Views verwaltet und abrufbar macht |
| Online Store | schneller Speicher für aktuelle Feature-Werte, für Serving-Anfragen in Echtzeit |

## Projektstruktur

```text
feature_repo/
├── feature_store.yaml   # Konfiguration: Projektname, Registry, Online Store
├── features.py          # Entity- und Feature-View-Definitionen
└── data/
    └── people_stats_with_id.parquet   # Quelle: people_stats.csv + person_id + event_timestamp
```

```yaml
# feature_store.yaml
project: mlops_course
registry: data/registry.db
provider: local
online_store:
  type: sqlite
  path: data/online_store.db
entity_key_serialization_version: 3
```

```python
# features.py
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

`people_stats_with_id.parquet` entsteht aus `people_stats.csv`, ergänzt um eine `person_id`-Spalte (fortlaufende Nummer) und eine `event_timestamp`-Spalte (Feast braucht einen Zeitstempel pro Zeile, auch wenn sich die Werte hier nicht ändern).

**Warum `value_type=ValueType.INT64` explizit gesetzt wird:** Ohne diese Angabe registriert `feast apply` die Entity zwar ohne Fehler, aber `feast materialize` befüllt den Online Store danach lautlos mit 0 Zeilen (kein Fehler, keine Warnung – einfach ein leeres Ergebnis bei jeder späteren Abfrage). Getestet und bestätigt: mit explizitem `value_type` funktioniert die Befüllung zuverlässig.

**Wichtig für den Live-Vortrag – `demo.py` niemals in `feature_repo/` ablegen:** `feast apply` durchsucht jede `.py`-Datei im `feature_repo/`-Ordner nach Feature-Definitionen. Eine Datei, die dort selbst schon `get_online_features()` aufruft, bringt `feast apply` zum Absturz, weil die Feature View zu diesem Zeitpunkt noch nicht registriert ist. Das Abruf-Skript gehört deshalb eine Ebene höher (siehe `project/checkpoints/m03-feature-store/demo.py`, außerhalb von `feature_repo/`).

## Feast anwenden und befüllen

```bash
cd feature_repo
feast apply
feast materialize 2025-01-01T00:00:00 2027-01-01T00:00:00
```

- `feast apply` liest `features.py`, registriert Entity und Feature View und legt die Online-Store-Tabelle an.
- `feast materialize <von> <bis>` kopiert die Werte aus der Parquet-Quelle für den angegebenen Zeitraum in den Online Store. **Getestet:** `feast materialize-incremental` schrieb im Test lautlos 0 Zeilen in den Online Store (keine Fehlermeldung, aber leeres Ergebnis bei der Abfrage) – deshalb hier bewusst `feast materialize` mit explizitem Zeitraum statt `materialize-incremental`.

## Features abrufen

```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")
result = store.get_online_features(
    features=["person_features:height", "person_features:age"],
    entity_rows=[{"person_id": 42}],
).to_dict()
print(result)
```

Getestet mit `feast` 0.67.0: `{'person_id': [42], 'height': [171.0], 'age': [39]}` – identisch mit Zeile 42 in `people_stats.csv` (`171,72,39`).

**Stand: Oktober 2026 – vor Kursbeginn mit der installierten Feast-Version gegenprüfen, die API ändert sich zwischen Versionen.**

## Fazit

- Ein Feature Store trennt die Feature-Definition von einzelnen Skripten und macht sie für Training und Serving gemeinsam nutzbar.
- `Entity` und `Feature View` sind die zentralen Bausteine, um Features zu registrieren; `feast apply` registriert sie, `feast materialize` befüllt den Online Store.
- Für dieses eintägige Projekt bleibt es bei der Demo – `height`/`age` kommen in Lab 1.2 und 4.2 weiterhin direkt aus der CSV-Datei.

Modul 4 zeigt, wie das trainierte Modell selbst für andere Anwendungen erreichbar gemacht wird.
