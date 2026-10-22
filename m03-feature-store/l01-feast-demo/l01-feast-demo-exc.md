# Lab 3.1 – Übung: Feature Stores – Konzept und Mini-Demo mit Feast

**Heute im Kurs:** Trainer-Demo (siehe Agenda) – die folgenden Aufgaben sind für das Selbststudium danach gedacht, um Feast eigenständig nachzuvollziehen.
**Ändert die Gewicht-Projektbasis?** Nein – Demo, keine Codeänderung am Projekt.

## Vorbereitung

`feast` ist installiert (`pip install -r project/requirements.txt`). `project/data/people_stats.csv` liegt bereit.

## Aufgaben

1. Erzeuge aus `people_stats.csv` eine Parquet-Datei mit zusätzlicher `person_id`-Spalte (fortlaufende Nummer) und `event_timestamp`-Spalte.
2. Lege einen `feature_repo/`-Ordner mit `feature_store.yaml` (lokaler Provider, SQLite-Online-Store) an.
3. Definiere in `features.py` eine `Entity` (`person_id`, `value_type=ValueType.INT64`) und eine `FeatureView` mit den Feldern `height`, `age`.
4. Führe `feast apply` im `feature_repo/`-Ordner aus.
5. Befülle den Online Store mit `feast materialize <von> <bis>` (expliziter Zeitraum, nicht `materialize-incremental`).
6. Rufe die Features für `person_id=42` ab (Skript **außerhalb** von `feature_repo/` platzieren) und vergleiche das Ergebnis mit Zeile 42 in `people_stats.csv`.

## Checkpoint

- `feast apply` läuft ohne Fehler durch.
- `feast materialize` schreibt sichtbar Zeilen in den Online Store (nicht 0).
- Der Abruf für `person_id=42` liefert dieselben `height`/`age`-Werte wie die CSV-Zeile.

## Abschlusskriterien

- Ein Satz, der erklärt, warum `value_type=ValueType.INT64` und die Position von `demo.py` außerhalb von `feature_repo/` beide notwendig sind (siehe Handout).

## Fallback

Bei Problemen mit `feast materialize`: zuerst `value_type` der Entity prüfen, dann den Zeitraum des `materialize`-Aufrufs gegen die `event_timestamp`-Werte der Parquet-Datei prüfen.
