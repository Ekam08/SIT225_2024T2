import csv
import cv2
import os
import time
import logging
from datetime import datetime
from arduino_iot_cloud import ArduinoCloudClient

# Configuration
DEVICE_ID = "728421bd-9235-42ce-8c77-6a3829d836c8"
SECRET_KEY = "6##LaaQuWykb2KuNcfECUy#d!"
DATA_FOLDER = "data"
SAMPLE_DURATION = 10  # seconds

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variables for accelerometer data
x = y = z = None

# Callbacks for cloud updates
def on_x_changed(client, value):
    global x
    x = value
    logging.info(f"X updated: {x}")

def on_y_changed(client, value):
    global y
    y = value
    logging.info(f"Y updated: {y}")

def on_z_changed(client, value):
    global z
    z = value
    logging.info(f"Z updated: {z}")

# Initialize IoT client
client = ArduinoCloudClient(
    device_id=DEVICE_ID,
    username=DEVICE_ID,
    password=SECRET_KEY,
    sync_mode=True
)

# Register cloud variables
client.register("x", value=None, on_write=on_x_changed)
client.register("y", value=None, on_write=on_y_changed)
client.register("z", value=None, on_write=on_z_changed)

# Ensure data directory exists
os.makedirs(DATA_FOLDER, exist_ok=True)

def capture_image(filename):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        logging.info(f"Image saved: {filename}")
    else:
        logging.error("Failed to capture image")
    cap.release()

def save_to_csv(filename, data):
    with open(os.path.join(DATA_FOLDER, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "x", "y", "z"])
        writer.writerows(data)
    logging.info(f"CSV saved: {filename}")

def main():
    logging.info("Starting data capture...")
    client.start()
    sequence = 1

    try:
        while True:
            start_time = time.time()
            data = []
            logging.info(f"Starting capture cycle {sequence}")

            # Data collection loop
            while (time.time() - start_time) < SAMPLE_DURATION:
                client.update()  # Process incoming messages

                if None not in (x, y, z):
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    data.append([timestamp, x, y, z])
                    logging.debug(f"Recorded: {x}, {y}, {z}")
                else:
                    logging.warning("Missing data - check device connection")
                
                time.sleep(0.1)  # Shorter sleep for better responsiveness

            if data:
                timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
                csv_filename = f"{sequence}_{timestamp_str}.csv"
                img_filename = f"{sequence}_{timestamp_str}.jpg"
                save_to_csv(csv_filename, data)
                capture_image(os.path.join(DATA_FOLDER, img_filename))
            else:
                logging.warning("No data collected this cycle")

            sequence += 1

    except KeyboardInterrupt:
        logging.info("Stopped by user")
    except Exception as e:
        logging.error(f"Error: {str(e)}", exc_info=True)
    finally:
        client.stop()
        logging.info("Disconnected from cloud")

if __name__ == "__main__":
    main()