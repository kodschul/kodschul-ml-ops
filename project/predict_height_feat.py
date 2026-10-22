import joblib
import pandas as pd 

import matplotlib.pyplot as plt

df = pd.read_csv("./data/people_dataset.csv")

model = joblib.load("./data/weight_pred_height_feat.model")

X = df[["Height"]][10:30]

y = model.predict(X)

plt.scatter(X["Height"], y, color="blue")
plt.show()
