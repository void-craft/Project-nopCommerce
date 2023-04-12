import pytest
import time
from pageobjects.login_page import LoginPage
from pageobjects.customer_addition_page import CustomerAddition
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
import string
import random


class Test003CustomerAddition:
    BASEURL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()
    LOGGER = LogGen.log_gen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.LOGGER.info("************* Test003CustomerAddition **********")
        self.driver = setup
        self.driver.get(self.BASEURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.USERNAME)
        self.lp.set_password(self.PASSWORD)
        self.lp.click_login()
        self.LOGGER.info("************* Login Successful **********")

        self.LOGGER.info("******* Starting Customer Addition Test **********")

        self.add_customer = CustomerAddition(self.driver)
        self.add_customer.click_customers_menu()
        self.add_customer.click_customers_menu_item()

        self.add_customer.click_add_new()

        self.LOGGER.info("************* Providing Customer Info **********")

        self.email = random_generator() + "@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("test123")
        self.add_customer.set_customer_roles("Guests")
        self.add_customer.set_manager_of_vendor("Vendor 2")
        self.add_customer.set_gender("Female")
        self.add_customer.set_first_name("Void")
        self.add_customer.set_last_name("Craft")
        self.add_customer.set_dob("2/03/2000")  # Format: D / MM / YYY
        self.add_customer.set_company_name("Void Crafter")
        self.add_customer.set_admin_content("This Is For Testing.........")
        self.add_customer.click_save()

        self.LOGGER.info("************* Saving Customer Info **********")

        self.LOGGER.info("********* Customer Addition Validation Started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.LOGGER.info("********* Customer Addition Test Passed *********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.LOGGER.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.LOGGER.info("******* Ending Customer Addition Test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

