import json
import logging
from config.config import abs_path
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class ValidateResponse:
    
    def validate_response(self, actual_response=None, endpoint=None):
        expected_response = self.read_input_data_json(f"{abs_path}/clickup_api/input_data/{endpoint}.json")
        if "body" in actual_response:
            self.validate_values(expected_response["status_code"], actual_response["status_code"], key_compare="status_code")
            self.validate_values(expected_response["response"]["body"], actual_response["body"], key_compare="body")
            self.validate_values(expected_response["headers"], actual_response["headers"], key_compare="headers")
            self.validate_values(expected_response["request"], actual_response["request"], key_compare="request")
            
    def validate_values(self, expected_value, actual_value, key_compare):
        """        
        """
        error_message = f"Error got: {actual_value}, expected {expected_value}"
        if key_compare == "body":
            if isinstance(actual_value, list):
                LOGGER.debug("Expected value: %s", expected_value)
                LOGGER.debug("Actual value: %s", actual_value)
                assert self.compare_json(expected_value[0], actual_value[0]), error_message
            else:
                LOGGER.debug("Expected value: %s", expected_value)
                LOGGER.debug("Actual value: %s", actual_value)
                assert self.compare_json(expected_value, actual_value), error_message
        elif key_compare == "headers":
            LOGGER.debug("Expected value: %s", expected_value)
            LOGGER.debug("Actual value: %s", actual_value)
            assert expected_value.items() <= actual_value.items(), error_message
        elif key_compare == "request":
            LOGGER.debug("Expected value: %s", expected_value)
            LOGGER.debug("Actual value: %s", actual_value)
            assert self.compare_json(expected_value, actual_value), error_message
        else:
            LOGGER.debug("Expected status: %s", expected_value)
            LOGGER.debug("Actual status: %s", actual_value)
            assert expected_value == actual_value, error_message
    
    @staticmethod
    def read_input_data_json(file_name):
        LOGGER.debug("Reading input data from file: %s", file_name)
        with open(file_name, encoding="utf8") as json_file:
            data = json.load(json_file)
        LOGGER.debug("Data read of %s is %s", file_name, data)
        json_file.close()
        return data
    
    @staticmethod
    def compare_json(json1, json2):
        """
        """
        for key in json1.keys():
            if key in json2:
                LOGGER.debug("Key %s found in json2", key)
            else:
                LOGGER.debug("Key %s not found in json2", key)
                return False
        return True
    
if __name__ == "__main__":
    v = ValidateResponse()
    v.validate_response()    
