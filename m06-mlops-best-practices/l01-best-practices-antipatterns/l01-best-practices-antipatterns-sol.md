# Lab 6.1 – Lösung: MLOps Best Practices & Anti-Patterns

1. **Nicht tun.** Ohne Metrikvergleich kann ein schlechteres Modell unbemerkt die `production`-Version ersetzen (siehe Leitfrage 1 im Handout). Richtig: erst MAE/R² beider Versionen in der MLflow-UI vergleichen, dann den Alias umsetzen.

2. **Tun.** Das koppelt Code-Stand und Datenstand (`.dvc`-Verweisdatei) in einem Commit – genau das Prinzip aus Modul 2, das spätere Reproduzierbarkeit ermöglicht.

3. **Nicht tun.** Ohne Versionsangabe kann sich die API einer Bibliothek ändern, ohne dass es auffällt (genau das ist mit Evidently in Modul 5 passiert: ältere Tutorials nutzen eine andere Import-Syntax als die aktuell installierte Version). Richtig: Version in `requirements.txt` festhalten.

4. **Tun.** Ein kurzer Test vor der Freigabe deckt offensichtliche Fehler auf, bevor andere Personen oder Systeme sich auf den Endpunkt verlassen (Modul 4).

5. **Nicht tun.** Ohne vorheriges `dvc add` geht der alte Stand verloren, sobald die Datei überschrieben wird – ein Rollback ist dann nicht mehr möglich (Modul 2).

6. **Tun, aber zu selten.** Drift kann sich auch innerhalb weniger Tage zeigen; ein fester, aber kurzer Prüfrhythmus (z. B. wöchentlich oder bei jeder neuen Datencharge) ist in der Praxis üblicher als ein monatlicher Check. Die Grundhaltung „regelmäßig statt nie" ist aber bereits richtig.

## Erweiterung: `compare_before_promote.py`

```bash
python checkpoints/m06-mlops-best-practices/compare_before_promote.py
```

Getestet: Das Skript liest beide Runs aus `mlflow.db`, vergleicht `mae_kg` (`height_only`: 7.36, `height_age`: 6.66) und setzt den Alias `production` nur, wenn die aktuell markierte Version nicht bereits die beste ist. In einem zusätzlichen Test wurde absichtlich die schlechtere Version (`height_only`) als `production` markiert (Simulation von Aussage 1) – das Skript erkannte die Abweichung und setzte den Alias korrekt auf die bessere Version zurück.

## Grenzen

Diese Übung ist bewusst reflexionsorientiert, kein Coding-Lab – sie fasst zusammen und führt keine neue Technik ein. Die Erweiterung ist optional und zeigt nur Aussage 1 praktisch, nicht alle sechs Aussagen.
