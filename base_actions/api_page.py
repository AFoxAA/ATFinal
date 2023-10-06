import logging
from typing import Any
import requests
import yaml
from testing_exceptions import ErrorReceivingToken, ErrorEntranceInvalidUrl, ErrorReceivingPostRequest


class RestAPI:
    def __init__(self) -> None:
        with open('config.yaml', 'r') as f:
            self.config = yaml.safe_load(f)

        self.url_login: str = self.config['url_login']
        self.url_profile: str = self.config['url_profile']
        self.session = requests.Session()

    def login(self) -> Any:
        logging.info('Получение токена для входа')
        try:
            response = requests.post(self.url_login, data={"username": self.config['login_valid'],
                                                           "password": self.config['password_valid']})
            if response.status_code == 200:
                return response.json().get("token")
            else:
                error_message = ErrorReceivingToken(response.status_code)
                logging.exception(error_message)
        except Exception:
            error_message = ErrorEntranceInvalidUrl(self.url_login)
            logging.exception(error_message)

    def get_username(self, token: Any) -> Any:
        logging.info('Получение данных с сервера')
        try:
            url: str = self.url_profile
            headers: dict[str, Any] = {"X-Auth-Token": token}
            response = self.session.get(url, headers=headers)
            return response.json()['username']
        except Exception:
            error_message = ErrorReceivingPostRequest()
            logging.exception(error_message)
