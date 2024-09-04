import allure

from data import Data
from qa_scooter_api import QaScooterApi


class TestLoginCourier:
    @allure.title('Проверка авторизации по логину и паролю')
    def test_login(self):
        login_courier = QaScooterApi.login_for_courier()
        assert login_courier.status_code == 200

    @allure.title('Проверка авторизации с несуществующим логином')
    def test_invalid_login(self):
        login_courier = QaScooterApi.invalid_login()
        assert login_courier.status_code == 404 and login_courier.text == Data.LOGIN_ERROR_RESPONSE

    @allure.title('Проверка авторизации с несуществующим паролем')
    def test_invalid_password(self):
        login_courier = QaScooterApi.invalid_password()
        assert login_courier.status_code == 404 and login_courier.text == Data.LOGIN_ERROR_RESPONSE

    @allure.title('Проверка авторизации без ввода логина')
    def test_auth_without_login(self):
        login_courier = QaScooterApi.auth_without_login()
        assert login_courier.status_code == 400 and login_courier.text == Data.LOGIN_ERROR_RESPONSE_WITHOUT_LOGIN

    @allure.title('Проверка возврата id при вводе валидной пары логин-пароль')
    def test_login_returned_id(self):
        login_courier = QaScooterApi.login_for_courier()
        id_number = login_courier.json()['id']
        assert login_courier.json() == {"id": id_number}


