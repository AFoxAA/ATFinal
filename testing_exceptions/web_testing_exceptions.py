from typing import Any


class LocatorError(Exception):
    def __init__(self, locator: Any, time: Any) -> None:
        self.locator: Any = locator
        self.time: Any = time
        self.message: str = f'Элемент с локатором {self.locator} не найден после ожидания {self.time} секунд'

    def __str__(self) -> str:
        return self.message


class SiteAccessError(Exception):
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url
        self.message: str = f'Не удается получить доступ к сайту {self.base_url}. Пожалуйста, убедитесь в корректности URL.'

    def __str__(self) -> str:
        return self.message


class ErrorWhenSavingScreenshot(Exception):
    def __init__(self) -> None:
        self.message: str = ('Ошибка при сохранении скриншота. '
                             'В файле ".yaml" отсутствует значение для директории сохранения скриншотов.')

    def __str__(self) -> str:
        return self.message


class TextInputError(Exception):
    def __init__(self, locator: Any, word: Any) -> None:
        self.locator: Any = locator
        self.word: Any = word
        self.message: str = f'Ошибка при вводе текста "{self.word}" в текстовое поле ввода "{self.locator}"'

    def __str__(self) -> str:
        return self.message


class ErrorWhenClicking(Exception):
    def __init__(self) -> None:
        self.message: str = 'Ошибка при клике на элемент'

    def __str__(self) -> str:
        return self.message


class ErrorReceivingText(Exception):
    def __init__(self, element_name: Any) -> None:
        self.element_name: Any = element_name
        self.message: str = f'Ошибка при получении текста из {self.element_name}'

    def __str__(self) -> str:
        return self.message


class DirectoryNameError(Exception):
    def __init__(self) -> None:
        self.message: str = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                             'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')

    def __str__(self) -> str:
        return self.message


class ErrorReceivingToken(Exception):
    def __init__(self, status_code: int) -> None:
        self.status_code: int = status_code
        self.message: str = f'Ошибка при получении токена, код ошибки: {self.status_code}'

    def __str__(self) -> str:
        return self.message


class ErrorEntranceInvalidUrl(Exception):
    def __init__(self, url_login: int) -> None:
        self.url_login: Any = url_login
        self.message: str = f'Ошибка: неверный URL для входа: {self.url_login}'

    def __str__(self) -> str:
        return self.message


class ErrorReceivingPostRequest(Exception):
    def __init__(self) -> None:
        self.message: str = 'Ошибка: не удалось получить запрос поста'

    def __str__(self) -> str:
        return self.message


class ErrorApi(Exception):
    def __init__(self) -> None:
        self.message: str = 'Тест не пройден с исключением: '

    def __str__(self) -> str:
        return self.message
