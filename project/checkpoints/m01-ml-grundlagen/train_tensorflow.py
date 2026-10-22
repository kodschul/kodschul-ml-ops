"""
Checkpoint: Lab 1.4 - Handschriftliche Ziffern erkennen mit TensorFlow.

Trainer-Demo-Code. Ersetzt die fruehere Version (Gewicht-Regression mit
TensorFlow), die zwar den Workflow zeigte, aber keinen echten Vorteil
gegenueber scikit-learn demonstrierte. MNIST zeigt einen Fall, in dem ein
neuronales Netz einem einfachen Modell tatsaechlich ueberlegen ist.

Getestet mit tensorflow 2.22.0-rc0: Test-Genauigkeit 0.9761 (neuronales
Netz) vs. 0.926 (LogisticRegression auf Rohpixeln).

Ausfuehren aus dem project/-Ordner:
    python checkpoints/m01-ml-grundlagen/train_tensorflow.py
"""
import numpy as np
import tensorflow as tf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

with np.load("data/mnist.npz") as f:
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
print("Test-Genauigkeit (neuronales Netz):", round(test_acc, 4))

X_train_flat = X_train.reshape(len(X_train), -1)
X_test_flat = X_test.reshape(len(X_test), -1)

baseline = LogisticRegression(max_iter=300)
baseline.fit(X_train_flat, y_train)
baseline_acc = accuracy_score(y_test, baseline.predict(X_test_flat))
print("Test-Genauigkeit (LogisticRegression):", round(baseline_acc, 4))
