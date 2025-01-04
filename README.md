# Cafe Orders

Управление заказами для кафе. Создание, редактирование и удаление заказов, а также API для работы с заказами.

## Установка

1. Клонируй репозиторий:
    ```bash
    git clone https://github.com/yourusername/cafe_orders.git
    cd cafe_orders
    ```

2. Создай и активируй виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для macOS/Linux
    venv\Scripts\activate     # Для Windows
    ```

3. Установи зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:
    ```bash
    python manage.py migrate
    ```

5. Создай суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

6. Запусти сервер:
    ```bash
    python manage.py runserver
    ```

Теперь приложение доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Примеры использования

### Веб-приложение
- [Список заказов](http://127.0.0.1:8000/)
- [Создать заказ](http://127.0.0.1:8000/create/)

### API

1. **Получить список заказов**  
    `GET http://127.0.0.1:8000/api/orders/`

2. **Создать заказ**  
    `POST http://127.0.0.1:8000/api/orders/`  
    Пример тела запроса:
    ```json
    {
        "table_number": 6,
        "items": "Burger, Fries",
        "total_price": 18.0,
        "status": "new"
    }
    ```

3. **Получить заказ по ID**  
    `GET http://127.0.0.1:8000/api/orders/{id}/`

4. **Обновить заказ**  
    `PUT http://127.0.0.1:8000/api/orders/{id}/`

5. **Удалить заказ**  
    `DELETE http://127.0.0.1:8000/api/orders/{id}/`

## Тестирование

Запустите тесты с помощью `pytest`:
```bash
pytest
