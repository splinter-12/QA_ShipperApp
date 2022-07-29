from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Ie(executable_path=r"C:\Users\HP\Desktop\SELENIUM\IEDriverServer.exe")

driver.get("https://www.google.com")






'''
#assert "jumia" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.send_keys("jumia")
elem.send_keys(Keys.ENTER)

print("hello!")
time.sleep(10)
#driver.title = "jumia - Recherche Google"

if (driver.title=="jumia - Recherche Google"):
    print("SUCCEEDED")
else:
    print("failed!!!")

#assert "No results found." not in driver.page_source
driver.close()
'''


















