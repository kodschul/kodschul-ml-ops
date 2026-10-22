# Lab 1.4 – Lösung: Handschriftliche Ziffern erkennen mit TensorFlow

## Aufgaben 1-4: Daten laden, Modell bauen, trainieren

```python
import numpy as np
import tensorflow as tf

with np.load("project/data/mnist.npz") as f:
    X_train, y_train = f["x_train"], f["y_train"]
    X_test, y_test = f["x_test"], f["y_test"]

X_train = X_train / 255.0
X_test = X_test / 255.0

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

model.fit(X_train, y_train, epochs=5, verbose=2)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print("Test-Genauigkeit:", round(test_acc, 4))
```

Ergebnis (getestet, `tensorflow` 2.22.0-rc0, Seed 60):

```text
Test-Genauigkeit: 0.9761
```

## Aufgabe 5: LogisticRegression-Baseline

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

Ergebnis: `LogisticRegression-Genauigkeit: 0.926` (Trainingsdauer ca. 34 Sekunden).

## Aufgabe 6: Vergleich

| Modell | Test-Genauigkeit | Trainingsdauer |
| --- | --- | --- |
| `LogisticRegression` auf Rohpixeln | 92.6 % | ca. 34 s |
| Neuronales Netz (`Flatten` + `Dense` + `Dense`) | 97.6 % | wenige Sekunden |

Die Fehlerquote sinkt von 7.4 % auf 2.4 % (rund ein Drittel) – das neuronale Netz lernt über die verdeckte Schicht Kombinationen von Pixeln, während `LogisticRegression` nur eine gewichtete Summe aller Pixel pro Ziffer bilden kann.

## Grenzen

Dieses Modell ist nicht Teil der Gewicht-Projektpipeline – es demonstriert nur, wann ein neuronales Netz gegenüber einem einfachen Modell einen echten Vorteil bringt (hier: Bilddaten mit nicht-linearen Mustern).
