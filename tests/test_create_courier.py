import allure
import pytest
from endpoints.create_courier import CreateCourier, ChangedData
from helper.test_data import TestData

create_courier = CreateCourier()
changed_data = ChangedData()

class TestCourier:

    @allure.title('Тест на проверку возможности успешного создания курьера, ручка - /api/v1/courier')
    def test_creating_courier(self, create_courier_data):
        create_courier.create_courier_api(create_courier_data[0])
        # Проверка, что код статуса ответа - 201, а в теле ответа - {"ok": True})
        create_courier.check_successful_creation_courier()

    @allure.title('Тест на проверку невозможности создания двух идентичных курьеров, ручка - /api/v1/courier')
    def test_impossible_to_create_two_identical_couriers(self, create_courier_data):
        create_courier.create_courier_api(create_courier_data[0])
        with allure.step('Попытка создания идентичного курьера'):
            create_courier.create_courier_api(create_courier_data[0])
        # Проверка, что невозможно создать два идентичных курьера
        # код статуса ответа - 409, а в теле ответа -
        # {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        create_courier.check_login_already_in_use()


    @allure.title('Тест на проверку невозможности создания курьеров с одинаковым логином, ручка - /api/v1/courier')
    def test_impossible_to_create_two_couriers_with_identical_login(self,create_courier_data):
        create_courier.create_courier_api(create_courier_data[0])
        # Создание копии регистрационных данных для изменения пароля и имени
        payload = changed_data.changing_password_first_name_data(create_courier_data[0])
        with allure.step('Попытка создания курьера с существующим логином'):
            create_courier.create_courier_api(payload)
        # Проверка, что невозможно создать два идентичных курьера
        # код статуса ответа - 409, а в теле ответа -
        # {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        create_courier.check_login_already_in_use()

    @allure.title('Тест на проверку невозможности создания курьера без логина или пароля, ручка - /api/v1/courier')
    @pytest.mark.parametrize(
    'payload', TestData.payload)
    def test_impossible_to_create_courier_without_login_or_password(self, payload):
        # Создание курьера
        create_courier.create_courier_api(payload)
        # Проверка, что код статуса ответа - 400, а в теле ответа -
        # {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
        create_courier.check_not_enough_data_to_create_courier()
