import logging

import requests

from config.config import URL
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestSections:
    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("Setup Class method")
        cls.url_sections = f"{URL["URL_TODO"]}sections"
        cls.list_sections = []
        cls.rest_client = RestClient()

    def test_get_all_sections(self, create_project, log_test_name):
        """
        Test to get all sections
        """
        url_get_all_sections = f"{URL["URL_TODO"]}sections?project_id={create_project}"
        response = self.rest_client.request(method_name="get",url=url_get_all_sections)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"


    def test_create_section(self,create_project, log_test_name):
        """
        Test to create a section
        """
        body_section = {
            "name": "Section created from API",
            "project_id": create_project
        }
        response = self.rest_client.request(method_name="post", url=self.url_sections, body=body_section)
        #to be deleted
        id_section_created = response["body"]["id"]
        self.list_sections.append(id_section_created)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"


    
    def test_update_section(self, create_section, log_test_name):
        """
        Test to update a section
        """
        id_section_update = create_section
        LOGGER.debug("Section ID to update: %s", id_section_update)
        body_section = {
            "name": "Section updated from API"
        }
        url_sections_update= f"{self.url_sections}/{id_section_update}"
        response = self.rest_client.request(method_name="post", url=url_sections_update, body=body_section)
        #to be deleted
        id_section_created = response["body"]["id"]
        self.list_sections.append(id_section_created)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
    
    def test_delete_section(self, create_section, log_test_name):
        """
        Test to delete a section
        """
        id_section = create_section
        url_sections_delete = f"{self.url_sections}/{id_section}"
        response = self.rest_client.request(method_name="delete", url=url_sections_delete)
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"


    @classmethod
    def teardown_class(cls):
        """
        Delete all the test data created
        """
        LOGGER.info("Cleanup sections...")
        for id_section in cls.list_sections:
            response = cls.rest_client.request(method_name="delete",url=f"{cls.url_sections}/{id_section}")
            LOGGER.info("Section ID deleted: %s", id_section)
            if response["status_code"] != 204:
                LOGGER.error("Section id deleted: %s", id_section)
