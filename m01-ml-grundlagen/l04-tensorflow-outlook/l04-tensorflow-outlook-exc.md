# Lab 1.4 – Übung: Handschriftliche Ziffern erkennen mit TensorFlow

**Heute im Kurs:** Trainer-Demo (siehe Agenda) – die folgenden Aufgaben sind für das Selbststudium danach gedacht, um den Workflow eigenständig nachzuvollziehen.
**Ändert die Gewicht-Projektbasis?** Nein – eigenständiges Bilderkennungs-Beispiel, nicht Teil der Gewicht-Pipeline.

## Vorbereitung

`project/data/mnist.npz` liegt bereit (70.000 handgeschriebene Ziffern, liegt lokal vor, kein Download nötig).

## Aufgaben

1. Lade `project/data/mnist.npz` mit `numpy` und skaliere die Pixelwerte (0-255) auf den Bereich 0-1.
2. Baue ein `tf.keras.Sequential`-Modell: `Flatten` → `Dense(128, activation="relu")` → `Dense(10, activation="softmax")`.
3. Kompiliere das Modell mit `optimizer="adam"`, `loss="sparse_categorical_crossentropy"`, `metrics=["accuracy"]`.
4. Trainiere 5 Epochen (`model.fit(X_train, y_train, epochs=5)`) und werte auf den Testdaten aus.
5. Trainiere zum Vergleich eine `LogisticRegression` auf denselben (geflachten) Rohpixeln und berechne die Accuracy.
6. Vergleiche beide Genauigkeiten und die ungefähre Trainingsdauer.

## Checkpoint

- Das neuronale Netz erreicht eine Test-Genauigkeit nahe 97-98 %.
- Die `LogisticRegression`-Baseline erreicht eine Genauigkeit nahe 92-93 %, braucht aber spürbar länger zum Trainieren (ca. 30+ Sekunden statt weniger Sekunden).

## Abschlusskriterien

- Ein Satz, der benennt, um wie viel das neuronale Netz besser abschneidet und woran das liegt (Kombination von Pixelmustern über die verdeckte Schicht, statt nur gewichteter Summe aller Pixel).

## Fallback

Bei langsamer Hardware: `epochs=3` statt `5` reicht für eine deutlich sichtbare Überlegenheit gegenüber der Baseline.
