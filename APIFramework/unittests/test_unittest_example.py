import unittest
import logging

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

    def test_example_two(self):
        LOGGER.debug("Test example two")
    