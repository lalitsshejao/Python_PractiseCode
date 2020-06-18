import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title Of the page is :", self.driver.title)
        self.driver.close()

    def test_NewTours(self):
        self.driver=webdriver.Chrome(executable_path="D:\\Udemy_Selenium\\lib\\chromedriver.exe")
        self.driver.get("http://www.newtours.demoaut.com/")
        print("Title Of the page is :", self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()