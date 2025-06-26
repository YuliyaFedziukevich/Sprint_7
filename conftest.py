import allure
import pytest
from endpoints.create_courier import CreateCourier
from endpoints.order_endpoints import OrderEndpoint
from helper.generator import GeneratorUserData
from helper.test_data import TestData

@pytest.fixture(scope='function')
def create_courier_data():
    create_courier = CreateCourier()
    generator_user_data = GeneratorUserData()
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

    # Удаление курьера
    with allure.step("Авторизация курьера"):
        authorization_courier = create_courier.check_courier_authorization(authorization_courier_request_body)
    with allure.step("Удаление курьера"):
        create_courier.delete_courier(authorization_courier.json()['id'])


@pytest.fixture(scope='function')
def create_courier_and_authorization():
    generator_user_data = GeneratorUserData()
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

    create_courier = CreateCourier()
    with allure.step("Создание курьера"):
        create_courier.create_courier_api(create_courier_request_body)
    with allure.step("Авторизация курьера"):
        courier_response = create_courier.check_courier_authorization(authorization_courier_request_body)
    yield [create_courier_request_body, authorization_courier_request_body, login, password], create_courier

    with allure.step("Удаление курьера"):
        create_courier.delete_courier(courier_response.json()['id'])


@pytest.fixture(scope='function', params=TestData.color_option)
def create_order(request):
    with allure.step('Добавление в тестовые данные цвета самоката'):
        order_payload = TestData.payload_order.copy()
        order_payload['color'] = request.param
    # Создание заказа
    order_endpoint = OrderEndpoint()
    response = order_endpoint.create_order(order_payload)
    yield order_endpoint
    with allure.step('Отмена заказа'):
        order_endpoint.cancel_order(response)
