import allure
import requests
import urls
from data import Data


class QaScooterApi:
    @staticmethod
    @allure.step('Создаем рандомного курьера')
    def create_new_random_courier():
        body = Data.RANDOM_COUIER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    @allure.step('Создаем курьера с определенными параметрами')
    def create_new_courier():
        body = Data.CREATE_COURIER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    @allure.step('Создаем курьера без логина')
    def create_invalid_courier():
        body = Data.CREATE_INVALID_COURIER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся по логину и паролю для последующего удаления курьера')
    def login():
        body = Data.LOGIN_BODY
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся по логину и паролю')
    def login_for_courier():
        body = Data.LOGIN_BODY_FOR_AUTH
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся с неверным логином курьера')
    def invalid_login():
        body = Data.LOGIN_INVALID_BODY
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся с неверным паролем курьера')
    def invalid_password():
        body = Data.LOGIN_INVALID_BODY
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся без логина курьера')
    def auth_without_login():
        body = Data.AUTH_WITHOUT_LOGIN
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders():
        return requests.get(urls.BASE_URL + urls.GET_ORDERS)

    @staticmethod
    @allure.step('Создаем курьера с определенными параметрами')
    def create_new_courier_as_in_analytics():
        body = Data.CREATE_COURIER_BODY_AS_IN_ANALYTICS
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    @allure.step('Авторизуемся с логином и паролем курьера')
    def login_as_in_analytics():
        body = Data.LOGIN_BODY_AS_IN_ANALYTICS
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)


