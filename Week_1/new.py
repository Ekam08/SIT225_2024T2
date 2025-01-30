import serial
import random
import time
boud_rate =9600

task= serial.Serial('COM11',boud_rate , timeout=5)
while True:
    random_blink=random.randint(2,3)
    task.write(bytes(str(random_blink),'utf-8'))
    print(f"sent >>> {random_blink} blinks")
    time.sleep(1)

    reply = task.readline().decode('utf-8').strip()
    if reply.isdigit():
        delay=int(reply)
        print(f"received <<< {delay} seconds")
        print(f"sleep for {delay} seconds")
        time.sleep(delay)
        print("*****End*******")