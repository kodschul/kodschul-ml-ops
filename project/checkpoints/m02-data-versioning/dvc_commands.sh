#!/bin/bash
# Checkpoint: Lab 2.2 - Datenpipeline mit DVC versionieren.
# Referenzablauf der Befehle; einzeln ausfuehren und Ausgaben pruefen,
# nicht blind als Skript laufen lassen (git log-Ausgabe wird pro Lauf gebraucht).

set -e

git init
dvc init
git add .dvc .dvcignore
git commit -m "chore: dvc initialisiert"

# v1: Ausgangsdatensatz versionieren
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc data/.gitignore
git commit -m "data: people_stats v1 (199 Zeilen)"

# v2: neue Datencharge einspielen
cp data/people_weight_stats_10x.csv data/people_stats.csv
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc
git commit -m "data: people_stats v2 (196 Zeilen, neue Charge)"

# Verlauf ansehen, dann mit dem Commit-Hash von v1 fortfahren:
git log --oneline -- data/people_stats.csv.dvc

# Rollback auf v1 (Platzhalter <commit-von-v1> durch echten Hash ersetzen):
# git checkout <commit-von-v1> -- data/people_stats.csv.dvc
# dvc checkout
