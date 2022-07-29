from selenium.webdriver.common.by import By
from BOM.Locators.locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.emailTextBox = LoginPageLocators.emailTextBox
        self.passwordTextBox = LoginPageLocators.passwordTextBox
        self.submit = LoginPageLocators.submit

    def enter_Email(self, email):
        self.driver.find_element(By.NAME, value=self.emailTextBox).send_keys(email)

    def enter_Password(self, password):
        self.driver.find_element(By.NAME, value=self.passwordTextBox).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, value=self.submit).click()
