
import time
from kivy.app import App
from signal_k_client import SignalKClient
from light_controller import LightController
from gui import GUI
from system_monitor import SystemMonitor

class MyApp(App):
    def build(self):
        # Initialize the SignalK Client
        mqtt_client = SignalKClient("http://your-signalk-server:port")

        # Initialize the light controller
        light_controller = LightController(mqtt_client)

        # Initialize the GUI
        gui = GUI(light_controller)

        # Initialize the system monitor
        system_monitor = SystemMonitor(mqtt_client, wifi_manager, gui)

        # Start the system monitor
        system_monitor.start()

        return gui

if __name__ == "__main__":
    MyApp().run()
