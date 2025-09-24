# Базовые URL
BASE_URL = "https://ab5b6342-117c-4360-9e44-bafca21672b8.serverhub.praktikum-services.ru"
CREATE_ORDER_URL = f"{BASE_URL}/api/v1/orders"
GET_ORDER_BY_TRACK_URL = f"{BASE_URL}/api/v1/orders/track"

# Настройки базы данных
DB_CONFIG = {
    'dbname': 'scooter_rent',
    'user': 'morty',
    'password': 'smith',
    'host': 'serverhub.praktikum-services.ru',
    'port': '4554'
}