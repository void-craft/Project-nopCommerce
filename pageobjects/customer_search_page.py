from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CustomerSearch(BasePage):
    # Add customer Page
    TEXT_EMAIL_ID = (By.ID, "SearchEmail")
    TEXT_FIRSTNAME_ID = (By.ID, "SearchFirstName")
    TEXT_LASTNAME_ID = (By.ID, "SearchLastName")
    BUTTON_SEARCH_ID = (By.ID, "search-customers")
    TABLE_SEARCH_RESULTS_XPATH = (By.XPATH, "//table[@role='grid']")
    TABLE_TABLE_XPATH = (By.XPATH, "//table[@id='customers-grid']")
    TABLE_ROWS_XPATH = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    TABLE_COLUMNS_XPATH = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
    TEXT_CUSTOMER_ROLE_XPATH = (By.XPATH, "//input[@role='listbox']")
    LISTITEM_ADMINISTRATORS_XPATH = (By.XPATH, "//li[contains(text(),'Administrators')]")
    LISTITEM_REGISTERED_XPATH = (By.XPATH, "//li[contains(text(),'Registered')]")
    LISTITEM_GUESTS_XPATH = (By.XPATH, "//li[contains(text(),'Guests')]")
    LISTITEM_VENDOR_XPATH = (By.XPATH, "//li[contains(text(),'Vendors')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.list_item = None

    def set_customer_role(self, role):
        self.click_element(self.TEXT_CUSTOMER_ROLE_XPATH)
        if role == 'Registered':
            self.list_item = self.wait_for_element(self.LISTITEM_REGISTERED_XPATH)
        elif role == 'Administrators':
            self.list_item = self.wait_for_element(self.LISTITEM_ADMINISTRATORS_XPATH)
        elif role == 'Guests':
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

    def set_email(self, email):
        self.clear_and_send_keys(self.TEXT_EMAIL_ID, email)

    def set_firstname(self, firstname):
        self.clear_and_send_keys(self.TEXT_FIRSTNAME_ID, firstname)

    def set_lastname(self, lastname):
        self.clear_and_send_keys(self.TEXT_LASTNAME_ID, lastname)

    def click_search(self):
        self.click_element(self.BUTTON_SEARCH_ID)

    def get_number_of_rows(self):
        return len(self.wait_for_elements(self.TABLE_ROWS_XPATH))

    def get_no_of_columns(self):
        return len(self.wait_for_elements(self.TABLE_COLUMNS_XPATH))

    def search_customer_by_email(self, email):
        flag = False
        for row in range(1, self.get_number_of_rows()+1):
            table = self.wait_for_element(self.TABLE_TABLE_XPATH)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(row) + "]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, fullname):
        flag = False
        for row in range(1, self.get_number_of_rows()+1):
            table = self.wait_for_element(self.TABLE_TABLE_XPATH)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(row) + "]/td[3]").text
            if name == fullname:
                flag = True
                break
        return flag

    def search_customer_by_role(self, customer_role):
        flag = False
        for row in range(1, self.get_number_of_rows() + 1):
            table = self.wait_for_element(self.TABLE_TABLE_XPATH)
            role = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(row) + "]/td[4]").text
            if customer_role in role:
                flag = True
                break
        return flag
