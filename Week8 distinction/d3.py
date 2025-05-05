import pandas as pd
import matplotlib.pyplot as plt
import os

# Folder containing the accelerometer data CSV files
data_folder = r'C:\msys64\home\ekam1\python\8.1p\data'

# Iterate through the data folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        # Load the accelerometer data
        data_path = os.path.join(data_folder, filename)
        data = pd.read_csv(data_path)

        # Check if the CSV contains accelerometer data (x, y, z)
        if 'x' in data.columns and 'y' in data.columns and 'z' in data.columns:
            # Plot accelerometer data
            plt.figure(figsize=(10, 6))
            plt.plot(data['x'], label='X-axis')
            plt.plot(data['y'], label='Y-axis')
            plt.plot(data['z'], label='Z-axis')

            # Title and labels
            plt.title(f'Accelerometer Data for {filename}')
            plt.xlabel('Time (samples)')
            plt.ylabel('Acceleration')
            plt.legend()

            # Show the plot
            plt.show()
