# FAQ

**Warum trainiert Lab 1.2 heute direkt mit `Height` und `Age` zusammen, statt zuerst nur mit `Height`?**
In der ursprünglichen Fassung wurde zuerst nur `Height` trainiert, um den Effekt eines zusätzlichen Features sichtbar zu machen (MAE sinkt von 7.36 kg auf 6.66 kg). Da die Teilnehmerin diesen Effekt bereits aus eigener Erfahrung kennt, entfällt der Zwischenschritt – die Zahlen bleiben als Vergleich im Handout erhalten.

**Warum ist Modul 1 heute so kurz (65 statt ursprünglich 165 Minuten)?**
Die Teilnehmerin hat bereits ein ML-Modell gebaut (Master-Thesis) und braucht keine Einführung in ML-Grundlagen – nur einen kurzen Begriffsabgleich und das eine Projektmodell, mit dem der restliche Tag arbeitet. Die gewonnene Zeit fließt in echte Hands-on-Tiefe für Versionierung, Serving und Best Practices.

**Warum ist die Accuracy beim Titanic-Beispiel nur rund 78 % und nicht höher?**
Das Lab nutzt bewusst nur 3 Features (`Pclass`, `Age`, `Sex`) statt aller verfügbaren Spalten, um die Grundidee der logistischen Regression klar zu halten. Mehr Features (z. B. `Fare`, `SibSp`, `Parch`) können die Genauigkeit erhöhen, auf Kosten von mehr Komplexität.

**Warum nutzt Lab 1.4 Bilddaten (MNIST) statt wieder das Gewicht-Beispiel?**
Bei Größe/Alter → Gewicht (2 Features, ~200 Zeilen) schneidet ein neuronales Netz nicht besser ab als `LinearRegression` – das zeigt zwar den gleichen Workflow, aber nicht, wofür TensorFlow tatsächlich gebraucht wird. Bilderkennung ist ein Fall, in dem ein neuronales Netz einem einfachen Modell wirklich überlegen ist (97.6 % vs. 92.6 % Genauigkeit, siehe Lab 1.4).

**Wird die DVC-Übung mit einem Remote-Storage (Cloud) durchgeführt?**
Nein, Lab 2.2 arbeitet rein lokal. Ein Remote-Storage wäre für Teamarbeit sinnvoll, ist aber für ein Einzelsetting an einem Tag nicht nötig.

**Warum gibt es sowohl DVC als auch MLflow – reicht nicht eins von beiden?**
Sie lösen unterschiedliche Probleme: DVC versioniert die Eingabedaten (welcher Datenstand), MLflow versioniert, was beim Training daraus entsteht (Parameter, Metriken, Modell je Run) und verwaltet produktive Modellversionen. In der Praxis werden beide meist zusammen eingesetzt (Lab 2.3).

**Warum braucht MLflow eine SQLite-Datei statt einfach nur eines Ordners?**
Neuere MLflow-Versionen (ab 3.x) unterstützen den klassischen reinen Dateiordner nicht mehr als Tracking-Backend, sobald die Model Registry genutzt wird – eine lokale SQLite-Datenbank ist der heute empfohlene, einfachste Ersatz dafür (Lab 2.3).

**Warum wird Feast nur als Demo gezeigt und nicht selbst installiert?**
Aus Zeitgründen: Eine eigene Feast-Installation inklusive Online-Store würde mehr Zeit beanspruchen, als das Zeitbudget von Modul 3 zulässt. Die Konzepte (Entity, Feature View) werden trotzdem vollständig erklärt.

**Was passiert, wenn die API in Lab 4.2 einen unrealistischen Wert bekommt (z. B. negatives Alter)?**
Ohne zusätzliche Prüfung liefert das Modell trotzdem eine Zahl zurück – Pydantic prüft nur den Datentyp, nicht die fachliche Plausibilität. Die Erweiterung in Lab 4.2 zeigt, wie eine einfache Prüfung ergänzt wird.

**Warum wird in Lab 5.1 kein eigenes Modell auf Drift überwacht, sondern nur die Rohdaten verglichen?**
Für die Kurszeit reicht der direkte Vergleich der beiden Datenstände (`people_stats.csv` vs. `people_weight_stats_10x.csv`), um das Grundprinzip von Data Drift zu zeigen, ohne ein zusätzliches Monitoring-Setup für das Modell selbst aufzubauen.

**Was mache ich mit dem Projekt nach dem Kurs?**
Alle Datensätze liegen in `project/data/`, alle Code-Beispiele in den jeweiligen Lab-Lösungen (`-sol.md`). Der komplette Ablauf (Training → Versionierung → Serving → Monitoring) lässt sich eigenständig auf dem eigenen Rechner wiederholen.
