import pytest
import sender_stand_request
import data
from configuration import CREATE_ORDER_URL, GET_ORDER_BY_TRACK_URL

class TestCreateOrder:
    def test_create_order_success(self):
        """Тест успешного создания заказа"""
        # Создаем заказ
        response = sender_stand_request.create_order(data.ORDER_BODY)
        
        # Проверяем статус код
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        # Проверяем наличие трек-номера
        track_number = response.json().get("track")
        assert track_number is not None, "Трек-номер не получен в ответе"
        
        return track_number

    def test_get_order_by_track_success(self):
        """Тест получения заказа по трек-номеру"""
        # Сначала создаем заказ
        create_response = sender_stand_request.create_order(data.ORDER_BODY)
        track_number = create_response.json().get("track")
        
        # Получаем заказ по трек-номеру
        get_response = sender_stand_request.get_order_by_track(track_number)
        
        # Проверяем статус код
        assert get_response.status_code == 200, f"Ожидался статус 200, получен {get_response.status_code}"
        
        # Проверяем данные заказа
        order_data = get_response.json()
        assert "order" in order_data, "Ключ 'order' отсутствует в ответе"
        assert order_data["order"]["firstName"] == data.ORDER_BODY["firstName"]
        assert order_data["order"]["lastName"] == data.ORDER_BODY["lastName"]

    def test_create_and_get_order_integration(self):
        """Интеграционный тест: создание + получение заказа"""
        # Шаг 1: Создание заказа
        create_response = sender_stand_request.create_order(data.ORDER_BODY)
        assert create_response.status_code == 201
        
        track_number = create_response.json().get("track")
        assert track_number is not None
        
        # Шаг 2: Получение заказа по треку
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200
        
        order_info = get_response.json()
        assert order_info.get("order") is not None