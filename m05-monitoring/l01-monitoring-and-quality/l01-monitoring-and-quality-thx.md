# Lab 5.1: Monitoring-Konzepte im Überblick mit Mini-Demo

**Leitfragen:**

<details>
<summary>Woran erkennt man, dass ein Modell „veraltet"?</summary>

Entweder die Modell-Performance sinkt messbar (z. B. höhere MAE auf neuen Daten), oder die Verteilung der Eingabedaten verschiebt sich gegenüber den Trainingsdaten (Data Drift) – beides ein Hinweis, dass das gelernte Muster nicht mehr zur aktuellen Realität passt.

</details>

<details>
<summary>Ab welchem Signal würde man im echten Betrieb reagieren – zum Beispiel neu trainieren?</summary>

Sobald eine Kennzahl (z. B. Mittelwert oder Streuung eines Features) dauerhaft und deutlich von der Trainingsverteilung abweicht, nicht bei jeder kleinen Schwankung einzelner Anfragen.

</details>

- Ein einmal trainiertes Modell bleibt unverändert, auch wenn sich die realen Daten mit der Zeit verändern.
- Monitoring prüft regelmäßig, ob aktuelle Daten noch zur Trainingsverteilung passen.

## Warum Monitoring nach dem Deployment

Ein Modell lernt eine feste Beziehung aus den Trainingsdaten. Verändert sich die reale Welt (z. B. eine neue Personengruppe, veränderte Messmethoden), bleibt das Modell unverändert – es „merkt" nichts von der Veränderung, bis jemand es überprüft.

| Begriff | Bedeutung |
| --- | --- |
| Data Drift | die Verteilung der Eingabedaten verschiebt sich gegenüber den Trainingsdaten |
| Modellverfall (Model Decay) | die Vorhersagequalität sinkt mit der Zeit, oft als Folge von Data Drift |

## Tool-Überblick

| Tool | Fokus |
| --- | --- |
| Evidently | Vergleichsreports zwischen Referenz- und aktuellen Daten (Drift, Datenqualität) |
| NannyML | Schätzung der Modell-Performance ohne aktuelle echte Labels |
| Grafana | Dashboards für Kennzahlen über die Zeit, meist in Kombination mit einer Metrik-Datenbank |

## Mini-Demo: Referenz- vs. aktuelle Daten vergleichen

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

Getestet mit `evidently` 0.7.23 (Oktober 2026). Ältere Evidently-Versionen (0.3.x/0.4.x) verwenden stattdessen `from evidently.report import Report` und `from evidently.metric_preset import DataDriftPreset` – vor Kursbeginn mit der installierten Version gegenprüfen.

## Was der Vergleich zeigt

Die tatsächlichen Kennzahlen beider Datensätze:

| Kennzahl | `people_stats.csv` (Referenz) | `people_weight_stats_10x.csv` (aktuell) |
| --- | --- | --- |
| Zeilen | 199 | 196 |
| Gewicht – Mittelwert | 76.6 kg | 79.5 kg |
| Gewicht – Streuung (Std.) | 10.9 kg | 11.0 kg |
| Gewicht – Minimum | 50 kg | 50 kg |
| Gewicht – Maximum | 100 kg | 104 kg |

Der Mittelwert verschiebt sich um knapp 3 kg nach oben, Minimum und Streuung bleiben nahezu gleich, das Maximum steigt leicht. Ein Report wie oben würde diese Verschiebung als Drift-Signal für das Feature `Weight` markieren.

## Fazit

- Monitoring prüft, ob aktuelle Daten noch zur Trainingsverteilung passen – unabhängig davon, ob schon eine Performance-Verschlechterung sichtbar ist.
- Eine Verschiebung im Mittelwert ist ein typisches erstes Drift-Signal, auch wenn Minimum/Maximum kaum abweichen.
- Ein Drift-Signal ist ein Hinweis zum Nachschauen, nicht automatisch ein Grund für sofortiges Neutraining.

Der Tagesabschluss verbindet alle Schritte – Training, Versionierung, Feature Store, Serving, Monitoring – zu einem Gesamtbild.
