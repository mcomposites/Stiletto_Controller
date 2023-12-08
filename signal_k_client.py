import requests

class SignalKClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        try:
            response = requests.get(self.base_url + path)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error in GET request: {e}")
            return None

    def post(self, path, data):
        try:
            response = requests.post(self.base_url + path, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error in POST request: {e}")
            return None
