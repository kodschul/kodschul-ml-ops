# Lab 6.1: MLOps Best Practices & Anti-Patterns

**Leitfragen:**

<details>
<summary>Was kann passieren, wenn ein neues Modell direkt als „production" markiert wird, ohne die Metriken vorher mit der aktuellen Version zu vergleichen?</summary>

Ein schlechteres Modell kann unbemerkt ein besseres ersetzen – ohne Versionsvergleich fällt das erst auf, wenn die Vorhersagen in der Praxis auffällig schlecht werden, womöglich erst nach Tagen oder Wochen. Mit MLflow lässt sich das verhindern, indem die Metriken der neuen Version vor dem Alias-Wechsel mit der aktuellen `production`-Version verglichen werden.

</details>

<details>
<summary>Warum ist „funktioniert bei mir auf dem Rechner" keine ausreichende Prüfung vor einem Produktiv-Deployment?</summary>

Unterschiedliche Paketversionen (siehe die Evidently-API-Änderung in Modul 5), unterschiedliche Daten oder ein fehlender Validierungsschritt können dazu führen, dass etwas lokal funktioniert, aber in einer anderen Umgebung bricht. Erst ein reproduzierbarer, versionierter Stand (Daten, Code, Modell, Paketversionen) macht „funktioniert" zu einer verlässlichen Aussage.

</details>

- Dieser Tag hat fünf Bausteine gezeigt: ML-Grundlagen, Datenversionierung (DVC), Modell-/Experiment-Versionierung (MLflow), Feature Stores, Serving und Monitoring. Dieses Modul fasst zusammen, welche Gewohnheiten aus der Praxis diese Bausteine zu einem verlässlichen Gesamtsystem machen – und welche typischen Fehler das Gegenteil bewirken.
- Keine neue Technik, sondern eine Zusammenfassung: was aus den bisherigen Modulen als wiederkehrendes Prinzip mitgenommen werden sollte.

## Tun / Nicht tun

| Bereich | Tun | Nicht tun |
| --- | --- | --- |
| Reproduzierbarkeit | Daten (DVC), Code (Git) und Modell/Experiment (MLflow) gemeinsam versionieren, damit jeder Stand nachvollziehbar ist | sich auf „ich erinnere mich schon, welche Daten das waren" verlassen |
| Abhängigkeiten | Paketversionen in `requirements.txt` festhalten (pinnen), besonders bei Bibliotheken mit häufigen API-Änderungen | Pakete ohne Versionsangabe installieren und darauf hoffen, dass sich nichts geändert hat (siehe Evidently-Beispiel in Modul 5) |
| Deployment | eine neue Modellversion erst anhand der Metriken mit der aktuellen `production`-Version vergleichen, bevor der Alias umgesetzt wird | ein neu trainiertes Modell ungeprüft produktiv setzen, nur weil das Training „durchgelaufen" ist |
| Validierung | die API mit bekannten Testwerten prüfen, bevor sie für andere erreichbar ist (z. B. der `curl`-Test aus Lab 4.2) | eine API starten und direkt als „fertig" betrachten, ohne eine einzige Testanfrage gestellt zu haben |
| Rollback | durch durchgängige Versionierung jederzeit auf einen früheren Daten-, Code- oder Modellstand zurückkehren können | Änderungen überschreiben, ohne dass der vorherige Stand noch auffindbar ist |
| Monitoring | Datenqualität/Drift regelmäßig prüfen, auch wenn das Modell „bisher gut lief" | annehmen, ein einmal gut funktionierendes Modell bleibe automatisch so gut |

## Warum das zusammengehört

Jeder einzelne Baustein (DVC, MLflow, Feast, FastAPI, Evidently) löst für sich ein Teilproblem. Der eigentliche Nutzen entsteht erst durch das Zusammenspiel: Ein Rollback auf einen früheren Datenstand (DVC) ist nur sinnvoll nachvollziehbar, wenn auch bekannt ist, welches Modell (MLflow) mit diesem Datenstand zusammengehört. Eine erkannte Datendrift (Evidently) führt erst dann zu einer Handlung, wenn klar ist, welches Modell gerade `production` ist und wie es ersetzt wird.

## Fazit

- Versionierung (Daten, Code, Modell) ist die Voraussetzung für Reproduzierbarkeit und Rollback – keine optionale Zusatzübung.
- Ein Modell produktiv zu setzen ist ein bewusster Schritt (Metriken vergleichen, Alias setzen), kein automatischer Nebeneffekt des Trainings.
- Monitoring ist kein einmaliger Check, sondern eine laufende Gewohnheit – Daten und Anforderungen verändern sich, auch wenn der Code gleich bleibt.

Zum Tagesabschluss wird aus diesen Prinzipien eine kurze Showcase-Struktur für die eigene Pipeline abgeleitet.
