# Lab 1.4: Kurzer Ausblick – Handschriftliche Ziffern erkennen mit TensorFlow

**Leitfragen:**

<details>
<summary>Warum eignet sich Bilderkennung besser für ein neuronales Netz als für lineare/logistische Regression?</summary>

Ein Bild hat 784 Pixelwerte (28×28) als Eingabe, und der Zusammenhang zwischen Pixelmustern und einer Ziffer ist nicht linear trennbar – ein neuronales Netz kann über mehrere Schichten Kombinationen von Pixeln lernen, eine einzelne lineare Grenze pro Klasse reicht dafür nicht aus.

</details>

<details>
<summary>Was bedeuten 10 Ausgabeneuronen mit `softmax`?</summary>

Jedes der 10 Neuronen steht für eine Ziffer (0-9) und gibt eine Wahrscheinlichkeit aus; `softmax` sorgt dafür, dass alle 10 Werte zusammen 1 ergeben. Die Ziffer mit der höchsten Wahrscheinlichkeit ist die Vorhersage.

</details>

<details>
<summary>Ist die Genauigkeit besser als bei `LogisticRegression` – und woran liegt das?</summary>

Ja, deutlich: in diesem Lauf 97.6 % (neuronales Netz) gegenüber 92.6 % (`LogisticRegression`) – das neuronale Netz lernt über die verdeckte Schicht Kombinationen von Pixeln, während `LogisticRegression` nur eine gewichtete Summe aller Pixel pro Ziffer bilden kann.

</details>

<details>
<summary>Was bleibt am Workflow gleich, was ändert sich gegenüber Lab 1.2/1.3?</summary>

Gleich bleiben Daten laden, Modell erzeugen, trainieren, auf Testdaten auswerten. Neu sind die Netzarchitektur (mehrere Schichten), das Training über Epochen statt eines einzelnen `fit()`-Schritts, und dass die Eingabe hier ein Bild (28×28 Pixel) statt einer Tabelle mit wenigen Spalten ist.

</details>

- MNIST ist ein Standarddatensatz mit 70.000 handgeschriebenen Ziffern (28×28 Pixel, Werte 0-255, Graustufen), 10 Klassen (0-9). Die Datei liegt lokal vor (`project/data/mnist.npz`), kein Download am Kurstag nötig.
- Dieses Lab ist eine Trainer-Demo – der Workflow wird gezeigt, nicht selbst nachgebaut.
- Lab 1.3 war bereits Klassifikation (2 Klassen: überlebt/nicht überlebt). MNIST ist ebenfalls Klassifikation, jetzt mit 10 Klassen statt 2.

## Daten laden

```python
import numpy as np

with np.load("project/data/mnist.npz") as f:
    X_train, y_train = f["x_train"], f["y_train"]
    X_test, y_test = f["x_test"], f["y_test"]

print(X_train.shape, y_train.shape)   # (60000, 28, 28) (60000,)
print(X_test.shape, y_test.shape)     # (10000, 28, 28) (10000,)

X_train = X_train / 255.0
X_test = X_test / 255.0
```

Jedes Bild ist ein 28×28-Array mit Helligkeitswerten 0 (schwarz) bis 255 (weiß). Division durch 255 skaliert sie auf den Bereich 0-1 – dieselbe Idee wie `StandardScaler` in anderen Labs, hier aber eine einfache, für Pixelwerte übliche Variante.

## Netzarchitektur

```python
import tensorflow as tf

tf.keras.utils.set_random_seed(60)
model = tf.keras.Sequential([
    tf.keras.Input(shape=(28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax"),
])
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

| Schicht | Aufgabe |
| --- | --- |
| `Flatten` | wandelt das 28×28-Bild in einen Vektor mit 784 Werten um |
| `Dense(128, relu)` | verdeckte Schicht, kombiniert die 784 Pixelwerte zu 128 gelernten Merkmalen |
| `Dense(10, softmax)` | Ausgabeschicht, eine Wahrscheinlichkeit pro Ziffer (0-9) |

`sparse_categorical_crossentropy` ist die passende Loss-Funktion für Klassifikation mit mehr als 2 Klassen, wenn das Label eine einzelne Zahl (hier: 0-9) statt einer One-Hot-codierten Liste ist.

## Trainieren und auswerten

```python
model.fit(X_train, y_train, epochs=5, verbose=2)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print("Test-Genauigkeit:", round(test_acc, 4))
```

Getestet mit `tensorflow` 2.22.0-rc0, 5 Epochen, Seed 60 (Trainingsdauer: wenige Sekunden):

```text
Epoch 1/5  accuracy: 0.9254
Epoch 2/5  accuracy: 0.9668
Epoch 3/5  accuracy: 0.9771
Epoch 4/5  accuracy: 0.9834
Epoch 5/5  accuracy: 0.9875
Test-Genauigkeit: 0.9761
```

## Vergleich mit einem einfachen Modell

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train_flat = X_train.reshape(len(X_train), -1)
X_test_flat = X_test.reshape(len(X_test), -1)

baseline = LogisticRegression(max_iter=300)
baseline.fit(X_train_flat, y_train)
baseline_acc = accuracy_score(y_test, baseline.predict(X_test_flat))
print("LogisticRegression-Genauigkeit:", round(baseline_acc, 4))
```

Getestet: `LogisticRegression-Genauigkeit: 0.926` (Trainingsdauer: ca. 34 Sekunden, also auch spürbar langsamer als das neuronale Netz).

| Modell | Test-Genauigkeit | Trainingsdauer |
| --- | --- | --- |
| `LogisticRegression` auf Rohpixeln | 92.6 % | ca. 34 s |
| Neuronales Netz (`Flatten` + `Dense` + `Dense`) | 97.6 % | wenige Sekunden |

Der Unterschied ist diesmal nicht nur theoretisch: die Fehlerquote sinkt von 7.4 % auf 2.4 %, also auf rund ein Drittel – anders als beim Gewicht-Beispiel in Lab 1.2, wo scikit-learn und ein einfaches Netz etwa gleich gut abschnitten.

## Fazit

- Bei Bilddaten zeigt sich ein echter Vorteil neuronaler Netze: höhere Genauigkeit (97.6 % vs. 92.6 %) bei gleichzeitig kürzerer Trainingszeit.
- Die Netzarchitektur wächst mit der Aufgabe: `Flatten` für Bilder als Eingabe, `softmax` + `sparse_categorical_crossentropy` für mehr als 2 Klassen.
- Derselbe Grundworkflow (Daten laden → Modell bauen → trainieren → auswerten) bleibt über alle Labs in Modul 1 gleich, nur Architektur und Loss-Funktion passen sich an Datentyp und Aufgabe an.

Modul 2 verlässt die Modellwahl und widmet sich der Frage, wie die Trainingsdaten selbst nachvollziehbar versioniert werden.
