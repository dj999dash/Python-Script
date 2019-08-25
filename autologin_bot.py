from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import os

#Enter your credentials

usernameStr = ""
passwordStr = ""
url=""

# if using chrome

browser = webdriver.Chrome()
browser.get((url)) 

username = browser.find_element_by_id('Username')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('next')
nextButton.click()

password = WebDriverWait(browser , 10).until(EC.presence_of_element_located((By.ID , 'Passwd')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()
