import allure
from data import ResponseErrors
from src.api.order_api import OrderApi
from data import TestData


class TestCreateOrder:
    @allure.title('Тест успешного создания заказа')
    @allure.description('Проверка, что при передаче ингредиентов и токена заказ создается')
    def test_create_new_order(self, login_user, ingredients):
        order_api = OrderApi()
        response = order_api.create_new_order(ingredients, login_user)
        response_data = response.json()
        assert response_data['success'] is True and 'order' in response_data and 'number' in response_data['order']

    @allure.title('Тест создания заказа без авторизации')
    @allure.description('Проверка, что, если не передать access-token при создании заказа, заказ не создается')
    def test_create_new_order_without_auth(self, ingredients):
        order_api = OrderApi()
        response = order_api.create_new_order(ingredients)
        response_data = response.json()
        assert response.status_code == 401 and response_data['success'] is False

    @allure.title('Тест создания заказа без ингредиентов')
    @allure.description('Проверка, что, если не передать ингредиенты при создании заказа, заказ не создается')
    def test_create_new_order_without_ingredients(self, login_user):
        order_api = OrderApi()
        response = order_api.create_new_order(access_token=login_user)
        response_data = response.json()
        assert response.status_code == ResponseErrors.CREATE_ORDER_WITHOUT_INGREDIENTS_DATA['code'] and response_data  == ResponseErrors.CREATE_ORDER_WITHOUT_INGREDIENTS_DATA['body']

    @allure.title('Тест создания заказа c неверными хэшами ингредиентов')
    @allure.description('Проверка, что, если не передать неверные хэши ингредиентов при создании заказа, заказ не создается')
    def test_create_new_order_with_wrong_ingredients(self, login_user):
        order_api = OrderApi()
        invalid_ingredients = TestData.invalid_ingredients
        response = order_api.create_new_order(ingredients_data=invalid_ingredients,access_token=login_user)
        assert response.status_code == 500