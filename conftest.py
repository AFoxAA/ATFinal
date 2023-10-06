import pytest
import yaml
from datetime import datetime
from typing import Any, Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('config.yaml', encoding='utf-8') as file:
    file_data: Any = yaml.safe_load(file)
    browser: Any = file_data['browser']
    sleep: Any = file_data['sleep']


@pytest.fixture(scope='session')
def initialize_web_driver() -> Generator:
    driver = None

    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(sleep)

    yield driver

    driver.quit()


@pytest.fixture()
def user_account() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ВХОДА ПОЛЬЗОВАТЕЛЯ В АККАУНТ'


@pytest.fixture()
def expected_account_name() -> str:
    return f'Hello, {file_data["login_valid"]}'


@pytest.fixture()
def page_title() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ОТКРЫТИЯ СТРАНИЦЫ "ABOUT"'


@pytest.fixture()
def expected_page_title() -> str:
    return 'About Page'


@pytest.fixture()
def page_title_font() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ШРИФТА В ЗАГОЛОВКА СТРАНИЦЫ "ABOUT"'


@pytest.fixture()
def expected_font() -> str:
    return '32px'


@pytest.fixture()
def empty_login_and_password_fields() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С ПУСТЫМИ ПОЛЯМИ ЛОГИН И ПАРОЛЬ'


@pytest.fixture()
def invalid_login() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С НЕВАЛИДНЫМ ЛОГИНОМ'


@pytest.fixture()
def invalid_password() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С НЕВАЛИДНЫМ ПАРОЛЕМ'


@pytest.fixture()
def empty_login_field() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С ПУСТЫМ ПОЛЕМ ЛОГИН И ВАЛИДНЫМ ПАРОЛЕМ'


@pytest.fixture()
def empty_password_field() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С ПУСТЫМ ПОЛЕМ ПАРОЛЯ И ВАЛИДНЫМ ЛОГИНОМ'


@pytest.fixture()
def error_number() -> str:
    return '401'


@pytest.fixture()
def get_username_restapi() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА RESTAPI. GET ЗАПРОС ВОЗВРАЩАЕТ JSON С ПРАВИЛЬНЫМ USERNAME'


@pytest.fixture()
def expected_username() -> str:
    return 'ANTA'


@pytest.fixture()
def site_vulnerabilities() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ВЫПОЛНЕНИЯ БЫСТРОЙ ПРОВЕРКИ САЙТА НА УЯЗВИМОСТИ ПРИ ПОМОЩИ УТИЛИТЫ КОМАНДНОЙ СТРОКИ NIKTO'


@pytest.fixture()
def expected_result() -> str:
    return '0 error(s)'


@pytest.fixture()
def expected_site() -> str:
    return 'https://test-stand.gb.ru/'


@pytest.fixture(autouse=True)
def print_time() -> Generator[Any, Any, None]:
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S")))
    yield
    print("\nFinish: {}".format(datetime.now().strftime("%H:%M:%S")))
