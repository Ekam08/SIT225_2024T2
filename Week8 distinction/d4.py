import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Folder containing the accelerometer data CSV files
data_folder = r'C:\msys64\home\ekam1\python\8.1p\data'

# Function to extract statistical features
def extract_features(data):
    features = {
        'mean_x': np.mean(data['x']),
        'mean_y': np.mean(data['y']),
        'mean_z': np.mean(data['z']),
        'std_x': np.std(data['x']),
        'std_y': np.std(data['y']),
        'std_z': np.std(data['z']),
        'max_x': np.max(data['x']),
        'max_y': np.max(data['y']),
        'max_z': np.max(data['z']),
        'min_x': np.min(data['x']),
        'min_y': np.min(data['y']),
        'min_z': np.min(data['z'])
    }
    return features

# Create a DataFrame to store the extracted features
feature_data = []

# Iterate through the data folder and process each CSV file
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        # Load the accelerometer data
        data_path = os.path.join(data_folder, filename)
        data = pd.read_csv(data_path)

        # Extract statistical features
        features = extract_features(data)
        features['filename'] = filename
        feature_data.append(features)

# Convert feature data into a DataFrame
feature_df = pd.DataFrame(feature_data)

# Show the extracted features for each file
print(feature_df)

# You can also visualize the features to see if there's a pattern
feature_df.plot(kind='bar', x='filename', figsize=(12, 6))
plt.title('Extracted Features for Each Activity')
plt.xlabel('Filename')
plt.ylabel('Feature Value')
plt.show()
