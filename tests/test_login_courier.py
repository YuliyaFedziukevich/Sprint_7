import allure
import pytest
from endpoints.create_courier import CreateCourier, ChangedData
from helper.generator import GeneratorUserData
from helper.test_data import TestData

create_courier = CreateCourier()
changed_data = ChangedData()
generator_user_data = GeneratorUserData()

class TestCouriersLogin:
    @allure.title('Успешная авторизация курьера с заполнением всех обязательных полей, ручка - /api/v1/courier/login')
    def test_successful_courier_authorization(self, create_courier_and_authorization):
        data, courier_creator = create_courier_and_authorization
        # Проверка, что код статуса ответа - 200, а в теле ответа - ('id:')
        courier_creator.check_successful_authorization()

    @allure.title('Успешная авторизация курьера невозможна при вводе неверного логина или пароля, ручка - /api/v1/courier/login')
    @pytest.mark.parametrize('cmd', TestData.type_of_data_change)
    def test_successful_courier_authorization_not_possible_with_incorrect_login_or_password(self, cmd, create_courier_data):
        # Создание курьера с получением авторизационных данных
        create_courier.create_courier_api(create_courier_data[0])
        changed_data_to_authorization = changed_data.changing_data(create_courier_data[0], cmd, 0)
        with allure.step('Авторизация курьера с измененными данными'):
            create_courier.check_courier_authorization(changed_data_to_authorization)
        # Проверка, что авторизация курьера невозможна, код статуса - 404, а в теле ответа -"Учетная запись не найдена"
        create_courier.check_user_not_found()

    @allure.title('Успешная авторизация курьера невозможна при пустых обязательных полей - логин или пароль, ручка - /api/v1/courier/login')
    @ pytest.mark.parametrize('cmd', TestData.type_of_data_change)
    def test_successful_courier_authorization_not_possible_by_empty_required_fields(self, cmd, create_courier_data):
        # Создание курьера с получением авторизационных данных
        create_courier.create_courier_api(create_courier_data[0])
        changed_data_to_authorization = changed_data.changing_data(create_courier_data[0], cmd, 1)
        with allure.step('Авторизация курьера с измененными данными'):
            create_courier.check_courier_authorization(changed_data_to_authorization)
        # Проверка, что авторизация курьера невозможна, код статуса - 400, а в теле ответа -"Недостаточно данных для входа"
        create_courier.check_not_enough_data_to_login()

    @allure.title('Успешная авторизация курьера невозможна, если какого-то поля нет - логина или пароля, ручка - /api/v1/courier/login')
    @ pytest.mark.parametrize('cmd', TestData.type_of_missing_data)
    def test_successful_courier_authorization_not_possible_by_missing_required_fields(self, cmd, create_courier_data):
        # Создание курьера с получением авторизационных данных
        create_courier.create_courier_api(create_courier_data[0])
        changed_data_to_authorization = changed_data.check_missing_data(create_courier_data[0], cmd)
        with allure.step('Авторизация курьера с измененными данными'):
            create_courier.check_courier_authorization(changed_data_to_authorization)
        # Проверка, что авторизация курьера невозможна, код статуса - 400, а в теле ответа -"Недостаточно данных для входа"
        create_courier.check_not_enough_data_to_login()

    @allure.title('Успешная авторизация несуществующего курьера невозможна, ручка - /api/v1/courier/login')
    def test_successful_authorization_of_non_existent_courier_not_possible(self):
        authorization_data = {
            'login': generator_user_data.create_login_courier(),
            'password': generator_user_data.create_password_courier()}
        # Авторизация курьера
        create_courier.check_courier_authorization(authorization_data)
        # Проверка, что учетная запись не найдена - код статуса ответа - 404, а в теле ответа - ('Учетная запись не найдена')
        create_courier.check_user_not_found()
