from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class LoginPage(BasePage):
    TEXT_USERNAME_ID = By.ID, "Email"
    TEXT_PASSWORD_ID = By.ID, "Password"
    BUTTON_LOGIN_XPATH = By.XPATH, "//button[text()='Log in']"
    LINK_LOGOUT_LINKTEXT = By.LINK_TEXT, "Logout"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_username(self, username):
        self.clear_and_send_keys(self.TEXT_USERNAME_ID, username)

    def set_password(self, password):
        self.clear_and_send_keys(self.TEXT_PASSWORD_ID, password)

    def click_login(self):
        self.click_element(self.BUTTON_LOGIN_XPATH)

    def click_logout(self):
        self.click_element(self.LINK_LOGOUT_LINKTEXT)
