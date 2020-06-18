from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)
assert "Welcome: Mercury Tours" in driver.title
driver.implicitly_wait(10)

print(driver.current_url)
# time.sleep(5)
driver.find_element_by_xpath("//input[@name='login']").click()
print(driver.title)
driver.back()
print(driver.title)
# time.sleep(2)
driver.forward()
# time.sleep(2)
print(driver.title)
driver.back()
ele_userName = driver.find_element_by_name("userName")
print(ele_userName.is_displayed())
print(ele_userName.is_enabled())

ele_password = driver.find_element_by_name("password")
print(ele_password.is_displayed())
print(ele_password.is_enabled())

signin_btn = driver.find_element_by_xpath("//input[@name='login']")
print(signin_btn.is_displayed())
ele_userName.send_keys("mercury")
ele_password.send_keys("mercury")
signin_btn.click()
print(driver.title)
flight_type_roundtrip= driver.find_element_by_xpath("//input[@value='roundtrip']")
print(flight_type_roundtrip.is_displayed())
print("Status of Round Trip Radio button is ",flight_type_roundtrip.is_selected())
flight_type_OneWay= driver.find_element_by_xpath("//input[@value='oneway']")
print("Status of One Way Radio button is ",flight_type_OneWay.is_selected())
driver.close()