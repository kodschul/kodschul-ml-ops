# ML-Grundlagen-Cheatsheet

Schnellreferenz für die in Modul 1 (lineare Regression, logistische Regression, TensorFlow) verwendeten Befehle.

## Daten laden und aufteilen

| Befehl | Wirkung |
| --- | --- |
| `pd.read_csv("pfad.csv")` | CSV-Datei als DataFrame laden |
| `df[["Spalte1", "Spalte2"]]` | mehrere Spalten als Features auswählen |
| `train_test_split(X, y, test_size=0.2, random_state=60)` | Daten reproduzierbar in Training/Test aufteilen |
| `df[df["Spalte"].notna()]` | Zeilen mit fehlendem Wert in `Spalte` entfernen |

## Lineare Regression (Lab 1.2)

| Befehl | Wirkung |
| --- | --- |
| `LinearRegression()` | Modell für Regression (Zahl als Label) |
| `model.fit(X_train, y_train)` | Modell trainieren |
| `model.predict(X_test)` | Vorhersagen für neue Daten berechnen |
| `mean_absolute_error(y_test, y_pred)` | durchschnittlicher Fehler in Label-Einheit |
| `r2_score(y_test, y_pred)` | Anteil erklärter Varianz (1.0 = perfekt) |

## Logistische Regression (Lab 1.3)

| Befehl | Wirkung |
| --- | --- |
| `LogisticRegression(max_iter=1000)` | Modell für Klassifikation (Kategorie als Label) |
| `[1 if x == "a" else 0 for x in spalte]` | kategoriale Werte in Zahlen umwandeln |
| `accuracy_score(y_test, y_pred)` | Anteil korrekt vorhergesagter Zeilen |
| `confusion_matrix(y_test, y_pred)` | Fehlerarten getrennt nach tatsächlich/vorhergesagt |

## TensorFlow (Lab 1.4)

| Befehl | Wirkung |
| --- | --- |
| `np.load("datei.npz")` | NumPy-Archivdatei laden (z. B. Bilddaten) |
| `X / 255.0` | Pixelwerte (0-255) auf den Bereich 0-1 skalieren |
| `tf.keras.Sequential([...])` | Netzarchitektur aus Schichten definieren |
| `tf.keras.layers.Flatten()` | mehrdimensionale Eingabe (z. B. Bild) in einen Vektor umwandeln |
| `tf.keras.layers.Dense(n, activation=...)` | vollvernetzte Schicht mit `n` Neuronen |
| `model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")` | Optimierer und Fehlerfunktion für Mehrklassen-Klassifikation festlegen |
| `model.fit(X, y, epochs=5)` | Training über mehrere Durchläufe |
| `model.evaluate(X_test, y_test)` | Loss und Metrik auf Testdaten berechnen |
| `tf.keras.utils.set_random_seed(60)` | Training reproduzierbar machen |

## Modell speichern

| Befehl | Wirkung |
| --- | --- |
| `joblib.dump(model, "modell.joblib")` | trainiertes scikit-learn-Modell speichern |
| `joblib.load("modell.joblib")` | gespeichertes Modell wieder laden |
