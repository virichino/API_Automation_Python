import logging
from dotenv import load_dotenv
import pytest
from entities.folder import Folder
from entities.goals import Goals
from entities.spaces import Spaces
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

load_dotenv()

@pytest.fixture()
def create_goal(request):
    """
    Method to create a goal as precondition
    """
    goal = Goals()
    goal_created = goal.create_goal()
    LOGGER.info("Response from create goal: %s", goal_created["body"])
    
     # Conditionally execute the teardown based on the test name
    if request.function.__name__ != "test_deleteGoal":
        yield goal_created["body"]
        goal.delete_goal(goal_created["body"]["goal"]["id"])
    else:
        yield goal_created["body"]  # Skip the teardown
                    

@pytest.fixture()
def log_test_name(request):
    """
    Method to get logs for the test
    """
    LOGGER.info("------------Test '%s' STARTED------------", request.node.name)   
    def fin():
        LOGGER.info("------------Test '%s' COMPLETED------------", request.node.name)
    request.addfinalizer(fin)

@pytest.fixture()
def create_space():
    """
    Test to create a space
    """        
    space = Spaces()
    space_id = space.create_space()
    yield space_id
    space.delete_space(space_id["body"]["id"])
    
@pytest.fixture()
def create_folder():
    """
    Test to create a folder
    """
    folder = Folder()
    space = Spaces()
    folder_created, space_created = folder.create_folder()
    yield folder_created
    space.delete_space(space_created)

@pytest.fixture()
def delete_list_spaces(request):
    """
    Test to delete a space
    """
    space = Spaces()
    yield space.delete_list_spaces
    
    
def pytest_addoption(parser):
    parser.addoption("--envCly", action="store", default="dev", help="Environment where the tests are eecuted")
    parser.addoption("--browserWeb", action="store", default="chrome", help="Browser to execute the UI tests")