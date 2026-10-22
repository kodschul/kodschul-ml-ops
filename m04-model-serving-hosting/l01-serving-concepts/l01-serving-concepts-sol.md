# Lab 4.1 – Lösung: Modell speichern und bereitstellen

## Aufgabe 1: Checkliste ausgefüllt

| Kriterium | Eigene Einschätzung |
| --- | --- |
| Anzahl Nutzer:innen | 1 (Teilnehmer:in selbst, zum Ausprobieren und Zeigen) |
| Erwartetes Anfragevolumen | sehr niedrig, einzelne Testanfragen |
| Passende Serving-Option | einfache REST-API (FastAPI) |
| Begründung | kein Mehraufwand durch Serving-Server-Infrastruktur nötig, Ergebnis ist trotzdem über HTTP erreichbar und vorführbar |

## Aufgabe 2: Wann eine andere Option passt

MLflow Model Serving würde sich lohnen, sobald mehrere Modellversionen gleichzeitig verwaltet und verglichen werden müssen (z. B. mehrere Teammitglieder trainieren eigene Varianten). TFServe/KServe würde sich lohnen, sobald das Modell produktiv mit hoher Anfragelast und in einer Kubernetes-Umgebung betrieben werden soll – beides liegt außerhalb des heutigen Rahmens mit 1 Teilnehmer:in und lokaler Nutzung.
