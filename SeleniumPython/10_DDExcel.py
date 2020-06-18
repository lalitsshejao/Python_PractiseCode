import XLUtils
from selenium import webdriver
import time
file = "C:\DownloadedFiles\LoginData.xlsx"
url = "http://www.newtours.demoaut.com/"

driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

rows=XLUtils.getRowCount(file,"login")

for r in range (2,rows+1):
    userName=XLUtils.readData(file, "login",r,1)
    password=XLUtils.readData(file, "login",r,2)

    driver.find_element_by_name("userName").send_keys(userName)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//input[@name='login']").click()
    print(driver.title)
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test Passed")
        XLUtils.writeData(file, "login",r,3,"Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(file, "login", r, 3, "Failed")

    driver.find_element_by_link_text("Home").click()

driver.close()