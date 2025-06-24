import allure
from endpoints.base_endpoints import Endpoint
from helper.api import API

base_endpoints = Endpoint()
api =API()

class TestOrderList:
    @allure.title('Получение списка заказов, ручка - /api/v1/orders')
    def test_get_orders_list(self):
        with allure.step('Получение списка заказов'):
            base_endpoints.get(api.get_list_of_orders)
        # Проверка, что код статуса ответа - 200, а в теле ответа - (orders)
        base_endpoints.check_successful_get_list_of_orders()
