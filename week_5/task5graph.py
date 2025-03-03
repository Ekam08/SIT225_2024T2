import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = "C:\msys64\home\ekam1\python\gyro_data.csv"

df = pd.read_csv(csv_file_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["x"], label="X-Axis", color="blue")
plt.plot(df["timestamp"], df["y"], label="Y-Axis", color="orange")
plt.plot(df["timestamp"], df["z"], label="Z-Axis", color="green")

# Formatting the plot
plt.xlabel("Time")
plt.ylabel("Gyroscope Readings")
plt.title("Gyroscope Sensor Data Over 30 Minutes")
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Show the plot
plt.show()