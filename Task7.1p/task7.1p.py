import serial
import datetime

def get_timestamp():
    """Returns the current timestamp in YYYY-MM-DD HH:MM:SS format."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


ser = serial.Serial('COM12', 9600, timeout=1)

print("Recording data... Press Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()  
        if line:
            try:
                temp, hum = map(float, line.split(','))  # Convert to float
                timestamp = get_timestamp()  # Get real-time timestamp

               
                print(f"{timestamp},{temp},{hum}")
            except ValueError:
                print("Invalid data received, skipping...")
except KeyboardInterrupt:
    print("Data capture stopped.")
finally:
    ser.close()  
