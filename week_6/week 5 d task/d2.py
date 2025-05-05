import paho.mqtt.client as mqtt
import redis
import json
import time  # Import time for generating timestamps if missing

# ✅ Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# ✅ MQTT Configuration
MQTT_BROKER = "5d4aafde18724b279c7d3a17424397ba.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_TOPIC = "arduino/gyroscope"
MQTT_USERNAME = "Ekam_08"
MQTT_PASSWORD = "Ekamgaba@123"

# ✅ Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" Connected to MQTT Broker successfully")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f" Connection failed with error code {rc}")

# ✅ Callback when a message is received
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())  # Convert received JSON data
        print(f" Received Data: {data}")

        # ✅ Check if 'timestamp' exists, else generate one
        if 'timestamp' not in data:
            data['timestamp'] = int(time.time())  # Use current time as timestamp
            print(f": {data['timestamp']}")

        # ✅ Store the data in Redis
        redis_client.set(f"gyro:{data['timestamp']}", json.dumps(data))
        print(f" Data stored in Redis with key: gyro:{data['timestamp']}")

    except Exception as e:
        print(f" Error storing data: {e}")

# ✅ Set up MQTT Client with SSL/TLS
client = mqtt.Client()
client.tls_set()  # Enable SSL/TLS for HiveMQ Cloud

# ✅ Set username and password
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# ✅ Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# ✅ Connect to the MQTT broker
print(f" Connecting to MQTT broker at {MQTT_BROKER}...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)


print(" Listening for MQTT messages...")
client.loop_forever()
