from typing import Any
from base_actions import BaseActions
from base_actions import PageElementLocators


class LoginPageHelper(BaseActions):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def enter_login(self, login: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_LOGIN_FIELD'], login,
                                      description='"Поле ввода логина на странице авторизации"')

    def enter_password(self, password: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_PASSWORD_FIELD'], password,
                                      description='"Поле ввода password на странице авторизации"')

    def click_on_the_login_button(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_BUTTON_LOGIN'],
                              description='на кнопку "Login" на странице авторизации')

    def checking_error_text(self) -> str:
        return self.get_text_from_element(self.locators.get_locators()['LOCATOR_ERROR_MESSAGE'],
                                          description='для проверки ошибки входа пользователя в личный кабинет')
