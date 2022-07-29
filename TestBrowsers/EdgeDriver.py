from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Edge(executable_path=r"C:\Users\HP\Desktop\SELENIUM\msedgedriver.exe")

driver.get("https://www.google.com")
