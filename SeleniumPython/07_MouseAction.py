from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

tooltip= driver.find_element_by_link_text("Tooltips")
action=ActionChains(driver)
driver.execute_script("arguments[0].scrollIntoView();",tooltip)
action.move_to_element(tooltip).perform()

doubleclickText=driver.find_element_by_xpath("//h2[contains(text(),'Double Click')]")
doubleclick=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

driver.execute_script("arguments[0].scrollIntoView();",doubleclickText)
time.sleep(3)
action.double_click(doubleclick).perform()

