"""
(c) Copyright Jalasoft. 2024

test_logger.py
    test the configuration of logger file and get logger method
"""
import logging
import pytest
from config.config import URL
from helpers.res_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestProjects:
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
        cls.url_projects = f"{URL["URL_TODO"]}projects"
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @classmethod
    def teardown_class(cls):
        """
        Delete all the test created
        """
        LOGGER.info("Cleanup projects...")
        for id_project in cls.list_projects:
            url_delete_project = f"{cls.url_projects}/{id_project}"
            response = cls.rest_client.request("delete", url=url_delete_project)
            if response["status_code"] == 204:
                LOGGER.info("Project ID deleted: %s", id_project)
       
    @pytest.mark.projects
    def test_get_all_projects(self, log_test_name):
        """
        Method to get all projects
        """
        response = self.rest_client.request(method_name="get", url=self.url_projects)          
        self.validate.validate_response(response, endpoint="get_all_projects")      
        #assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"

    def test_create_project(self, log_test_name):
        """
        Method to create a project
        """
        body_project = {
            "name": "Project created from API 2"
        }
        response = self.rest_client.request(method_name="post", url=self.url_projects, body=body_project)
        id_project_created = response["body"]["id"]
        self.list_projects.append(id_project_created)
        self.validate.validate_response(response, endpoint="create_project")
        #assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"

    def test_delete_project(self, create_project, log_test_name):
        """
        Method to delete a project
        """
        id_project = create_project
        url_todo = f"{self.url_projects}/{create_project}"
        response = self.rest_client.request(method_name="delete", url=url_todo) 
        self.validate.validate_response(response, endpoint="delete_project")    
        #assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"

    def test_update_project(self, create_project, log_test_name):
        """
        Method to update a project
        """
        id_project = create_project
        LOGGER.debug("ID project to update: %s", id_project)
        url_todo_update = f"{self.url_projects}/{id_project}"
        body_project = {
            "name": "Project updated from API"
        }
        response = self.rest_client.request(method_name="post", url=url_todo_update, body=body_project)
        #add to a list of projects to be deleted
        self.list_projects.append(id_project)
        self.validate.validate_response(response, endpoint="update_project")    
        #assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
