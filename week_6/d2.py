import paho.mqtt.client as mqtt
import couchdb
import json

# CouchDB connection
couch = couchdb.Server('http://127.0.0.1:5984/')
db_name = "task5d"

if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# MQTT Settings
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 8883
MQTT_TOPIC = "arduino/gyroscope"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"Received Data: {data}")
        db.save(data)  # Store in CouchDB
    except Exception as e:
        print(f"Error storing data: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Listening for MQTT messages...")
client.loop_forever()
