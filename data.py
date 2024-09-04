import helper


class Data:

    CREATE_COURIER_BODY = {
    "login": "voldemort",
    "password": "1234",
    "firstName": "tom"
}
    CREATE_INVALID_COURIER_BODY = {
        "password": "1234",
        "firstName": "tom"
    }
    RANDOM_COUIER_BODY = {'login': helper.Help.generated_login(),
                'password': helper.Help.generated_password(),
                'firstName': helper.Help.generated_name()}

    LOGIN_BODY = {
    "login": "voldemort",
    "password": "1234"
}
    LOGIN_BODY_FOR_AUTH = {
    "login": "voldemort304",
    "password": "1234"
}

    CREATE_ERROR_RESPONSE = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    CREATE_ERROR_RESPONSE_AS_IN_ANALYTICS = '{"code":409,"message":"Этот логин уже используется"}'
    CREATE_ERROR_RESPONSE_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    LOGIN_INVALID_BODY = {
            "login": "voldemort30",
            "password": "1234"
        }

    LOGIN_ERROR_RESPONSE = '{"code":404,"message":"Учетная запись не найдена"}'

    PASSWORD_INVALID_BODY = {
            "login": "voldemort",
            "password": "12345"
        }

    LOGIN_ERROR_RESPONSE_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'

    AUTH_WITHOUT_LOGIN = {
        "password": "1234"
    }

    CREATE_COURIER_BODY_AS_IN_ANALYTICS = {
        "login": "teenage_mutant_ninja_turtle",
        "password": "Stick",
        "firstName": "Donatello"
    }

    LOGIN_BODY_AS_IN_ANALYTICS = {
        "login": "teenage_mutant_ninja_turtle",
        "password": "Stick"
    }

    BLACK_COLOR = ["BLACK"]
    BLACK_AND_GREY_COLORS = "BLACK", "GREY"
    EMPTY_COLOR = ["  "]



