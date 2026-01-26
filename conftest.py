import pytest
from methods.register_methods import UserRegisterMethods
from selenium import webdriver  


from helper import *

# pytest --browser-chrome
# pytest --browser-firefox

class WebDriverFactory:
    @staticmethod
    def get_webdriver(browser_name):

        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported: {browser_name}")
    
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action= "store", default="chrome",help="Выбор браузера: 'chrome' или 'firefox'"

    )


@pytest.fixture
def driver(request):

    browser_name = request.config.getoption("--browser")

    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit

@pytest.fixture
def user_payload():
    # Используем твой метод для генерации словаря
    return UserRegisterMethods.gen_data(generate_registration_data)

@pytest.fixture
def create_and_delete_user(user_payload):
    
    response = UserRegisterMethods.create_user(user_payload)
    assert response.status_code == 200, f"Ошибка регистрации: {response.text}"
    
    token = response.json().get("accessToken")

    yield user_payload
    UserRegisterMethods.delete_user(token)