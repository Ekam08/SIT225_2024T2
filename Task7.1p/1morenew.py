from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv("task7.csv")



df["timestamp_num"] = np.arange(len(df))

# Create and train the model
model = LinearRegression()
X = df["timestamp_num"].values.reshape(-1, 1)  
y = df["humidity"].values  # Dependent variable
model.fit(X, y)

# Predict values
df["humidity_pred"] = model.predict(X)


plt.figure(figsize=(10, 5))
plt.scatter(df["timestamp"], df["humidity"], label="Actual Humidity", marker="d")
plt.plot(df["timestamp"], df["humidity_pred"], label="Predicted Humidity (Regression)", color="red")
plt.xlabel("Timestamp")
plt.ylabel("Humidity (%)")
plt.legend()
plt.title("Humidity Over Time with Linear Regression")
plt.grid(True)
plt.show()