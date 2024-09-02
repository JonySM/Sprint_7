import allure
import pytest
import requests
import urls
from qa_scooter_api import QaScooterApi


class TestOrders:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize('color', ["BLACK", "BLACK, GREY", "  "])
    def test_orders_scooters(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }
        response = requests.post(urls.BASE_URL + urls.CREATE_ORDER, json=payload)
        create_request = response
        track_number = create_request.json()['track']
        assert create_request.json() == {"track": track_number}

    @allure.title('Проверка тела при возврате списка заказов')
    def test_get_orders(self):
        orders = QaScooterApi.get_orders()
        assert orders.status_code == 200 and orders.json()['orders'][0]['id'] == 309461
        assert orders.status_code == 200 and orders.json()['orders'][0]['courierId'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['firstName'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['lastName'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['address'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['metroStation'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['phone'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['rentTime'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['deliveryDate'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['track'] == 601382
        assert orders.status_code == 200 and orders.json()['orders'][0]['color'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['comment'] is None
        assert orders.status_code == 200 and orders.json()['orders'][0]['createdAt'] == '2024-06-30T17:49:45.156Z'
        assert orders.status_code == 200 and orders.json()['orders'][0]['updatedAt'] == '2024-06-30T17:49:45.156Z'
        assert orders.status_code == 200 and orders.json()['orders'][0]['status'] == 0








