import pytest
import allure
from methods.register_methods import UserRegisterMethods
from methods.order_methods import OrderMethods
from request_data.data_user import *
from request_data.data_order import OrderIngridient

class TestRegestrationUser:

    @allure.title("Успешное создание пользователя")
    def test_registered_user_and_deleted_in_sucessfull(self, create_and_delete_user):
        
        payload = UserRegisterMethods.login_body(create_and_delete_user)
        response = UserRegisterMethods.login_user(payload)

        assert response.status_code == DataCode.OK
        assert response.json().get("success") is True

    @allure.title("Ошибка при создании уже существующего пользователя")
    def test_create_user_duplicate_(self, create_and_delete_user):

        user_data = create_and_delete_user
        response = UserRegisterMethods.create_user(user_data)

        assert response.status_code == DataCode.FORBIDDEN
        assert response.json().get("message") == DataMasseage.FORBIDDEN_DUBLICATE
        
    @allure.title("Ошибка регистрации: не заполнено поле {missing_field}")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_error(self, user_payload, missing_field):

        payload = user_payload.copy()
        payload.pop(missing_field)

        response = UserRegisterMethods.create_user(payload)

        assert response.status_code == DataCode.FORBIDDEN
        assert response.json().get("message") == DataMasseage.FORBIDDEN_FIELD



    @allure.title("Ошибка входа с неверным логином и паролем")
    def test_login_and_password_invalid_error(self):

        invalid_payload = UserRegisterMethods.invalid_login_payload()
        response = UserRegisterMethods.login_user(invalid_payload)

        assert response.status_code == DataCode.UNAUTHORIZED
        assert response.json().get("message") == DataMasseage.UNAUTHORIZED_MASSEAGE 

class TestOrderUser:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized_success(self, create_and_delete_user, order_payload):

        login_payload = UserRegisterMethods.login_body(create_and_delete_user)
        login_response = UserRegisterMethods.login_user(login_payload)
        token = UserRegisterMethods.save_token(login_response)
    
        response = OrderMethods.create_order(order_payload, token)

        assert response.status_code == DataCode.OK
        assert response.json().get("success") is True 

    @allure.title("Создание заказа без авторизации")
    @allure.description("Система позволяет создать заказ неавторизированным пользователям")
    @pytest.mark.xfail(reason="Код 200 Ok при создании заказа неавторизированным пользователем в место 401 UNAUTHORIZED")
    def test_create_order_not_authorized_success(self, order_payload):
       
        response = OrderMethods.create_order(order_payload)

        assert response.status_code == DataCode.UNAUTHORIZED
        assert response.json().get("success") is False   


    @allure.title("Ошибка: создание заказа без ингредиентов")
    def test_create_order_no_ingredients_error(self, create_and_delete_user):

        login_payload = UserRegisterMethods.login_body(create_and_delete_user)
        login_response = UserRegisterMethods.login_user(login_payload)
        token = UserRegisterMethods.save_token(login_response)


        empty_payload = OrderIngridient.empty_dictionary

        response = OrderMethods.create_order(empty_payload, token)

        assert response.status_code == DataCode.BAD_REQUEST
        assert response.json().get("message") == DataMasseage.BAD_REQUEST_MESSEAGE 

    @allure.title("Ошибка: создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash_error(self, create_and_delete_user):
    
        login_payload = UserRegisterMethods.login_body(create_and_delete_user)
        login_response = UserRegisterMethods.login_user(login_payload)
        token = UserRegisterMethods.save_token(login_response)

        invalid_payload = OrderIngridient.invalid_dictionary

        response = OrderMethods.create_order(invalid_payload, token)


        assert response.status_code == 500