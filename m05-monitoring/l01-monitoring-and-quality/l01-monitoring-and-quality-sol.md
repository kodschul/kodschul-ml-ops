# Lab 5.1 – Lösung: Monitoring-Konzepte im Überblick mit Mini-Demo

## Aufgaben 1-3: Report erzeugen

```python
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference = pd.read_csv("project/data/people_stats.csv")
current = pd.read_csv("project/data/people_weight_stats_10x.csv")

report = Report([DataDriftPreset()])
result = report.run(current_data=current, reference_data=reference)
result.save_html("drift_report.html")
```

Getestet mit `evidently` 0.7.23 (Oktober 2026). Ältere Evidently-Versionen (0.3.x/0.4.x) verwenden stattdessen `from evidently.report import Report` und `from evidently.metric_preset import DataDriftPreset`.

## Aufgaben 4-5: Kennzahlen vergleichen

```python
print(reference["Weight"].describe())
print(current["Weight"].describe())
```

Ergebnis (getestet):

| Kennzahl | `people_stats.csv` (Referenz) | `people_weight_stats_10x.csv` (aktuell) |
| --- | --- | --- |
| Zeilen | 199 | 196 |
| Gewicht – Mittelwert | 76.6 kg | 79.5 kg |
| Gewicht – Streuung (Std.) | 10.9 kg | 11.0 kg |
| Gewicht – Minimum | 50 kg | 50 kg |
| Gewicht – Maximum | 100 kg | 104 kg |

Der Mittelwert verschiebt sich um knapp 3 kg nach oben, Minimum und Streuung bleiben nahezu gleich, das Maximum steigt leicht. Der Report markiert `Weight` als Feature mit erkennbarem Drift-Signal, vor allem wegen der Mittelwertverschiebung, nicht wegen der Extremwerte.

## Grenzen

Dieser Vergleich prüft nur die Rohdaten (Data Drift), nicht die tatsächliche Vorhersagequalität eines Modells auf den neuen Daten – dafür wären echte, aktuelle Labels nötig, die hier nicht vorliegen.
