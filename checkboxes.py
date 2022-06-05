from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")


driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Radiobox buttons which is in circle form and can be check one at a time
# Checkboxes are square in shape and can be check multiple at a time

driver.find_element_by_id("checkboxoption1")
driver.find_element_by_id("checkboxoption2")
driver.find_element_by_id("checkboxoption3")

checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
for checkbox in checkboxes:
    checkbox.click()

# for checkbox in checkboxes:
#     if checkbox == checkboxes[1]:
#         pass
#     else:
#         checkbox.click()