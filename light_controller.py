class LightController:
    def __init__(self, signal_k_client):
        self.signal_k_client = signal_k_client
        self.light_states = {}
        self.accessory_states = {}

    def turn_on_light(self, light_id):
        # Ensure the light state includes both 'state' and 'brightness'
        current_state = self.light_states.get(light_id, {"state": "OFF", "brightness": 100})
        # Update the light state on SignalK server
        # This is an example and might need to be adjusted based on your SignalK setup
        self.signal_k_client.post(f"/lights/{light_id}", {"state": "ON", "brightness": current_state["brightness"]})
        self.light_states[light_id] = {"state": "ON", "brightness": current_state["brightness"]}

    def turn_off_light(self, light_id):
        # Update the light state on SignalK server
        self.signal_k_client.post(f"/lights/{light_id}", {"state": "OFF"})
        if light_id in self.light_states:
            self.light_states[light_id]["state"] = "OFF"

    def set_brightness(self, light_id, brightness):
        # Ensure brightness value is within the acceptable range (0-100)
        brightness = max(0, min(100, brightness))
        # Update the light state on SignalK server
        self.signal_k_client.post(f"/lights/{light_id}", {"brightness": brightness})
        self.light_states[light_id] = {"state": "ON", "brightness": brightness}
    
    def turn_on_accessory(self, accessory_id):
        # Update the accessory state on SignalK server
        # Example implementation, adjust based on your SignalK setup
        self.signal_k_client.post(f"/accessories/{accessory_id}", {"state": "ON"})
        self.accessory_states[accessory_id] = "ON"

    def turn_off_accessory(self, accessory_id):
        # Update the accessory state on SignalK server
        self.signal_k_client.post(f"/accessories/{accessory_id}", {"state": "OFF"})
        self.accessory_states[accessory_id] = "OFF"

    # Optionally, a method to get the current state of a light or accessory
    def get_state(self, item_id):
        return self.light_states.get(item_id) or self.accessory_states.get(item_id, "OFF")