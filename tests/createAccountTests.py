from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import unittest
import HtmlTestRunner
import sys
import time
sys.path.append("pages")
sys.path.append("locators")
from locators import LoginPageLocators
from pages import LoginPage
loginURL = "https://dev-shipper-app.empowerdatalogistics.com/auth/login"
class EmPowerClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(20) 
        print("the first page in create account tests are running")

    def test_1_correct_informations(self):
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
        self.assertIsNotNone(self.driver.find_element(By.XPATH, LoginPageLocators.Create_Company ))

    def test_2_empty_Firstname_field(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("")
        login.last_Name("KAOUTAR")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        actual_message = self.driver.find_element(By.XPATH, LoginPageLocators.actual_message1).text
        expected_message = '* First Name is required'
        login.click_next()
        self.assertEqual(expected_message,actual_message)

    def test_3_empty_lastname_field(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        actual_message = self.driver.find_element(By.XPATH, LoginPageLocators.actual_message2).text
        expected_message = '* Last Name is required'
        login.click_next()
        self.assertEqual(expected_message,actual_message)

    def test_4_empty_email_field(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        actual_message = self.driver.find_element(By.XPATH, LoginPageLocators.actual_message3).text
        expected_message = '* Email is required'
        login.click_next()
        self.assertEqual(expected_message,actual_message)

    def test_5_wrong_email_format(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutarn.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        actual_message = self.driver.find_element(By.XPATH, LoginPageLocators.actual_message4).text
        expected_message ='Email must be a valid email'
        login.click_next()
        self.assertEqual(expected_message,actual_message)
    def test_6_correct_email_format(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        try:
            self.driver.find_element(By.XPATH, LoginPageLocators.actual_message4)
        except:
            print("correct format")
        login.click_next()

    def test_7_empty_password_field(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("")
        login.confirm_password_input("")
        login.click_check_box()
        actual_message = self.driver.find_element(By.XPATH,LoginPageLocators.actual_message5).text
        expected_message ='* Password is Required'
        login.click_next()
        self.assertEqual(expected_message,actual_message)

    def test_8_password_notStrong_enough(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("dd")
        login.confirm_password_input("dd")
        login.click_check_box()
        login.click_next()
        actual_message = self.driver.find_element(By.XPATH, LoginPageLocators.actual_message6).text
        expected_message ='* Must be 8 characters or more'
        self.assertEqual(expected_message,actual_message)

    def test_9_check_box_notClicked(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_next()
        actual_message = self.driver.find_element(By.XPATH, '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[1]/div').text
        expected_message ='Please check your required fields'
        self.assertEqual(expected_message,actual_message)

    def test_10_not_similar_passwords(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("kaoutar")
        login.last_Name("kaoutar")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW")
        login.click_check_box()
        login.click_next()
        confirm_password_border = Color.from_string(self.driver.find_element(By.XPATH,LoginPageLocators.conf_password_border).value_of_css_property('border-color'))
        HEX_COLOUR = Color.from_string('#f64e60')
        assert confirm_password_border == HEX_COLOUR

    def test_11_too_long_inputs(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("some veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeery looooooooooooooong naaaaaaaaaaaame")
        login.last_Name("another veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeery loooooooooooooooooooooooooong naaaaaaaaaaaaaaaaaaaame")
        login.Email_input("theSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaameheeeeeeeeeeeeeeeeeere@n.coooooooooooooooooooom")
        login.phone("99999999999")
        login.password_input("CoW1!222@222222222222222eeeeeeeeeeeeeeeeeeeeewwwwwwwwwwwwwwwwwwwwwww")
        login.confirm_password_input("CoW1!222@222222222222222eeeeeeeeeeeeeeeeeeeeewwwwwwwwwwwwwwwwwwwwwww")
        login.click_check_box()
        login.click_next()
        self.assertIsNone(self.driver.find_element(By.XPATH, LoginPageLocators.choose_plan_txt))

    def test_12_name_lessThan_2caracteres(self):
        self.driver.get(loginURL)
        login = LoginPage(self.driver)
        login.click_create_account()
        login.first_name("s")
        login.last_Name("a")
        login.Email_input("kaoutar@n.com")
        login.phone("99999999999")
        login.password_input("CoW1!222@")
        login.confirm_password_input("CoW1!222@")
        login.click_check_box()
        login.click_next()
        self.assertIsNone(self.driver.find_element(By.XPATH,LoginPageLocators.choose_plan_txt))

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("create account tests are done")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/createAcount1'))















