import requests
import config  

class HttpClient:
    def __init__(self, server_url, email, password):
        self.server_url = server_url
        self.email = email
        self.password = password
        self.token = None
        self.login()

    def login(self):
        try:
            response = requests.post(f"{self.server_url}/{config.LOGIN_ENDPOINT}", json={"email": self.email, "password": self.password})
            response.raise_for_status()
            data = response.json().get('data')
            if data:
                self.token = data.get('token')
            if not self.token:
                raise ValueError("Token not found in response")
            else:
                print(f"{self.token}")
        except requests.exceptions.RequestException as e:
            print(f"Error logging in: {e}")
        except ValueError as e:
            print(f"Error: {e}")

    def post_data(self, endpoint, data):
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.post(f"{self.server_url}/{endpoint}", json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error posting data: {e}")
            return None

    def get_commands(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.get(f"{self.server_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting commands: {e}")
            return None
