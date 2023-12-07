import subprocess

class WiFiManager:
    def start_network(self):
        pass

    def stop_network(self):
        pass

    def check_network_status(self):
        result = subprocess.run(["nmcli", "-t", "-f", "ACTIVE", "connection", "show", "--active"], capture_output=True, text=True)
        return bool(result.stdout.strip())
