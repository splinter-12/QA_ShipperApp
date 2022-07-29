from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import sys
sys.path.append("locators")
sys.path.append("pages")
from locators import LoginPageLocators
import time
from pages import LoginPage
loginURL = "https://dev-shipper-app.empowerdatalogistics.com/auth/login"
class ForgotPasswordClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        cls.driver.implicitly_wait(5) 
        print("Forgot password tests are running")

    def test_1_submit_success(self):
        self.driver.get(loginURL)
        self.driver.refresh()
        login = LoginPage(self.driver)
        login.click_ForgotPassword()
        login.enter_theEmail("mehdi.kharraz@outlook.com")
        login.submit_theEmail()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,LoginPageLocators.verify_email))

    def test_2_submit_fail(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_ForgotPassword()
        login.enter_theEmail("aaaa.aa@aa.com")
        login.submit_theEmail()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,LoginPageLocators.user_not_found))

    def test_3_wrong_format(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_ForgotPassword()
        login.enter_theEmail("mehdi.kharrazoutook.com")
        login.submit_theEmail()
        EmailErrorMessage2 = self.driver.find_element(By.XPATH, LoginPageLocators.emailerrorMessage3).text
        expectedMessage2 = 'Wrong email format'
        self.assertEqual(EmailErrorMessage2,expectedMessage2)

    def test_4_empty_field(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_ForgotPassword()
        login.enter_theEmail("")
        login.submit_theEmail()
        EmailErrorMessage = self.driver.find_element(By.XPATH, LoginPageLocators.emailerrorMessage3).text
        expectedmessage = 'Required field'
        self.assertEqual(EmailErrorMessage,expectedmessage)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("forgot password tests are done\n")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/forgot_password'))

