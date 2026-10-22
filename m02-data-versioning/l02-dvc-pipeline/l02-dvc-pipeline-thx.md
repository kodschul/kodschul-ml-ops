# Lab 2.2: Datenpipeline mit DVC versionieren

**Leitfragen:**

<details>
<summary>Wie macht DVC eine Datenänderung rückgängig machbar?</summary>

Jeder `dvc add`-Aufruf erzeugt eine neue `.dvc`-Verweisdatei, die zusammen mit dem Code in Git committet wird. Ein `git checkout` auf einen früheren Commit plus `dvc checkout` stellt den dazu passenden Datenstand wieder her.

</details>

<details>
<summary>Was gehört ins Git-Repo, was in den DVC-Remote?</summary>

Ins Git-Repo gehören Code und die kleinen `.dvc`-Verweisdateien. Die eigentlichen Datendateien liegen im DVC-Cache (lokal) bzw. in einem DVC-Remote (z. B. Cloud-Storage), wenn mit anderen geteilt wird.

</details>

- `dvc init` richtet DVC in einem bestehenden Git-Repository ein.
- `dvc add <datei>` erzeugt eine `.dvc`-Verweisdatei und verschiebt die echte Datei in den DVC-Cache.

**Hinweis:** Dieses Lab arbeitet rein lokal, ohne DVC-Remote (Cloud-Storage) – für den Kurstag reicht das, um Versionierung und Rollback zu zeigen.

## Voraussetzung

Ein Git-Repository existiert bereits im Projektordner:

```bash
cd project
git init
```

## DVC einrichten

```bash
dvc init
git add .dvc .dvcignore
git commit -m "chore: dvc initialisiert"
```

## Ersten Datenstand versionieren

```bash
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc data/.gitignore
git commit -m "data: people_stats v1 (199 Zeilen)"
```

`dvc add` verschiebt `people_stats.csv` in den DVC-Cache und legt an seiner Stelle `data/people_stats.csv.dvc` ab – eine kleine Textdatei mit einem Hash-Verweis auf den Dateiinhalt. DVC trägt die echte Datei zusätzlich automatisch in `data/.gitignore` ein, damit Git sie nicht doppelt verfolgt.

## Neue Datencharge einspielen

```bash
cp data/people_weight_stats_10x.csv data/people_stats.csv
dvc add data/people_stats.csv
git add data/people_stats.csv.dvc
git commit -m "data: people_stats v2 (196 Zeilen, neue Charge)"
```

Derselbe Dateiname (`people_stats.csv`) enthält jetzt neuen Inhalt; DVC erkennt die Änderung über den Hash und erzeugt eine neue Verweisversion.

## Zur vorherigen Version zurückkehren

```bash
git log --oneline -- data/people_stats.csv.dvc
git checkout <commit-von-v1> -- data/people_stats.csv.dvc
dvc checkout
```

`git checkout <commit> -- <datei>` stellt nur die `.dvc`-Verweisdatei auf den alten Stand zurück; `dvc checkout` liest daraufhin die passende Datenversion aus dem Cache und ersetzt `people_stats.csv` damit.

## Fazit

- `dvc add` + `git commit` erzeugt einen versionierten Datenstand, gekoppelt an einen Code-Stand.
- Ein Rollback kombiniert `git checkout` (für die `.dvc`-Datei) mit `dvc checkout` (für die echten Daten).
- Ohne DVC-Remote bleibt der Cache lokal – für Teamarbeit würde ein Remote (z. B. S3, Google Cloud Storage) ergänzt.

Modul 3 zeigt, wie Features statt ganzer Dateien konsistent zwischen Training und Produktivbetrieb bereitgestellt werden.
