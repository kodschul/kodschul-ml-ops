import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

import matplotlib.pyplot as plt


df = pd.read_csv("./data/people_stats.csv")

print("Total Dataset: ", len(df))

X = df[["Height"]]
y = df["Weight"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=60)

print("Training Dataset: ", len(X_train))
print("Test Dataset: ", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred), " kg")
print("R^2: ", r2_score(y_test, y_pred))

plt.scatter(X_test, y_test, color="green")
plt.scatter(X_test, y_pred, color="blue")
plt.show()
