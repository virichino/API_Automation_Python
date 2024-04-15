"""
Module to test the spaces endpoints
"""
import logging
import pytest
import allure
from config.config import MAX_SPACES, URL, HEADERS
from entities.common import Common
from helpers.res_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger


LOGGER = get_logger(__name__, logging.DEBUG)

@allure.feature("Spaces")
class TestSpaces:
    """
    Class to test the spaces endpoint
    """
    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("SetupClass method")
        cls.url_clickup = URL["URL_CLICKUP"]
        cls.header_clickup = HEADERS["HEADERS_CLICKUP"]
        cls.url_space = f"{cls.url_clickup}/space"
        cls.common = Common()
        cls.team_id = cls.common.get_team_id()
        cls.url_with_team_space = f"{cls.url_clickup}team/{cls.team_id}/space"
        cls.user_id = cls.common.get_user_id()
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.list_spaces = []

    @allure.title("Test to get all spaces")
    @allure.description("Method to get all spaces")
    @allure.tag("CRUD")
    @allure.testcase("test_get_all_spaces")
    @pytest.mark.crud
    @pytest.mark.spaces
    def test_get_all_spaces(self, log_test_name):  # pylint: disable=unused-argument
        """
        Test to get all spaces
        """
        url_get_all_spaces = f"{self.url_clickup}team/{self.team_id}/space"
        response = self.rest_client.request("get", url=url_get_all_spaces)
        self.validate.validate_response(response, endpoint="get_all_spaces")

    @allure.title("Test to create a space")
    @allure.description("Method to update a space")
    @allure.tag("CRUD")
    @allure.testcase("test_create_space")
    @pytest.mark.crud
    @pytest.mark.spaces
    def test_create_space(self,log_test_name): # pylint: disable=unused-argument
        """
        Test to create a space
        """
        body_space = {
        "name": f"New Space Create By API {self.common.get_date()}",
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
        id_space_created = response["body"]["id"]
        self.list_spaces.append(id_space_created)
        self.validate.validate_response(response, endpoint="create_space")

    @allure.title("Test to update a space")
    @allure.description("Method to update a space")
    @allure.tag("CRUD")
    @allure.testcase("test_update_space")
    @pytest.mark.crud
    @pytest.mark.spaces
    def test_update_space(self, create_space, log_test_name):  # pylint: disable=unused-argument
        """
        Test to update a space
        """
        id_space = create_space["body"]["id"]
        LOGGER.debug("ID space to update: %s", id_space)
        url_space_update = f"{self.url_space}/{id_space}"
        body_space = {
            "name": f"Space Name Updated {self.common.get_date()}",
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
                }
            }
        }
        response = self.rest_client.request("put", url=url_space_update, json=body_space)
        self.list_spaces.append(id_space)
        self.validate.validate_response(response, endpoint="create_space")

    @allure.title("Test to delete a space")
    @allure.description("Method to delete a space")
    @allure.tag("CRUD")
    @allure.testcase("test_delete_space")
    @pytest.mark.crud
    @pytest.mark.spaces
    def test_delete_space(self, create_space, log_test_name):  # pylint: disable=unused-argument
        """
        Test to delete a space
        """
        id_space = create_space["body"]["id"]
        LOGGER.debug("ID space to delete: %s", id_space)
        url_space_delete = f"{self.url_space}/{id_space}"
        response = self.rest_client.request("delete", url=url_space_delete)
        self.validate.validate_response(response, endpoint="delete_space")

    @allure.title("Test to create the limit of spaces")
    @allure.description("Test to verify the quantity of spaces available to create for a free account")
    @allure.tag("FUNCTIONAL")
    @allure.testcase("test_create_space")
    @pytest.mark.functional
    @pytest.mark.spaces
    def test_create_max_number_of_space(self,delete_list_spaces,log_test_name):  # pylint: disable=unused-argument
        """
        Test to create a space
        """
        url_create_space = f"{self.url_clickup}team/{self.team_id}/space"
        for index in range(0, MAX_SPACES):
            body_space = {
                "name": f"New Space Create By API {index}",
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
            response = self.rest_client.request("post", url=url_create_space, json=body_space)
            LOGGER.info("Response from create space: %s", response["body"])
            id_space_created = response["body"]["id"]
            self.list_spaces.append(id_space_created)
            self.validate.validate_response(response, endpoint="create_space")

        body_last_space = {
                "name": f"New Space Create By API {self.common.get_date()}",
                "multiple_assignees": True,
                "features": {
                    "due_dates": {
                    "enabled": True,
                    "start_date": False,
                    "remap_due_dates": True,
                    "remap_closed_due_date": False
                    }
                }
            }
        response = self.rest_client.request("post", url=url_create_space, json=body_last_space)
        delete_list_spaces(self.list_spaces)
        self.validate.validate_response(response, endpoint="create_max_quantity_of_spaces")

    @allure.title("Test to verify that a space cannot have repeated names")
    @allure.description("Test to verify that a space cannot have repeated names")
    @allure.tag("FUNCTIONAL")
    @allure.testcase("test_create_space_with_same_name")
    @pytest.mark.functional
    @pytest.mark.spaces
    def test_create_space_with_same_name(self, delete_list_spaces, log_test_name):  # pylint: disable=unused-argument
        """
        Test to verify if a space with the same name can be created
        """
        body_last_space = {
            "name": "New Space Create By API",
            "multiple_assignees": True,
            "features": {
                "due_dates": {
                "enabled": True,
                "start_date": False,
                "remap_due_dates": True,
                "remap_closed_due_date": False
                }
            }
        }
        response = self.rest_client.request("post", url=self.url_with_team_space, json=body_last_space)
        LOGGER.info("Response from create space: %s", response["body"])
        id_space_created = response["body"]["id"]
        self.list_spaces.append(id_space_created)
        self.validate.validate_response(response, endpoint="create_space")
        response = self.rest_client.request("post", url=self.url_with_team_space, json=body_last_space)
        delete_list_spaces(self.list_spaces)
        self.validate.validate_response(response, endpoint="create_space_with_same_name")

    def teardown_method(self):
        """
        Method to teardown the project class
        """
        LOGGER.debug("TeardownClass method")
        for id_space in self.list_spaces:
            response = self.rest_client.request("delete", url=f"{self.url_space}/{id_space}")
            # cls.delete_space(id_space)
            if response["status_code"] != 204:
                LOGGER.info("Section id deleted: %s", id_space)
