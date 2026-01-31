import allure
from src.base_http_client import BaseHttpClient
from curl import *


class UserApi(BaseHttpClient):
    @allure.step('[POST] запрос на создание пользователя')
    def create_new_user(self, register_data):
        return self.post(register_url, data=register_data)

    @allure.step('[POST] запрос для авторизации пользователя')
    def login_user(self, login_data):
        return self.post(login_url, data=login_data)

    @allure.step('[DELETE] запрос на удаление пользователя')
    def delete_user(self, access_token):
        return self.delete(delete_user_url, params={'authorization': access_token})

    @allure.step('[POST] запрос на выход пользователя из системы')
    def logout(self, refresh_token):
        return self.post(logout_url, data={'authorization': refresh_token})