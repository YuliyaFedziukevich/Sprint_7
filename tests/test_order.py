import allure

class TestOrder:
    @allure.title('Тест на проверку возможности успешного создания заказа, ручка - /api/v1/orders')
    def test_creating_courier(self, create_order):
        order_endpoint = create_order
        # Проверка, что код статуса ответа - 201, а в теле ответа - (track)
        order_endpoint.check_successful_creation_order()
