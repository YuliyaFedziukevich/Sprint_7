import allure
from helper.api import API
from helper.test_data import TestData
from endpoints.base_endpoints import Endpoint

test_data = TestData()
api =API()

class OrderEndpoint(Endpoint):
    @allure.step('Создание заказа')
    def create_order(self, payload_order_data):
        return self.post(api.creating_order, payload_order_data)

    @allure.step('Получение списка заказов')
    def get_list_of_orders(self):
        self.get(api.get_list_of_orders)

    @allure.step('Отмена заказа')
    def cancel_order(self, request):
        self.put(api.cancel_order, request.json())
