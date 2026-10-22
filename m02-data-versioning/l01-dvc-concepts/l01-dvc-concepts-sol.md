# Lab 2.1 – Lösung: Warum Daten-Versionierung?

## Aufgabe 1: Was ohne Versionierung passiert

Ohne Versionierung lässt sich die Frage nicht beantworten: Die alte Datei wurde überschrieben, es existiert keine Kopie des Standes von letzter Woche. Im besten Fall gibt es eine manuell angelegte Sicherungskopie mit unklarem Namen; im schlechtesten Fall ist der alte Datenstand endgültig verloren und das Trainingsergebnis nicht mehr nachvollziehbar.

## Aufgabe 2: Die zwei nötigen Informationen

Um ein Trainingsergebnis zu reproduzieren, müssen gleichzeitig bekannt sein:

- der **Code-Stand** (welche Version des Trainingsskripts wurde ausgeführt), und
- der **Datenstand** (welche Version der Trainingsdaten wurde verwendet).

Git liefert den ersten Teil zuverlässig. DVC ergänzt den zweiten Teil, indem es jeden Datenstand über einen Verweis mit einem Git-Commit verknüpft.
