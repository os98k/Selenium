from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")

driver.get("https://www.cleartrip.com/do/search/flights")

driver.find_element_by_name("from").send_keys("del")

from_airports = driver.find_element_by_xpath("//ul[@id='ui-id-1']/li/div")
for airport in from_airports:
    if airport.text =="Del Rio, US - Del Rio (DRT)"


static_dropdown.deselect_by_visible_text("Option3")
time.sleep(2)
static_dropdown.deselect_by_index(2)
time.sleep(2)
static_dropdown.deselect_by_value("option1")
time.sleep(2)

