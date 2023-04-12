import pytest
from selenium import webdriver
from pageobjects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test001Login:
    BASEURL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()
    LOGGER = LogGen.log_gen()

    def test_homepage_title(self, setup):
        self.LOGGER.info("******** Test001Login ***********")
        self.LOGGER.info("******** Verifying Homepage Title ***********")
        self.driver = setup
        self.driver.get(self.BASEURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.LOGGER.info("******** Homepage Title Test Has Passed ***********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage_title.png")
            self.driver.close()
            self.LOGGER.error("******** Homepage Title Test Has Failed ***********")
            assert False

    def test_login(self, setup):
        self.LOGGER.info("******** Verifying Login Test ***********")
        self.driver = setup
        self.driver.get(self.BASEURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.USERNAME)
        self.login_page.set_password(self.PASSWORD)
        self.login_page.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.LOGGER.info("******** Login Test Has Passed ***********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.LOGGER.error("******** Login Test Has Failed ***********")
            assert False
