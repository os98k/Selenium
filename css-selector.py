from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#tagname[attribute = 'value']
driver.find_element_by_css_selector("input[value= 'radio1']").click()
driver.find_element_by_css_selector("#name").send_keys("osama")
