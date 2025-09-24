# Scooter QA Project

Проект автоматизации тестирования API и базы данных сервиса аренды самокатов.

## 📁 Структура проекта

- `database/queries.sql` - SQL запросы для заданий
- `tests/test_api.py` - автотесты API
- `tests/test_database.py` - автотесты базы данных
- `docs/test_screenshot.png` - скриншот запуска тестов

## 🚀 Запуск тестов

```bash
# Установка зависимостей
pip install -r database/requirements.txt

# Запуск всех тестов
python -m pytest tests/ -v

# Запуск тестов API
python -m pytest tests/test_api.py -v

# Запуск тестов БД
python -m pytest tests/test_database.py -v