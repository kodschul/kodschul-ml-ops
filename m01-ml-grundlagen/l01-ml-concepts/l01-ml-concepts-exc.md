# Lab 1.1 – Übung: Was ist Machine Learning?

**Heute im Kurs:** kurzer mündlicher Abgleich im Plenum (10 Min.), keine schriftliche Einzelübung – die Teilnehmerin kennt die Grundbegriffe bereits aus eigener Praxis. Die folgenden Aufgaben dienen als Gesprächsleitfaden und optional als Selbststudium-Referenz.

**Ändert die Gewicht-Projektbasis?** Nein – Vorbereitung, es wird noch kein Modell trainiert.

## Ausgangslage

Ein Ausschnitt aus `project/data/people_stats.csv`:

| Height | Weight | Age |
| --- | --- | --- |
| 161 | 90 | 49 |
| 173 | 78 | 54 |
| 195 | 63 | 35 |
| 157 | 61 | 65 |
| 195 | 59 | 21 |
| 177 | 50 | 24 |
| 179 | 67 | 29 |
| 176 | 100 | 63 |

## Aufgaben

1. Markiere in der Tabelle, welche Spalte(n) Features sind und welche Spalte das Label ist, wenn das Ziel „Gewicht aus Größe und Alter vorhersagen" lautet.
2. Beschreibe in einem Satz, was ein trainiertes Modell mit einer neuen Zeile (`Height=180, Age=40`, `Weight` unbekannt) tun würde.
3. Nenne ein Beispiel aus dem Datensatz, bei dem zwei Personen ähnliche Größe, aber sehr unterschiedliches Gewicht haben – und formuliere eine mögliche Erklärung (welches Feature könnte fehlen?).

## Checkpoint

- Features und Label sind korrekt benannt (`Height`, `Age` als Features; `Weight` als Label).
- Für Aufgabe 2 ist beschrieben, dass das Modell aus den gelernten Mustern einen Gewichtswert vorhersagt, ohne die echte Zeile je gesehen zu haben.

## Abschlusskriterien

- Alle drei Aufgaben sind beantwortet und mit einer kurzen Begründung versehen.
