class ResponseBody:
    response_successful_creation_courier = {'ok': True}
    response_login_already_in_use = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    response_not_enough_data_to_create_courier = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    response_not_enough_data_to_login = {"code": 400, "message": "Недостаточно данных для входа"}
    response_check_user_not_found = {"code": 404, "message": "Учетная запись не найдена"}

class TestData:
    payload = [
        {'login': '', 'password': '', 'firstName': ''},  # все поля пустые
        {'login': '', 'password': 'password', 'firstName': 'firstName'},  # пустое поле логин
        {'login': 'login', 'password': '', 'firstName': 'firstName'}, # пустое поле пароль
        {'password': 'password', 'firstName': 'firstName'},  # без поля логин
        {'login': 'login', 'firstName': 'firstName'},  # без поля пароль
        {'login': None, 'password': None, 'firstName': None}  # все поля - None
    ]

    type_of_data_change = ['changePwd', 'changeLogin', 'changeBoth']
    type_of_missing_data = ['missingPwd', 'missingLogin', 'missingBoth']

    payload_order= {
            'firstName': 'Ivan',
            'lastName': 'Ivanov',
            'address': 'Minsk, 1 apt.',
            'metroStation': 1,
            'phone': '+7 111 222 333 4',
            'rentTime': 1,
            'deliveryDate': '2025-12-01',
            'comment': 'Preferably in the morning'}
    color_option = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

