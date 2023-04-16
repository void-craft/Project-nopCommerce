import pytest
from selenium.webdriver.common.by import By
from pageobjects.login_page import LoginPage
from pageobjects.customer_addition_page import CustomerAddition
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium import webdriver


class Test003CustomerAddition:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()
    LOGGER = LogGen.log_gen()  # Logger

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.LOGGER.info("************* Test003CustomerAddition **********")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
# login
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.USERNAME)
        self.login_page.set_password(self.PASSWORD)
        self.login_page.click_login()
        self.LOGGER.info("************* Login Successful **********")
# adding customer
        self.LOGGER.info("******* Starting Customer Addition Test **********")

        self.add_customer = CustomerAddition(self.driver)
        self.add_customer.click_customers_menu()
        self.add_customer.click_customers_menu_item()
        self.add_customer.click_add_new()

        self.LOGGER.info("************* Providing Customer Info **********")

        self.add_customer.set_email()
        self.add_customer.set_password()
        self.add_customer.set_first_name("Void")
        self.add_customer.set_last_name("Craft")
        self.add_customer.set_gender("Female")
        self.add_customer.set_dob("2/03/2000")
        self.add_customer.set_customer_roles("Guests")
        self.add_customer.set_manager_of_vendor("2")
        self.add_customer.set_company_name("Void Crafter")
        self.add_customer.set_admin_content("This Is For Testing.........")
        self.add_customer.click_save()

        self.LOGGER.info("************* Saving Customer Info **********")

        self.LOGGER.info("********* Customer Addition Validation Started *****************")

        self.message = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.message)
        if 'customer has been added successfully.' in self.message:
            assert True
            self.LOGGER.info("********* Customer Addition Test Passed *********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.LOGGER.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.LOGGER.info("******* Ending Customer Addition Test **********")
