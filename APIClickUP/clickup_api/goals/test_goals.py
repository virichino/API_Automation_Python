
import logging

import pytest
from entities.common import Common
from helpers.res_client import RestClient
from utils.logger import get_logger
from config.config import HEADERS, URL
from helpers.validate_response import ValidateResponse
import allure

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.feature("Sections")
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
        common = Common()
        team_id = common.get_team_id()
        cls.url_with_team_goals = f"{cls.url_clickup}team/{team_id}/goal"         
        cls.user_id = common.get_user_id()
        cls.validate = ValidateResponse()
        
                                      
        cls.list_goals = []
          
    @allure.title("Test to get all goals")
    @allure.description("Method to get all goals")
    @allure.tag("CRUD")
    @allure.testcase("test_getAll_goals")
    @allure.issue("BUG-123")
    @pytest.mark.crud
    @pytest.mark.goals 
    def test_getAll_goals(self,create_goal,log_test_name):
        """
        Method to get all goals
        """        
        response = self.rest_client.request("get",url=self.url_with_team_goals)
        self.validate.validate_response(response, endpoint="get_all_goals")   

    @allure.title("Test to create a goals")
    @allure.description("Method to create all goals")
    @allure.tag("CRUD")
    @allure.testcase("test_create_goal")
    @pytest.mark.crud
    @pytest.mark.goals     
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
        response = self.rest_client.request("post", url=self.url_with_team_goals, json=body_goal)
        LOGGER.info("Response from create goal: %s", response["body"])
        id_goal_created = response["body"]["goal"]["id"]
        self.list_goals.append(id_goal_created)
        self.validate.validate_response(response, endpoint="create_goal")  
        

    @allure.title("Test to update a goal")
    @allure.description("Method to update a goals")
    @allure.tag("CRUD")
    @allure.testcase("test_update_goal")
    @pytest.mark.crud
    @pytest.mark.goals    
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
        response = self.rest_client.request("put", url=url_goal_update, json=body_goal)
        self.validate.validate_response(response, endpoint="update_goal")  
    
    @allure.title("Test to delete a goal")
    @allure.description("Method to delete a goals")
    @allure.tag("CRUD")
    @allure.testcase("test_deleteGoal")
    @pytest.mark.crud
    @pytest.mark.goals  
    def test_deleteGoal(self,create_goal,log_test_name):
        """
        Method to delete a goal
        """
        id_goal = create_goal["goal"]["id"]
        LOGGER.debug("ID goal to delete: %s", id_goal)
        url_goal_delete = f"{self.url_goals}/{id_goal}"
        response = self.rest_client.request('delete',url=url_goal_delete)
        self.validate.validate_response(response, endpoint="delete_goal") 
        
    @classmethod
    def teardown_class(cls):
        """
        Method to delete all the test data created
        """
        LOGGER.info("--------Teardown class---------")
        for id_goal in cls.list_goals:
            request = cls.rest_client.request('delete',url=f"{cls.url_goals}/{id_goal}")
            assert request["status_code"] == 200, f"Error: {request['status_code']}, expected 200"
