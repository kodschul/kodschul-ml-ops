# Projekt: Gewicht-Vorhersage

Durchgängiges Projekt des Kurstages: ein Regressionsmodell sagt das Körpergewicht aus Größe (und später zusätzlich Alter) vorher. Das Modell wächst über den Tag von einem einfachen Trainingsskript zu einer versionierten, servierten und überwachten Mini-Pipeline.

**Zwei verschiedene Ordner, zwei verschiedene Zwecke:**

- **`final-system/`** – das konsolidierte Endergebnis: ein kleines, lauffähiges System (Training, Serving, Monitoring, Datenversionierung), mit dem direkt gestartet werden kann. Siehe [`final-system/README.md`](final-system/README.md).
- **`checkpoints/`** – Referenzcode pro Lab zum Nachvollziehen und Vergleichen, inklusive der Labs, die laut Agenda *nicht* Teil des Projekts sind (TensorFlow-Ausblick, Feature-Store-Demo).

## Daten

| Datei | Zeilen | Spalten | Verwendung |
| --- | --- | --- | --- |
| `data/people_stats.csv` | 199 | `Height` (cm), `Weight` (kg), `Age` (Jahre) | Ausgangsdatensatz, Modul 1, 2 und 4 |
| `data/people_weight_stats_10x.csv` | 196 | gleich wie oben | "neue Datencharge" (im Schnitt ca. 3 kg schwerer), Modul 2 (Versionierung) und Modul 5 (Drift-Check) |
| `data/titanic_train.csv` | 891 | u. a. `Pclass`, `Sex`, `Age`, `Survived` | eigenständiges Klassifikations-Beispiel in Lab 1.3, nicht Teil der Gewicht-Pipeline |
| `data/mnist.npz` | 70.000 Bilder | 28×28-Graustufenbilder, Label 0-9 | eigenständiges Bilderkennungs-Beispiel in Lab 1.4, nicht Teil der Gewicht-Pipeline |

## Wachstum über den Tag

| Modul | Schritt | Ergebnis |
| --- | --- | --- |
| M1 | Modell auf `people_stats.csv` trainieren (erst `Height`, dann `Height`+`Age`) | trainiertes `LinearRegression`-Modell |
| M2 | Datensatz mit DVC versionieren, Wechsel auf `people_weight_stats_10x.csv` nachvollziehbar machen; beide Modellvarianten mit MLflow protokollieren und das bessere als `production` registrieren | zwei versionierte Datenstände, zwei nachvollziehbare MLflow-Runs, eine registrierte Modellversion |
| M3 | Features `height`/`age` als Feature-Store-Konzept kennenlernen (Demo, keine Codeänderung am Projekt) | - |
| M4 | Modell als lokale API bereitstellen (Eingabe: Größe + Alter, Ausgabe: Gewicht) | lauffähiger Endpunkt |
| M6 | Best Practices über die gesamte Pipeline reflektieren (Reproduzierbarkeit, Validierung, Rollback) | - |
| M5 | Datenqualität/Drift zwischen beiden Datenständen prüfen | Evidently-Report |

## Ordnerstruktur

