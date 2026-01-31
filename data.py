class ResponseErrors:
    USER_ALREADY_EXIST = {
        'code': 403,
        'body': {
            'message': 'User already exists',
            'success': False
        }
    }
    USER_REGISTRATION_NOT_ENOUGH_DATA = {
        'code': 403,
        'body': {
            'message': 'Email, password and name are required fields',
            'success': False
        }
    }
    USER_LOGIN_WITH_WRONG_DATA = {
        'code': 401,
        'body': {
            'success': False,
            'message': 'email or password are incorrect',
        }
    }

    CREATE_ORDER_WITHOUT_INGREDIENTS_DATA = {
        'code': 400,
        'body': {
            'success': False,
            'message': 'Ingredient ids must be provided',
        }
    }

class TestData:
    test_user_data = {
        'name': 'Елена',
        'email': 'dyshpan_33_001@mail.ru',
        'password': '123456',
    }

    invalid_ingredients = ['ingredient_1', 'ingredient_2', 'ingredient_3']