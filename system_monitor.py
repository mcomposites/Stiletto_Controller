
import threading
import time

class SystemMonitor:
    def __init__(self, mqtt_client, wifi_manager, gui):
        self.mqtt_client = mqtt_client
        self.wifi_manager = wifi_manager
        self.gui = gui
        self.monitoring_active = False

    def start(self):
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self.monitor_loop)
        self.monitor_thread.start()

    def monitor_loop(self):
        while self.monitoring_active:
            self.update()
            time.sleep(10)  # Adjust the sleep time as needed

    def update(self):
        if not self.check_connectivity():
            self.display_warning("WiFi connection lost!")

    def check_connectivity(self):
        # Replace with actual connectivity check logic
        return self.wifi_manager.is_connected()

    def display_warning(self, message):
        # Implement how you want to display the warning on the GUI
        self.gui.display_status(message)

    def stop(self):
        self.monitoring_active = False
        self.monitor_thread.join()
