import logging
from dotenv import load_dotenv
import pytest
import requests
from config.config import HEADERS, TIMEOUT, URL

from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

load_dotenv()

@pytest.fixture()
def create_goal(request):
    """
    Method to create a goal as precondition
    """
    LOGGER.info("Create goal fixture")
    rest_client = RestClient(headers=HEADERS["HEADERS_CLICKUP"])
    team_id = get_team_id(rest_client)
    user_id = get_user_id(rest_client)
    url_goals = f"{URL["URL_CLICKUP"]}team/{team_id}/goal"
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
    LOGGER.info("Response from create goal: %s", response["body"])
    
     # Conditionally execute the teardown based on the test name
    if request.function.__name__ != "test_deleteGoal":
        yield response["body"]
        delete_goal(response["body"]["goal"]["id"], rest_client)
    else:
        yield response["body"]  # Skip the teardown
    
    
                
def delete_goal(goal_id, rest_client):
    """
    Method to delete a goal
    """
    LOGGER.info("Clean up of goal")
    url = f"{URL["URL_CLICKUP"]}goal/{goal_id}"
    response = rest_client.request(method_name="delete",url=url)
    LOGGER.info("Goal deleted: %s", response["status_code"])
    assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"

def get_team_id(requests):
    """
    Method to get the team id
    """
    url_team = f"{URL["URL_CLICKUP"]}team"
    response = requests.request("get",url=url_team)
    LOGGER.info("Response from get team id: %s", response["body"])
    return response["body"]["teams"][0]["id"]

def get_user_id(requests):
    """
    Method to get the user id
    """
    url_user = f"{URL["URL_CLICKUP"]}user"
    response = requests.request("get",url=url_user)
    LOGGER.info("Response from get user id: %s", response["body"])
    return response["body"]["user"]["id"]

@pytest.fixture()
def log_test_name(request):
    LOGGER.info("------------Test '%s' STARTED------------", request.node.name)   
    def fin():
        LOGGER.info("------------Test '%s' COMPLETED------------", request.node.name)
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--envCly", action="store", default="dev", help="Environment where the tests are eecuted")
    parser.addoption("--browserWeb", action="store", default="chrome", help="Browser to execute the UI tests")