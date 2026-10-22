# Monitoring-Cheatsheet

Schnellreferenz für die in Modul 5 verwendeten Begriffe und Befehle.

| Begriff/Befehl | Bedeutung |
| --- | --- |
| Data Drift | Verteilung der Eingabedaten verschiebt sich gegenüber den Trainingsdaten |
| Modellverfall (Model Decay) | sinkende Vorhersagequalität über die Zeit, oft Folge von Data Drift |
| `Report([DataDriftPreset()])` | Evidently-Report mit Standard-Drift-Metriken definieren |
| `report.run(current_data=..., reference_data=...)` | Report für zwei Datenstände berechnen |
| `result.save_html("datei.html")` | Report als HTML-Datei speichern, im Browser zu öffnen |

## Faustregeln

- Referenzdaten = der Datenstand, mit dem das Modell trainiert wurde; aktuelle Daten = der neueste verfügbare Stand.
- Eine Verschiebung im Mittelwert ist oft das erste sichtbare Drift-Signal, auch wenn Minimum/Maximum kaum abweichen.
- Die Evidently-API ändert sich zwischen Versionen – `from evidently import Report` + `from evidently.presets import DataDriftPreset` (ab 0.7.x) vs. `from evidently.report import Report` + `from evidently.metric_preset import DataDriftPreset` (0.3.x/0.4.x). Vor Kursbeginn mit der installierten Version gegenprüfen.
