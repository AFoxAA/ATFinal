import logging
import pytest
from base_actions import RestAPI
from testing_exceptions import ErrorApi


def test_positive_restapi_correct_username(get_username_restapi: str, expected_username: str) -> None:
    logging.info(get_username_restapi)
    api_client = RestAPI()
    token = api_client.login()
    posts = api_client.get_username(token)

    try:
        assert expected_username == posts, (
            logging.exception(f'username "{expected_username}" не найдено в списке предложенных'))
    except Exception:
        error_message = ErrorApi()
        logging.exception(f'{error_message}')
        raise


if __name__ == '__main__':
    pytest.main(['-vv'])
