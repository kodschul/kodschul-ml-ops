# MLOps-1-Com – Handout-Übersicht

Ordnerstruktur der Kurs-Handouts (jedes Lab hat einen eigenen `lNN/`-Unterordner im `mNN`-Modulordner).

| Ordner / Datei | Inhalt |
| --- | --- |
| `00-setup-and-installation.md` | Python-Umgebung, Pakete, Funktionstest, Fallback |
| `m00-overview/` | Overview, Topics, Glossar, Best Practices, FAQ |
| `m01-ml-grundlagen/` | Lab 1.1–1.4: ML-Grundlagen, lineare Regression, logistische Regression, TensorFlow-Ausblick + Cheatsheet |
| `m02-data-versioning/` | Lab 2.1–2.2: Daten-Versionierung mit DVC + Cheatsheet |
| `m03-feature-store/` | Lab 3.1: Feature-Store-Konzept mit Feast (Trainer-Demo) |
| `m04-model-serving-hosting/` | Lab 4.1–4.2: Serving-Konzepte, Modell als API + Cheatsheet |
| `m05-monitoring/` | Lab 5.1: Monitoring & Datenqualität (Trainer-Demo) |
| `project/` | Projekt-Datensätze und -Beschreibung (Gewicht-Vorhersage) |

## Modul 1: ML-Grundlagen

| Ordner / Datei | Inhalt |
| --- | --- |
| `l01-ml-concepts/` | Features/Label, überwachtes Lernen, Regression vs. Klassifikation |
| `l02-sklearn-training/` | Lineare Regression: Gewicht aus Größe (+Alter), scikit-learn |
| `l03-logreg-titanic/` | Logistische Regression: Titanic-Überleben, Accuracy/Confusion Matrix |
| `l04-tensorflow-outlook/` | TensorFlow-Ausblick (Trainer-Demo, nur Theorie) |
| `ml-grundlagen-cheatsheet.md` | Befehlsreferenz für alle vier Labs |

## Modul 2: Data Versioning

| Ordner / Datei | Inhalt |
| --- | --- |
| `l01-dvc-concepts/` | Warum Daten-Versionierung, Git vs. DVC |
| `l02-dvc-pipeline/` | DVC einrichten, zwei Datenstände versionieren, Rollback |
| `dvc-cheatsheet.md` | Befehlsreferenz DVC |

## Modul 3: Feature Store

| Ordner / Datei | Inhalt |
| --- | --- |
| `l01-feast-demo/` | Feature-Store-Konzept, Entity/Feature View, Feast-Beispielcode (Trainer-Demo, nur Theorie) |

## Modul 4: Model Serving & Hosting

| Ordner / Datei | Inhalt |
| --- | --- |
| `l01-serving-concepts/` | Serialisierung, Serving-Optionen im Vergleich, Checkliste |
| `l02-model-api/` | Gewichts-Modell als FastAPI-Endpunkt bereitstellen |
| `serving-cheatsheet.md` | Befehlsreferenz Serving |

## Modul 5: Monitoring

| Ordner / Datei | Inhalt |
| --- | --- |
| `l01-monitoring-and-quality/` | Data Drift, Tool-Überblick, Evidently-Mini-Demo (Trainer-Demo, nur Theorie) |

## Projekt

`project/README.md` beschreibt den Datensatz und wie das Gewicht-Vorhersage-Projekt über den Tag wächst. Daten liegen in `project/data/` (`people_stats.csv`, `people_weight_stats_10x.csv`, `titanic_train.csv`); `project/requirements.txt` und `project/.gitignore` liefern die Arbeitsumgebung für die Übungen. `project/final-system/` ist das konsolidierte, mit `make train`/`make serve`/`make monitor` startbare Endergebnis (nur der Pipeline-Teil, der laut Agenda als Projekt zählt). `project/checkpoints/` enthält die finalen, lauffähigen Codestände aller Labs (inkl. der Nicht-Projekt-Demos TensorFlow und Feast) zum Vergleichen und Nachvollziehen.
