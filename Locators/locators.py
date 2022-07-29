
class LoginPageLocators(object):
    emailTextBox = 'email'
    passwordTextBox = 'password'
    submit = '//button[@type="submit"]'
    ForgotPassword = 'kt_login_forgot'
    ForgotPasswordEmail = 'Email'
    submitEmail = 'kt_login_forgot_submit'
    verify_email = '//*[@id="root"]/div[1]/div/div/div/div[2]/div/div/div/div/h2'
    user_not_found = "//div[@id='swal2-html-container']"
    cancel = 'kt_login_forgot_cancel'
    user = '//*[@id="kt_header"]/div/div[2]/div[4]/div[1]/div'
    logout ='//*[@id="kt_header"]/div/div[2]/div[4]/div[2]/div[3]/div[2]/a'
    dash_bord = '//*[@id="kt_header_menu"]/ul/li[1]'
    #    Create a Shipper Account locators : 
    createAccount = 'kt_login_signup' #id
    First_name = 'FirstName'#name
    last_name = 'LastName'#name
    Email = 'Email'#name
    emailerrorMessage1 = "//div[contains(text(),'* Email is Required')]"
    emailerrorMessage2 = "//div[contains(text(),'Wrong email format')]"
    emailerrorMessage3 = '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div'
    phone_number = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[3]/div/div/input'#xpath
    password = 'Password'#name
    passworderrorMessage = "//div[contains(text(),'* Password is Required')]"
    passworderrorMessage2 = "//div[contains(text(),'Minimum 3 symbols')]"
    confirm_password = 'ConfirmPassword'#name
    next_button1 = '//*[@id="kt_wizard"]/div[2]/div/div[2]/div/button' #xpath
    checkBox = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[5]/div[2]/div/label' #xpath
    cancelForgotPaassProcess =  '//*[@id="kt_login"]/div/div/div[2]/div/div/div'
#    Create Company info :
    Create_Company = '//*[@id="kt_wizard"]/div[2]/div/div[1]/h4'
    Company_Name = 'CompanyName'#name
    Address1 = 'Address1'#name
    Address2 = 'Address2'#name
    Country = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div/div/div[1]'#xpath
    selectedCountry = "//div[contains(text(),'Canada')]"#xpath
    state = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[4]/div[1]/div[2]/div/div/div[1]' #xpath
    selectedState = "//div[contains(text(),'British Columbia')]"
    city1 = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[5]/div/div[1]/div'#xpath
    city2 = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[5]/div/div[1]/div/input'#xpath
    zip = 'Zipcode'#name
    next_Button2 = '//*[@id="kt_wizard"]/div[2]/div/div[2]/div[2]/button' #xpath
    back ='//*[@id="kt_wizard"]/div[2]/div/div[4]/div[1]/button'
    #create account 1
    actual_message1= "//div[contains(text(),'* First Name is required')]"
    actual_message2= '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]'
    actual_message3= '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[2]/div/div'
    actual_message4= '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[2]/div/div/div'
    actual_message5= '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[4]/div/div[2]/div'
    actual_message6= "//div[contains(text(),'* Must be 8 characters or more')]"
    conf_password_border= '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[5]/div[1]/div/input'
    choose_plan_txt = '//*[@id="kt_wizard"]/div[2]/div/div[1]/h4'
    #create account 2
    SetUpText = '//*[@id="kt_wizard"]/div[2]/div/h4'
    message_Link = "//div[contains(text(),'Company Name is required')]"
    #create account 3
    price_link_text = "//p[contains(text(),'$99.00')]"
    price_link_text2 = "//p[contains(text(),'$89.10')]"
    price_link_text3 = "//p[contains(text(),'$84.00')]"
    link_text ="//div[contains(text(),'* Please choose a plan')]"
    coupon_text ='//*[@id="swal2-html-container"]'
    coupon_button_validation ="//button[contains(text(),'OK')]"
    #create account 4 
    sammuray_text = '//*[@id="kt_wizard"]/div[2]/div/div[1]/h4'
    cardName_text = "//div[contains(text(),'Card Name is required')]"
    requiredFields = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[1]'
    cvv_validation = "//div[contains(text(),'CVV is not valid!')]"


#   Choose Plan
    monthly = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[1]/label' #xpath
    annual = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[2]/label' #xpath
    daily = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[3]/label' #xpath
    CouponCheck = '//*[@id="kt_wizard"]/div[2]/div/div[2]/div[1]/label' #xpath
    Coupon = 'Coupon' #name
    apply = '//*[@id="kt_wizard"]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/button' #xpath
    reset = '//*[@id="kt_wizard"]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/button' #xpath
    next_button3 = '//*[@id="kt_wizard"]/div[2]/div/div[4]/div[2]/button'#xpath
#    Set up your credit or debit card
    Checkboxes1 = 'Checkboxes1'#name
    adress1_billing = 'BillingAddress1' #name
    adress1_billing = 'BillingAddress2'#name
    country_billing = 'react-select-14-input'#id
    state_billing = 'react-select-15-input'#id
    city = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[5]/div[1]/div/input' #xpath
    zipcode ='BillingZipcode'#name
    CardName = 'CardName'#name
    CardNumber = 'CardNumber'#name
    experation_month = '//*[@id="kt_wizard"]/div[2]/div/div[1]/div[4]/div[1]/div/div[1]/div/div[1]' #xpath
    experation_month1 = "//div[contains(text(),'3')]"

    experation_year ='//*[@id="kt_wizard"]/div[2]/div/div[1]/div[4]/div[2]/div/div[1]/div'#xpath
    experation_year1 ="//div[contains(text(),'2027')]"#xpath
    CardCvv = 'CardCvc' #name
    next_button4 = '//*[@id="kt_wizard"]/div[2]/div/div[2]/div[2]/button'#xpath
#    sammuray
    submit_button = '//*[@id="kt_wizard"]/div[2]/div/div[2]/div[2]/button' #xpath
