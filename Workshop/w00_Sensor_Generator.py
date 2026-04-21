import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "broker.emqx.io"
PORT = 1883

TOPIC_PREFIX = "idt"

LOCATIONS = {
    "factory": {
        "temp": (28, 40),
        "hum": (40, 70),
        "light": (300, 900),
        "co2": (500, 1500),
        "motion": (0, 1),
    },
    "hospital": {
        "temp": (22, 28),
        "hum": (45, 65),
        "light": (200, 700),
        "co2": (400, 1000),
        "motion": (0, 1),
    },
    "home": {
        "temp": (24, 35),
        "hum": (40, 75),
        "light": (50, 600),
        "co2": (350, 900),
        "motion": (0, 1),
    },
    "warehouse": {
        "temp": (26, 38),
        "hum": (35, 70),
        "light": (100, 500),
        "co2": (450, 1200),
        "motion": (0, 1),
    },
    "farm": {
        "temp": (20, 36),
        "hum": (50, 90),
        "light": (500, 1200),
        "co2": (300, 800),
        "motion": (0, 1),
    },
}


def rand_float(low: float, high: float, digits: int = 2) -> float:
    return round(random.uniform(low, high), digits)


def rand_int(low: int, high: int) -> int:
    return random.randint(low, high)


def generate_sensor_data(location: str) -> dict:
    cfg = LOCATIONS[location]

    data = {
        "location": location,
        "temp": rand_float(*cfg["temp"]),
        "hum": rand_float(*cfg["hum"]),
        "light": rand_int(*cfg["light"]),
        "co2": rand_int(*cfg["co2"]),
        "motion": rand_int(*cfg["motion"]),
        "timestamp": int(time.time()),
    }
    return data


def main():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)

    print("Connected to broker")
    print("Publishing multi-location sensor data...\n")

    while True:
        for location in LOCATIONS:
            topic = f"{TOPIC_PREFIX}/{location}/sensor"
            data = generate_sensor_data(location)
            payload = json.dumps(data)

            client.publish(topic, payload)
            print(f"[SEND] {topic} -> {payload}")

        print("-" * 80)
        time.sleep(2)


if __name__ == "__main__":
    main()