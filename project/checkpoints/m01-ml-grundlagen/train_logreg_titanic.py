"""
Checkpoint: Lab 1.3 - Ueberleben auf der Titanic mit logistischer Regression.

Eigenstaendiges Klassifikations-Beispiel (nicht Teil der Gewicht-Pipeline),
mit den 3 vereinfachten Features Pclass, Age, Sex.

Ausfuehren aus dem project/-Ordner:
    python checkpoints/m01-ml-grundlagen/train_logreg_titanic.py
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/titanic_train.csv")
df = df[df["Age"].notna()]
df["Sex"] = [1 if s == "male" else 0 for s in df["Sex"]]

X = df[["Pclass", "Age", "Sex"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
