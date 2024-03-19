import logging
from utils.logger import get_logger
import pytest

LOGGER = get_logger(__name__, logging.DEBUG)

@pytest.fixture()
def fixture_example(request):
    LOGGER.debug("Fixture example")
    environment = request.config.getoption("--env")
    LOGGER.warning("Environment selected: %s", environment)    
    return environment

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment where the tests are eecuted")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to execute the UI tests")