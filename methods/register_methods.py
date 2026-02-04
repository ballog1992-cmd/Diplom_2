import allure
import requests
from curl import Url
from request_data.data_user import DataTestloginUser

class UserRegisterMethods:

    
    @staticmethod
    @allure.step("Создать пользователя")
    def create_user(body):
        return requests.post(Url.REG_USER, json=body)
    
    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(body):
        return requests.post(Url.LOGIN_PAGE, json=body)

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(Url.DEL_USER, headers=headers)
    
    @staticmethod
    @allure.step("Формируем тело запроса для логина")
    def login_body(user_data):
        
        return {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    @staticmethod
    @allure.step("Генерируем данные")
    def gen_data(generate_registration_data):
        name, email, password = generate_registration_data()
        payload = {"email": email, "password": password, "name": name}
        return payload
    
    @staticmethod
    @allure.step("Не зарегестрированные email с паролем")
    def invalid_login_payload():
        return {
            "email": DataTestloginUser.email,
            "password": DataTestloginUser.password
        }
    
    @staticmethod
    @allure.step("Сохранить токен")
    def save_token(login_response):
        return login_response.json().get("accessToken")
         