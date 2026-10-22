# Kursüberblick: MLOps – Praxiseinstieg in 1 Tag

## Ziel

Nach diesem Tag ist ein eigenes Regressionsmodell (Gewicht aus Größe und Alter) trainiert, versioniert, als API bereitgestellt und auf Datenqualität geprüft. Die Teilnehmer:in kann den gesamten Ablauf in eigenen Worten erklären und intern zeigen.

## Zielgruppe

1 Teilnehmer:in, Einsteiger:in in Machine Learning. Grundkenntnisse in Python sind hilfreich, aber nicht zwingend – alle Schritte werden live demonstriert und begleitet.

## Voraussetzungen

- Laptop mit Internetzugang, Python 3.10+, Code-Editor (z. B. VS Code) oder Jupyter.
- Installation vor Kursbeginn laut [`00-setup-and-installation.md`](../00-setup-and-installation.md): scikit-learn, pandas, numpy, matplotlib, joblib, tensorflow, dvc, feast, mlflow, fastapi, uvicorn, evidently.
- Projekt-Datensätze liegen bereits in `project/data/` (`people_stats.csv`, `people_weight_stats_10x.csv`, `titanic_train.csv`).

## Projekt: Gewicht-Vorhersage

Ein Regressionsmodell sagt das Körpergewicht aus Größe (und später zusätzlich Alter) vorher, auf Basis von `people_stats.csv` (199 Personen, Größe in cm, Gewicht in kg). Das Projekt wächst über den Tag: trainieren → Daten versionieren (DVC) und Modelle/Experimente versionieren (MLflow) → Feature-Store-Konzept kennenlernen → als API bereitstellen → Best Practices reflektieren → auf Datenqualität prüfen. Ein zweites, eigenständiges Beispiel (Titanic-Überleben, logistische Regression) macht in Modul 1 zusätzlich den Unterschied zwischen Regression und Klassifikation greifbar.

## Tagesablauf

| Zeit | Block |
| --- | --- |
| 09:00–09:15 | Auftakt |
| 09:15–09:55 | Modul 1, Teil 1: ML-Recap (kompakt) + Lab 1.2 Projektmodell trainieren |
| 09:55–10:20 | Modul 1, Teil 2: Klassifikation (Titanic) & TensorFlow – kompakter Trainer-Demo-Ausblick |
| 10:20–10:35 | Pause |
| 10:35–11:15 | Modul 2, Teil 1: Lab 2.1+2.2 Datenversionierung mit DVC |
| 11:15–12:05 | Modul 2, Teil 2: Lab 2.3 Modell-/Experiment-Versionierung mit MLflow (+ Plattform-Vergleich) |
| 12:05–13:05 | Mittag |
| 13:05–13:25 | Modul 3: Feature-Store-Konzept mit Feast (Demo) |
| 13:25–13:55 | Modul 4, Teil 1: Serving-Konzepte |
| 13:55–14:10 | Pause |
| 14:10–14:55 | Modul 4, Teil 2: Lab 4.2 Modell als API |
| 14:55–15:20 | Modul 6: MLOps Best Practices & Anti-Patterns |
| 15:20–15:50 | Modul 5: Monitoring & Data Quality |
| 15:50–16:00 | Tagesabschluss |

Modul 1 ist bewusst stark gekürzt (von ursprünglich 165 auf 65 Min.): Die Teilnehmerin bringt ML-Vorkenntnisse aus einer Master-Thesis mit, braucht also keine Einführung, nur einen kurzen Begriffsabgleich und das eine Projektmodell, auf dem der restliche Tag aufbaut. Klassifikation (Titanic) und TensorFlow (MNIST) laufen als kompakter Trainer-Demo-Block statt als eigene Einzelübungen. Die gewonnene Zeit fließt in echte Hands-on-Tiefe für Modul 2 (DVC **und** MLflow), Modul 4 (Serving) und das neue Modul 6 (Best Practices) – genau der Teil, den die Teilnehmerin laut eigener Aussage noch nicht beherrscht.

## Arbeitsweise

Einzelsetting mit 1 Teilnehmer:in, trainerbegleitet. Übungen werden direkt am eigenen Rechner umgesetzt; Trainer-Demo-Labs (TensorFlow-Ausblick, Feature-Store-Demo, Monitoring-Demo) werden vorgeführt und gemeinsam besprochen, ohne eigene Umsetzung.
