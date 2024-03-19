"""
curl -X 'POST' \
  'http://127.0.0.1:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=etaquichiri&password=phantom&scope=&client_id=&client_secret='
"""
import logging
import pytest
from config.config import URL,TIMEOUT
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestFastAPI:
    """
    Class to test get_logger method
    """
    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("SetupClass method")
        cls.list_projects = []
        cls.url_token = "http://127.0.0.1:8000/token"
        headers_fast_api = {
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
        }
        body_token = {
            "grant_type":"",
            "username":"etaquichiri",
            "password":"phantom",
            "scope":"",
            "client_secret=":""
        }
        cls.rest_client = RestClient(headers=headers_fast_api)
        response = cls.rest_client.request(method_name="post", url=cls.url_token, body=body_token)
        cls.access_token = response["body"]["access_token"]


    def test_token(self):
        """
        Method to get tokens
        """
        HEADERS_FAST_API = {
            "Authorization": f"Bearer {self.access_token}"
        }
        url_get_users = 'http://127.0.0.1:8000/users/me/'
        rest_client = RestClient(headers=HEADERS_FAST_API)
        response = rest_client.request(method_name="get", url=url_get_users)
        LOGGER.info("Response from get all users: %s", response["body"])
