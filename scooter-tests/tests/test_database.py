import psycopg2
import pytest

class TestScooterDatabase:
    DB_CONFIG = {
        'dbname': 'scooter_rent',
        'user': 'morty',
        'password': 'smith',
        'host': 'serverhub.praktikum-services.ru',
        'port': '4554'
    }
    
    def test_database_connection(self):
        """Тест подключения к базе данных"""
        try:
            connection = psycopg2.connect(**self.DB_CONFIG)
            assert connection is not None
            connection.close()
        except Exception as e:
            pytest.fail(f"Ошибка подключения к БД: {e}")
    
    def test_couriers_query(self):
        """Тест запроса курьеров с заказами в доставке"""
        connection = psycopg2.connect(**self.DB_CONFIG)
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.login, COUNT(o.id) AS delivery_orders_count
                FROM "Couriers" c
                LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true
                GROUP BY c.login;
            """)
            result = cursor.fetchall()
            assert len(result) > 0, "Нет данных о курьерах"
        connection.close()
    
    def test_orders_statuses(self):
        """Тест статусов заказов"""
        connection = psycopg2.connect(**self.DB_CONFIG)
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT track, 
                       CASE 
                           WHEN finished = true THEN 2
                           WHEN cancelled = true THEN -1
                           WHEN "inDelivery" = true THEN 1
                           ELSE 0
                       END AS status
                FROM "Orders";
            """)
            result = cursor.fetchall()
            assert len(result) > 0, "Нет данных о заказах"
        connection.close()