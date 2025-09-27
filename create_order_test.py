# Катерина Искакова, 34-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_order_and_get_by_track():
    """
    Тест для проверки создания заказа и получения данных по треку
    """
    # Шаг 1: Выполнить запрос на создание заказа
    response = sender_stand_request.create_order(data.order_body)
    
    # Проверка, что заказ создан успешно (статус код 201)
    assert response.status_code == 201, f"Ожидался статус код 201, получен {response.status_code}"
    
    # Шаг 2: Сохранить номер трека заказа
    track = response.json()["track"]
    
    # Шаг 3: Выполнить запрос на получение заказа по треку заказа
    response = sender_stand_request.get_order_by_track(track)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

if __name__ == "__main__":
    test_create_order_and_get_by_track()