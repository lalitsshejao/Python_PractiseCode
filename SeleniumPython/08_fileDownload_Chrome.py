from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chroOption=Options()
chroOption.add_experimental_option("prefs",{"download.default_directory": "C:\DownloadedFiles"})

driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe",chrome_options=chroOption)

driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")


#for Text
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("Hello... How are you \n Hello... How are you \n Hello... How are you ")
driver.find_element_by_xpath("//button[@id='createTxt']").click()
driver.find_element_by_xpath("//a[@id='link-to-download']").click()

#for PDF
driver.find_element_by_xpath("//textarea[@id='pdfbox']").send_keys("Hello... How are you \n Hello... How are you \n Hello... How are you ")
driver.find_element_by_xpath("//button[@id='createPdf']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@id='pdf-link-to-download']").click()
