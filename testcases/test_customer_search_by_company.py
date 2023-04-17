import time

import pytest
from pageobjects.login_page import LoginPage
from pageobjects.customer_addition_page import CustomerAddition
from pageobjects.customer_search_page import CustomerSearch
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium import webdriver


class Test007CustomerSearchByCompany:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()
    LOGGER = LogGen.log_gen()

    @pytest.mark.regression
    def test_customer_search_by_company(self, setup):

        self.LOGGER.info("************* Test007CustomerSearchByCompany **********")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.USERNAME)
        self.login_page.set_password(self.PASSWORD)
        self.login_page.click_login()
        self.LOGGER.info("************* Login successful **********")

        self.LOGGER.info("******* Starting Customer Search By Company **********")

        self.add_customer = CustomerAddition(self.driver)
        self.add_customer.click_customers_menu()
        self.add_customer.click_customers_menu_item()

        self.LOGGER.info("************* Searching Customer by Company **********")

        search_customer = CustomerSearch(self.driver)
        search_customer.set_customer_company("Test Company")
        search_customer.click_search()
        time.sleep(5)
        status = search_customer.search_customer_by_company("Test Company")
        self.driver.close()
        assert status

        self.LOGGER.info("***************  TestCase Test007CustomerSearchByCompany Is Complete *********** ")
