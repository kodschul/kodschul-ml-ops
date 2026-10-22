# Final System: Gewicht-Vorhersage-Service

Das zusammengesetzte Endergebnis des Kurstages: ein kleines, aber vollständiges System aus Training, versionierten Daten, Serving-API und Monitoring. Im Unterschied zu `checkpoints/` (Referenzcode pro Lab zum Nachvollziehen) ist das hier die eine konsolidierte Struktur, die als Ausgangspunkt für einen echten Dienst dient.

**Was zum "Projekt" gehört und was nicht:** Laut Agenda wächst nur dieser Pfad als durchgängiges Projekt: Training (M1) → Datenversionierung (M2) → Serving (M4) → Monitoring (M5). TensorFlow (Lab 1.4) und der Feature-Store (M3) sind laut Agenda ausdrücklich `Projekt: nein` – eigenständige Demos, kein Teil des produktiven Pfads. Deshalb tauchen sie hier nicht auf; ihr Referenzcode liegt in `../checkpoints/m01-ml-grundlagen/train_tensorflow.py` bzw. `../checkpoints/m03-feature-store/`.

## Struktur

```text
final-system/
├── README.md
├── Makefile
├── src/
│   ├── train.py      # Training, speichert models/weight_model.joblib
│   ├── track.py       # MLflow Tracking + Model Registry (Lab 2.3)
│   ├── api.py         # FastAPI-Serving, laedt models/weight_model.joblib
│   └── monitor.py     # Drift-Check, erzeugt reports/drift_report.html
├── scripts/
│   └── version_data.sh   # DVC-Versionierung von ../data/people_stats.csv
├── models/             # entsteht durch `make train` (gitignored)
├── mlflow.db            # entsteht durch `make track` (gitignored)
└── reports/             # entsteht durch `make monitor` (gitignored)
```

Daten liegen bewusst nicht doppelt hier, sondern werden aus `../data/` gelesen (`people_stats.csv`, `people_weight_stats_10x.csv`) – ein System, eine Datenquelle.

## Ausführen

```bash
cd project/final-system
pip install -r ../requirements.txt     # oder: make setup

make train      # trainiert und speichert models/weight_model.joblib
make track      # protokolliert beide Modellvarianten in MLflow, registriert die bessere als "production"
make serve      # startet die API unter http://127.0.0.1:8000 (Strg+C zum Beenden)
```

In einem zweiten Terminal, während `make serve` läuft:

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"height": 180, "age": 35}'
curl http://127.0.0.1:8000/health
```

Nach dem Beenden der API:

```bash
make monitor        # vergleicht Datenstände, erzeugt reports/drift_report.html
make version-data   # versioniert data/people_stats.csv mit DVC (im project/-Ordner)
make mlflow-ui      # öffnet die MLflow-Oberfläche unter http://127.0.0.1:5001 (Strg+C zum Beenden)
```

## Reihenfolge für ein frisches System

1. `make train` – ohne trainiertes Modell kann die API nicht starten.
2. `make track` – hält fest, mit welchen Parametern/Metriken das Modell entstand, und markiert es als `production`.
3. `make version-data` – hält den gerade verwendeten Datenstand in Git/DVC fest.
4. `make serve` – Service lokal verfügbar machen.
5. `make monitor` – prüfen, ob eine neue Datencharge vom trainierten Stand abweicht; bei deutlicher Abweichung zurück zu Schritt 1 mit aktualisierten Daten.

## Grenzen dieses Stands

- Kein Remote-Storage für DVC (rein lokal), kein Authentifizierungs-/Rate-Limiting in der API, kein automatisches Neutraining bei erkanntem Drift – für den Kurstag bewusst weggelassen, siehe `../../agenda.md`.
