# Lab 1.3: Überleben auf der Titanic vorhersagen mit logistischer Regression

**Leitfragen:**

<details>
<summary>Was unterscheidet eine Regressions- von einer Klassifikationsaufgabe?</summary>

Regression sagt eine Zahl vorher (Gewicht in kg), Klassifikation eine Kategorie aus einer festen Menge (überlebt/nicht überlebt). Der Trainingsablauf ist gleich, nur Modelltyp und Metrik ändern sich.

</details>

<details>
<summary>Warum muss `Sex` vor dem Training in Zahlen umgewandelt werden?</summary>

scikit-learn-Modelle rechnen nur mit Zahlen. Ein Text wie `"male"`/`"female"` muss vorher in `1`/`0` kodiert werden.

</details>

<details>
<summary>Was zeigt die Confusion Matrix, das die Accuracy allein nicht zeigt?</summary>

Sie zeigt, welche Art von Fehler passiert: ob das Modell eher Überlebende übersieht (false negatives) oder fälschlich Überleben vorhersagt (false positives) – zwei verschiedene Fehlerarten mit unterschiedlichen Konsequenzen.

</details>

- Logistische Regression ist trotz des Namens ein Klassifikationsmodell: Es sagt eine Wahrscheinlichkeit zwischen 0 und 1 vorher und rundet auf eine Kategorie.
- Dieses Beispiel nutzt bewusst nur 3 Features (`Pclass`, `Sex`, `Age`) statt der 6 im Originalskript, um die Grundidee klar zu halten.

## Datensatz

`project/data/titanic_train.csv` enthält 891 Passagiere der Titanic, u. a.:

| Spalte | Bedeutung |
| --- | --- |
| `Survived` | Zielspalte: 0 = nicht überlebt, 1 = überlebt |
| `Pclass` | Ticketklasse (1 = erste Klasse, 3 = dritte Klasse) |
| `Sex` | Geschlecht (`"male"`/`"female"`) |
| `Age` | Alter in Jahren, bei 177 Zeilen unbekannt (leer) |

## Kategoriale Werte kodieren

```python
df["Sex"] = [1 if s == "male" else 0 for s in df["Sex"]]
```

Jede Zeichenkette wird vor dem Training durch eine Zahl ersetzt. Das Modell selbst weiß danach nicht mehr, dass `1` ursprünglich `"male"` war – die Zuordnung muss beim Lesen der Ergebnisse im Kopf behalten werden.

## Fehlende Werte

177 der 891 Zeilen haben kein bekanntes Alter. Die einfachste Lösung für dieses Lab: Zeilen ohne `Age` werden verworfen.

```python
df = df[df["Age"].notna()]
```

Das reduziert den Datensatz auf 714 nutzbare Zeilen. Eine Alternative (Lücken mit dem Median füllen) behält mehr Zeilen, wurde hier aber bewusst weggelassen, um die Übung einfach zu halten.

## Logistische Regression trainieren

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

`max_iter=1000` erhöht die Anzahl der Optimierungsschritte gegenüber dem Standardwert – ohne das bricht das Training bei diesem Datensatz mit einer Warnung ab, bevor es konvergiert.

## Accuracy und Confusion Matrix

| Metrik | Bedeutung |
| --- | --- |
| Accuracy | Anteil korrekt vorhergesagter Zeilen an allen Testzeilen |
| Confusion Matrix | Tabelle aus tatsächlicher und vorhergesagter Kategorie, zeigt beide Fehlerarten getrennt |

```python
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

Eine Confusion Matrix für ein binäres Label hat diese Form:

| | Vorhergesagt: 0 | Vorhergesagt: 1 |
| --- | --- | --- |
| **Tatsächlich: 0** | richtig negativ | falsch positiv |
| **Tatsächlich: 1** | falsch negativ | richtig positiv |

## Fazit

- Klassifikation nutzt denselben Ablauf wie Regression (Split → `fit` → `predict` → Metrik), aber ein anderes Modell und andere Metriken.
- Kategoriale Features müssen vor dem Training in Zahlen umgewandelt werden.
- Die Confusion Matrix zeigt zwei unterschiedliche Fehlerarten, die eine einzelne Accuracy-Zahl verdeckt.

Lab 1.4 kehrt zur Gewicht-Vorhersage zurück und zeigt denselben Workflow mit TensorFlow.
