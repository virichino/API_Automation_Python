
import logging

import requests
from helpers.res_client import RestClient
from utils.logger import get_logger
from config.config import HEADERS, TIMEOUT, URL

LOGGER = get_logger(__name__, logging.DEBUG)
class TestGoals:

    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("SetupClass method")
        cls.url_clickup = URL["URL_CLICKUP"]
        cls.header_clickup = HEADERS["HEADERS_CLICKUP"]
        cls.url_user = f"{cls.url_clickup}user"        
        cls.url_goals = f"{cls.url_clickup}/goal"
        
        cls.rest_client = RestClient(cls.header_clickup)  
        request = cls.rest_client.request("get",f"{cls.url_clickup}team/")        
        team_id = request["body"]["teams"][0]["id"]
        cls.url_with_team_goals = f"{cls.url_clickup}team/{team_id}/goal" 
        
        response = cls.rest_client.request("get",url=cls.url_user)
        cls.user_id = response["body"]["user"]["id"] 
                                
        cls.list_goals = []

    def test_getAll_goals(self,create_goal,log_test_name):
        """
        Method to get all goals
        """        
        request = self.rest_client.request("get",url=self.url_with_team_goals)
        assert request["status_code"] == 200, f"Error: {request["status_code"]}, expected 200"

    def test_create_goal(self,log_test_name):
        """
        Method to create a goal
        """
        body_goal = {
            "name": "Goal Name1",
            "due_date": 1568036964079,
            "description": "Goal Description",
            "multiple_owners": True,
            "owners": [
                self.user_id
            ],
            "color": "#32a852"
        }
        request = self.rest_client.request("post", url=self.url_with_team_goals, json=body_goal)
        LOGGER.info("Response from create goal: %s", request["body"])
        id_goal_created = request["body"]["goal"]["id"]
        self.list_goals.append(id_goal_created)
        assert request["status_code"] == 200, f"Error: {request["status_code"]}, expected 200"

    def test_update_goal(self,create_goal,log_test_name):
        """
        Method to update a goal
        """
        id_goal = create_goal["goal"]["id"]
        LOGGER.debug("ID goal to update: %s", id_goal)
        url_goal_update = f"{self.url_goals}/{id_goal}"
        body_goal = {
            "name": "Goal Name Updated",
            "due_date": 1568036964079,
            "description": "Goal Description Updated",
            "multiple_owners": True,
            "rem_owners": [
                self.user_id
            ],
            "add_owners": [
                self.user_id
            ],
            "color": "#32a852"
        }
        request = self.rest_client.request("get", url=url_goal_update, json=body_goal)
        assert request["status_code"] == 200, f"Error: {request["status_code"]}, expected 200"
    
    def test_deleteGoal(self,create_goal,log_test_name):
        """
        Method to delete a goal
        """
        id_goal = create_goal["goal"]["id"]
        LOGGER.debug("ID goal to delete: %s", id_goal)
        url_goal_delete = f"{self.url_goals}/{id_goal}"
        request = self.rest_client.request('delete',url=url_goal_delete)
        assert request["status_code"] == 200, f"Error: {request["status_code"]}, expected 200"
        
    @classmethod
    def teardown_class(cls):
        """
        Method to delete all the test data created
        """
        LOGGER.info("--------Teardown class---------")
        for id_goal in cls.list_goals:
            request = cls.rest_client.request('delete',url=f"{cls.url_goals}/{id_goal}")
            assert request["status_code"] == 200, f"Error: {request["status_code"]}, expected 200"
