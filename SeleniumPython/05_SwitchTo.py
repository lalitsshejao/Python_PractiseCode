from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(2)
driver.switch_to.alert.accept()     #click OK buttom
time.sleep(5)
driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(2)
driver.switch_to.alert.dismiss()    #Click Cancel Button


driver.get("https://www.selenium.dev/selenium/docs/api/java/")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("METHOD").click()

time.sleep(5)

driver.close()