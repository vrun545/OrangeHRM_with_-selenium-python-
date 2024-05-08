import time

from selenium.webdriver.common.by import By

from helper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):

    email_WebElement = (By.XPATH, '//input[@name="username"]')
    password_WebElement = (By.XPATH, '//input[@name="password"]')
    loginBtn_WebElement = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.webElement_Enter(self.email_WebElement, username)
        self.webElement_Enter(self.password_WebElement, password)
        self.webElement_Click(self.loginBtn_WebElement)
        time.sleep(2)
