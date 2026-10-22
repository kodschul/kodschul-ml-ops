# Lab 2.1 – Übung: Warum Daten-Versionierung?

**Dauer:** ca. 10 Minuten
**Ändert die Gewicht-Projektbasis?** Nein – Vorbereitung für Lab 2.2.

## Ausgangslage

Szenario: `people_stats.csv` wurde letzte Woche zum Training eines Modells verwendet. Heute liegt eine neue Datei mit demselben Namen vor, aber mit mehr/anderen Werten (`people_weight_stats_10x.csv` als Platzhalter für „neue Datencharge").

## Aufgaben

1. Beschreibe in 2-3 Sätzen, was ohne Versionierung passiert, wenn jemand nach dem Austausch der Datei fragt: „Mit welchen Daten wurde das Modell von letzter Woche trainiert?"
2. Notiere, welche zwei Dinge gleichzeitig bekannt sein müssen, um ein Trainingsergebnis später zu reproduzieren (Code-Stand und …?).

## Checkpoint

- Beide Antworten benennen das Kernproblem: ohne Versionierung ist der verwendete Datenstand nicht mehr rekonstruierbar.

## Abschlusskriterien

- Aufgabe 2 nennt explizit „Code-Stand und Datenstand" als die zwei nötigen Informationen.
