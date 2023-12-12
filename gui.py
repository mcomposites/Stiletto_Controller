from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Define switch names globally if they are consistent across the application
switch_names = ["nav_lights", "anchor_lights", "deck_lights", "spreader_lights", "port_cabin", "starboard_cabin", "switch_7", "switch_8"]

# Main Screen with Controls
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=3, spacing=10)
        self.create_controls()
        self.add_widget(self.layout)
        self.add_settings_button()

    def create_controls(self):
        for name in switch_names:
            self.layout.add_widget(Label(text=name))
            self.layout.add_widget(Switch(active=False))
            self.layout.add_widget(Slider(min=0, max=100, value=50))

    #def on_enter(self, *args):
    #    self.ids.controls_grid.clear_widgets()
    #    for name in switch_names:
    #        self.ids.controls_grid.add_widget(Label(text=name))
    #        self.ids.controls_grid.add_widget(Switch(active=False))
    #        self.ids.controls_grid.add_widget(Slider(min=0, max=100, value=50))

    def add_settings_button(self):
        settings_button = Button(text='Advanced Settings', size_hint=(1, 0.1))
        settings_button.bind(on_press=self.switch_to_advanced_settings)
        self.add_widget(settings_button)
        
    def switch_to_advanced_settings(self, instance):
        #logic to switch to the advanced settings screen
        self.manager.current = 'advanced_settings'

# Advanced Settings Screen
class AdvancedSettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(AdvancedSettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.log = TextInput(text='Log messages here...', readonly=True, multiline=True, size_hint=(1, 0.8))
        layout.add_widget(self.log)
        back_button = Button(text='Back to Main Screen', size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_to_main)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'

# Screen Manager
class MyScreenManager(ScreenManager):
    # Example of a custom method to add screens dynamically
    pass


# Main App
class MyApp(App):
    def build(self):
        self.manager = MyScreenManager()
        
        self.manager.add_widget(MainScreen(name='main'))
        self.manager.add_widget(AdvancedSettingsScreen(name='advanced_settings'))
        
        return self.manager
    def switch_to_advanced_settings(self):
        self.manager.current = 'advanced_settings'

if __name__ == '__main__':
    MyApp().run()
