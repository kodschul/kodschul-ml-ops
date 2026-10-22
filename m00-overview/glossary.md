# Glossar

| Begriff | Bedeutung | Modul/Lab |
| --- | --- | --- |
| Feature | Eingabespalte, aus der ein Modell lernt (z. B. `Height`, `Age`) | 1.1 |
| Label | Zielspalte, die ein Modell vorhersagen soll (z. B. `Weight`) | 1.1 |
| Überwachtes Lernen | Training mit bekannten Feature-Label-Paaren | 1.1 |
| Regression | Überwachtes Lernen mit einer Zahl als Label | 1.1, 1.2 |
| Klassifikation | Überwachtes Lernen mit einer Kategorie als Label | 1.1, 1.3 |
| Train/Test-Split | Aufteilung der Daten in Trainings- und Testanteil zur fairen Bewertung | 1.2 |
| Überanpassung (Overfitting) | Modell merkt sich Trainingsdaten statt die zugrunde liegende Beziehung zu lernen | 1.1 |
| MAE (Mean Absolute Error) | durchschnittlicher absoluter Vorhersagefehler, in Label-Einheit | 1.2 |
| R² (Bestimmtheitsmaß) | Anteil der erklärten Varianz des Labels | 1.2 |
| Accuracy | Anteil korrekt vorhergesagter Zeilen bei Klassifikation | 1.3 |
| Confusion Matrix | Tabelle aus tatsächlicher und vorhergesagter Kategorie | 1.3 |
| Epoche | ein vollständiger Trainingsdurchlauf über die Trainingsdaten (neuronale Netze) | 1.4 |
| `Flatten` | Keras-Schicht, wandelt ein mehrdimensionales Bild in einen flachen Vektor um | 1.4 |
| `softmax` | Aktivierungsfunktion, wandelt mehrere Ausgabewerte in Wahrscheinlichkeiten um, die zusammen 1 ergeben | 1.4 |
| DVC (Data Version Control) | versioniert Datendateien gekoppelt an Git-Commits | 2.1, 2.2 |
| `.dvc`-Datei | kleine Verweisdatei in Git, zeigt auf die echte Datenversion im DVC-Cache | 2.2 |
| MLflow Run | ein protokollierter Trainingslauf mit Parametern, Metriken und Modell-Artefakt | 2.3 |
| MLflow Experiment | Gruppe zusammengehöriger Runs (hier: alle Gewicht-Modell-Varianten) | 2.3 |
| Model Registry (MLflow) | verwaltet durchnummerierte Versionen eines benannten Modells | 2.3 |
| Alias (MLflow) | Markierung einer Modellversion (z. B. `production`), ersetzt die veralteten „Stages" | 2.3 |
| Kubeflow / Metaflow | größere ML-Plattformen (Pipeline-Orchestrierung, meist Kubernetes); Vergleichsoption zu MLflow | 2.3 |
| Pachyderm | Alternative zu DVC, koppelt Datenversionen an automatisierte Pipeline-Schritte | 2.1 |
| Data Drift | Verschiebung der Eingabedatenverteilung gegenüber den Trainingsdaten | 5.1 |
| Great Expectations / Deequ | Tools zur regelbasierten Datenqualitätsprüfung (Erwartungen an Daten explizit definieren) | 5.1 |
| Feature Store | zentrale Quelle für Features, konsistent für Training und Serving | 3.1 |
| Entity (Feast) | Schlüssel, zu dem Features gehören (z. B. eine Person) | 3.1 |
| Feature View (Feast) | Gruppe zusammengehöriger Features für eine Entity | 3.1 |
| Serialisierung | Speichern eines trainierten Modells als Datei (`joblib.dump`) | 4.1 |
| REST-API | Schnittstelle, über die ein Modell per HTTP erreichbar gemacht wird | 4.1, 4.2 |
| Pydantic `BaseModel` | definiert Eingabe-/Ausgabeformat einer FastAPI-Anfrage | 4.2 |
| Modellverfall (Model Decay) | sinkende Vorhersagequalität über die Zeit, oft Folge von Data Drift | 5.1 |
