# Lab 1.3 – Übung: Überleben auf der Titanic vorhersagen mit logistischer Regression

**Dauer:** ca. 12 Minuten
**Heute im Kurs:** Trainer-Demo statt Einzelübung – die Teilnehmerin kennt logistische Regression bereits; Code und Ergebnis werden gemeinsam durchgegangen. Die folgenden Aufgaben dienen als Grundlage für die Demo und optional als Selbststudium-Referenz.
**Ändert die Gewicht-Projektbasis?** Nein – eigenständiges Klassifikations-Beispiel, nicht Teil der Gewicht-Pipeline.

## Ausgangslage

`project/data/titanic_train.csv` liegt bereit (891 Zeilen, Spalten u. a. `Survived`, `Pclass`, `Sex`, `Age`).

## Aufgaben

1. Lade `project/data/titanic_train.csv` mit `pandas` und entferne Zeilen ohne bekanntes `Age`.
2. Wandle `Sex` in `1` (männlich) / `0` (weiblich) um.
3. Wähle `Pclass`, `Age`, `Sex` als Features und `Survived` als Label.
4. Teile die Daten mit `train_test_split` im Verhältnis 80/20 auf (`random_state=10`).
5. Trainiere ein `LogisticRegression`-Modell (`max_iter=1000`) mit den Trainingsdaten.
6. Berechne Accuracy und Confusion Matrix auf den Testdaten.
7. Lies aus der Confusion Matrix ab: Welche Fehlerart ist häufiger – Überlebende, die als „nicht überlebt" vorhergesagt werden, oder umgekehrt?

## Checkpoint

- Ein trainiertes `LogisticRegression`-Modell existiert.
- Accuracy liegt als Prozentwert vor, die Confusion Matrix als 2x2-Tabelle.

## Abschlusskriterien

- Ein Satz, der benennt, welche der beiden Fehlerarten in der eigenen Confusion Matrix häufiger auftritt.

## Fallback

Bei Problemen mit `max_iter`-Warnungen: `max_iter` auf `2000` erhöhen, das Modell bleibt sonst unverändert.
