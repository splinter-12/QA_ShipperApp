from selenium.webdriver.common.by import By
from BOM.Locators.locators import LoginPageLocators


class forgetPassword:
    def __init__(self, driver):    
        self.driver = driver   
        self.cancel = LoginPageLocators.cancel
        self.ForgotPasswordEmail = LoginPageLocators.ForgotPasswordEmail
        self.ForgotPassword = LoginPageLocators.ForgotPassword
        self.emailTextBox = LoginPageLocators.emailTextBox
        self.submitEmail = LoginPageLocators.submitEmail
  
    def click_ForgotPassword(self):
        self.driver.find_element(By.ID, value=self.ForgotPassword).click()

    def enter_theEmail(self, Email):
        self.driver.find_element(By.NAME, value=self.ForgotPasswordEmail).send_keys(Email)

    def submit_theEmail(self):
        self.driver.find_element(By.ID, value=self.submitEmail).click()

    def cancel_operation(self):
        self.driver.find_element(By.ID, value=self.cancel).click()
        
        
