import logging
from config.config import HEADERS, URL
from entities.common import Common
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class Spaces:
    def __init__(self, rest_client = None):
        self.url_clickup = URL["URL_CLICKUP"]
        self.header_clickup = HEADERS["HEADERS_CLICKUP"]       
        self.url_space = f"{self.url_clickup}/space"
        self.common = Common()
        self.team_id = self.common.get_team_id()
        if rest_client is None:
            self.rest_client = RestClient()
    
    def create_space(self):
        """
        Method to create an space
        """
        body_space = {
        "name": f"New Space Create By API as precondition {self.common.get_date()}",
        "multiple_assignees": True,
        "features": {
            "due_dates": {
            "enabled": True,
            "start_date": False,
            "remap_due_dates": True,
            "remap_closed_due_date": False
            },
            "time_tracking": {
            "enabled": False
            },
            "tags": {
            "enabled": True
            },
            "time_estimates": {
            "enabled": True
            },
            "checklists": {
            "enabled": True
            },
            "custom_fields": {
            "enabled": True
            },
            "remap_dependencies": {
            "enabled": True
            },
            "dependency_warning": {
            "enabled": True
            },
            "portfolios": {
            "enabled": True
            }
        }
        }
        url_create_space = f"{self.url_clickup}team/{self.team_id}/space"
        response = self.rest_client.request("post", url=url_create_space, json=body_space)
        LOGGER.info("Response from create space: %s", response["body"])
        return response

    def delete_space(self, created_space_id):
        """
        Method to delete an space
        """
        LOGGER.debug("ID space to delete: %s", created_space_id)
        url_space_delete = f"{self.url_space}/{created_space_id}"
        response = self.rest_client.request("delete", url=url_space_delete)
        return response
    
    def delete_list_spaces(self, list_spaces):
        """
        Method to delete a list of spaces
        """
        LOGGER.debug("TeardownClass method")
        for id_space in list_spaces:
            response = self.rest_client.request("delete", url=f"{self.url_space}/{id_space}")
            # cls.delete_space(id_space)
            if response["status_code"] != 204:
                LOGGER.info("Section id deleted: %s", id_space)  
    