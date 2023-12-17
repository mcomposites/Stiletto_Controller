from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from light_controller import LightController

# Define switch names globally if they are consistent across the application
light_names = ["nav_lights", "anchor_lights", "deck_lights", "spreader_lights", "port_cabin", "starboard_cabin", "switch_7", "switch_8"]
accessory_names = ["bilge_port", "bilge_starboard", "switch_3", "switch_4", "port_cabin", "starboard_cabin", "switch_7", "switch_8"]


# Main Screen with Controls
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # Create a FloatLayout as the base layout
        base_layout = FloatLayout()

        # Add a background image
        bg_image = Image(source='/home/anderson/Documents/Stiletto_Project/Stiletto_Controller/Stiletto_Controller/american3.png', allow_stretch=True, keep_ratio=False)
        base_layout.add_widget(bg_image)

        # Create a BoxLayout for your labels and buttons
        box_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Add 'CONTROL PANEL' label
        label = Label(text='CONTROL PANEL', color=(1,1,1,1), font_size='70sp', bold=True)
        box_layout.add_widget(label)

        # Navigation buttons
        button1 = Button(text='Lights Control', background_color=(1,1,1,0.5), font_size=40, on_press=lambda x: self.manager.change_screen('lights_control'))
        box_layout.add_widget(button1)
        button2 = Button(text='Power to Accessories', background_color=(1,1,1,0.5), font_size=40, on_press=lambda x: self.manager.change_screen('power_to_accessories'))
        box_layout.add_widget(button2)
        button3 = Button(text='Advanced Settings', background_color=(1,1,1,0.5), font_size=40, on_press=lambda x: self.manager.change_screen('advanced_settings'))
        box_layout.add_widget(button3)

        # Add the BoxLayout to the base FloatLayout
        base_layout.add_widget(box_layout)

        # Add the base layout to the screen
        self.add_widget(base_layout)
        
class LightsControlScreen(Screen):
    def __init__(self, light_controller, **kwargs):
        super(LightsControlScreen, self).__init__(**kwargs)
        self.light_controller = light_controller
        main_layout = BoxLayout(orientation='vertical')

        # Grid layout for light controls
        grid_layout = GridLayout(cols=3, spacing=(10, 10))
        for light_id in light_names:
            label = Label(text=light_id)
            switch = Switch(active=False, size_hint_y=None, height=60)
            slider = Slider(min=0, max=100, value=50, size_hint_y=None, height=60)

            # Set light_id as an attribute on the switch
            setattr(switch, 'light_id', light_id)
            setattr(slider, 'light_id', light_id)
            
            # Use a default argument in lambda to capture the current value of light_id
            switch.bind(active=self.toggle_light)
            slider.bind(value=self.set_light_brightness)
            
            # Bind slider event here if necessary
            grid_layout.add_widget(label)
            grid_layout.add_widget(switch)
            grid_layout.add_widget(slider)

        main_layout.add_widget(grid_layout)
        back_button = Button(text='Back to Main', size_hint=(1, 0.1))
        back_button.bind(on_press=lambda x: self.manager.change_screen('main'))
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)
        
    def toggle_light(self, instance, value):
        light_id = instance.light_id
        if value:
            self.light_controller.turn_on_light(light_id)
        else:
            self.light_controller.turn_off_light(light_id)

    def set_light_brightness(self, instance, brightness):
        light_id = instance.light_id
        self.light_controller.set_brightness(light_id, brightness)
        
# Power to Accessories Screen
class PowerToAccessoriesScreen(Screen):
    def __init__(self, light_controller, **kwargs):
        super(PowerToAccessoriesScreen, self).__init__(**kwargs)
        self.light_controller = light_controller
        main_layout = BoxLayout(orientation='vertical')  # Main layout

        # Grid layout for switches
        grid_layout = GridLayout(cols=2, spacing=10)
        for accessory_id in accessory_names:
            label = Label(text=accessory_id)
            switch = Switch(active=False)

            setattr(switch, 'accessory_id', accessory_id)
            
            # Bind events to light controller methods
            switch.bind(active=self.toggle_accessory)

            grid_layout.add_widget(label)
            grid_layout.add_widget(switch)

        main_layout.add_widget(grid_layout)

        # Back button
        back_button = Button(text='Back to Main', size_hint=(1, 0.1))
        back_button.bind(on_press=lambda x: self.manager.change_screen('main'))
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)
        
    def toggle_accessory(self, instance, value):
        accessory_id = instance.accessory_id
        if value:
            self.light_controller.turn_on_accessory(accessory_id)
        else:
            self.light_controller.turn_off_accessory(accessory_id)
# Advanced Settings Screen
class AdvancedSettingsScreen(Screen):
    def __init__(self, signal_k_client, **kwargs):
        super(AdvancedSettingsScreen, self).__init__(**kwargs)
        self.signal_k_client = signal_k_client  # SignalKClient instance

        layout = BoxLayout(orientation='vertical')

        # Log for displaying messages
        self.log = TextInput(text='Log messages here...', readonly=True, multiline=True, size_hint=(1, 0.8))
        layout.add_widget(self.log)

        # Button for requesting Signal K access
        request_access_button = Button(text='Request Signal K Access', size_hint=(1, 0.1))
        request_access_button.bind(on_press=self.request_access)
        layout.add_widget(request_access_button)

        # Back button
        back_button = Button(text='Back to Main Screen', size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'

    def request_access(self, instance):
        # Update the log with the access request status
        self.log.text = 'Requesting Signal K access...'
        
        # Logic to initiate the access request
        description = "Advanced Settings Access Request"
        access_response = self.signal_k_client.request_access(description)

        if access_response:
            # Append response to the log
            self.log.text += f'\nAccess response: {access_response}'
        else:
            self.log.text += '\nError initiating access request.'

# Screen Manager
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
    def change_screen(self, screen_name):
        self.current = screen_name


# Main App
class MyApp(App):
    def build(self):
        self.manager = MyScreenManager()

        return self.manager

    def switch_to_advanced_settings(self):
        self.manager.current = 'advanced_settings'

if __name__ == '__main__':
    MyApp().run()
