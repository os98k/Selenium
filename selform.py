
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\SelTest\\chromedriver.exe")


driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

try: 
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()

except:
    print('No element was found with this class, so just skiiiping....')

num1 = driver.find_element_by_id("sum1")
num1.send_keys(Keys.NUMPAD7, Keys.NUMPAD4)

num2= driver.find_element_by_id("sum2")
num2.send_keys(74)

link = driver.find_element_by_css_selector(a[href^="https" ])

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()

#btn2 = driver.find_element_by_class_name("btn btn-default").click




