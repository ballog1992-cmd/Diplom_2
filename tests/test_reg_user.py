import pytest
import allure
from methods.register_methods import UserRegisterMethods
from request_data.data_user import *


class TestAuthAPI:

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