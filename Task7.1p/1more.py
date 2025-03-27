import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime

df = pd.read_csv("task7.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["timestamp_num"] = (df["timestamp"] - df["timestamp"].min()).dt.total_seconds()

# Create and train the linear regression model
model = LinearRegression()
X = df["timestamp_num"].values.reshape(-1, 1)  # Independent variable (timestamps in seconds)
y = df["temperature"].values  # Dependent variable (temperature)

model.fit(X, y)  # Train the model

# Predict temperatures
df["temperature_pred"] = model.predict(X)

# Plot actual vs predicted temperature
plt.figure(figsize=(10, 5))
plt.scatter(df["timestamp"], df["temperature"], label="Actual Temperature")
plt.plot(df["timestamp"], df["temperature_pred"], label="Predicted Temperature (Regression)", color="red")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.title("Temperature Over Time with Linear Regression")
plt.grid(True)
plt.show()