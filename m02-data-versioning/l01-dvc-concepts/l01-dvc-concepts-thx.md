# Lab 2.1: Warum Daten-Versionierung?

**Leitfragen:**

<details>
<summary>Warum reicht Git allein für Trainingsdaten nicht aus?</summary>

Git ist für Textdateien (Code) optimiert und wird bei großen Binär-/CSV-Dateien langsam und unhandlich, weil jede Version komplett im Repo-Verlauf gespeichert wird. DVC lagert die Daten selbst aus und verwaltet nur einen kleinen Verweis darauf in Git.

</details>

<details>
<summary>Was versioniert DVC zusätzlich?</summary>

DVC versioniert die tatsächlichen Datendateien (über einen Verweis, die `.dvc`-Datei) gekoppelt an den Git-Commit – so lässt sich zu jedem Code-Stand nachvollziehen, mit welchem Datenstand er trainiert wurde.

</details>

- Ohne Datenversionierung ist nicht nachvollziehbar, mit welchem Datenstand ein Modell trainiert wurde.
- DVC (Data Version Control) koppelt Datendateien an Git-Commits, ohne die Dateien selbst in Git zu speichern.

## Das Problem

Ein Modell wird heute mit `people_stats.csv` trainiert und liefert eine bestimmte MAE. Eine Woche später wird dieselbe Datei durch eine neue, größere Datencharge ersetzt (z. B. weil neue Personen erfasst wurden). Ohne Versionierung:

- Es ist nicht mehr feststellbar, welcher Datenstand zu welchem trainierten Modell gehört.
- Ein Ergebnis aus der Vorwoche lässt sich nicht mehr reproduzieren.
- Ein Rollback auf den alten Datenstand ist nur möglich, wenn zufällig eine Kopie existiert.

## Git allein löst das nicht zuverlässig

Git speichert bei jeder Änderung einer Datei eine vollständige neue Version im Repository-Verlauf. Bei großen CSV- oder Binärdateien wächst das Repository dadurch schnell und wird langsam zu klonen.

## Was DVC stattdessen macht

| Komponente | Ort | Inhalt |
| --- | --- | --- |
| `.dvc`-Datei | im Git-Repo | Verweis (Hash) auf die tatsächliche Datenversion |
| echte Daten | DVC-Cache / Remote-Storage | die eigentlichen Dateiinhalte |
| Git-Commit | im Git-Repo | verknüpft Code-Stand und `.dvc`-Datei zu einem Zeitpunkt |

Ein `git checkout <commit>` wechselt den Code-Stand; `dvc checkout` stellt danach die passende Datenversion wieder her.

## Fazit

- Git versioniert Code effizient, aber nicht große Datendateien.
- DVC versioniert Daten über einen kleinen Verweis in Git, die echten Dateien liegen separat.
- Jeder Git-Commit kann so eindeutig einem Datenstand zugeordnet werden.

Lab 2.2 richtet DVC für den Projekt-Datensatz ein und versioniert zwei unterschiedliche Datenstände.
