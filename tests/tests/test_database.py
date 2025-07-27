import pytest
from database.connector import DatabaseConnector
from database.queries import DatabaseQueries

def test_couriers_with_delivery_orders():
    """Тест для задания 1: Курьеры с заказами в доставке"""
    with DatabaseConnector() as conn:
        with conn.cursor() as cursor:
            cursor.execute(DatabaseQueries.get_couriers_with_delivery_orders())
            result = cursor.fetchall()
            assert len(result) > 0, "Нет данных о курьерах"
            for row in result:
                assert isinstance(row[0], str), "Логин курьера должен быть строкой"
                assert isinstance(row[1], int), "Количество заказов должно быть числом"

def test_orders_statuses():
    """Тест для задания 2: Статусы заказов"""
    with DatabaseConnector() as conn:
        with conn.cursor() as cursor:
            cursor.execute(DatabaseQueries.get_orders_with_statuses())
            result = cursor.fetchall()
            assert len(result) > 0, "Нет данных о заказах"
            for row in result:
                assert isinstance(row[0], str), "Трек номер должен быть строкой"
                assert row[1] in (-1, 0, 1, 2), f"Неверный статус заказа: {row[1]}"