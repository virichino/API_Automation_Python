import logging
from helpers.res_client import RestClient
from utils.logger import get_logger
from config.config import URL
import pytest

LOGGER = get_logger(__name__, logging.DEBUG)

@pytest.fixture()
def create_project(request):
    LOGGER.debug("Create project fixture")
    environment = request.config.getoption("--env")
    LOGGER.warning("Environment selected: %s", environment)    

    body_project = {
            "name": "Project created from API 2"
        }
    url = f"{URL["URL_TODO"]}projects"
    rest_client = RestClient()
    response = rest_client.request(method_name="post",url=url,body=body_project)

    LOGGER.info("Fixture project created: %s", response["body"])
    project_id=response["body"]["id"]
    yield project_id
    delete_project(project_id, rest_client)

@pytest.fixture()
def get_project():
    LOGGER.debug("Get project fixture")
    url = f"{URL["URL_TODO"]}projects"
    rest_client = RestClient()
    response = rest_client.request(method_name="get",url=url)
    project_id = response["body"][0]["id"]
    return project_id

@pytest.fixture()
def create_section(create_project):

    LOGGER.debug("Create section fixture")

    body_section = {
        "project_id": f"{create_project}",
        "name": "Section from fixture"
    }
    url_section = URL["URL_TODO"]+"sections"
    rest_client = RestClient()
    response = rest_client.request("post", url_section, body=body_section)
    id_section_created = response["body"]["id"]
    return id_section_created

def delete_project(project_id, rest_client):
    LOGGER.debug("Clean up of project")
    url = f"{URL["URL_TODO"]}projects/{project_id}"
    response = rest_client.request(method_name="delete",url=url)
    LOGGER.info("Project deleted: %s", response["status_code"])
    assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"

@pytest.fixture()
def log_test_name(request):
    LOGGER.info("------------Test '%s' STARTED------------", request.node.name)   
    def fin():
        LOGGER.info("------------Test '%s' COMPLETED------------", request.node.name)
    request.addfinalizer(fin)

@pytest.fixture()
def create_tasks():
    """
    Test to create a task
    """
    content_task_body = {
        "content": "Task created from API",
        "due_string": "2021-12-31",
        "due_lang": "en",
        "priority": 4
    }
    rest_client = RestClient()
    url_tasks = f"{URL["URL_TODO"]}tasks"
    response = rest_client.request(method_name="post", url=url_tasks, body=content_task_body)
    #to be deleted
    
    assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
    return response["body"]["id"]

@pytest.fixture()
def create_comment(create_tasks):
    """
    Test to create a comment
    """
    body_comment = {
        "task_id": f"{create_tasks}",
        "content": "Comment created from API"
    }
    rest_client = RestClient()
    url_comments = f"{URL["URL_TODO"]}comments"
    response = rest_client.request(method_name="post", url=url_comments, body=body_comment)
    #to be deleted
    id_comment_created = response["body"]["id"]
    yield id_comment_created
    delete_comment(id_comment_created, rest_client)
    
def delete_comment(id_comment_delete, rest_client):
    """
    Test to delete a comment
    """
    url_comments = f"{URL["URL_TODO"]}comments/{id_comment_delete}"
    response = rest_client.request(method_name="delete",url=url_comments)
    if response["status_code"] == 204:
        LOGGER.info("Comment id: %s deleted", id_comment_delete)    

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment where the tests are eecuted")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to execute the UI tests")