import logging
from entities.common import Common
from helpers.res_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger
from config.config import HEADERS, URL
import allure

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.feature("Folders")
class TestFolders:
    
    @classmethod
    def setup_class(cls):
        """
        Method to setup the folder class
        """

        LOGGER.debug("SetupClass method")
        cls.url_clickup = URL["URL_CLICKUP"]
        cls.header_clickup = HEADERS["HEADERS_CLICKUP"]
        cls.url_user = f"{cls.url_clickup}user"        
        cls.url_folders = f"{cls.url_clickup}/folder"
        
        cls.rest_client = RestClient(cls.header_clickup)  
        common = Common()
        team_id = common.get_team_id()
        cls.url_with_team_folder = f"{cls.url_clickup}team/{team_id}/folder"         
        cls.user_id = common.get_user_id()
        cls.validate = ValidateResponse()
        
                                      
        cls.list_folders= []
        
    @allure.title("Test to get all folders")
    @allure.description("Method to get all folders")
    @allure.tag("CRUD")
    @allure.testcase("test_getAll_folders")     
    def test_getAll_folders(self,create_space,log_test_name):
        """
        Test to get all folders
        """
        space_id = create_space["body"]["id"]
        url_get_all_folders = f"{self.url_clickup}space/{space_id}/folder"
        response = self.rest_client.request("get",url=url_get_all_folders)
        self.validate.validate_response(response, endpoint="get_all_folders")         
        
    @allure.title("Test to create a folder")
    @allure.description("Method to update a folder")
    @allure.tag("CRUD")
    @allure.testcase("test_create_folder") 
    def test_create_folder(self,create_space,log_test_name):
        """
        Test to create a folder
        """
        space_id = create_space["body"]["id"]
        body_folder = {
            "name": "New Folder Name"
            }
        url_create_folder = f"{self.url_clickup}space/{space_id}/folder"
        response = self.rest_client.request("post", url=url_create_folder, json=body_folder)
        LOGGER.info("Response from create folder: %s", response["body"])
        id_folder_created = response["body"]["id"]
        self.list_folders.append(id_folder_created)
        self.validate.validate_response(response, endpoint="create_folder")   
    
    @allure.title("Test to update a folder")
    @allure.description("Method to update a folder")
    @allure.tag("CRUD")
    @allure.testcase("test_update_folder") 
    def test_update_folder(self,create_folder,log_test_name):
        """
        Test to update a folder
        """
        folder_id = create_folder["body"]["id"]
        body_folder = {
            "name": "New Folder Name Updated"
            }
        url_update_folder = f"{self.url_clickup}folder/{folder_id}"
        response = self.rest_client.request("put", url=url_update_folder, json=body_folder)
        LOGGER.info("Response from update folder: %s", response["body"])
        self.validate.validate_response(response, endpoint="update_folder")   

    @allure.title("Test to delete a folder")
    @allure.description("Method to delete a folder")
    @allure.tag("CRUD")
    @allure.testcase("test_delete_folder")         
    def test_delete_folder(self,create_folder,log_test_name):
        """
        Test to delete a folder
        """
        folder_id = create_folder["body"]["id"]
        url_delete_folder = f"{self.url_clickup}folder/{folder_id}"
        response = self.rest_client.request("delete", url=url_delete_folder)
        self.validate.validate_response(response, endpoint="delete_folder")          
        