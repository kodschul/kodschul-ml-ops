# Lab 1.1: Was ist Machine Learning?

**Leitfragen:**

<details>
<summary>Was unterscheidet überwachtes von unüberwachtem Lernen?</summary>

Überwachtes Lernen trainiert mit bekannten Beispielpaaren aus Eingabe und richtigem Ergebnis (z. B. Größe → Gewicht). Unüberwachtes Lernen findet Muster in Daten ohne vorgegebenes Ergebnis (z. B. Gruppen ähnlicher Datenpunkte).

</details>

<details>
<summary>Was ist ein Feature, was ein Label – hier konkret: Größe, Alter, Gewicht?</summary>

Ein Feature ist eine Eingabespalte, aus der das Modell lernt (`Height`, `Age`). Das Label ist die Zielspalte, die vorhergesagt werden soll (`Weight`).

</details>

<details>
<summary>Woran erkennt man ein überangepasstes Modell?</summary>

Es erklärt die Trainingsdaten sehr gut, versagt aber bei neuen, unbekannten Daten – die Testmetrik ist deutlich schlechter als die Trainingsmetrik.

</details>

- Ein Modell lernt aus Beispieldaten, es wird nicht programmiert.
- Überwachtes Lernen hat zwei Grundtypen: Regression (Zahl) und Klassifikation (Kategorie).

## Features und Label

Ein Datensatz für überwachtes Lernen besteht aus Eingabespalten (Features) und einer Zielspalte (Label):

| Height | Weight | Age |
| --- | --- | --- |
| 161 | 90 | 49 |
| 173 | 78 | 54 |
| 195 | 63 | 35 |
| 157 | 61 | 65 |
| 195 | 59 | 21 |

In diesem Datensatz (`project/data/people_stats.csv`) sind `Height` und `Age` die Features, `Weight` ist das Label. Ein Modell lernt aus vielen solcher Zeilen, wie Features und Label zusammenhängen, und wendet das Gelernte danach auf neue, unbekannte Zeilen an.

## Regression vs. Klassifikation

Überwachtes Lernen hat zwei Grundformen, die sich nur im Typ des Labels unterscheiden:

| Typ | Label | Beispiel heute | Metrik |
| --- | --- | --- | --- |
| Regression | eine Zahl | Gewicht in kg (Lab 1.2) | MAE, R² |
| Klassifikation | eine Kategorie | überlebt/nicht überlebt (Lab 1.3) | Accuracy, Confusion Matrix |

Beide folgen demselben Ablauf: Daten aufteilen, Modell trainieren, mit unbekannten Daten testen, Ergebnis mit einer Metrik bewerten.

## Training, Test und Überanpassung

Ein Modell wird nie auf allen vorhandenen Daten bewertet, sondern auf einem zurückgehaltenen Testanteil, den es beim Training nicht gesehen hat.

- **Trainingsdaten:** das Modell lernt daraus die Beziehung zwischen Features und Label.
- **Testdaten:** unbekannte Zeilen, an denen gemessen wird, ob das Gelernte verallgemeinert.
- **Überanpassung (Overfitting):** das Modell merkt sich Eigenheiten der Trainingsdaten statt die zugrunde liegende Beziehung zu lernen – gute Trainingsmetrik, schlechte Testmetrik.

## Fazit

- Ein Feature ist eine Eingabespalte, ein Label die Zielspalte.
- Regression sagt eine Zahl vorher, Klassifikation eine Kategorie – gleicher Trainingsablauf, andere Metrik.
- Training/Test-Split prüft, ob ein Modell verallgemeinert oder nur die Trainingsdaten auswendig gelernt hat.

Lab 1.2 wendet das auf den ersten eigenen Datensatz an: Gewicht aus Größe vorhersagen.
