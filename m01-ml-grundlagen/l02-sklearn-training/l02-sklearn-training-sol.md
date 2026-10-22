# Lab 1.2 – Lösung: Gewicht aus Größe (und Alter) vorhersagen mit scikit-learn

## Aufgabe 1-5: Modell nur mit `Height`

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("project/data/people_stats.csv")

X = df[["Height"]]
y = df["Weight"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=60
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R^2:", r2_score(y_test, y_pred))
```

Ergebnis (mit `people_stats.csv`, 199 Zeilen, `random_state=60`):

```text
MAE: 7.36 kg
R^2: 0.037
```

## Aufgabe 6: Modell mit `Height` und `Age`

```python
X = df[["Height", "Age"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=60
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R^2:", r2_score(y_test, y_pred))
```

Ergebnis:

```text
MAE: 6.66 kg
R^2: 0.29
```

## Aufgabe 7: Vergleich

| Modell | MAE | R² |
| --- | --- | --- |
| `Height` | 7.36 kg | 0.037 |
| `Height` + `Age` | 6.66 kg | 0.29 |

`Age` verbessert die Vorhersage: der Fehler sinkt um 0.7 kg, und R² steigt von 0.037 auf 0.29 – mit nur der Größe erklärt das Modell kaum Varianz im Gewicht, mit Alter zusätzlich deutlich mehr. Beide Werte bleiben niedrig, weil der Datensatz nur zwei Features enthält und weitere Einflussfaktoren (z. B. Körperbau) fehlen.

## Erweiterung: Modell speichern

```python
import joblib

joblib.dump(model, "weight_model.joblib")
```

Das gespeicherte Modell (trainiert mit `Height` + `Age`) wird in Lab 4.2 geladen und über eine API bereitgestellt.
