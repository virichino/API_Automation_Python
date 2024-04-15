"""
Module to manage goals in ClickUp
"""
import logging
from config.config import HEADERS, URL
from entities.common import Common
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class Goals:
    """
    Class to manage goals in ClickUp
    """
    def __init__(self, rest_client = None):
        self.url_clickup = URL["URL_CLICKUP"]
        self.header_clickup = HEADERS["HEADERS_CLICKUP"]
        self.url_space = f"{self.url_clickup}/goal"
        self.common = Common()
        self.team_id = self.common.get_team_id()
        if rest_client is None:
            self.rest_client = RestClient()

    def create_goal(self):
        """
        Method to create a goal
        """
        rest_client = RestClient(headers=HEADERS["HEADERS_CLICKUP"])
        common = Common()
        team_id = common.get_team_id()
        user_id = common.get_user_id()
        url_goals = f"{URL['URL_CLICKUP']}team/{team_id}/goal"
        body_goal = {
            "name": "Goal Name Fixture 1",
            "due_date": 1568036964079,
            "description": "Goal Description",
            "multiple_owners": True,
            "owners": [
                user_id
            ],
            "color": "#32a852"
        }
        response = rest_client.request("post",url=url_goals, json=body_goal)
        return response

    def delete_goal(self, goal_id):
        """
        Method to delete a goal
        """
        LOGGER.info("Clean up of goal")
        url = f"{URL['URL_CLICKUP']}goal/{goal_id}"
        response = self.rest_client.request(method_name="delete",url=url)
        LOGGER.info("Goal deleted: %s", response["status_code"])
        assert response["status_code"] == 200, f"Error: {response['status_code']}, expected 204"
