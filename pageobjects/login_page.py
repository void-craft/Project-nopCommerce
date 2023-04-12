from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    TEXT_USERNAME_ID = (By.ID, "Email")
    TEXT_PASSWORD_ID = (By.ID, "Password")
    BUTTON_LOGIN_XPATH = (By.XPATH, "//button[text()='Log in']")
    LINK_LOGOUT_LINKTEXT = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        element = self.driver.find_element(*self.TEXT_USERNAME_ID)
        element.clear()
        element.send_keys(username)

    def set_password(self, password):
        element = self.driver.find_element(*self.TEXT_PASSWORD_ID)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.BUTTON_LOGIN_XPATH).click()

    def click_logout(self):
        self.driver.find_element(*self.LINK_LOGOUT_LINKTEXT).click()
