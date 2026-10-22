# Lab 1.2: Gewicht aus Größe (und Alter) vorhersagen mit scikit-learn

**Leitfragen:**

<details>
<summary>Warum werden Daten in Training/Test aufgeteilt?</summary>

Damit die Modellgüte an Zeilen gemessen wird, die das Modell beim Training nicht gesehen hat – sonst würde man nur messen, wie gut sich das Modell die Trainingsdaten gemerkt hat.

</details>

<details>
<summary>Was sagt die MAE in kg konkret aus?</summary>

Der durchschnittliche absolute Fehler der Vorhersage in Kilogramm – bei MAE = 8 kg liegt eine Vorhersage im Schnitt 8 kg neben dem echten Gewicht.

</details>

<details>
<summary>Verbessert das zweite Feature `Age` die Vorhersage – und warum (nicht)?</summary>

Das hängt vom Datensatz ab: Ein zusätzliches Feature hilft nur, wenn es tatsächlich mit dem Label zusammenhängt. Ob `Age` hilft, zeigt der Vergleich der MAE vor und nach der Erweiterung in der Übung.

</details>

- Lineare Regression sucht die Gerade (bzw. Ebene bei mehreren Features), die den Zusammenhang zwischen Features und Label am besten beschreibt.
- scikit-learn übernimmt die Rechnung; die Aufgabe besteht darin, Daten korrekt vorzubereiten und das Ergebnis richtig zu lesen.

## Trainingsablauf mit scikit-learn

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
print("MAE:", mean_absolute_error(y_test, y_pred), "kg")
print("R^2:", r2_score(y_test, y_pred))
```

- `test_size=0.2` reserviert 20 % der Zeilen für den Test.
- `random_state=60` macht den Split reproduzierbar – derselbe Code liefert immer denselben Split.
- `model.fit(X_train, y_train)` ist der eigentliche Trainingsschritt; danach enthält `model` die gelernte Gerade.

## Evaluationsmetriken

| Metrik | Bedeutung | Einheit |
| --- | --- | --- |
| MAE (Mean Absolute Error) | durchschnittlicher absoluter Fehler | gleiche Einheit wie das Label (hier: kg) |
| R² (Bestimmtheitsmaß) | Anteil der Gewichtsschwankung, den das Modell erklärt (1.0 = perfekt, 0.0 = nicht besser als der Durchschnittswert) | ohne Einheit |

Ein niedriger MAE und ein hoher R² zusammen zeigen ein Modell, das sowohl im Durchschnitt nah dran liegt als auch die Streuung der Daten gut erklärt.

## Ein zweites Feature ergänzen

Dieselbe `LinearRegression` funktioniert mit mehreren Features, ohne dass sich der Ablauf ändert – nur `X` bekommt eine weitere Spalte:

```python
X = df[["Height", "Age"]]
```

Der Rest des Codes (Split, `fit`, `predict`, Metriken) bleibt identisch. Das Modell lernt jetzt eine Ebene statt einer Geraden, die beide Features gleichzeitig berücksichtigt.

## Fazit

- Der Trainingsablauf ist immer gleich: Split → `fit` → `predict` → Metrik.
- MAE in kg ist die direkt verständliche Metrik für dieses Projekt; R² zeigt zusätzlich, wie viel der Schwankung erklärt wird.
- Ein zweites Feature hinzuzufügen ändert nur `X`, nicht den restlichen Code.

Lab 1.3 wechselt von Regression zu Klassifikation: dieselbe Grundlogik, aber ein kategoriales Label.
