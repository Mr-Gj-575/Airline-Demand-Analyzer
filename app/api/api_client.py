from flask import current_app
import requests

class APIClient:
    def __init__(self):
        self.base_url = current_app.config['API_BASE_URL']

    def fetch_data(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def get_airline_data(self, airline_code):
        endpoint = f"airlines/{airline_code}/data"
        return self.fetch_data(endpoint)

    def get_route_data(self, origin, destination):
        endpoint = "routes"
        params = {'origin': origin, 'destination': destination}
        return self.fetch_data(endpoint, params)