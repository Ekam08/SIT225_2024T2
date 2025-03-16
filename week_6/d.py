import paho.mqtt.client as mqtt
import pymongo
import ssl
import json
import time

# 🟢 MQTT Broker Configuration (HiveMQ Cloud)
MQTT_BROKER = "5d4aafde18724b279c7d3a17424397ba.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  # SSL Port
MQTT_USER = "Ekam_08"  # Same as in Arduino
MQTT_PASSWORD = "Ekamgaba@123"  # Same as in Arduino
MQTT_TOPIC = "arduino/gyroscope"  # Must match Arduino topic

# 🟢 MongoDB Configuration (Alternative NoSQL Database)
MONGO_URI = "mongodb://localhost:27017/"  # Change if using a cloud MongoDB
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["task"]
collection = db["gyroscope data"]

# 🟢 Callback function: When message is received
def on_message(client, userdata, message):
    try:
        # Decode MQTT message (JSON format)
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)  # Convert JSON to Python dictionary

        # Extract x, y, z values
        x, y, z = data["x"], data["y"], data["z"]
        record = {
            "x": x,
            "y": y,
            "z": z,
            "timestamp": time.time()
        }

        # Insert into MongoDB
        collection.insert_one(record)
        print("✅ Data Stored:", record)

    except Exception as e:
        print("❌ Error:", e)

# 🟢 MQTT Setup
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)  # Set username & password
mqtt_client.tls_set(cert_reqs=ssl.CERT_NONE)  # Disable SSL verification
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.on_message = on_message

print("🔄 Listening for MQTT messages from Arduino...")
mqtt_client.loop_forever()  # Keep running to receive data
