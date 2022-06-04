from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

name = driver.find_element_by_id("name")
#name = driver.find_element_by_name("enter-name")
#name = driver.find_element_by_class_name("inputs")

name.send_keys("Osama Shakeel")

driver.find_element_by_id("alertbtn").click()
a = driver.find_element_by_id("openwindow").text
print(a)

driver.find_element_by_link_text("Free Access to InterviewQues/ResumeAssistance/Material").click()