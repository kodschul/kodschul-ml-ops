# Kursüberblick: MLOps – Praxiseinstieg in 1 Tag

## Ziel

Nach diesem Tag ist ein eigenes Regressionsmodell (Gewicht aus Größe und Alter) trainiert, versioniert, als API bereitgestellt und auf Datenqualität geprüft. Die Teilnehmer:in kann den gesamten Ablauf in eigenen Worten erklären und intern zeigen.

## Zielgruppe

1 Teilnehmer:in, Einsteiger:in in Machine Learning. Grundkenntnisse in Python sind hilfreich, aber nicht zwingend – alle Schritte werden live demonstriert und begleitet.

## Voraussetzungen

- Laptop mit Internetzugang, Python 3.10+, Code-Editor (z. B. VS Code) oder Jupyter.
- Installation vor Kursbeginn laut [`00-setup-and-installation.md`](../00-setup-and-installation.md): scikit-learn, pandas, numpy, matplotlib, joblib, tensorflow, dvc, feast, mlflow/fastapi/uvicorn, evidently.
- Projekt-Datensätze liegen bereits in `project/data/` (`people_stats.csv`, `people_weight_stats_10x.csv`, `titanic_train.csv`).

## Projekt: Gewicht-Vorhersage

Ein Regressionsmodell sagt das Körpergewicht aus Größe (und später zusätzlich Alter) vorher, auf Basis von `people_stats.csv` (199 Personen, Größe in cm, Gewicht in kg). Das Projekt wächst über den Tag: trainieren → versionieren → Feature-Store-Konzept kennenlernen → als API bereitstellen → auf Datenqualität prüfen. Ein zweites, eigenständiges Beispiel (Titanic-Überleben, logistische Regression) macht in Modul 1 zusätzlich den Unterschied zwischen Regression und Klassifikation greifbar.

## Tagesablauf

| Zeit | Block |
| --- | --- |
| 09:00–09:15 | Auftakt |
| 09:15–10:30 | Modul 1: ML-Grundlagen – Lab 1.1 ML-Konzepte, Lab 1.2 lineare Regression |
| 10:30–10:45 | Pause |
| 10:45–12:15 | Modul 1 (Fortsetzung): Lab 1.3 logistische Regression (Titanic), Lab 1.4 TensorFlow-Ausblick |
| 12:15–13:15 | Mittag |
| 13:15–14:45 | Modul 2 (Data Versioning), Modul 3 (Feature Store), Modul 4 Teil 1 (Serving-Konzepte) |
| 14:45–15:00 | Pause |
| 15:00–15:45 | Modul 4 Teil 2: Lab 4.2 Modell als API |
| 15:45–16:10 | Modul 5: Monitoring & Data Quality |
| 16:10–16:30 | Tagesabschluss |

Der Vormittag (Modul 1) ist bewusst breiter budgetiert, da lineare Regression, logistische Regression und TensorFlow die gesicherten Kerninhalte des Tages sind. Der Nachmittag (Modul 2-5) ist knapper budgetiert; einzelne Teile (Feast-Demo, DVC-Hands-on, Evidently-Demo) können je nach Zeitverlauf als Trainer-Demo statt als eigene Übung laufen.

## Arbeitsweise

Einzelsetting mit 1 Teilnehmer:in, trainerbegleitet. Übungen werden direkt am eigenen Rechner umgesetzt; Trainer-Demo-Labs (TensorFlow-Ausblick, Feature-Store-Demo, Monitoring-Demo) werden vorgeführt und gemeinsam besprochen, ohne eigene Umsetzung.
