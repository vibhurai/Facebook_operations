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
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        # cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://en-gb.facebook.com/login/')
        # print(driver.current_url)
        login = login_class(driver)
        login.enter_username("shilarai26@gmail.com")
        login.enter_pass("viDhu@2007")
        login.click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# if __name__ == '__main__':
#         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\user\Desktop\Kaustubh\Proj_1\Test\Reports'))
