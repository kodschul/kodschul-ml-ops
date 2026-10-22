"""
Checkpoint: Lab 1.2 - Gewicht aus Groesse und Alter vorhersagen.

Finale Version mit beiden Features (Height + Age), wie in Lab 1.2 Aufgabe 6-7
hergeleitet. Speichert das trainierte Modell fuer Lab 4.2.

Ausfuehren aus dem project/-Ordner:
    python checkpoints/m01-ml-grundlagen/train_linreg.py
"""
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/people_stats.csv")

X = df[["Height", "Age"]]
y = df["Weight"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=60
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", round(mean_absolute_error(y_test, y_pred), 2), "kg")
print("R^2:", round(r2_score(y_test, y_pred), 3))

joblib.dump(model, "weight_model.joblib")
print("Modell gespeichert als weight_model.joblib")
