# FAQ

**Warum wird in Lab 1.2 zuerst nur `Height` verwendet, obwohl `Age` auch verfügbar ist?**
Um den Effekt eines zusätzlichen Features sichtbar zu machen: Erst wird mit einem Feature trainiert, dann mit zwei – der MAE-Unterschied zeigt direkt, ob das zweite Feature hilft.

**Warum ist die Accuracy beim Titanic-Beispiel nur rund 78 % und nicht höher?**
Das Lab nutzt bewusst nur 3 Features (`Pclass`, `Age`, `Sex`) statt aller verfügbaren Spalten, um die Grundidee der logistischen Regression klar zu halten. Mehr Features (z. B. `Fare`, `SibSp`, `Parch`) können die Genauigkeit erhöhen, auf Kosten von mehr Komplexität.

**Warum nutzt Lab 1.4 Bilddaten (MNIST) statt wieder das Gewicht-Beispiel?**
Bei Größe/Alter → Gewicht (2 Features, ~200 Zeilen) schneidet ein neuronales Netz nicht besser ab als `LinearRegression` – das zeigt zwar den gleichen Workflow, aber nicht, wofür TensorFlow tatsächlich gebraucht wird. Bilderkennung ist ein Fall, in dem ein neuronales Netz einem einfachen Modell wirklich überlegen ist (97.6 % vs. 92.6 % Genauigkeit, siehe Lab 1.4).

**Wird die DVC-Übung mit einem Remote-Storage (Cloud) durchgeführt?**
Nein, Lab 2.2 arbeitet rein lokal. Ein Remote-Storage wäre für Teamarbeit sinnvoll, ist aber für ein Einzelsetting an einem Tag nicht nötig.

**Warum wird Feast nur als Demo gezeigt und nicht selbst installiert?**
Aus Zeitgründen: Eine eigene Feast-Installation inklusive Online-Store würde mehr Zeit beanspruchen, als das Zeitbudget von Modul 3 zulässt. Die Konzepte (Entity, Feature View) werden trotzdem vollständig erklärt.

**Was passiert, wenn die API in Lab 4.2 einen unrealistischen Wert bekommt (z. B. negatives Alter)?**
Ohne zusätzliche Prüfung liefert das Modell trotzdem eine Zahl zurück – Pydantic prüft nur den Datentyp, nicht die fachliche Plausibilität. Die Erweiterung in Lab 4.2 zeigt, wie eine einfache Prüfung ergänzt wird.

**Warum wird in Lab 5.1 kein eigenes Modell auf Drift überwacht, sondern nur die Rohdaten verglichen?**
Für die Kurszeit reicht der direkte Vergleich der beiden Datenstände (`people_stats.csv` vs. `people_weight_stats_10x.csv`), um das Grundprinzip von Data Drift zu zeigen, ohne ein zusätzliches Monitoring-Setup für das Modell selbst aufzubauen.

**Was mache ich mit dem Projekt nach dem Kurs?**
Alle Datensätze liegen in `project/data/`, alle Code-Beispiele in den jeweiligen Lab-Lösungen (`-sol.md`). Der komplette Ablauf (Training → Versionierung → Serving → Monitoring) lässt sich eigenständig auf dem eigenen Rechner wiederholen.
