import allure
import requests
from curl import Url

class OrderMethods:

    @staticmethod
    @allure.step("Получить все данные об ингредиентах")
    def get_ingredients_list():
        return requests.get(Url.INGREDIENTS)

    @staticmethod
    @allure.step("Сформировать список ID ингредиентов")
    def get_only_ingredients_ids(response):
        
        data = response.json().get("data")
        return [ingredient["_id"] for ingredient in data]

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload, token=None):
        headers = {"Authorization": token}
        return requests.post(Url.ORDERS, json=payload, headers=headers)