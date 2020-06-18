from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
print(driver.title)

ele_skill_Dropdown= driver.find_element_by_id("Skills")
drop= Select(ele_skill_Dropdown)

drop.select_by_index(4)     #select by index
time.sleep(5)

drop.select_by_value("Backup Management")     #Select by Value
time.sleep(5)

drop.select_by_visible_text("Python")     #Select by Visible text
time.sleep(5)

#count of elements present
print("Count of options present in dropdown ",len(drop.options))

#print the list of options present
for i in drop.options:
    print(i.text)

time.sleep(5)
driver.close()