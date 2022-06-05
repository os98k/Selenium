from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

static_dropdown= Select(driver.find_element_by_xpath("//select[@id = 'dropdown-class-example']"))
static_dropdown.select_by_visible_text("Option3")
time.sleep(2)
static_dropdown.select_by_index(2)
time.sleep(2)
static_dropdown.select_by_value("option1")
time.sleep(2)

