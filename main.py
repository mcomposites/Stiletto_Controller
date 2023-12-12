
import time
from kivy.app import App
from signal_k_client import SignalKClient
f
from kivy.app import App
from gui import MyApp
from gui import MainScreen, AdvancedSettingsScreen, MyScreenManager
from signal_k_client import SignalKClient
from light_controller import LightController
from system_monitor import SystemMonitor

# Define the main application class
class StilettoApp(App):
    def build(self):
        # Initialize the SignalK Client
        signal_k_client = SignalKClient("http://your-signalk-server:port")

        # Initialize the light controller with the SignalK client
        light_controller = LightController(signal_k_client)
        
        # Initialize the ScreenManager
        screen_manager = MyScreenManager()

        # Create instances of your screens
        main_screen = MainScreen(name='main')
        advanced_settings_screen = AdvancedSettingsScreen(name='advanced_settings')

        # Add screens to the ScreenManager
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(advanced_settings_screen)

        # Initialize the system monitor with the SignalK client and the app interface
        system_monitor = SystemMonitor(signal_k_client, self)

        # Start the system monitor (you might need to handle threading or async calls)
        system_monitor.start()

        # Return the main application interface

        return screen_manager

# Run the application
if __name__ == '__main__':
    StilettoApp().run()

