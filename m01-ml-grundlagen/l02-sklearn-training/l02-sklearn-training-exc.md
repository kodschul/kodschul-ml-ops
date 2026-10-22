# Lab 1.2 – Übung: Gewicht aus Größe (und Alter) vorhersagen mit scikit-learn

**Dauer:** ca. 55 Minuten
**Ändert die Gewicht-Projektbasis?** Ja – erzeugt das erste trainierte Modell des Tages.

## Vorbereitung

`project/data/people_stats.csv` liegt bereit (Spalten `Height`, `Weight`, `Age`).

## Aufgaben

1. Lade `project/data/people_stats.csv` mit `pandas` und wähle `Height` als Feature, `Weight` als Label.
2. Teile die Daten mit `train_test_split` im Verhältnis 80/20 auf (`random_state=60`).
3. Trainiere ein `LinearRegression`-Modell mit den Trainingsdaten.
4. Sage das Gewicht für die Testdaten vorher und berechne MAE sowie R².
5. Notiere beide Werte.
6. Wiederhole die Schritte 1-5, diesmal mit `Height` **und** `Age` als Features.
7. Vergleiche die MAE aus Schritt 5 und Schritt 6 – welches Modell liegt im Schnitt näher am echten Gewicht?

## Checkpoint

- Zwei trainierte Modelle existieren: eines mit einem Feature, eines mit zwei Features.
- Für beide liegt ein MAE-Wert in kg und ein R²-Wert vor.

## Abschlusskriterien

- Ein Satz, der festhält, ob `Age` die Vorhersage verbessert hat, mit dem konkreten MAE-Unterschied.

## Erweiterung

Speichere das bessere der beiden Modelle mit `joblib.dump(model, "weight_model.joblib")` – dieses Modell wird in Lab 4.2 als API bereitgestellt.
