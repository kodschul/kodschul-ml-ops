# Lab 1.1 – Lösung: Was ist Machine Learning?

## Aufgabe 1: Features und Label markieren

- Features: `Height`, `Age`
- Label: `Weight`

Das Ziel bestimmt, welche Spalte Label ist – hier ist es `Weight`, weil genau diese Spalte vorhergesagt werden soll.

## Aufgabe 2: Vorhersage für eine neue Zeile

Für `Height=180, Age=40` würde das Modell auf Basis der gelernten Beziehung zwischen Größe/Alter und Gewicht in den Trainingsdaten einen Gewichtswert schätzen, zum Beispiel einen Wert nahe am Durchschnittsgewicht ähnlicher Größe/Alter-Kombinationen im Datensatz. Das Modell „kennt" die echte Person nicht, es überträgt nur das gelernte Muster.

## Aufgabe 3: Ähnliche Größe, unterschiedliches Gewicht

Zwei Zeilen mit `Height=195`: eine Person wiegt 63 kg (Age 35), eine andere 59 kg (Age 21). Beide sind sich in der Größe sehr ähnlich, aber das Gewicht unterscheidet sich kaum – in diesem Beispiel passt die Erklärung über `Age` nicht eindeutig. Ein deutlicheres Beispiel: `Height=176, Weight=100, Age=63` gegenüber `Height=177, Weight=50, Age=24` – fast identische Größe, aber 50 kg Unterschied. Das zeigt, dass Größe allein das Gewicht nicht vollständig erklärt; weitere Faktoren (z. B. Körperbau, Aktivität) fehlen im Datensatz und werden nicht modelliert.

## Grenzen

Mit nur zwei Features (`Height`, `Age`) bleibt ein Teil der Gewichtsschwankung unerklärt – das ist normal und wird in Lab 1.2 an der Testmetrik (MAE) sichtbar.
