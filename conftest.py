import pytest
from pygments.lexers import q

from generator import Generator
from src.api.user_api import UserApi
from src.api.order_api import OrderApi
from data import TestData


@pytest.fixture
def generate_user_data():
    email = Generator.email_generator()
    password = Generator.password_generator()
    name = Generator.name_generator()
    create_user_body = { 'email': email, 'password': password, 'name': name }
    yield create_user_body
    user_api = UserApi()
    login_user_data = user_api.login_user({'email': email, 'password': password}).json()
    if 'accessToken' in login_user_data:
        user_api.delete_user(login_user_data['accessToken'])

@pytest.fixture
def register_user():
    email = Generator.email_generator()
    password = Generator.password_generator()
    name = Generator.name_generator()
    create_user_body = { 'email': email, 'password': password, 'name': name }
    user_api = UserApi()
    user_data = user_api.create_new_user(create_user_body)
    yield create_user_body
    if 'accessToken' in user_data:
        user_api.delete_user(user_data['accessToken'])
        
@pytest.fixture
def login_user():
    user_api = UserApi()
    test_user_data = TestData.test_user_data
    user_data = user_api.login_user({'email': test_user_data['email'], 'password': test_user_data['password']}).json()
    access_token = user_data['accessToken']
    refresh_token = user_data['refreshToken']
    yield access_token
    user_api.logout(refresh_token)

@pytest.fixture
def ingredients():
    order_api = OrderApi()
    response = order_api.get_ingredients()
    if response.status_code == 200:
        response_data = response.json()
        ingredients_list = response_data.get('data', [])
        if ingredients_list and len(ingredients_list) >= 3:
            return [ingredient['_id'] for ingredient in ingredients_list[:3]]
        return []
    return []