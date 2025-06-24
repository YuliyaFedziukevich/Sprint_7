**!!! Внимание !!!**
* Приложение содержит баг - раздел "Логин курьера" - "если какого-то поля нет, запрос возвращает ошибку": если нет поля "Логин" нет, как и положено, возвращается ошибка с кодом 400 с текстом "Недостаточно данных для входа", однако, если нет поля "Пароль" или обоих полей ("Логин" и "Пароль") - ошибка не соответствует заявленной в документации.
* Таким образом, тест test_successful_courier_authorization_not_possible_by_missing_required_fields в файле test_login_courier в двух вариантах условий параметризации из 3-х (нет поля "Пароль", нет обоих полей) имеет статус (Failed).
* При этом, если проводить тесты, что поля/одно из полей пустые, а не отсутствуют в теле запроса, все тесты имеют статус Passed.

**Тестовые сценарии**:
* 1 "Создание курьера"
* 2 "Логин курьера"
* 3 "Создание заказа"
* 4 "Список заказов"

* **Перечень используемых папок и файлов для каждого из сценариев**:
* 1 "Создание курьера":
* - endpoints/base_endpoints.py, endpoints/create_courier.py, 
* - helper/api.py, helper/generator.py, helper/test_data.py, 
* - tests/test_create_courier.py
* 2 "Логин курьера"
* - endpoints/base_endpoints.py, endpoints/create_courier.py, 
* - helper/api.py, helper/generator.py, helper/test_data.py, 
* - tests/test_login_courier.py
* 3 "Создание заказа"
* - endpoints/base_endpoints.py, 
* - helper/api.py, helper/test_data.py, 
* - tests/test_order.py
* 4 "Список заказов"
* - endpoints/base_endpoints.py,
* - helper/api.py,
* - tests/test_order_list.py

**Перечень папок и файлов**:
* 1 **endpoints** - содержит методы и шаги, используемые для тестирования:
* -  base_endpoints.py - общие методы для тестирования;
* - create_courier.py - методы для тестирования курьера (создание, авторизация);
* 2 **helper** - содержит тестовые данные, используемые в обоих сценариях:
* - api.py - перечень используемых при тестировании api;
* - generator.py - содержит класс с методами для генерирования данных для курьера;
* - test_data.py - тестовые данные для всех сценариев;
* 3 **results** - Allure-отчёт в формате JSON;
* 4 **tests.py** - - содержит тесты для каждого из сценариев:
* - tests/test_create_courier.py - тесты на проверку создания курьера (ручка - /api/v1/courier);
* - tests/test_login_courier.py - тесты на проверку авторизации курьера (ручка - /api/v1/courier/login);
* - test_order.py - тестирование создания заказа (ручка - /api/v1/orders);
* - test_order_list.py - тестирование получения списка заказов (ручка - /api/v1/orders);
* 5 **allure_report** - сгенерированный Allure-отчёт
* 6 **conftest.py** - содержит фикстуры; 
* 7 **requirements.txt** - файл с внешними зависимостями. 