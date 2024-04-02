import logging
from config.config import HEADERS, URL
from entities.common import Common
from entities.spaces import Spaces
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class Folder:
    def __init__(self, rest_client = None):
        self.url_clickup = URL["URL_CLICKUP"]
        self.header_clickup = HEADERS["HEADERS_CLICKUP"]       
        self.url_space = f"{self.url_clickup}/folder"
        self.common = Common()
        self.team_id = self.common.get_team_id()
        if rest_client is None:
            self.rest_client = RestClient()
    
    def create_folder(self):
        """
        Method to create a goal
        """
        space = Spaces()        
        url_clickup = URL["URL_CLICKUP"]
        space_id = space.create_space()["body"]["id"]
        body_folder = {
            "name": "New Folder Name"
            }
        rest_client = RestClient(headers=HEADERS["HEADERS_CLICKUP"])
        url_create_folder = f"{url_clickup}space/{space_id}/folder"
        request = rest_client.request("post", url=url_create_folder, json=body_folder)
        return request, space_id

    def delete_folder(self, goal_id):
        """
        Method to delete a goal
        """
        LOGGER.info("Clean up of goal")
        url = f"{URL["URL_CLICKUP"]}goal/{goal_id}"
        response = self.rest_client.request(method_name="delete",url=url)
        LOGGER.info("Goal deleted: %s", response["status_code"])
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"     
    