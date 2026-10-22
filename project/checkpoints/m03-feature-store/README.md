# Checkpoint: Lab 3.1 - Feature Store Demo

Schritt für Schritt, getestet mit `feast` 0.67.0.

**Wichtig:** `feast apply` importiert jede `.py`-Datei im `feature_repo/`-Ordner, um Feature-Definitionen zu finden. `demo.py` liegt deshalb bewusst eine Ebene höher (`m03-feature-store/demo.py`), nicht in `feature_repo/` – sonst versucht `feast apply`, `demo.py` zu importieren und scheitert, weil die Feature View zu diesem Zeitpunkt noch nicht registriert ist.

```bash
# 1. Aus dem project/-Ordner: Parquet-Quelle erzeugen
python checkpoints/m03-feature-store/prepare_data.py

# 2. In den feature_repo/-Ordner wechseln
cd checkpoints/m03-feature-store/feature_repo

# 3. Entity und Feature View registrieren
feast apply

# 4. Online Store befüllen (expliziter Zeitraum, nicht "materialize-incremental")
feast materialize 2025-01-01T00:00:00 2027-01-01T00:00:00

# 5. Eine Ebene zurück, dann Features abrufen
cd ..
python demo.py
```

Erwartete Ausgabe von Schritt 5 (Zeile 42 in `people_stats.csv` ist `171,72,39`):

```text
{'person_id': [42], 'height': [171.0], 'age': [39]}
```
