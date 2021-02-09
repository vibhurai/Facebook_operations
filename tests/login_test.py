from selenium import webdriver
import unittest
import HtmlTestRunner
from Kaustubh.proj_2.pages.login import login_class
from Kaustubh.proj_2.pages.homepage import  homepage_class
from Kaustubh.proj_2.pages.dashboard import dash_class
from Kaustubh.proj_2.pages.friends import friends_class
from selenium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://en-gb.facebook.com/login/')
        login = login_class(driver)
        login.enter_username("kr619@rediffmail.com")
        login.enter_pass("kr619r")
        login.click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# if __name__ == '__main__':
#         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\user\Desktop\Kaustubh\Proj_1\Test\Reports'))
