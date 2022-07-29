from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import sys
import HtmlTestRunner
sys.path.append("locators")
sys.path.append("pages")
from locators import LoginPageLocators
from pages import LoginPage
loginURL = "https://dev-shipper-app.empowerdatalogistics.com/auth/login"
class LoginPageClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3) 
        print("login ests are running")

    def test_01_login_success(self):
        self.driver.get(loginURL)
        self.driver.refresh()
        login = LoginPage(self.driver)
        login.enter_Email("mehdi.kharraz@outlook.com")
        login.enter_Password("P@ssw0rd123")
        login.click_submit()
        self.assertIsNotNone(self.driver.find_element(By.XPATH, LoginPageLocators.dash_bord))
        login.click_user()
        login.click_logout()

    def test_02_email_field_empty(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.enter_Email("")
        login.enter_Password("P@ssw0rd123")
        login.click_submit()
        EmailErrorMessage1 = self.driver.find_element(By.XPATH, LoginPageLocators.emailerrorMessage1).text
        expectedMessage = '* Email is Required'
        message_1 = "Email field shouldn't be empyt"
        self.assertEqual(EmailErrorMessage1,expectedMessage,message_1)


    def test_03_email_wrong_format(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.enter_Email("mehdi.kharrazoutlook.com")
        login.enter_Password("P@ssw0rd123")
        login.click_submit()
        EmailErrorMessage2 = self.driver.find_element(By.XPATH, LoginPageLocators.emailerrorMessage2).text
        expectedMessage2 = 'Wrong email format'
        message_2 = "choose a correct email format"
        self.assertEqual(EmailErrorMessage2,expectedMessage2,message_2)
        

    def test_04_password_field_empty(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.enter_Email("mehdi.kharraz@outlook.com")
        login.enter_Password('')
        login.click_submit()
        PasswordErrorMessage_1 = self.driver.find_element(By.XPATH, LoginPageLocators.passworderrorMessage).text
        expectedMessage3 = '* Password is Required'
        self.assertEqual( PasswordErrorMessage_1, expectedMessage3)

    def test_05_password_notenough_symbols(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.enter_Email("mehdi.kharraz@outlook.com")
        login.enter_Password('dd')
        login.click_submit()
        PasswordErrorMessage_2 = self.driver.find_element(By.XPATH, LoginPageLocators.passworderrorMessage2).text
        expectedMessage3 = 'Minimum 3 symbols'
        self.assertEqual( PasswordErrorMessage_2, expectedMessage3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("login tests are done\n")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/login'))

