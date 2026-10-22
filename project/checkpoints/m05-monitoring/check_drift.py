"""
Checkpoint: Lab 5.1 - Monitoring-Konzepte im Ueberblick mit Mini-Demo.

Vergleicht die Referenzdaten mit der neuen Datencharge und erzeugt einen
Evidently-Report. Getestet mit evidently 0.7.23 (Oktober 2026) - die API
hat sich gegenueber aelteren Evidently-Versionen (0.3.x/0.4.x) geaendert;
bei einer anderen installierten Version ggf. anpassen.

Ausfuehren aus dem project/-Ordner:
    python checkpoints/m05-monitoring/check_drift.py
"""
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference = pd.read_csv("data/people_stats.csv")
current = pd.read_csv("data/people_weight_stats_10x.csv")

report = Report([DataDriftPreset()])
result = report.run(current_data=current, reference_data=reference)
result.save_html("drift_report.html")

print("Report gespeichert als drift_report.html")
print("Referenz - Gewicht Mittelwert:", round(reference["Weight"].mean(), 1), "kg")
print("Aktuell  - Gewicht Mittelwert:", round(current["Weight"].mean(), 1), "kg")
