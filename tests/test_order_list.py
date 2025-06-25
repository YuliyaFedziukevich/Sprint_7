import allure
from endpoints.order_endpoints import OrderEndpoint

order_endpoint = OrderEndpoint()

class TestOrderList:
    @allure.title('Получение списка заказов, ручка - /api/v1/orders')
    def test_get_orders_list(self):
        # Получение списка заказов
        order_endpoint.get_list_of_orders()
        # Проверка, что код статуса ответа - 200, а в теле ответа - (orders)
        order_endpoint.check_successful_get_list_of_orders()
