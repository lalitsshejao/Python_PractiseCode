from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.co.in")

print (driver.title)

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()

driver.find_element(By.ID,"flight-origin-hp-flight").clear()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys (" SFO")
time.sleep(5)
driver.find_element(By.ID,"flight-destination-hp-flight").clear()
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys (" NYC")

# wait.until(EC.element_to_be_clickable(By.XPATH,"//[@id='flight-departing-hp-flight']"))
driver.find_element(By.ID,"flight-departing-hp-flight").click()
driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys ("01/06/2020")

driver.find_element(By.ID,"flight-returning-hp-flight").click()
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys (Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)  # To clear the existing values

driver.find_element(By.ID,"flight-returning-hp-flight").send_keys ("05/06/2020")
driver.find_element_by_xpath("//button[@class='datepicker-close-btn close btn-text']").click()

time.sleep(2)
driver.find_element_by_xpath ("//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

wait = WebDriverWait(driver,10)
element= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(5)

driver.close()