# Яндекс Самокат - API Testing Project

Проект для автоматизированного тестирования API Яндекс Самокат в рамках дипломной работы по курсу "Инженер по тестированию плюс".

## 📋 Описание проекта

Этот проект содержит автоматизированные тесты для проверки функциональности API Яндекс Самокат, включая:
- Создание заказа через API
- Получение заказа по номеру трека
- Проверку корректности ответов API

## 🏗️ Структура проекта

```
Diplom_redactura/
├── configuration.py          # Конфигурация API endpoints
├── data.py                  # Тестовые данные
├── sender_stand_request.py  # Функции для работы с API
├── create_order_test.py     # Основной тест
├── SQL_1.txt               # SQL запрос для анализа курьеров
├── SQL_2.txt               # SQL запрос для анализа статусов заказов
└── README.md               # Документация проекта
```

## 🔧 Компоненты проекта

### configuration.py
Конфигурационный файл с настройками API:
```python
URL_SERVICE = "https://8a1b6a25-16ad-43df-8cb6-33d74d3d3ddc.serverhub.praktikum-services.ru"
DOC_PATH = "/docs/"
CREATE_ORDER_PATH = "/api/v1/orders"
GET_ORDER_PATH = "/api/v1/orders/track"
```

### data.py
Тестовые данные для создания заказа:
```python
order_body = {
    "firstName": "Катерина",
    "lastName": "Федорова",
    "address": "Попова, 142",
    "metroStation": 4,
    "phone": "+7 900 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-10-06",
    "comment": "Как можно быстрее",
    "color": ["BLACK"]
}
```

### sender_stand_request.py
Модуль с функциями для работы с API:
- `create_order(order_body)` - создание заказа
- `get_order_by_track(track)` - получение заказа по треку

### create_order_test.py
Основной тест, проверяющий полный цикл работы с заказом:
1. Создание заказа → проверка статус кода 201
2. Извлечение номера трека из ответа
3. Получение заказа по треку → проверка статус кода 200

## 🚀 Установка и запуск

### Требования
- Python 3.6+
- requests
- pytest

### Установка зависимостей
```bash
pip install requests pytest
```

### Запуск теста
```bash
python create_order_test.py
```

Или через pytest:
```bash
pytest create_order_test.py
```

## 📊 SQL Аналитика

Проект включает два SQL запроса для анализа данных:

### SQL_1.txt
Запрос для получения статистики по курьерам с активными заказами:
```sql
SELECT login, COUNT(*) as orders_in_delivery 
FROM "Couriers" c 
JOIN "Orders" o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.login 
ORDER BY orders_in_delivery DESC;
```

### SQL_2.txt
Запрос для получения статусов заказов с числовым представлением:
```sql
SELECT track, 
       CASE 
           WHEN finished = true THEN 2 
           WHEN cancelled = true THEN -1 
           WHEN "inDelivery" = true THEN 1 
           ELSE 0 
       END as status 
FROM "Orders" 
ORDER BY track;
```

## 🔗 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/api/v1/orders` | Создание нового заказа |
| GET | `/api/v1/orders/track` | Получение заказа по номеру трека |

## 📈 Статус коды

| Код | Описание |
|-----|----------|
| 200 | Успешное получение данных |
| 201 | Заказ успешно создан |
| 400 | Некорректный запрос |
| 404 | Ресурс не найден |

## 👤 Автор

**Катерина Искакова**  
34-я когорта - Финальный проект  
Инженер по тестированию плюс
