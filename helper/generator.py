import allure
from endpoints.base_endpoints import Endpoint

class GeneratorUserData(Endpoint):
    @allure.step('Создание случайного логина для курьера')
    def create_login_courier(self):
        return self.generate_random_string(5)

    @allure.step('Создание случайного пароля для курьера')
    def create_password_courier(self):
        return self.generate_random_string(5)

    @allure.step('Создание случайного имени для курьера')
    def create_first_name_courier(self):
        return self.generate_random_string(5)