import logging
from config.config import URL
from helpers.res_client import RestClient
from utils.logger import get_logger
import datetime

LOGGER = get_logger(__name__, logging.DEBUG)

class Common:
    def __init__(self, rest_client = None):
       
        if rest_client is None:
            self.rest_client = RestClient()
    
    def get_team_id(self):
        """
        Method to get the team id
        """
        url_team = f"{URL["URL_CLICKUP"]}team"
        response = self.rest_client.request("get",url=url_team)
        LOGGER.info("Response from get team id: %s", response["body"])
        return response["body"]["teams"][0]["id"]

    def get_user_id(self):
        """
        Method to get the user id
        """
        url_user = f"{URL["URL_CLICKUP"]}user"
        response = self.rest_client.request("get",url=url_user)
        LOGGER.info("Response from get user id: %s", response["body"])
        return response["body"]["user"]["id"]
    
    def get_date(self, days = 0):
        """
        Method to get the date
        """
        return datetime.datetime.now() + datetime.timedelta(days=days)