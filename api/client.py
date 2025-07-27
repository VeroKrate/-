import requests
from config.settings import API_CONFIG

class ScooterApiClient:
    def __init__(self):
        self.base_url = API_CONFIG['base_url']
    
    def create_order(self, order_data):
        """Создание заказа"""
        url = f"{self.base_url}/api/v1/orders"
        response = requests.post(url, json=order_data)
        response.raise_for_status()
        return response.json()
    
    def get_order_by_track(self, track):
        """Получение заказа по треку"""
        url = f"{self.base_url}/api/v1/orders/track?t={track}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()