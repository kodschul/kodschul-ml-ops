# Lab 1.3 – Lösung: Überleben auf der Titanic vorhersagen mit logistischer Regression

## Aufgabe 1-2: Daten laden und bereinigen

```python
import pandas as pd

df = pd.read_csv("project/data/titanic_train.csv")
df = df[df["Age"].notna()]
df["Sex"] = [1 if s == "male" else 0 for s in df["Sex"]]
```

Von 891 Zeilen bleiben 714 mit bekanntem `Age`.

## Aufgabe 3-5: Features wählen, splitten, trainieren

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = df[["Pclass", "Age", "Sex"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

## Aufgabe 6: Accuracy und Confusion Matrix

```python
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

Ergebnis (143 Testzeilen, `random_state=10`):

```text
Accuracy: 78.32 %
Confusion Matrix:
[[71 14]
 [17 41]]
```

| | Vorhergesagt: 0 | Vorhergesagt: 1 |
| --- | --- | --- |
| **Tatsächlich: 0 (nicht überlebt)** | 71 | 14 |
| **Tatsächlich: 1 (überlebt)** | 17 | 41 |

## Aufgabe 7: Fehlerart interpretieren

17 Überlebende wurden fälschlich als „nicht überlebt" vorhergesagt (false negatives), 14 Nicht-Überlebende als „überlebt" (false positives) – in diesem Testsplit sind beide Fehlerarten ähnlich häufig, mit leicht mehr false negatives.

## Grenzen

Mit nur 3 Features und 714 Zeilen bleibt die Accuracy bei rund 78 % – das Originalskript des Trainers (`past/code/ml/logreg/logreg_train.py`) nutzt zusätzlich `Fare`, `SibSp` und `Parch` und kann dadurch etwas genauer werden, auf Kosten von mehr Komplexität.
