# Lab 5.1 – Übung: Monitoring-Konzepte im Überblick mit Mini-Demo

**Heute im Kurs:** Trainer-Demo (siehe Agenda) – die folgenden Aufgaben sind für das Selbststudium danach gedacht, um den Drift-Check eigenständig nachzuvollziehen.
**Ändert die Gewicht-Projektbasis?** Ja – prüft die Datenqualität der beiden Datenstände aus Modul 2.

## Vorbereitung

`evidently` ist installiert (`pip install -r project/requirements.txt`). `project/data/people_stats.csv` und `project/data/people_weight_stats_10x.csv` liegen bereit.

## Aufgaben

1. Lies `pip show evidently` und notiere die installierte Version.
2. Lade beide CSV-Dateien mit `pandas` (`people_stats.csv` als Referenz, `people_weight_stats_10x.csv` als aktuell).
3. Erzeuge einen `Report([DataDriftPreset()])`, führe ihn mit `report.run(current_data=..., reference_data=...)` aus und speichere das Ergebnis als `drift_report.html`.
4. Öffne `drift_report.html` im Browser und finde die Kennzahl für das Feature `Weight`.
5. Vergleiche Mittelwert, Minimum und Maximum beider Datensätze (z. B. mit `df["Weight"].describe()`).

## Checkpoint

- `drift_report.html` existiert und lässt sich im Browser öffnen.
- Der Report markiert `Weight` als Feature mit erkennbarer Verschiebung.
- Die Mittelwerte beider Datensätze sind notiert (Referenz ca. 76.6 kg, aktuell ca. 79.5 kg).

## Abschlusskriterien

- Ein Satz, der benennt, ob die Verschiebung eher im Mittelwert, in der Streuung oder in den Extremwerten sichtbar ist.

## Fallback

Falls die installierte Evidently-Version eine andere Import-Syntax erwartet (`from evidently.report import Report` statt `from evidently import Report`): im Handout die zur installierten Version passende Variante nutzen, siehe Hinweis dort.
