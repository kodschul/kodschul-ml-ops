# Lab 4.1: Modell speichern und bereitstellen

**Leitfragen:**

<details>
<summary>Was unterscheidet „Modell im Code laden" von „Modell als Service bereitstellen"?</summary>

Beim Laden im Code nutzt nur das eine Skript/Programm das Modell direkt. Als Service bereitgestellt ist das Modell über eine definierte Schnittstelle (z. B. HTTP-API) von beliebigen anderen Anwendungen nutzbar, ohne deren Code oder Sprache zu kennen.

</details>

<details>
<summary>Wann lohnt sich ein dedizierter Serving-Server?</summary>

Bei hohem Anfragevolumen, mehreren Modellversionen gleichzeitig oder wenn viele unterschiedliche Anwendungen dasselbe Modell nutzen sollen – für ein einzelnes internes Tool reicht oft eine einfache API.

</details>

- Ein trainiertes Modell ist zunächst nur eine Datei; erst eine Schnittstelle macht es für andere Anwendungen nutzbar.
- Serialisierung speichert ein trainiertes Modell so, dass es später ohne erneutes Training geladen werden kann.

## Modelle serialisieren

```python
import joblib

joblib.dump(model, "weight_model.joblib")
geladen = joblib.load("weight_model.joblib")
```

`joblib` speichert das komplette trainierte Modellobjekt (gelernte Koeffizienten inklusive) in einer Datei. Beim Laden entsteht ein identisches Modell, ohne erneutes Training.

## Serving-Optionen im Vergleich

| Option | Prinzip | Geeignet für |
| --- | --- | --- |
| Modell im Code laden | `joblib.load()` direkt im Anwendungscode | ein einzelnes Skript/eine einzelne Anwendung |
| Einfache REST-API (FastAPI) | Modell einmal laden, über HTTP-Endpunkt erreichbar machen | kleine Projekte, ein bis wenige Anwendungen |
| MLflow Model Serving | MLflow verwaltet Modellversionen und stellt sie über einen Server bereit | mehrere Modellversionen, Teamnutzung |
| TFServe / KServe | spezialisierte Serving-Server für TensorFlow-Modelle bzw. Kubernetes-Umgebungen | hohe Last, viele gleichzeitige Modelle, produktive Skalierung |

## Event-basierte Pipelines und Plattformen

Für Echtzeitszenarien mit kontinuierlichem Datenstrom (statt einzelner Anfragen) existieren event-basierte ML-Pipelines, die Vorhersagen direkt auf eingehende Ereignisse anwenden. Plattformen wie Kubeflow, MLflow oder Metaflow bündeln Versionierung, Serving und Monitoring in einer gemeinsamen Umgebung, statt einzelne Tools manuell zu kombinieren.

## Fazit

- Serialisierung (`joblib.dump`/`load`) ist die Grundlage jeder Serving-Variante.
- Die Wahl der Serving-Option hängt von Anfragevolumen, Anzahl Nutzer:innen und Teamgröße ab.
- Für dieses Projekt reicht eine einfache REST-API – das wird in Lab 4.2 umgesetzt.
