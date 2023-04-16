from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CustomerAddition(BasePage):
    LINK_CUSTOMERS_MENU_XPATH = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    # LINK_CUSTOMERS_MENU_ITEM_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p")
    LINK_CUSTOMERS_MENU_ITEM_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    BUTTON_ADD_NEW_XPATH = (By.XPATH, "//a[contains(.,'Add new')]")
    TEXT_EMAIL_XPATH = (By.XPATH, "//input[@id='Email']")
    TEXT_PASSWORD_XPATH = (By.XPATH, "//input[@id='Password']")
    TEXT_CUSTOMER_ROLES_XPATH = (By.XPATH, "//input[@class='k-input' and @role='listbox']")
    LISTITEM_ADMINISTRATORS_XPATH = (By.XPATH, "//li[contains(text(),'Administrators')]")
    LISTITEM_REGISTERED_XPATH = (By.XPATH, "//li[contains(text(),'Registered')]")
    LISTITEM_GUESTS_XPATH = (By.XPATH, "//li[contains(text(),'Guests')]")
    LISTITEM_VENDOR_XPATH = (By.XPATH, "//li[contains(text(),'Vendors')]")
    DROPDOWN_MANAGER_OF_VENDOR_XPATH = (By.XPATH, "//select[@id='VendorId']")
    RADIO_MALE_GENDER_ID = (By.ID, "Gender_Male")
    RADIO_FEMALE_GENDER_ID = (By.ID, "Gender_Female")
    TEXT_FIRSTNAME_XPATH = (By.XPATH, "//input[@id='FirstName']")
    TEXT_LASTNAME_XPATH = (By.XPATH, "//input[@id='LastName']")
    TEXT_DATE_OF_BIRTH_XPATH = (By.XPATH, "//input[@id='DateOfBirth']")
    TEXT_COMPANY_NAME_XPATH = (By.XPATH, "//input[@id='Company']")
    TEXT_ADMIN_COMMENT_ID = (By.ID, "AdminComment")
    BUTTON_SAVE_XPATH = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        super().__init__(driver)
        self.list_item = None
        self.driver = driver

    def click_customers_menu(self):
        self.click_element(self.LINK_CUSTOMERS_MENU_XPATH)

    def click_customers_menu_item(self):
        self.click_element(self.LINK_CUSTOMERS_MENU_ITEM_XPATH)

    def click_add_new(self):
        self.click_element(self.BUTTON_ADD_NEW_XPATH)

    def set_email(self):
        email = self.generate_random_email()
        self.clear_and_send_keys(self.TEXT_EMAIL_XPATH, email)

    def set_password(self):
        password = self.generate_random_password(8)
        self.clear_and_send_keys(self.TEXT_PASSWORD_XPATH, password)

    def set_customer_roles(self, role):
        self.click_element(self.TEXT_CUSTOMER_ROLES_XPATH)
        if role == 'Registered':
            self.list_item = self.wait_for_element(self.LISTITEM_REGISTERED_XPATH)
        elif role == 'Administrators':
            self.list_item = self.wait_for_element(self.LISTITEM_ADMINISTRATORS_XPATH)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest
            self.list_item = self.click_element((By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"))
            self.list_item = self.wait_for_element(self.LISTITEM_GUESTS_XPATH)
        elif role == 'Registered':
            self.list_item = self.wait_for_element(self.LISTITEM_REGISTERED_XPATH)
        elif role == 'Vendors':
            self.list_item = self.wait_for_element(self.LISTITEM_VENDOR_XPATH)
        else:
            self.list_item = self.wait_for_element(self.LISTITEM_GUESTS_XPATH)
        # self.list_item.click()  # if it is not working, use javascript like below
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def set_manager_of_vendor(self, value):
        self.click_element(self.DROPDOWN_MANAGER_OF_VENDOR_XPATH)
        self.select_dropdown_by_value(self.DROPDOWN_MANAGER_OF_VENDOR_XPATH, value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.click_element(self.RADIO_MALE_GENDER_ID)
        elif gender == 'Female':
            self.click_element(self.RADIO_FEMALE_GENDER_ID)
        else:
            self.click_element(self.RADIO_MALE_GENDER_ID)

    def set_first_name(self, firstname):
        self.clear_and_send_keys(self.TEXT_FIRSTNAME_XPATH, firstname)

    def set_last_name(self, lastname):
        self.clear_and_send_keys(self.TEXT_LASTNAME_XPATH, lastname)

    def set_dob(self, date_of_birth):
        self.clear_and_send_keys(self.TEXT_DATE_OF_BIRTH_XPATH, date_of_birth)

    def set_company_name(self, company_name):
        self.clear_and_send_keys(self.TEXT_COMPANY_NAME_XPATH, company_name)

    def set_admin_content(self, content):
        self.clear_and_send_keys(self.TEXT_ADMIN_COMMENT_ID, content)

    def click_save(self):
        self.click_element(self.BUTTON_SAVE_XPATH)
