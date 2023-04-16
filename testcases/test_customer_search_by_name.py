import pytest
from pageobjects.login_page import LoginPage
from pageobjects.customer_addition_page import CustomerAddition
from pageobjects.customer_search_page import CustomerSearch
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium import webdriver


class Test005CustomerSearchByName:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()
    LOGGER = LogGen.log_gen()

    @pytest.mark.regression
    def test_customer_search_by_name(self, setup):

        self.LOGGER.info("************* Test005CustomerSearchByName **********")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.USERNAME)
        self.login_page.set_password(self.PASSWORD)
        self.login_page.click_login()
        self.LOGGER.info("************* Login successful **********")

        self.LOGGER.info("******* Starting Customer Search By Name **********")

        self.add_customer = CustomerAddition(self.driver)
        self.add_customer.click_customers_menu()
        self.add_customer.click_customers_menu_item()

        self.LOGGER.info("************* Searching Customer by Name **********")

        search_customer = CustomerSearch(self.driver)
        search_customer.set_firstname("Victoria")
        search_customer.set_lastname("Terces")
        search_customer.click_search()
        status = search_customer.search_customer_by_name("Victoria Terces")
        self.driver.close()
        assert status
        self.LOGGER.info("***************  TestCase Test004CustomerSearchByName Is Complete *********** ")
