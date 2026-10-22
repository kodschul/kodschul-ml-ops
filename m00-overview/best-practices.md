# Best Practices

- **Immer mit Train/Test-Split arbeiten.** Eine Metrik auf Trainingsdaten allein zeigt nur, wie gut ein Modell sich die Daten gemerkt hat, nicht ob es verallgemeinert.
- **Kategoriale Werte vor dem Training kodieren.** scikit-learn-Modelle rechnen nur mit Zahlen; Texte wie `"male"`/`"female"` müssen vorher umgewandelt werden (Lab 1.3).
- **Modellkomplexität zur Aufgabe passen.** Ein neuronales Netz ist nicht automatisch besser – bei einfachen, tabellarischen Zusammenhängen (Lab 1.2) reicht `LinearRegression`; bei Bilddaten (Lab 1.4) zeigt sich der Vorteil neuronaler Netze deutlich (97.6 % vs. 92.6 % Genauigkeit).
- **Features vor dem Training in einen vergleichbaren Wertebereich bringen.** `LinearRegression`/`LogisticRegression` sind unempfindlich gegenüber der Größenordnung der Eingaben, neuronale Netze (TensorFlow) nicht – Pixelwerte (0-255) werden deshalb vor dem Training auf 0-1 skaliert (Lab 1.4).
- **Datenstand und Code-Stand gemeinsam versionieren.** Ein Modell ist nur reproduzierbar, wenn sowohl der Code als auch die exakte Trainingsdatenversion bekannt sind (Modul 2).
- **Eingabe- und Ausgabeformat einer API explizit definieren.** Ein `BaseModel` macht sichtbar, welche Felder erwartet werden, statt es implizit im Code zu verstecken (Lab 4.2).
- **Typ-Validierung ersetzt keine fachliche Prüfung.** Eine API kann einen negativen Wert als gültige Zahl akzeptieren, obwohl er fachlich unsinnig ist – zusätzliche Prüfungen bleiben nötig (Lab 4.2).
- **Mittelwertverschiebung als erstes Drift-Signal beobachten.** Schon eine Verschiebung im Mittelwert eines Features kann auf eine veränderte Datenrealität hindeuten, auch wenn Minimum/Maximum kaum abweichen (Lab 5.1).
- **Features einmal zentral definieren, nicht mehrfach im Code.** Ein Feature Store verhindert, dass Training und Serving dieselbe Berechnung unterschiedlich implementieren (Lab 3.1).
