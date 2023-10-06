import time
from typing import Generator
import pytest
import logging
from site_pages import LoginPageHelper
from testing_exceptions import DirectoryNameError


def test_negative_empty_logging_fields(initialize_web_driver: Generator, empty_login_and_password_fields: str,
                                       error_number: str) -> None:
    logging.info(empty_login_and_password_fields)

    login_page = LoginPageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()
    login_page.go_to_site()

    login_page.click_on_the_login_button()
    time.sleep(1)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, logging.exception('Test_negative_empty_logging_fields')


def test_negative_invalid_login(initialize_web_driver: Generator, invalid_login: str, error_number: str) -> None:
    logging.info(invalid_login)
    login_page = LoginPageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()

    login_page.enter_login(file_config_data['login_invalid'])
    login_page.enter_password(file_config_data['password_valid'])
    login_page.click_on_the_login_button()
    time.sleep(1)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, logging.exception('Test_negative_invalid_login')


def test_negative_invalid_password(initialize_web_driver: Generator, invalid_password: str, error_number: str) -> None:
    logging.info(invalid_password)
    login_page = LoginPageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()

    login_page.enter_login(file_config_data['login_valid'])
    login_page.enter_password(file_config_data['password_invalid'])
    login_page.click_on_the_login_button()
    time.sleep(1)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, logging.exception('Test_negative_invalid_password')


def test_negative_empty_login_field(initialize_web_driver: Generator, empty_login_field: str,
                                    error_number: str) -> None:
    logging.info(empty_login_field)
    login_page = LoginPageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()
    login_page.go_to_site()

    login_page.enter_password(file_config_data['password_valid'])
    login_page.click_on_the_login_button()
    time.sleep(1)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, logging.exception('Test_negative_empty_login_field')


def test_negative_empty_password_field(initialize_web_driver: Generator, empty_password_field: str,
                                       error_number: str) -> None:
    logging.info(empty_password_field)
    login_page = LoginPageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()
    login_page.go_to_site()

    login_page.enter_login(file_config_data['login_valid'])
    login_page.click_on_the_login_button()
    time.sleep(1)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, logging.exception('Test_negative_empty_password_field')


if __name__ == '__main__':
    pytest.main(['-vv'])
