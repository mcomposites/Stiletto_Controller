
from kivy.app import App
from gui import MainScreen, AdvancedSettingsScreen, LightsControlScreen, PowerToAccessoriesScreen, MyScreenManager
from signal_k_client import SignalKClient
from light_controller import LightController
from system_monitor import SystemMonitor

class StilettoApp(App):
    def build(self):
        # Initialize components
        signal_k_client = SignalKClient("http://your-signalk-server:port")
        light_controller = LightController(signal_k_client)
        screen_manager = MyScreenManager()

        # Create and add screens
        main_screen = MainScreen(name='main')
        advanced_settings_screen = AdvancedSettingsScreen(name='advanced_settings')
        lights_control_screen = LightsControlScreen(light_controller, name='lights_control')
        power_to_accessories_screen = PowerToAccessoriesScreen(light_controller, name='power_to_accessories')

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(advanced_settings_screen)
        screen_manager.add_widget(lights_control_screen)
        screen_manager.add_widget(power_to_accessories_screen)

        # Initialize and start the system monitor
        system_monitor = SystemMonitor(signal_k_client, self)
        system_monitor.start()  # Consider handling threading or async calls

        return screen_manager

if __name__ == '__main__':
    StilettoApp().run()

