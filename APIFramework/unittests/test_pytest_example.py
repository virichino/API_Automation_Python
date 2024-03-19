import logging
import sys
import pytest

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestPytestExample:
    """
    Class to test get_logger method
    """
    def setup_method(self):
        LOGGER.debug("Setup")

    @classmethod
    def setup_class(cls):
        LOGGER.debug("SetupClass")
    
    @classmethod
    def teardown_class(cls):
        LOGGER.debug("TearDownClass")

    def teardown_method(self):
        LOGGER.debug("TearDown")

    @pytest.mark.smoke
    def test_example_zero(self):
        LOGGER.debug("Test example zero")

    @pytest.mark.acceptance
    @pytest.mark.parametrize("name_parameter", ["one", "two", "three"])
    def test_example_one(self, fixture_example, name_parameter):
        LOGGER.debug("Test example one: %s", name_parameter)

    @pytest.mark.smoke
    #@pytest.mark.skip(reason="there is a bug related to the API: 123456")
    #@pytest.mark.skipif(sys.platform == "win32", reason="not executed on windows")
    def test_example_two(self, fixture_example):
        LOGGER.debug("Test example two: %s", fixture_example)
    