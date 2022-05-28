import os
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\SelTest\\chromedriver.exe")

driver.get("https://xplorefree.com/contact/")
#time.sleep(1)

name = driver.find_element_by_name("your-name")
name.send_keys('osama shakeel')

email= driver.find_element_by_name("your-email")
email.send_keys('o7aama@gmail.com')

password= driver.find_element_by_name("your-subject")
password.send_keys('Message')

new= driver.find_element_by_name("your-message")
new.send_keys("Hi, this is a random message sent through selenium automatic tool")

my_element = driver.find_element_by_class_name("wpcf7-submit")
my_element.click()
