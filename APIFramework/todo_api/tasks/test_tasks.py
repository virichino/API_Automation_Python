import logging

import requests

from config.config import URL
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestTasks:
    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("Setup Class method")
        cls.url_tasks = f"{URL["URL_TODO"]}tasks"
        cls.list_tasks = []
        cls.rest_client = RestClient()

    def test_get_all_sections(self, log_test_name):
        """
        Test to get all sections
        """
        response = self.rest_client.request(method_name="get",url=self.url_tasks)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"


    def test_create_tasks(self, log_test_name):
        """
        Test to create a task
        """
        content_task_body = {
            "content": "Task created from API",
            "due_string": "2021-12-31",
            "due_lang": "en",
            "priority": 4
        }
        response = self.rest_client.request(method_name="post", url=self.url_tasks, body=content_task_body)
        #to be deleted
        id_section_created = response["body"]["id"]
        self.list_tasks.append(id_section_created)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"


    def test_update_section(self, create_tasks, log_test_name):
        """
        Test to update a Task
        """
        LOGGER.debug("Task ID to update: %s", create_tasks)
        body_section = {
            "content": "task updated from API"
        }
        url_task_update= f"{self.url_tasks}/{create_tasks}"
        response = self.rest_client.request(method_name="post", url=url_task_update, body=body_section)
        #to be deleted
        id_section_created = response["body"]["id"]
        #self.list_sections.append(id_section_created)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
    
    def test_delete_task(self, create_tasks, log_test_name):
        """
        Test to delete a task
        """
        url_task_delete = f"{self.url_tasks}/{create_tasks}"
        response = self.rest_client.request(method_name="delete", url=url_task_delete)
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"

    def test_close_task(self, create_tasks, log_test_name):
        """
        Test to close a task
        """
        url_task_close = f"{self.url_tasks}/{create_tasks}/close"
        response = self.rest_client.request(method_name="post", url=url_task_close)
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"
        
    def test_reopen_task(self, create_tasks, log_test_name):
        """
        Test to reopen a task
        """
        url_task_reopen = f"{self.url_tasks}/{create_tasks}/reopen"
        response = self.rest_client.request(method_name="post", url=url_task_reopen)
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"        

    @classmethod
    def teardown_class(cls):
        """
        Delete all the test data created
        """
        LOGGER.info("Cleanup sections...")
        for id_tasks in cls.list_tasks:
            response = cls.rest_client.request(method_name="delete",url=f"{cls.url_tasks}/{id_tasks}")
            LOGGER.info("Section ID deleted: %s", id_tasks)
            if response["status_code"] != 204:
                LOGGER.error("Section id deleted: %s", id_tasks)
