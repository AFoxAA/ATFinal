from typing import Any
import yaml
from selenium.webdriver.common.by import By


class PageElementLocators:
    def __init__(self) -> None:
        self._dict_locators = None

    def get_locators(self) -> dict[Any, tuple[str, Any]]:
        if self._dict_locators is None:
            with open('locators.yaml') as file:
                get_locator = yaml.safe_load(file)

            dict_locators = {}

            for locator in get_locator['XPATH'].keys():
                dict_locators[locator] = (By.XPATH, get_locator['XPATH'][locator])

            for locator in get_locator['CSS'].keys():
                dict_locators[locator] = (By.CSS_SELECTOR, get_locator['CSS'][locator])

            self._dict_locators = dict_locators

        return self._dict_locators
