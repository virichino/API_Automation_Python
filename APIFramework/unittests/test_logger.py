"""
(c) Copyright Jalasoft. 2024

test_logger.py
    test the configuration of logger file and get logger method
"""
import logging
import unittest

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestLogger(unittest.TestCase):
    """
    Class to test get_logger method
    """
    def test_logger(self):
        """
        Method to test logging levels
        """
        LOGGER.debug("This is a debug message")
        LOGGER.info("This is an info message")
        LOGGER.warning("This is a warning message")
        LOGGER.error("This is an error message")
        LOGGER.critical("This is a critical message")
