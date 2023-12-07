
import time
from kivy.app import App
from mqtt_client import MQTTClient
from wifi_manager import WiFiManager
from light_controller import LightController
from gui import GUI
from system_monitor import SystemMonitor

class MyApp(App):
    def build(self):
        # Initialize the MQTT client
        mqtt_client = MQTTClient()

        # Initialize the WiFi manager
        wifi_manager = WiFiManager()

        # Initialize the light controller
        light_controller = LightController(mqtt_client)

        # Initialize the GUI
        gui = GUI(light_controller)

        # Initialize the system monitor
        system_monitor = SystemMonitor(mqtt_client, wifi_manager, gui)

        # Start the WiFi network
        wifi_manager.start_network()

        # Connect the MQTT client to the broker
        mqtt_client.connect("127.0.0.1", port=1883, keepalive=60)  # Replace with your MQTT broker's address

        # Start the system monitor
        system_monitor.start()

        return gui

if __name__ == "__main__":
    MyApp().run()
