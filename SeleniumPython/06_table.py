from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.execute_script("window.scrollBy(0,500)","")
time.sleep(5)

scroll_Tooltips = driver.find_element_by_xpath("//h2[contains(text(),'HTML Table')]")
driver.execute_script("arguments[0].scrollIntoView();",scroll_Tooltips)

rows = len(driver.find_elements_by_xpath("//div[@id='footer-1']//tr"))
print("Numbers of Rows: ", (rows))

columns = len(driver.find_elements_by_xpath("//div[@id='footer-1']//tr[2]//td"))
print(columns)
for r in range(2, rows+1):
    for c in range (1,columns+1):
        value= driver.find_element_by_xpath("//div[@id='footer-1']//tr["+str(r)+"]//td["+str(c)+"]").text
        print(value,end='       ')
    print()

driver.close()