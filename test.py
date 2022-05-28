import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\SelTest\\chromedriver.exe")

#driver.get("https:xplorefree.com")
#time.sleep(1)
driver.get("https://www.browserstack.com/users/sign_up")

name = driver.find_element_by_id("user_full_name")
name.send_keys('osama shakeel')

email= driver.find_element_by_id("user_email_login")
email.send_keys('o7aama@gmail.com')

password= driver.find_element_by_id("user_password")
password.send_keys('aspirefree258@A')

new= driver.find_element_by_id("tnc_checkbox").click()

my_element = driver.find_element_by_id("user_submit")
my_element.click()

"""
my_element = driver.find_element_by_class_name("btn btn-primary col-center users-registrations-new")
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(By.CLASS_NAME, 'btn btn-primary col-center users-registrations-new'),'Sign me up'
    
"""