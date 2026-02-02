import allure
import pytest

from data import TestData, ResponseErrors
from generator import Generator
from src.api.user_api import UserApi


class TestLoginUser:
    @allure.title('Тест успешного входа')
    @allure.description('Проверка, что зарегистрированный пользователь может авторизоваться')
    def test_success_user_login(self):
        user_api = UserApi()
        response = user_api.login_user({
            'email': TestData.test_user_data['email'],
            'password': TestData.test_user_data['password']
        })
        assert response.status_code == 200 and 'success' in response.json()

    @allure.title('Тест входа с неверными данными')
    @allure.description('Проверка, что при попытке входа с неверными логином или паролем возвращается ошибка')
    @pytest.mark.parametrize('login_user_data', [
        {'email': TestData.test_user_data['email'], 'password': Generator.password_generator()},
        {'email': Generator.email_generator(), 'password': TestData.test_user_data['password']}])
    def test_login_with_wrong_data(self, login_user_data):
        user_api = UserApi()
        response = user_api.login_user(login_user_data)
        assert response.status_code == ResponseErrors.USER_LOGIN_WITH_WRONG_DATA['code']and response.json() == ResponseErrors.USER_LOGIN_WITH_WRONG_DATA['body']