from selenium import webdriver
from selenium.webdriver.firefox.options import Options

ffpref=webdriver.FirefoxProfile()
ffpref.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
ffpref.set_preference("browser.download.manager.showWhenStarting", False)
ffpref.set_preference("browser.download.dir", "C:\DownloadedFiles")
ffpref.set_preference("browser.download.folderList",2)
ffpref.set_preference("pdfjs.disabled", True)

driver=webdriver.Firefox(executable_path="D:\\Udemy_Selenium\\lib\\geckodriver.exe",firefox_profile=ffpref)

driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")


#for Text
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("Hello... How are you")
driver.find_element_by_xpath("//button[@id='createTxt']").click()
driver.find_element_by_xpath("//a[@id='link-to-download']").click()

#for PDF
driver.find_element_by_xpath("//textarea[@id='pdfbox']").send_keys("Hello... How are you")
driver.find_element_by_xpath("//button[@id='createPdf']").click()
driver.find_element_by_xpath("//a[@id='pdf-link-to-download']").click()
