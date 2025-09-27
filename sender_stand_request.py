import configuration

import requests

import data 

# Функция для создания заказа
def create_order(order_body):
    # Выполняем POST-запрос к URL для создания заказа
    # Передаем данные заказа в теле запроса в формате JSON
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Функция для получения заказа по треку
def get_order_by_track(track):
    # Выполняем GET-запрос к URL для получения заказа по треку
    # Трек передается как параметр запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params={"t": track})
