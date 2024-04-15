"""
This module is used to make requests to the API
"""
import json as jsonSerializer
import logging
import requests
from config.config import HEADERS, URL
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class RestClient:
    """
    Class to make requests to the API
    """
    def __init__(self, headers=None):
        if headers is None:
            headers = HEADERS["HEADERS_CLICKUP"]
        self.session = requests.Session()
        self.session.headers.update(headers)

    def request(self, method_name, url, body=None, json=None):
        """
        Method to call to request methods
        :param method_name:     GET, POST, PUT, DELETE
        :param url:
        :param body:            body to use in request
        :param json:            json to use in request
        :return:
        """
        response_dict = {}
        try:
            response = self.select_method(method_name, self.session)(url=url, data=body, json=json)
            LOGGER.debug("Status Code : %s", response.status_code)
            LOGGER.debug("Response Content : %s", response.text)
            response.raise_for_status()
            if hasattr(response, "headers"):
                LOGGER.info("Response headers: %s", response.headers)
                response_dict["headers"] = response.headers
        except requests.exceptions.HTTPError as http_error:
            LOGGER.error("HTTP error: %s", http_error)
            response_dict["headers"] = response.headers
        except requests.exceptions.RequestException as request_error:
            LOGGER.error("Request error: %s", request_error)
            response_dict["headers"] = response.headers
        finally:
            if response.text:
                if response.ok:
                    response_dict["body"] = jsonSerializer.loads(response.text)
                else:
                    response_dict["body"] = {"msg": response.text}
            else:
                # case delete
                response_dict["body"] = {"msg": "No body content"}
            LOGGER.info("Status code: %s", response.status_code)
            response_dict["status_code"] = response.status_code
            response_dict["request"] = {
                "method": response.request.method,
                "url": (response.request.url).replace(URL["URL_CLICKUP"], "/"),
            }

        return response_dict

    @staticmethod
    def select_method(method_name, session):
        """
        Method to select the method to use in the request
        """
        methods = {
            "get": session.get,
            "post": session.post,
            "delete": session.delete,
            "put": session.put
        }
        return methods.get(method_name)
