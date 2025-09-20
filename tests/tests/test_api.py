import pytest
from api.client import ScooterApiClient

@pytest.fixture
def api_client():
    return ScooterApiClient()

@pytest.fixture
def sample_order_data():
    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+79991234567",
        "rentTime": 5,
        "deliveryDate": "2023-06-06",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }

def test_create_and_get_order(api_client, sample_order_data):
    # Шаг 1: Создание заказа
    create_response = api_client.create_order(sample_order_data)
    track = create_response.get("track")
    assert track is not None, "Трек номер не получен"
    
    # Шаг 2: Получение заказа по треку
    get_response = api_client.get_order_by_track(track)
    assert get_response.get("order") is not None, "Данные заказа не получены"
    assert get_response["order"]["firstName"] == sample_order_data["firstName"]