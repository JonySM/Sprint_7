import allure
import requests
from data import Data
from qa_scooter_api import QaScooterApi


class TestCreateCourier:
    @allure.title('Проверка создания рандомного курьера')
    def test_successful_creation_courier(self):
        create_request = QaScooterApi.create_new_random_courier()
        assert create_request.status_code == 201 and create_request.text == '{"ok":true}'

    @allure.title('Проверка на создание двух одинаковых курьеров с последующим удалением курьера')
    def test_cannot_create_two_identical_couriers(self):
        create_request_first = QaScooterApi.create_new_courier()
        assert create_request_first.status_code == 201 and create_request_first.text == '{"ok":true}'
        create_request_second = QaScooterApi.create_new_courier()
        assert create_request_second.status_code == 409 and create_request_second.text == Data.CREATE_ERROR_RESPONSE
        response = QaScooterApi.login()
        courier_id = response.json()['id']
        response_del = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")
        assert response_del.status_code == 200 and response_del.text == '{"ok":true}'

    @allure.title('Проверка создания курьера без логина')
    def test_cannot_create_couriers_without_login(self):
        create_request = QaScooterApi.create_invalid_courier()
        assert create_request.status_code == 400 and create_request.text == Data.CREATE_ERROR_RESPONSE_WITHOUT_LOGIN

    @allure.title('Проверка на создание двух одинаковых курьеров с последующим удалением курьера')
    def test_successful_creation_courier_as_in_analytics(self):
        create_request = QaScooterApi.create_new_courier_as_in_analytics()
        assert create_request.status_code == 201 and create_request.text == '{"ok":true}'
        create_request_second = QaScooterApi.create_new_courier_as_in_analytics()
        assert (create_request_second.status_code == 409 and create_request_second.text ==
                Data.CREATE_ERROR_RESPONSE_AS_IN_ANALYTICS)
        response = QaScooterApi.login_as_in_analytics()
        courier_id = response.json()['id']
        response_del = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")
        assert response_del.status_code == 200 and response_del.text == '{"ok":true}'




