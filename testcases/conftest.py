"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
        
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()


# Pytest HTML report
# Hook for adding Environment infor to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hema Priya'


@pytest.hookimpl(optionalhook=True)  # Hook for deleting, modifying Environment info from HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Alternative setup/clear fixture

# from selenium import webdriver
# import pytest


# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome Browser...............")
#     else:
#         driver = webdriver.Edge()
#         print("Launching default browser(Edge)................")
#     return driver

# def pytest_addoption(parser):  # This will get the value from CLI /hooks
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):  # Returns the browser value to set up method
#     return request.config.getoption("--browser")
