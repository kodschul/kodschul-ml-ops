#!/bin/bash
# Produktionssystem: Daten-Versionierung mit DVC.
# Versioniert ../data/people_stats.csv direkt im project/-Wurzelordner,
# damit alle Teile des Systems (Training, Serving) denselben Datenstand sehen.
#
# Ausfuehren aus final-system/:
#   bash scripts/version_data.sh

set -e
cd ..

if [ ! -d .git ]; then
  git init
fi
if [ ! -d .dvc ]; then
  dvc init
  git add .dvc .dvcignore
  git commit -m "chore: dvc initialisiert"
fi

dvc add data/people_stats.csv
git add data/people_stats.csv.dvc data/.gitignore
git commit -m "data: people_stats $(date +%Y-%m-%d)"

echo "Aktueller Datenstand versioniert. Verlauf:"
git log --oneline -- data/people_stats.csv.dvc
