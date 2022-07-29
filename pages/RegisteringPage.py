from BOM.Locators.locators import LoginPageLocators
from selenium.webdriver.common.by import By


class restring:
    def __init__(self, driver):
        self.driver = driver
        self.user = LoginPageLocators.user
        self.logout = LoginPageLocators.logout
        self.createAccount = LoginPageLocators.createAccount
        self.First_name = LoginPageLocators.First_name
        self.last_name = LoginPageLocators.last_name
        self.Email = LoginPageLocators.Email
        self.phone_number = LoginPageLocators.phone_number
        self.password = LoginPageLocators.password
        self.confirm_password = LoginPageLocators.confirm_password
        self.checkBox = LoginPageLocators.checkBox
        self.next_button1 = LoginPageLocators.next_button1
        self.Company_Name = LoginPageLocators.Company_Name
        self.Address1 = LoginPageLocators.Address1
        self.Address2 = LoginPageLocators.Address2
        self.Country = LoginPageLocators.Country
        self.state = LoginPageLocators.state
        self.city1 = LoginPageLocators.city1
        self.city2 = LoginPageLocators.city2
        self.zip = LoginPageLocators.zip
        self.next_Button2 = LoginPageLocators.next_Button2
        self.selectedCountry = LoginPageLocators.selectedCountry
        self.selectedState = LoginPageLocators.selectedState
        self.back = LoginPageLocators.back
        self.monthly = LoginPageLocators.monthly
        self.next_button3 = LoginPageLocators.next_button3
        self.Coupon = LoginPageLocators.Coupon
        self.CouponCheck = LoginPageLocators.CouponCheck
        self.apply = LoginPageLocators.apply
        self.Checkboxes1 = LoginPageLocators.Checkboxes1
        self.CardName = LoginPageLocators.CardName
        self.CardNumber = LoginPageLocators.CardNumber
        self.experation_month = LoginPageLocators.experation_month
        self.experation_month1 = LoginPageLocators.experation_month1
        self.experation_year = LoginPageLocators.experation_year
        self.experation_year1 = LoginPageLocators.experation_year1
        self.CardCvv = LoginPageLocators.CardCvv
        self.next_button4 = LoginPageLocators.next_button4
        self.coupon_button_validation = LoginPageLocators.coupon_button_validation

    def click_user(self):
        self.driver.find_element(By.XPATH, value=self.user).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, value=self.logout).click()

    def click_create_account(self):
        self.driver.find_element(By.ID, value=self.createAccount).click()

    def first_name(self, Fname):
        self.driver.find_element(By.NAME, value=self.First_name).send_keys(Fname)

    def last_Name(self, Lname):
        self.driver.find_element(By.NAME, value=self.last_name).send_keys(Lname)

    def Email_input(self, mail):
        self.driver.find_element(By.NAME, value=self.Email).send_keys(mail)

    def phone(self, phone):
        self.driver.find_element(By.XPATH, value=self.phone_number).send_keys(phone)

    def password_input(self, password):
        self.driver.find_element(By.NAME, value=self.password).send_keys(password)

    def confirm_password_input(self, password2):
        self.driver.find_element(By.NAME, value=self.confirm_password).send_keys(password2)

    def click_check_box(self):
        self.driver.find_element(By.XPATH, value=self.checkBox).click()

    def click_next(self):
        self.driver.find_element(By.XPATH, value=self.next_button1).click()

    def company_name_input(self, compname):
        self.driver.find_element(By.NAME, value=self.Company_Name).send_keys(compname)

    def Address1_input(self, address1):
        self.driver.find_element(By.NAME, value=self.Address1).send_keys(address1)

    def Address2_input(self, address2):
        self.driver.find_element(By.NAME, value=self.Address2).send_keys(address2)

    def Country_drop_down(self):
        self.driver.find_element(By.XPATH, value=self.Country).click()

    def selected_country(self):
        self.driver.find_element(By.XPATH, value=self.selectedCountry).click()

    def state_drop_down(self):
        self.driver.find_element(By.XPATH, value=self.state).click()

    def selected_state(self):
        self.driver.find_element(By.XPATH, value=self.selectedState).click()

    def city_click(self):
        self.driver.find_element(By.XPATH, value=self.city1).click()  #

    def city_input(self, City):
        self.driver.find_element(By.XPATH, value=self.city2).send_keys(City)

    def zip_input(self, Zip):
        self.driver.find_element(By.NAME, value=self.zip).send_keys(Zip)

    def next_Button2_click(self):
        self.driver.find_element(By.XPATH, value=self.next_Button2).click()

    def back_button_click(self):
        self.driver.find_element(By.XPATH, value=self.back).click()

    def monthly_click(self):
        self.driver.find_element(By.XPATH, value=self.monthly).click()

    def next_button3_click(self):
        self.driver.find_element(By.XPATH, value=self.next_button3).click()

    def coupon_click(self):
        self.driver.find_element(By.XPATH, value=self.CouponCheck).click()

    def coupon_apply(self):
        self.driver.find_element(By.XPATH, value=self.apply).click()

    def address_checkBox(self):
        self.driver.find_element(By.XPATH, value=self.Checkboxes1).click()

    def coupon_button_enter(self):
        self.driver.find_element(By.XPATH, value=self.coupon_button_validation).click()

    def send_coupon(self, Coup):
        self.driver.find_element(By.NAME, value=self.Coupon).send_keys(Coup)

    def send_Cardname(self, Cardname):
        self.driver.find_element(By.NAME, value=self.CardName).send_keys(Cardname)

    def send_CardNumber(self, Cardnumber):
        self.driver.find_element(By.NAME, value=self.CardNumber).send_keys(Cardnumber)

    def experation_month_checkBox(self):
        self.driver.find_element(By.XPATH, value=self.experation_month).click()

    def experation_month1_checkBox(self):
        self.driver.find_element(By.XPATH, value=self.experation_month1).click()

    def experation_year_checkBox(self):
        self.driver.find_element(By.XPATH, value=self.experation_year).click()

    def experation_year1_checkBox(self):
        self.driver.find_element(By.XPATH, value=self.experation_year1).click()

    def send_cvv(self, cardcvv):
        self.driver.find_element(By.NAME, value=self.CardCvv).send_keys(cardcvv)

    def next_button4_click(self):
        self.driver.find_element(By.XPATH, value=self.next_button4).click()
