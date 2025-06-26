url = 'https://qa-scooter.praktikum-services.ru'

class API:
    creating_courier = f'{url}/api/v1/courier'
    couriers_login = f'{url}/api/v1/courier/login'
    delete_courier = f'{url}/api/v1/courier/:id'
    creating_order = f'{url}/api/v1/orders'
    get_list_of_orders = f'{url}/api/v1/orders'
    cancel_order = f'{url}/api/v1/orders/cancel'
