# Lab 1.2 – Übung: Gewicht aus Größe (und Alter) vorhersagen mit scikit-learn

**Dauer:** ca. 30 Minuten (gekürzt von 55 Min. – der Height-only-Zwischenschritt entfällt, siehe `-thx.md`)
**Ändert die Gewicht-Projektbasis?** Ja – erzeugt das erste trainierte Modell des Tages.

## Vorbereitung

`project/data/people_stats.csv` liegt bereit (Spalten `Height`, `Weight`, `Age`).

## Aufgaben

1. Lade `project/data/people_stats.csv` mit `pandas` und wähle `Height` **und** `Age` als Features, `Weight` als Label.
2. Teile die Daten mit `train_test_split` im Verhältnis 80/20 auf (`random_state=60`).
3. Trainiere ein `LinearRegression`-Modell mit den Trainingsdaten.
4. Sage das Gewicht für die Testdaten vorher und berechne MAE sowie R².
5. Notiere beide Werte – zum Vergleich: ein Modell nur mit `Height` liefert MAE 7.36 kg/R² 0.037 (bereits bekannt, nicht mehr selbst nachzuvollziehen).

## Checkpoint

- Ein trainiertes Modell mit beiden Features (`Height`, `Age`) existiert.
- Ein MAE-Wert in kg und ein R²-Wert liegen vor.

## Abschlusskriterien

- Die MAE/R²-Werte sind notiert und liegen nahe an MAE 6.66 kg/R² 0.29.

## Erweiterung

Speichere das Modell mit `joblib.dump(model, "weight_model.joblib")` – dieses Modell wird in Lab 2.3 (MLflow) erneut (diesmal protokolliert) trainiert und in Lab 4.2 als API bereitgestellt.

