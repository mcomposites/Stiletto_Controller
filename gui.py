from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput

switch_names = ["nav_lights", "anchor_lights", "deck_lights", "spreader_lights", "port_cabin", "starboard_cabin", "switch_7", "switch_8"]

class GUI(BoxLayout):
    def __init__(self, light_controller, **kwargs):
        super(GUI, self).__init__(**kwargs)
        self.light_controller = light_controller
        self.orientation = 'vertical'

        self.light_switches = {}
        self.light_sliders = {}
        
        # Sliders and Switches
        for name in switch_names:
            hbox = BoxLayout(orientation='horizontal')
            
            switch = Switch(active=False)
            light_id = name.lower().replace(" ", "_")
            setattr(switch, 'light_id', light_id)
            switch.bind(active=self.on_switch_toggle)
            
            slider = Slider(min=0, max=100, value=50)
            slider_id = name.lower().replace(" ", "-") # Custom attribute for identification
            setattr(slider, 'light_id', slider_id)
            slider.bind(value=self.on_slider_change)
            
            self.light_switches[switch.light_id] = switch
            self.light_sliders[slider.light_id] = slider
            
            hbox.add_widget(Label(text=name))
            hbox.add_widget(switch)
            hbox.add_widget(slider)
            self.add_widget(hbox)

        # Logging Area
        self.log = TextInput(text='Log messages here...', readonly=True, multiline=True)
        self.add_widget(self.log)
        
    def on_switch_toggle(self, instance, value):
        light_id = instance.light_id
        if value: # Switch turned on
            self.light_controller.turn_on(light_id)
        else: #Switch turned off
            self.light_controller.turn_off(light_id)
            
    def on_slider_change(self, instance, value):
        light_id = instance.light_id
        try:
            self.light_controller.set_brightness(light_id, value)
            self.log_message(f"Set brightness of {light_id} to {value}")
        except Exception as e:
            self.log_message(f"Error setting brightness for {light_id}: {e}")

    def toggle_light(self, instance):
        self.light_controller.toggle_light()
        self.log_message("Light toggled")

    def log_message(self, message):
        self.log.text += message + "\n"

class YourLightControllerClass:
    def toggle_light(self):
        print("Light toggled")

class MyApp(App):
    def build(self):
        light_controller = YourLightControllerClass()
        return GUI(light_controller)

if __name__ == '__main__':
    MyApp().run()
