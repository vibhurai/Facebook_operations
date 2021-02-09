import HtmlTestRunner
from selenium import webdriver
import unittest
from Kaustubh.proj_2.pages.login import login_class
from selenium import webdriver
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
        login.enter_username("ENTER USERNAME HERE")
        login.enter_pass("ENTER PASSWORD HERE")
        login.click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

