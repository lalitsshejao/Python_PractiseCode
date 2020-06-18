from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")

driver.maximize_window()
driver.get("http://www.newtours.demoaut.com/")

links= driver.find_elements(By.TAG_NAME,"a")
print("Number Of Links Present on the Page: ",len(links))

for x in links:
    print("Link Text ", x.text)


driver.find_element(By.LINK_TEXT,"Destinations").click()
print (driver.title)
time.sleep(5)
driver.close()