"""
Produktionssystem: Monitoring.

Vergleicht den aktuellen Datenstand mit einer Referenz und erzeugt einen
Evidently-Drift-Report. Getestet mit evidently 0.7.23.

Ausfuehren aus final-system/:
    python src/monitor.py
"""
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

REFERENCE_PATH = "../data/people_stats.csv"
CURRENT_PATH = "../data/people_weight_stats_10x.csv"
REPORT_PATH = "reports/drift_report.html"

reference = pd.read_csv(REFERENCE_PATH)
current = pd.read_csv(CURRENT_PATH)

report = Report([DataDriftPreset()])
result = report.run(current_data=current, reference_data=reference)
result.save_html(REPORT_PATH)

print("Report gespeichert:", REPORT_PATH)
print("Referenz - Gewicht Mittelwert:", round(reference["Weight"].mean(), 1), "kg")
print("Aktuell  - Gewicht Mittelwert:", round(current["Weight"].mean(), 1), "kg")
