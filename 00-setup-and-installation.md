# Setup und Installation

Installation vor Kursbeginn, damit am Kurstag keine Zeit für Paket-Downloads verloren geht.

## Python-Umgebung

```bash
python3 --version   # 3.10 oder neuer
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## Pakete installieren

```bash
pip install -r project/requirements.txt
```

`project/requirements.txt` listet alle Pakete für den Kurstag; einzeln installieren (`pip install scikit-learn pandas ...`) funktioniert ebenso.

| Paket | Verwendet in |
| --- | --- |
| `scikit-learn` | Modul 1 (lineare und logistische Regression) |
| `pandas`, `numpy` | alle Module (Datenverarbeitung) |
| `matplotlib` | Modul 1 (Scatterplot, Confusion Matrix) |
| `joblib` | Modul 1 und 4 (Modell speichern/laden) |
| `tensorflow` | Modul 1 (TensorFlow-Ausblick) |
| `dvc` | Modul 2 (Daten-Versionierung) |
| `feast` | Modul 3 (Feature-Store-Demo) |
| `mlflow`, `fastapi`, `uvicorn` | Modul 4 (Model Serving) |
| `evidently` | Modul 5 (Datenqualität/Drift) |

## Funktionstest vor Kursbeginn

```bash
python3 -c "import sklearn, pandas, numpy, matplotlib, joblib, tensorflow; print('ok: Grundpakete')"
dvc init --subdir   # in einem leeren Testordner, danach wieder löschen
feast init test_repo   # prüft, ob Feast ohne zusätzliche Infrastruktur startet
```

`dvc init` und `feast init` benötigen keinen Internetzugang mehr, sobald die Pakete installiert sind. Ein Fehlschlag an dieser Stelle deutet auf ein Firewall-/Proxy-Problem beim vorherigen `pip install` hin.

## Projekt-Dateien

Die Datensätze liegen bereits in `output/project/data/` (`people_stats.csv`, `people_weight_stats_10x.csv`, `titanic_train.csv`, `mnist.npz`) und müssen am Kurstag nicht heruntergeladen werden.

## Fallback

Wenn die lokale Installation nicht rechtzeitig steht: Kurs auf einer vorbereiteten Trainer-Umgebung (vorkonfigurierte VM oder Cloud-Notebook) durchführen. DVC- und Feast-Übungen werden dann als Trainer-Demo statt als eigene Übung gezeigt.
