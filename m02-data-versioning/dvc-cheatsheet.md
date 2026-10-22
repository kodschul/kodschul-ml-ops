# DVC-Cheatsheet

Schnellreferenz für die in Modul 2 verwendeten Befehle.

| Befehl | Wirkung |
| --- | --- |
| `dvc init` | DVC in einem bestehenden Git-Repository einrichten |
| `dvc add <datei>` | Datei in den DVC-Cache verschieben, `.dvc`-Verweisdatei erzeugen |
| `git add <datei>.dvc` | Verweisdatei in Git aufnehmen (nicht die echten Daten) |
| `git log --oneline -- <datei>.dvc` | Versionsverlauf einer Datendatei anzeigen |
| `git checkout <commit> -- <datei>.dvc` | Verweisdatei auf einen früheren Stand zurücksetzen |
| `dvc checkout` | echte Daten passend zur aktuellen `.dvc`-Datei wiederherstellen |
| `dvc remote add <name> <url>` | Remote-Storage für Teamarbeit einrichten (in diesem Kurs nicht verwendet) |
| `dvc push` / `dvc pull` | Daten zu/von einem Remote synchronisieren (in diesem Kurs nicht verwendet) |

## Ablaufmuster für einen Rollback

1. `git log --oneline -- <datei>.dvc` → gewünschten Commit-Hash finden.
2. `git checkout <commit> -- <datei>.dvc` → Verweisdatei zurücksetzen.
3. `dvc checkout` → echte Datei passend dazu wiederherstellen.
