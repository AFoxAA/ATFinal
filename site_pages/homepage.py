from typing import Any
from base_actions import BaseActions
from base_actions import PageElementLocators


class HomePageHelper(BaseActions):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def account_name(self) -> str:
        return self.get_text_from_element(self.locators.get_locators()['LOCATOR_ACCOUNT_NAME'],
                                          description='для проверки входа пользователя в личный кабинет')

    def click_on_the_about_button(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_BUTTON_ABOUT'],
                              description='на кнопку "About" на домашней странице')
