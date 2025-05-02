import os
import csv
import time
import sys
import traceback
from arduino_iot_cloud import ArduinoCloudClient

# ——— Configuration ———
DEVICE_ID    = "538f431b-2be4-41e7-ab11-746e78182e57"
SECRET_KEY   = "S3hVkNsx8yx?Rq@2vhS3gYbQR"
CSV_FILENAME = "combined_accelerometer_data.csv"
SAMPLE_RATE  = 1.0  # seconds between writes

# ——— Globals for latest sensor values ———
x = y = z = None

# ——— Callbacks ———
def on_x_changed(client, value):
    global x
    x = value
    print(f"[x] = {x}")

def on_y_changed(client, value):
    global y
    y = value
    print(f"[y] = {y}")

def on_z_changed(client, value):
    global z
    z = value
    print(f"[z] = {z}")

# ——— CSV Setup ———
def init_csv(filename):
    if not os.path.isfile(filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time", "value_x", "value_y", "value_z"])
        print(f"→ Created '{filename}' with header")

# ——— Main ———
def main():
    global x, y, z

    init_csv(CSV_FILENAME)

    client = ArduinoCloudClient(
        device_id=DEVICE_ID,
        username=DEVICE_ID,
        password=SECRET_KEY,
        sync_mode=True
    )

    # Register exactly the variable names from your dashboard:
    client.register("x", value=None, on_write=on_x_changed)
    client.register("y", value=None, on_write=on_y_changed)
    client.register("z", value=None, on_write=on_z_changed)

    try:
        client.start()
        print("✔ Connected to Arduino IoT Cloud")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        sys.exit(1)

    try:
        while True:
            client.update()

            if x is not None and y is not None and z is not None:
                ts = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"→ Writing row: {ts}, {x}, {y}, {z}")
                with open(CSV_FILENAME, "a", newline="") as f:
                    csv.writer(f).writerow([ts, x, y, z])
                x = y = z = None
                time.sleep(SAMPLE_RATE)

    except KeyboardInterrupt:
        print("Interrupted by user")
    except Exception:
        print("Unexpected error:")
        traceback.print_exc()
    finally:
        client.stop()

if __name__ == "__main__":
    main()
