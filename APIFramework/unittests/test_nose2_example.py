from nose2.tools import params
import unittest
import logging
import allure

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class testUnitTestExample(unittest.TestCase):

    def setUp(self):
        LOGGER.debug("Setup")

    @classmethod
    def setUpClass(cls):
        LOGGER.debug("SetupClass")

    def tearDown(self):
        LOGGER.debug("TearDown")

    @classmethod
    def tearDownClass(cls):
        LOGGER.debug("TearDownClass")

    def test_example_one(self):
        LOGGER.debug("Test example one")

    @allure.story("Test todo API")
    @params("name1", "name2", "name3")
    def test_example_two(self, name):
        LOGGER.debug("Test example two with name: %s", name)
    