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

class EmPowerClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(20) 
        print("the third page in create account tests are running")

    def test_1_choosePlan_success(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.monthly_click()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.price_link_text).text
        text_holder = '$99.00'
        self.assertEqual(link_text,text_holder)
        login. next_button3_click()
        self.driver.refresh()

    def test_2_choose_no_plan(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login. next_button3_click()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.link_text).text
        text_holder = '* Please choose a plan'
        self.assertEqual(link_text,text_holder)
        self.driver.refresh()

    def test_3_only_CouponSelected(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.coupon_click()
        login. next_button3_click()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.link_text).text
        text_holder = '* Please choose a plan'
        self.assertEqual(link_text,text_holder)
        self.driver.refresh()

    def test_4_valid_coupon1(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.monthly_click()
        login.coupon_click()
        login.send_coupon("OEgPJumr")
        login.coupon_apply()
        login.coupon_button_enter()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.price_link_text2 ).text
        text_holder = '$89.10'
        self.assertEqual(link_text,text_holder)        
        login. next_button3_click()
        self.driver.refresh()

    def test_5_valid_coupon2(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.monthly_click()
        login.coupon_click()
        login.send_coupon("zXOmc41P ")
        login.coupon_apply()
        login.coupon_button_enter()
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.price_link_text3).text
        text_holder = '$84.00'
        self.assertEqual(link_text,text_holder)        
        login. next_button3_click()
        self.driver.refresh()

    def test_6_non_valid_coupon(self):
        login = LoginPage(self.driver)
        valid_informations(self)
        login.monthly_click()
        login.coupon_click()
        login.send_coupon("jjjj")
        login.coupon_apply() 
        link_text = self.driver.find_element(By.XPATH, LoginPageLocators.coupon_text).text  
        text_holder = 'Coupon not valid'
        self.assertEqual(link_text,text_holder) 
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("the first page in create account tests are done")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/createAcount3'))