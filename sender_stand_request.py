import requests
from configuration import CREATE_ORDER_URL, GET_ORDER_BY_TRACK_URL

def create_order(order_body):
    """Функция для создания заказа"""
    response = requests.post(CREATE_ORDER_URL, json=order_body)
    response.raise_for_status()
    return response

def get_order_by_track(track_number):
    """Функция для получения заказа по трек-номеру"""
    params = {'t': track_number}
    response = requests.get(GET_ORDER_BY_TRACK_URL, params=params)
    response.raise_for_status()
    return response