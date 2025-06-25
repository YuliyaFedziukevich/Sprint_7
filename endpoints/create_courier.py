import allure
from helper.api import API
from helper.test_data import TestData
from endpoints.base_endpoints import Endpoint
from helper.generator import GeneratorUserData

test_data = TestData()
api =API()
generator_user_data = GeneratorUserData()

class CreateCourier(Endpoint):

    @allure.step('Запрос на создание курьера')
    def create_courier_api(self, payload):
        self.post(api.creating_courier, payload)

    @allure.step('Запрос на удаление курьера')
    def delete_courier(self, payload):
        self.delete(api.delete_courier, payload)

    @allure.step('Авторизация курьера')
    def check_courier_authorization(self, authorization_data):
        return self.post(api.couriers_login, authorization_data)

    @allure.step('Генерирование случайных авторизационных данных - логина и пароля')
    def generate_authorization_data(self):
        authorization_data = {
            'login': generator_user_data.create_login_courier(),
            'password': generator_user_data.create_password_courier()}
        return authorization_data

class ChangedData:
    @allure.step('Создание копии регистрационных данных для изменения пароля и имени')
    def changing_password_first_name_data(self, creating_courier_data):
        changed_create_courier_data = creating_courier_data.copy()
        changed_create_courier_data['password'] = generator_user_data.create_password_courier()
        changed_create_courier_data['firstName'] = generator_user_data.create_first_name_courier()
        return changed_create_courier_data

    @allure.step('Создание копии авторизационных данных для изменения логина и/или пароля')
    def changing_data(self, authorization_data, cmd, index):
        new_payload_authorization = [
            {'login': generator_user_data.create_login_courier(),
             'password': generator_user_data.create_password_courier()},
            {'login': '', 'password': ''}
        ]
        changed_authorization_data = authorization_data.copy()
        if cmd == 'changePwd':
            changed_authorization_data['password'] = new_payload_authorization[index].get('password')
        elif cmd == 'changeLogin':
            changed_authorization_data['login'] = new_payload_authorization[index].get('login')
        elif cmd == 'changeBoth':
            changed_authorization_data['password'] = new_payload_authorization[index].get('password')
            changed_authorization_data['login'] = new_payload_authorization[index].get('login')
        return changed_authorization_data

    @allure.step('Создание копии авторизационных данных для удаления из тела запроса логина и/или пароля')
    def check_missing_data(self, authorization_data, cmd):
        changed_authorization_data = authorization_data.copy()
        if cmd == 'missingPwd':
            del changed_authorization_data['password']
        elif cmd == 'missingLogin':
            del changed_authorization_data['login']
        elif cmd == 'missingBoth':
            del changed_authorization_data['password']
            del changed_authorization_data['login']
        return changed_authorization_data
