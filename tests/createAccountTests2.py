from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import sys
import time
sys.path.append("pages")
sys.path.append("locators")
from locators import LoginPageLocators
from pages import LoginPage
loginURL = "https://dev-shipper-app.empowerdatalogistics.com/auth/login"
sys.path.append("createAccountTests")

def valid_informations(self):
    self.driver.get(loginURL)
    self.driver.refresh()
    login = LoginPage(self.driver)
    login.click_create_account()
    login.first_name("kaoutar")
    login.last_Name("KAOUTAR")
    login.Email_input("kaoutar@n.com")
    login.phone("99999999999")
    login.password_input("CoW1!222@")
    login.confirm_password_input("CoW1!222@")
    login.click_check_box()
    login.click_next()

class EmPowerClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5) 
        print("the second page in create account tests are running")

    def test_1_company_info(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.company_name_input("ka")
        login.Address1_input("somewhere")
        login.Address2_input("somewhere2")
        login.Country_drop_down()
        login.selected_country()
        login.state_drop_down()
        login.selected_state()
        login.city_click()
        login.city_input("city")
        login.zip_input("A1A 1A1")
        login.next_Button2_click()
        self.assertIsNotNone(self.driver.find_element(By.XPATH, LoginPageLocators.SetUpText))
        self.driver.refresh()

    def test_2_companyNameEmpty(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.company_name_input("")
        login.Address1_input("somewhere")
        message_link = self.driver.find_element(By.XPATH, LoginPageLocators.message_Link).text
        expected_message = "* Company Name is required"
        login.Address2_input("some other where")
        login.Country_drop_down()
        login.selected_country()
        login.state_drop_down()
        login.selected_state()
        login.city_click()
        login.city_input("city")
        login.zip_input("A1A 1A1")
        login.next_Button2_click()
        self.assertEqual(message_link,expected_message)
        self.driver.refresh()

    def test_3_companyName_lessThan2caracteres(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.company_name_input("j")
        login.Address1_input("somewhere")
        login.Address2_input("somewhere")
        login.Country_drop_down()
        login.selected_country()
        login.state_drop_down()
        login.selected_state()
        login.city_click()
        login.city_input("city")
        login.zip_input("A1A 1A1")
        login.next_Button2_click()
        self.assertIsNone(self.driver.find_element(By.XPATH, LoginPageLocators.SetUpText))

    def test_4_too_long_inputs(self):
        self.driver.refresh()
        login = LoginPage(self.driver)
        valid_informations(self)
        login.company_name_input("jf")
        login.Address1_input("somewheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeere")
        login.Address2_input("somewheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeere")
        login.Country_drop_down()
        login.selected_country()
        login.state_drop_down()
        login.selected_state()
        login.city_click()
        login.city_input("citttttttttttttttttttyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        login.zip_input("A1A 1A1A1A1A1A1AA1A1AA1A1A1A1A1A1A1A1A1AA1A1A1AA11AA1A1A1A1A1A1A1A1A1A1A1A1AAAAAAAAAAAAAAAAAA111111111111111111111AAAAAAAAAAAAA11111111111A")
        login.next_Button2_click()
        self.assertIsNone(self.driver.find_element(By.XPATH, LoginPageLocators.SetUpText))
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("done")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/createAcount2'))
