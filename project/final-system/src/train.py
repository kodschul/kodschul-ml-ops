"""
Produktionssystem: Training.

Trainiert das Gewicht-Vorhersage-Modell (Height + Age -> Weight) auf dem
aktuellen Datenstand und speichert es nach models/weight_model.joblib.

Ausfuehren aus final-system/:
    python src/train.py
"""
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = "../data/people_stats.csv"
MODEL_PATH = "models/weight_model.joblib"

df = pd.read_csv(DATA_PATH)

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

joblib.dump(model, MODEL_PATH)
print("Modell gespeichert:", MODEL_PATH)
