import pandas as pd
import matplotlib.pyplot as plt

# 🟢 Load Data from CSV File
csv_filename = "task.gyroscope data.csv"  # Change if your file has a different name
df = pd.read_csv(csv_filename)

# Ensure timestamp is in datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 🟢 Plot Single Graph with X, Y, Z Data
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["x"], label="X-axis", color="red")
plt.plot(df["timestamp"], df["y"], label="Y-axis", color="green")
plt.plot(df["timestamp"], df["z"], label="Z-axis", color="blue")

# Labels and Title
plt.xlabel("Time")
plt.ylabel("Gyroscope Values")
plt.title("Gyroscope Data Over Time (X, Y, Z)")
plt.legend()  # Show legend for X, Y, Z

# Show the plot
plt.show()
