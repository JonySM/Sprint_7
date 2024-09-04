import random
import allure


class Help:
    @staticmethod
    @allure.step('Создаем рандомное имя курьера')
    def generated_name():
        return f"Ivan{random.randint(1000, 9999)}"

    @staticmethod
    @allure.step('Создаем рандомный логин курьера')
    def generated_login():
        return f"UserPrakticum{random.randint(100, 9999)}"

    @staticmethod
    @allure.step('Создаем рандомный пароль курьера')
    def generated_password():
        return f"UserPrakticum!*{random.randint(100, 9999)}"