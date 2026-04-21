import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "broker.emqx.io"
TOPIC = "SLPYTHON/........"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("Publisher started...")
print("Sending data to topic:", TOPIC)

while True:
    data = {
        "temp": round(random.uniform(25, 35), 2),
        "hum": random.randint(40, 80)
    }

    payload = json.dumps(data)
    client.publish(TOPIC, payload)

    print("Send:", payload)
    time.sleep(2)
