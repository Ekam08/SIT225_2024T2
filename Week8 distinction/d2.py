import os
import csv
import cv2

# Folder containing your CSV and image files
data_folder = r'C:\msys64\home\ekam1\python\8.1p\data'  # Use raw string for file path

# CSV to store annotations
annotation_file = 'annotation_file.csv'

# Open the CSV file to write annotations
with open(annotation_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["filename", "activity"])

    # Iterate through your data folder to create annotations
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            # Get the corresponding image file (same name as the CSV, with .jpg extension)
            image_filename = filename.replace(".csv", ".jpg")
            image_path = os.path.join(data_folder, image_filename)

            print(f"Checking image file: {image_filename} at path: {image_path}")

            # Initialize activity_label with a default value
            activity_label = 0  # Default to no activity

            # Check if the image exists before attempting to load it
            if os.path.exists(image_path):
                # Read and display the image
                img = cv2.imread(image_path)
                cv2.imshow('Activity Image', img)
                key = cv2.waitKey(0) & 0xFF

                # Assign activity label based on user input
                if key == ord('1'):
                    activity_label = 1  # Activity 1 (e.g., waving)
                elif key == ord('2'):
                    activity_label = 2  # Activity 2 (e.g., shaking)
                elif key == ord('0'):
                    activity_label = 0  # No activity
            else:
                print(f"Warning: The image '{image_filename}' does not exist at {image_path}. Skipping...")

            # Write the filename and activity label to the annotation file
            writer.writerow([filename, activity_label])

cv2.destroyAllWindows()
