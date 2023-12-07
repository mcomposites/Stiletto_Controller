import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        # Optionally, assign other callbacks here, e.g., on_message, on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe inside on_connect callback to ensure re-subscription on reconnection
        client.subscribe("$SYS/#")

    def connect(self, host, port=1883, keepalive=60):
        try:
            self.client.connect(host, port, keepalive)
            self.client.loop_start()
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def subscribe(self, topic):
        self.client.subscribe(topic)


