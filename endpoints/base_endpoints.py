import allure
import requests
import random
import string

from helper.test_data import ResponseBody

response_body = ResponseBody()


class Endpoint:
    def __init__(self):
        self.last_response = None

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Метод POST')
    def post(self, url, payload):
        self.last_response = requests.post(url, json = payload)
        return self.last_response

    @allure.step('Метод GET')
    def get(self, url):
        self.last_response = requests.get(url)
        return self.last_response


    @allure.step('Метод PUT')
    def put(self, url, payload):
        self.last_response = requests.put(url, json=payload)
        return self.last_response

    @ allure.step('Метод DELETE')
    def delete(self, url, payload):
        self.last_response = requests.delete(url, json = payload)
        return self.last_response

    @allure.step('Проверка, что код статуса ответа - 200, а в теле ответа - (id:)')
    def check_successful_authorization(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 200
        assert 'id' in self.last_response.json()

    @allure.step('Проверка, что код статуса ответа - 200, а в теле ответа - (orders)')
    def check_successful_get_list_of_orders(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 200
        assert 'orders' in self.last_response.json()

    @allure.step('Проверка, что код статуса ответа - 201, а в теле ответа - ("ok": True)')
    def check_successful_creation_courier(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 201
        assert self.last_response.json() == response_body.response_successful_creation_courier

    @allure.step('Проверка, что код статуса ответа - 201, а в теле ответа - (track)')
    def check_successful_creation_order(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 201
        assert  'track' in self.last_response.json()
        return self.last_response.json()['track']

    @allure.step('Проверка, что код статуса ответа - 400, а в теле ответа -'
                 '("code": 400, "message": "Недостаточно данных для создания учетной записи")')
    def check_not_enough_data_to_create_courier(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 400
        assert self.last_response.json() == response_body.response_not_enough_data_to_create_courier

    @allure.step('Проверка, что код статуса ответа - 400, а в теле ответа -'
                 '("code": 400, "message": "Недостаточно данных для входа")')
    def check_not_enough_data_to_login(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 400
        assert self.last_response.json() == response_body.response_not_enough_data_to_login

    @allure.step('Проверка, что код статуса ответа - 404, а в теле ответа -'
                 '("code": 404 "message": "Учетная запись не найдена")')
    def check_user_not_found(self):
        code = 404
        assert self.last_response.status_code == code
        assert self.last_response.json() == response_body.response_check_user_not_found

    @allure.step('Проверка, что код статуса ответа - 409, а в теле ответа -'
                 '("code": 409, "message": "Этот логин уже используется. Попробуйте другой.")')
    def check_login_already_in_use(self):
        assert self.last_response is not None
        assert self.last_response.status_code == 409
        assert self.last_response.json() == response_body.response_login_already_in_use
