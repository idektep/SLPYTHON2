import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
TOPIC = "SLPYTHON/....."

def on_connect(client, userdata, flags, rc):
    print("Connected:", rc)
    client.subscribe(TOPIC)
    print("Subscribed to:", TOPIC)

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
