# Lab 2.2 – Übung: Datenpipeline mit DVC versionieren

**Dauer:** ca. 30 Minuten
**Ändert die Gewicht-Projektbasis?** Ja – versioniert `project/data/people_stats.csv` in zwei Ständen.

## Vorbereitung

`project/data/people_stats.csv` und `project/data/people_weight_stats_10x.csv` liegen bereit. Ein Git-Repository existiert im `project`-Ordner (`git init`, falls noch nicht geschehen).

## Aufgaben

1. Richte DVC im `project`-Ordner ein (`dvc init`) und committe die DVC-Konfiguration.
2. Versioniere `data/people_stats.csv` mit `dvc add` und committe die `.dvc`-Datei als „v1".
3. Ersetze den Inhalt von `data/people_stats.csv` durch den Inhalt von `data/people_weight_stats_10x.csv`, versioniere erneut und committe als „v2".
4. Finde über `git log --oneline -- data/people_stats.csv.dvc` den Commit von v1.
5. Stelle mit `git checkout <commit> -- data/people_stats.csv.dvc` und `dvc checkout` den Datenstand von v1 wieder her.
6. Prüfe mit `wc -l data/people_stats.csv`, ob wieder die ursprüngliche Zeilenzahl (199, da die Datei keinen abschließenden Zeilenumbruch hat) vorliegt.

## Checkpoint

- `git log --oneline -- data/people_stats.csv.dvc` zeigt zwei Commits (v1 und v2).
- Nach Schritt 5 zeigt `wc -l data/people_stats.csv` wieder 199 (der Stand von v1).

## Abschlusskriterien

- Beide Datenstände sind über Git-Commits nachvollziehbar, und der Rollback auf v1 wurde erfolgreich durchgeführt.

## Fallback

Bei Zeitdruck werden die Schritte 1-5 als Demonstration verfolgt statt selbst ausgeführt; Schritt 6 (Prüfung des Rollbacks) wird in jedem Fall eigenständig durchgeführt.
