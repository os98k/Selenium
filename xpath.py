from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")


driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Attribute & Value //tagname[@attribute = ‘value’]

driver.find_element_by_xpath("//input[@value= 'radio1']").click()
#text //tagname[text() = ‘type text here’]
a= driver.find_element_by_xpath("//legend[@value[text]= 'Checkbox Example']")
a.click()

#Parents to child //tagname[@attribute = ‘value’]/tagname
driver.find_element_by_xpath("//label[@for = ‘bmw’]/input").click()

#Parents to last child //tagname[@attribute = ‘value’]/tagname[last()]
driver.find_element_by_xpath("//select[@id='dropdown-class-example']/option(2)").click()
driver.find_element_by_xpath("//select[@id='dropdown-class-example']/option(last())").click()

#Grand parent to child //tagname[@attribute = ‘value’]/tagname/tagname
driver.find_element_by_xpath("//div[@class= 'tableFixHead']/table/tbody/tr(5)/td(2)").text

#Child to any ancestor //tagname[@attribute = ‘value’]/ancestor::tagname[@attribute = ‘value’]
driver.find_element_by_xpath("//option[value ='oprion3']/ancestor/::div[@class='block large-row-spacer")

#Starts with //tagname[starts-with(@attribute,’starting values’)]
driver.find_element_by_xpath("//option[start-with(@value,'option')]")

#contains //*[contains(@attribute,’value’)]
driver.find_element_by_xpath(//*[contains(@class,'npu')])

#Starts with and contains //tagname[starts-with(@attribute,'starting values') and contains(@attribute,’value')]
driver.find_element_by_xpath(//input[starts-with(@id,'name') and contains(@name, 'er-na')])