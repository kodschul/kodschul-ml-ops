# Lab 2.2 – Lösung: Datenpipeline mit DVC versionieren

## Aufgabe 1: DVC einrichten

```bash
cd project
git init          # falls noch kein Git-Repo existiert
dvc init
git add .dvc .dvcignore
git commit -m "chore: dvc initialisiert"
```

## Aufgabe 2: Ersten Datenstand versionieren (v1)

```bash
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc data/.gitignore
git commit -m "data: people_stats v1 (199 Zeilen)"
```

## Aufgabe 3: Neue Datencharge einspielen (v2)

```bash
cp data/people_weight_stats_10x.csv data/people_stats.csv
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc
git commit -m "data: people_stats v2 (196 Zeilen, neue Charge)"
```

## Aufgabe 4: Commit von v1 finden

```bash
git log --oneline -- data/people_stats.csv.dvc
```

Ausgabe (Beispiel, Hashes variieren):

```text
4f2a1c3 data: people_stats v2 (196 Zeilen, neue Charge)
9b7e0d1 data: people_stats v1 (199 Zeilen)
```

## Aufgabe 5: Rollback auf v1

```bash
git checkout 9b7e0d1 -- data/people_stats.csv.dvc
dvc checkout
```

## Aufgabe 6: Rollback prüfen

```bash
wc -l data/people_stats.csv
```

```text
199 data/people_stats.csv
```

Das entspricht wieder dem Stand von v1 (die Datei hat keinen abschließenden Zeilenumbruch, daher zählt `wc -l` eine Zeile weniger als Datensätze inklusive Kopfzeile).

## Grenzen

Dieser Rollback betrifft nur die Daten. Ein zuvor mit v2 trainiertes Modell müsste separat neu mit v1 trainiert werden, um wieder konsistent zum Datenstand zu sein.
