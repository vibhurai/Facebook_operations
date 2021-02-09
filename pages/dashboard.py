from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.support.wait import WebDriverWait


class dash_class:

    def __init__(self, driver):
        self.driver = driver

        self.dashboard_tb = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]'

        #status_positions
        self.write_area = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div'
        self.postbtn = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div'

        self.friend_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]'

        #comment_positions
        self.friend_button = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[2]'
        self.friend_name_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/a/span'
        self.comment_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div'


    def give_status(self, status):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.write_area).send_keys(status)
        self.driver.find_element_by_xpath(self.postbtn).click()

    def click(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dashboard_tb).click()

    def click_friend_name(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dashboard_tb).click()

    def comment_on_post(self, comment):
        time.sleep(5)
        button = self.driver.find_element_by_xpath(self.friend_button)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        button = self.driver.find_element_by_xpath(self.friend_name_posn)
        self.driver.execute_script("arguments[0].click();", button)

        self.driver.get('https://www.facebook.com/gaurav.rai.798278')
        time.sleep(3)
        button = self.driver.find_element_by_xpath(self.comment_posn)
        self.driver.execute_script("arguments[0].click();", button)
        # self.driver.execute_script("arguments[0].send_keys('username');", button)
        button.send_keys(comment)
        button.send_keys(Keys.ENTER)
