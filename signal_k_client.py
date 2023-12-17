import requests
import uuid

class SignalKClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client_id = str(uuid.uuid4())
        self.access_token = None  # To store the access token once approved

    def get(self, path):
        headers = self._get_auth_headers()
        return self._make_request(requests.get, path, headers=headers)

    def post(self, path, data):
        headers = self._get_auth_headers()
        return self._make_request(requests.post, path, headers=headers, json=data)

    def request_access(self, description):
        data = {
            "clientId": self.client_id,
            "description": description
        }
        return self.post("/signalk/v1/access/requests", data)

    def poll_access_request(self, href):
        return self._make_request(requests.get, href)

    def _make_request(self, method_func, path, **kwargs):
        try:
            response = method_func(self.base_url + path, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP Error: {e.response.status_code}"}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection Error"}
        except requests.exceptions.Timeout:
            return {"error": "Request Timeout"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error: {e}"}

    def _get_auth_headers(self):
        return {"Authorization": f"Bearer {self.access_token}"} if self.access_token else {}
