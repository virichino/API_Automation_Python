import logging
from config.config import URL
from helpers.res_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestComments:
    @classmethod
    def setup_class(cls):
        """
        Method to setup the project class
        """
        LOGGER.debug("Setup Class method")
        cls.list_comments=[]
        cls.url_comments = f"{URL["URL_TODO"]}comments"
        cls.rest_client = RestClient()

    def test_get_all_comments(self, create_tasks, log_test_name):
        """
        Test to get all comments
        """
        url_get_all_comments = f"{URL["URL_TODO"]}comments?task_id={create_tasks}"
        response = self.rest_client.request(method_name="get",url=url_get_all_comments)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
        
    def test_create_comment(self,create_tasks,log_test_name):
        """
        Test to create a comment
        """
        body_comment = {
            "task_id": f"{create_tasks}",
            "content": "Comment created from API"
        }
        response = self.rest_client.request(method_name="post", url=self.url_comments, body=body_comment)
        #to be deleted
        #id_comment_created = response["body"]["id"]
        #self.list_comments.append(id_comment_created)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"
        
    def test_delete_comment(self, create_comment ,log_test_name):
        """
        Test to delete a comment
        """
        id_comment_delete =  create_comment
        url_delete_comment = f"{self.url_comments}/{id_comment_delete}"
        response = self.rest_client.request(method_name="delete",url=url_delete_comment)
        assert response["status_code"] == 204, f"Error: {response["status_code"]}, expected 204"        

    def test_update_comment(self, create_comment, log_test_name):
        """
        Test to update a comment
        """
        id_comment_update = create_comment
        url_update_comment = f"{self.url_comments}/{id_comment_update}"
        body_update_comment = {
            "content": "Comment updated from API"
        }
        response = self.rest_client.request(method_name="post", url=url_update_comment, body=body_update_comment)
        assert response["status_code"] == 200, f"Error: {response["status_code"]}, expected 200"

