class LightController:
    # Other methods remain the same
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.light_states = {}
        
    def turn_on(self, light_id):
        # Ensure the light state includes both 'state' and 'brightness'
        current_state = self.light_states.get(light_id, {"state": "OFF", "brightness": 100})
        self.mqtt_client.publish(f"{light_id}", str(current_state["brightness"]))
        self.light_states[light_id] = {"state": "ON", "brightness": current_state["brightness"]}

    def turn_off(self, light_id):
        self.mqtt_client.publish(f"{light_id}", "0")
        if light_id in self.light_states:
            self.light_states[light_id]["state"] = "OFF"

    def set_brightness(self, light_id, brightness):
        #Ensure brightness value is within the acceptable range (0-100)
        brightness = max(0, min(100, brightness))
        #Retrieve the current state of the light, defaulting to "OFF" and brightness if not set 
        current_state = self.light_states.get(light_id, {"state": "OFF"})
        #Update the brightness in the current state
        current_state["brightness"] = brightness
        #Save the updated state back to the light_states dictionary
        self.light_states[light_id] = current_state
        
        if current_state["state"] == "ON":
            self.mqtt_client.publish(f"{light_id}", str(brightness))
