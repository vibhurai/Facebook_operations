from selenium import webdriver
import unittest
from Kaustubh.proj_2.pages.login import login_class
from Kaustubh.proj_2.pages.homepage import  homepage_class
from Kaustubh.proj_2.pages.dashboard import dash_class
from selenium import webdriver
import time

class status_post(unittest.TestCase):

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
        login = login_class(driver)
        login.enter_username("ENTER USERNAME HERE")
        login.enter_pass("ENTER PASSWORD HERE")
        login.click()

    def test_post_status(self):
        driver = self.driver
        time.sleep(3)
        driver.get('https://www.facebook.com/')
        home = homepage_class(driver)
        home.click()
        time.sleep(3)
        driver.get(driver.current_url)
        dash = dash_class(driver)
        dash.click()
        dash.give_status("Feeling good!")

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

