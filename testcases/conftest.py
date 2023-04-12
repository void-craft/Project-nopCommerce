from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...............")
    else:
        driver = webdriver.Edge()
        print("Launching default browser(Edge)................")
    return driver


def pytest_addoption(parser):     # Gets the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):    # Returns the browser value to set up method
    return request.config.getoption("--browser")


# Pytest HTML report

# Hook for adding Environment infor to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'Hema Priya'

# Hook for deleting, modifying Environment info from HTML report


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
