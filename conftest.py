import allure
import pytest
from endpoints.create_courier import CreateCourier
from helper.generator import GeneratorUserData
from helper.test_data import TestData

test_data = TestData()
generator_user_data = GeneratorUserData()

@pytest.fixture(scope='function')
def create_courier_data():
    create_courier = CreateCourier()
    with allure.step("Генерация данных для курьера"):
        login = generator_user_data.create_login_courier()
        password = generator_user_data.create_password_courier()
        first_name = generator_user_data.create_first_name_courier()
    with allure.step("Генерация данных для создания курьера"):
        create_courier_request_body = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
    with allure.step("Генерация данных для авторизации курьера"):
        authorization_courier_request_body = {
            'login': login,
            'password': password
        }
    yield [create_courier_request_body, authorization_courier_request_body, login, password]
    with allure.step("Авторизация курьера"):
        authorization_courier = create_courier.check_courier_authorization(authorization_courier_request_body)
    with allure.step("Удаление курьера"):
        create_courier.delete_courier(authorization_courier.json()['id'])


@pytest.fixture(scope='function')
def create_courier_and_authorization():
    create_courier = CreateCourier()
    with allure.step("Генерация данных для курьера"):
        login = generator_user_data.create_login_courier()
        password = generator_user_data.create_password_courier()
        first_name = generator_user_data.create_first_name_courier()
    with allure.step("Генерация данных для создания курьера"):
        create_courier_request_body = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
    with allure.step("Генерация данных для авторизации курьера"):
        authorization_courier_request_body = {
            'login': login,
            'password': password
        }
    with allure.step("Создание курьера"):
        create_courier.create_courier_api(create_courier_request_body)
    with allure.step("Авторизация курьера"):
        courier_response = create_courier.check_courier_authorization(authorization_courier_request_body)
    yield [create_courier_request_body, authorization_courier_request_body, login, password], create_courier
    with allure.step("Удаление курьера"):
        create_courier.delete_courier(courier_response.json()['id'])
