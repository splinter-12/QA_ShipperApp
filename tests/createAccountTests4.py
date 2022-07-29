from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import sys
import time
sys.path.append("locators")
from locators import LoginPageLocators
sys.path.append("pages")
from pages import LoginPage
loginURL = "https://dev-shipper-app.empowerdatalogistics.com/auth/login"

def valid_informations(self):
        self.driver.get(loginURL)
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
        login.company_name_input("ka")
        login.Address1_input("somewhere")
        login.Address2_input("some other where")
        login.Country_drop_down()
        login.selected_country()
        login.state_drop_down()
        login.selected_state()
        login.city_click()
        login.city_input("city")
        login.zip_input("A1A 1A1")
        login.next_Button2_click()
        login.monthly_click()
        login. next_button3_click()

class EmPowerClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(20) 
        print("the forth page in create account tests are running")

    # def test_1_valid_informations(self):
    #     login = LoginPage(self.driver)
    #     valid_informations(self)
    #     login.send_Cardname("ka")
    #     login.send_CardNumber("4242424242424242")
    #     login.experation_month_checkBox()
    #     login.experation_month1_checkBox()
    #     login.experation_year_checkBox()
    #     login.experation_year1_checkBox()
    #     login.send_cvv("1212")
    #     login.next_button4_click()
    #     self.assertIsNotNone(self.driver.find_element(By.XPATH,LoginPageLocators.sammuray_text ))
    #     self.driver.refresh()

    # def test_2_empty_cardNameFeild(self):
    #     login = LoginPage(self.driver)
    #     valid_informations(self)
    #     login.send_Cardname("")
    #     login.send_CardNumber("4242424242424242")
    #     link_text = self.driver.find_element(By.XPATH, LoginPageLocators.cardName_text).text  
    #     text_holder = '* Card Name is required' 
    #     login.experation_month_checkBox()
    #     login.experation_month1_checkBox()
    #     login.experation_year_checkBox()
    #     login.experation_year1_checkBox()
    #     login.send_cvv("1212")
    #     login.next_button4_click()
    #     self.assertEqual(link_text,text_holder)
    #     self.driver.refresh()

    def test_3_empty_card_number(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.send_Cardname("")
        login.send_CardNumber("")
        login.send_cvv("")
        login.next_button4_click()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.requiredFields).text  
        text_holder = 'Please check your required fields' 
        self.assertEqual(link_text,text_holder)
        self.driver.refresh()

    # def test_4_cvvNotValid(self):
    #     login = LoginPage(self.driver)
    #     valid_informations(self)
    #     login.send_Cardname("ac")
    #     login.send_CardNumber("4242424242424242")
    #     login.experation_month_checkBox()
    #     login.experation_month1_checkBox()
    #     login.experation_year_checkBox()
    #     login.experation_year1_checkBox()
    #     login.send_cvv("12")
    #     login.next_button4_click()
    #     link_text = self.driver.find_element(By.XPATH,LoginPageLocators.cvv_validation).text  
    #     text_holder = 'CVV is not valid!' 
    #     self.assertEqual(link_text,text_holder)
    #     self.driver.refresh()

    # def test_5_TooLong_CardName(self):
    #     login = LoginPage(self.driver)
    #     valid_informations(self)
    #     login.send_Cardname("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #     login.send_CardNumber("4242424242424242")
    #     login.experation_month_checkBox()
    #     login.experation_month1_checkBox()
    #     login.experation_year_checkBox()
    #     login.experation_year1_checkBox()
    #     login.send_cvv("1212")
    #     login.next_button4_click()
    #     self.assertIsNone(self.driver.find_element(By.XPATH, LoginPageLocators.sammuray_text))
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("done")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/createAcount4'))