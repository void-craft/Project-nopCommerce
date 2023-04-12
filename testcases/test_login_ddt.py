import time
import pytest
from selenium import webdriver
from pageobjects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import xlutils


class Test002DDTLogin:
    BASEURL = ReadConfig.get_application_url()
    PATH = ".//testdata/LoginData.xlsx"
    LOGGER = LogGen.log_gen()

    def test_login_ddt(self, setup):
        self.LOGGER.info("************ Test002DDTLogin *************")
        self.LOGGER.info("******** Verifying Login Test ***********")
        self.driver = setup
        self.driver.get(self.BASEURL)
        self.login_page = LoginPage(self.driver)

        self.rows = xlutils.get_row_count(self.PATH, 'Sheet1')
        print("Number of Rows in the Excel:", self.rows)
        list_status = []

        for row in range(2, self.rows+1):
            self.username = xlutils.read_data(self.PATH, 'Sheet1', row, 1)
            self.password = xlutils.read_data(self.PATH, 'Sheet1', row, 2)
            self.expected_result = xlutils.read_data(self.PATH, 'Sheet1', row, 3)

            self.login_page.set_username(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected_result == "Pass":
                    self.LOGGER.info("**** Passed *****")
                    self.login_page.click_logout()
                    list_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.LOGGER.error("**** Failed *****")
                    self.login_page.click_logout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.expected_result == "Pass":
                    self.LOGGER.error("**** Failed *****")
                    list_status.append("Fail")
                elif self.expected_result == "Fail":
                    self.LOGGER.info("**** Passed *****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.LOGGER.info("************* Login DDT Test Has Passed *************")
            self.driver.close()
            assert True
        else:
            self.LOGGER.error("************* Login DDT Test Has Failed *************")
            self.driver.close()
            assert False

        self.LOGGER.info("*********** End of Login DDT Test ***********")
        self.LOGGER.info("*********** Completed Test002DDTLogin ***********")

