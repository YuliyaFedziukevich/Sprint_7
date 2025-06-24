import allure
import pytest
from endpoints.base_endpoints import Endpoint
from helper.test_data import TestData
from helper.api import API

base_endpoints = Endpoint()
test_data = TestData()
api =API()

class TestOrder:
    @allure.title('Тест на проверку возможности успешного создания заказа, ручка - /api/v1/orders')
    @pytest.mark.parametrize('payload', test_data.color_option)
    def test_creating_courier(self, payload):
        with allure.step('Добавление в тестовые данные цвета самоката'):
            test_data.payload_order['color'] = payload
        with allure.step('Создание заказа'):
            base_endpoints.post(api.creating_order, test_data.payload_order)
        # Проверка, что код статуса ответа - 201, а в теле ответа - (track)
        order_track = base_endpoints.check_successful_creation_order()
        with allure.step('Отмена заказа'):
            base_endpoints.put(api.cancel_order, order_track)