```text
project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── people_stats.csv
│   ├── people_weight_stats_10x.csv
│   ├── titanic_train.csv
│   └── mnist.npz
├── final-system/            # das konsolidierte, lauffähige Endergebnis
│   ├── README.md
│   ├── Makefile
│   ├── src/
│   │   ├── train.py
│   │   ├── track.py
│   │   ├── api.py
│   │   └── monitor.py
│   ├── scripts/
│   │   └── version_data.sh
│   ├── models/               # entsteht durch `make train`
│   ├── mlflow.db              # entsteht durch `make track`
│   └── reports/              # entsteht durch `make monitor`
└── checkpoints/              # Referenzcode pro Lab (inkl. Nicht-Projekt-Labs)
    ├── m01-ml-grundlagen/
    │   ├── train_linreg.py          # Lab 1.2, finale Version (Height + Age)
    │   ├── train_logreg_titanic.py  # Lab 1.3, finale Version
    │   └── train_tensorflow.py      # Lab 1.4, finale Version
    ├── m02-data-versioning/
    │   ├── dvc_commands.sh          # Lab 2.2, vollständiger Befehlsablauf
    │   └── mlflow_tracking.py       # Lab 2.3, Tracking + Model Registry
    ├── m03-feature-store/
    │   ├── README.md                 # Lab 3.1, Ablaufschritte
    │   ├── prepare_data.py           # erzeugt die Parquet-Quelle
    │   ├── demo.py                   # ruft Features aus dem Online Store ab
    │   └── feature_repo/             # feature_store.yaml + features.py
    ├── m04-model-serving-hosting/
    │   └── serve.py                 # Lab 4.2, finale Version inkl. Plausibilitätsprüfung
    ├── m05-monitoring/
    │   └── check_drift.py           # Lab 5.1, finale Version
    └── m06-mlops-best-practices/
        └── compare_before_promote.py # Lab 6.1, Metrikvergleich vor dem Promoten (Anti-Pattern-Check)
```

- `requirements.txt` listet alle Pakete, die über den Tag gebraucht werden (`pip install -r project/requirements.txt`), siehe auch [`00-setup-and-installation.md`](../00-setup-and-installation.md).
- `.gitignore` schließt virtuelle Umgebung, gespeicherte Modelle (`*.joblib`, `*.pkl`), den Evidently-Report und die beim Feast-Checkpoint erzeugten Dateien (`checkpoints/m03-feature-store/feature_repo/data/`) von Git aus – diese Dateien entstehen lokal während der Übungen und müssen nicht versioniert werden.
- `checkpoints/` enthält die vollständigen, lauffähigen Endstände jedes Code-Labs – zum Vergleichen nach der eigenen Umsetzung oder zum Nachvollziehen, falls eine Übung nicht fertig wurde. Jede Datei entspricht exakt dem Code aus der jeweiligen `-sol.md`/`-thx.md`.
- Modell-Dateien (`.pkl`/`.joblib`), DVC-Metadaten (`.dvc/`, `*.dvc`), der Evidently-Report und die Feast-Datenbanken (`registry.db`, `online_store.db`) entstehen beim Ausführen der Checkpoint-Skripte bzw. während der Übungen im `project`-Arbeitsverzeichnis.

## Checkpoints ausführen

Die folgenden Schritte sind einzeln auszuführen, nicht als ein durchlaufendes Skript (der `uvicorn`-Server läuft dauerhaft und blockiert das Terminal, bis er mit Strg+C beendet wird).

```bash
cd project
pip install -r requirements.txt
```

```bash
python checkpoints/m01-ml-grundlagen/train_linreg.py        # erzeugt weight_model.joblib
python checkpoints/m01-ml-grundlagen/train_logreg_titanic.py
python checkpoints/m01-ml-grundlagen/train_tensorflow.py
```

```bash
bash checkpoints/m02-data-versioning/dvc_commands.sh         # Schritt für Schritt, nicht blind durchlaufen lassen
```

```bash
python checkpoints/m02-data-versioning/mlflow_tracking.py    # erzeugt mlflow.db, registriert "weight-predictor"
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001   # Strg+C zum Beenden
```

```bash
python checkpoints/m03-feature-store/prepare_data.py
cd checkpoints/m03-feature-store/feature_repo
feast apply
feast materialize 2025-01-01T00:00:00 2027-01-01T00:00:00
cd ..
python demo.py
cd ../../..
```

```bash
cd checkpoints/m04-model-serving-hosting
uvicorn serve:app --reload --port 8000
```

In einem zweiten Terminal, während die API läuft:

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"height": 180, "age": 35}'
```

Nach Beenden der API (Strg+C), zurück im `project`-Ordner:

```bash
python checkpoints/m05-monitoring/check_drift.py             # erzeugt drift_report.html
```

```bash
python checkpoints/m06-mlops-best-practices/compare_before_promote.py   # vergleicht MLflow-Runs, promotet nur nach Metrikvergleich
```
