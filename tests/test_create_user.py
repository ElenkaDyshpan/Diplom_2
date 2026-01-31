import allure
import pytest

from src.api.user_api import UserApi
from data import ResponseErrors
from generator import Generator


class TestCreateUser:
    @allure.title('Тест успешного создания пользователя')
    @allure.description('Проверка, что при передаче всех необходимых данных пользователь создается')
    def test_create_new_user(self, generate_user_data):
        user_api = UserApi()
        response = user_api.create_new_user(generate_user_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Тест создания пользователя, который уже зарегистрирован')
    @allure.description('Проверка, что невозможно повторно зарегистрировать пользователя')
    def test_create_user_twice(self, register_user):
        user_api = UserApi()
        response = user_api.create_new_user(register_user)
        assert response.status_code == ResponseErrors.USER_ALREADY_EXIST['code'] and response.json() == ResponseErrors.USER_ALREADY_EXIST['body']

    @allure.title('Тест создания пользователя если не переданы все данные')
    @allure.description(
        'Проверка, что при попытке создания пользователя без одного из обязательных полей возвращается ошибка')
    @pytest.mark.parametrize('register_user_data', [
        {'email': Generator.email_generator(), 'password': Generator.password_generator()},
        {'password': Generator.password_generator(), 'name': Generator.name_generator()},
        {'email': Generator.email_generator(), 'name': Generator.name_generator()},
    ])
    def test_create_user_without_all_data(self, register_user_data):
        user_api = UserApi()
        response = user_api.create_new_user(register_user_data)
        assert response.status_code == ResponseErrors.USER_REGISTRATION_NOT_ENOUGH_DATA['code'] and response.json() == ResponseErrors.USER_REGISTRATION_NOT_ENOUGH_DATA['body']