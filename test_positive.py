import time
from typing import Generator
import pytest
import logging
from site_pages import LoginPageHelper, HomePageHelper, AboutPageHelper
from testing_exceptions import DirectoryNameError


def test_positive_login_to_account(initialize_web_driver: Generator, expected_account_name: str,
                                   user_account: str) -> None:
    logging.info(user_account)

    login_page = LoginPageHelper(initialize_web_driver)
    homepage_page = HomePageHelper(initialize_web_driver)
    file_config_data = login_page.loading_config()
    login_page.go_to_site()

    login_page.enter_login(file_config_data['login_valid'])
    login_page.enter_password(file_config_data['password_valid'])
    login_page.click_on_the_login_button()
    received_name = homepage_page.account_name()
    time.sleep(2)

    try:
        login_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert received_name == expected_account_name, logging.exception("Test_positive_login_to_account FAIL")


def test_positive_opening_the_about_form(initialize_web_driver: Generator, page_title: str, expected_page_title: str):
    logging.info(page_title)

    homepage_page = HomePageHelper(initialize_web_driver)
    about_page = AboutPageHelper(initialize_web_driver)
    file_config_data = homepage_page.loading_config()

    homepage_page.click_on_the_about_button()
    received_header = about_page.finding_the_form_title_text()

    time.sleep(2)

    try:
        homepage_page.save_screenshot_filename_in_directory(file_config_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert received_header == expected_page_title, logging.exception('Test_positive_login_to_account FAIL')


def test_positive_title_font_about(initialize_web_driver: Generator, page_title_font: str, expected_font: str) -> None:
    logging.info(page_title_font)

    login_page = AboutPageHelper(initialize_web_driver)
    received_font = login_page.title_font()

    assert received_font == expected_font, logging.exception('Test_positive_login_button_color FAIL')


if __name__ == '__main__':
    pytest.main(['-vv'])
