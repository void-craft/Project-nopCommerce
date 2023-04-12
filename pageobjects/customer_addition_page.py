import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CustomerAddition:
    LINK_CUSTOMERS_MENU_XPATH = By.XPATH, "//a[@href='#']//span[contains(text(),'Customers')]"
    LINK_CUSTOMERS_MENU_ITEM_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    BUTTON_ADD_NEW_XPATH = (By.XPATH, "//a[@class='btn bg-blue']")

    TEXT_EMAIL_XPATH = (By.XPATH, "//input[@id='Email']")
    TEXT_PASSWORD_XPATH = (By.XPATH, "//input[@id='Password']")
    TEXT_FIRSTNAME_XPATH = (By.XPATH, "//input[@id='FirstName']")
    TEXT_LASTNAME_XPATH = (By.XPATH, "//input[@id='LastName']")
    RADIO_MALE_GENDER_ID = (By.ID, "Gender_Male")
    RADIO_FEMALE_GENDER_ID = (By.ID, "Gender_Female")
    TEXT_CUSTOMER_ROLES_XPATH = (By.XPATH, "//input[@id='FirstName']")
    LISTITEM_ADMINISTRATORS_XPATH = (By.XPATH, "//li[contains(text(),'Administrators')]")
    LISTITEM_REGISTERED_XPATH = (By.XPATH, "//li[contains(text(),'Registered')]")
    LISTITEM_GUESTS_XPATH = (By.XPATH, "//li[contains(text(),'Guests')]")
    LISTITEM_VENDOR_XPATH = (By.XPATH, "//li[contains(text(),'Vendors')]")

    DROPDOWN_MANAGER_OF_VENDOR_XPATH = (By.XPATH, "//*[@id='VendorId']")

    TEXT_DATE_OF_BIRTH_XPATH = (By.XPATH, "//input[@id='DateOfBirth']")
    TEXT_COMPANY_NAME_XPATH = (By.XPATH, "//input[@id='Company']")
    TEXT_ADMIN_COMMENT_ID = (By.ID, "AdminComment")
    BUTTON_SAVE_XPATH = "//button[@name='save']"

    def __init__(self, driver):
        self.list_item = None
        self.driver = driver

    def click_customers_menu(self):
        self.driver.find_element(*self.LINK_CUSTOMERS_MENU_XPATH).click()

    def click_customers_menu_item(self):
        self.driver.find_element(*self.LINK_CUSTOMERS_MENU_ITEM_XPATH).click()

    def click_add_new(self):
        self.driver.find_element(*self.BUTTON_ADD_NEW_XPATH).click()

    def set_email(self, email):
        self.driver.find_element(*self.TEXT_EMAIL_XPATH).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.TEXT_PASSWORD_XPATH).send_keys(password)

    def set_customer_roles(self, role):
        self.driver.find_element(*self.TEXT_CUSTOMER_ROLES_XPATH).click()
        time.sleep(3)
        if role == 'Registered':
            self.list_item = self.driver.find_element(*self.LISTITEM_REGISTERED_XPATH)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element(*self.LISTITEM_ADMINISTRATORS_XPATH)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_element(*self.LISTITEM_GUESTS_XPATH)
        elif role == 'Registered':
            self.list_item = self.driver.find_element(*self.LISTITEM_REGISTERED_XPATH)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element(*self.LISTITEM_VENDOR_XPATH)
        else:
            self.list_item = self.driver.find_element(*self.LISTITEM_GUESTS_XPATH)

        time.sleep(3)

        # self.list_item.click() if it is not working, use javascript like below

        self.driver.execute_script("arguments[0].click();", self.list_item)

    def set_manager_of_vendor(self, value):
        dropdown = Select(self.driver.find_element(self.DROPDOWN_MANAGER_OF_VENDOR_XPATH))
        dropdown.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(self.RADIO_MALE_GENDER_ID).click()
        elif gender == 'Female':
            self.driver.find_element(self.RADIO_FEMALE_GENDER_ID).click()
        else:
            self.driver.find_element(self.RADIO_MALE_GENDER_ID).click()

    def set_first_name(self, firstname):
        self.driver.find_element(self.TEXT_FIRSTNAME_XPATH).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(self.TEXT_LASTNAME_XPATH).send_keys(lastname)

    def set_dob(self, date_of_birth):
        self.driver.find_element(self.TEXT_DATE_OF_BIRTH_XPATH).send_keys(date_of_birth)

    def set_company_name(self, company_name):
        self.driver.find_element(self.TEXT_COMPANY_NAME_XPATH).send_keys(company_name)

    def set_admin_content(self, content):
        self.driver.find_element(self.TEXT_ADMIN_COMMENT_ID).send_keys(content)

    def click_save(self):
        self.driver.find_element(self.BUTTON_SAVE_XPATH).click()
