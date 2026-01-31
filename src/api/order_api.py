import allure

from curl import create_order_url, ingredients_url
from src.base_http_client import BaseHttpClient


class OrderApi(BaseHttpClient):
    @allure.step('[POST] запрос на создание заказа')
    def create_new_order(self, ingredients_data = None, access_token = None):
        headers = {'Authorization': access_token}
        create_order_data = None
        if ingredients_data:
            create_order_data = {
                'ingredients': ingredients_data
            }
        return self.post(create_order_url, data=create_order_data, headers=headers)

    @allure.step('[DET] запрос на получение ингредиентов')
    def get_ingredients(self):
        return self.get(ingredients_url)