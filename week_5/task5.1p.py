import serial
import time
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r"test1-a03c3-firebase-adminsdk-fbsvc-18d8a41a6c.json")  
firebase_admin.initialize_app(cred, {"databaseURL": "https://test1-a03c3-default-rtdb.asia-southeast1.firebasedatabase.app/"})  


ref = db.reference("gyroscope_data")

ser = serial.Serial("COM12", 9600, timeout=1)  
time.sleep(2)  

csv_file_path = "C:\\msys64\\home\\ekam1\\python\\gyro_data.csv"
with open(csv_file_path, "w") as file:
    file.write("timestamp,x,y,z\n")  


start_time = time.time()
duration = 1800  

while time.time() - start_time < duration:
    try:
        line = ser.readline().decode("utf-8").strip() 
        if line:
            values = line.split(",") 

            if len(values) == 3: 
                x, y, z = map(float, values)  
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  

                data = {"timestamp": timestamp, "x": x, "y": y, "z": z}

                ref.push(data)

                with open(csv_file_path, "a") as file:
                    file.write(f"{timestamp},{x},{y},{z}\n")

                print(f"{timestamp}, {x}, {y}, {z}")

    except Exception as e:
        print("Error:", e)

ser.close()
print(f" Data collection complete! CSV saved at: {csv_file_path}")