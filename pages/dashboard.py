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

    # constructor intitalising all the variable with the respective HTML positions
    def __init__(self, driver):
        self.driver = driver

        self.dashboard_tb = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a/span/span'

        #status_positions
        self.write_area = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span'
        self.postbtn = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div'
        self.text_area = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div'
        self.friend_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]'

        #comment_positions
        self.friend_button = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[2]'
        self.friend_search_button = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/label/input'
        self.friend_name_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/a/span'
        self.comment_posn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div'

        #add_friend_positions
        self.about_btn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div[1]'
        self.cities_lived = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[4]/a'
        self.city_link = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div[1]/a/div/span'
        self.person_name_on_city_page = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2/strong[1]/span/a/div/span'
        self.friend_request_btn = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/span/span'

    # function used to post status
    def give_status(self, status):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.write_area).click()#send_keys(status)

        time.sleep(2)
        self.driver.find_element_by_xpath(self.text_area).send_keys(status)

        time.sleep(2)
        self.driver.find_element_by_xpath(self.postbtn).click()

    # function to click the current user's profile button
    def click(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dashboard_tb).click()

    # function used to post comment
    def comment_on_post(self, comment):
        time.sleep(5)
        button = self.driver.find_element_by_xpath(self.friend_button)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(3)
        button = self.driver.find_element_by_xpath(self.friend_name_posn)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(3)
        self.driver.get(self.driver.current_url)

        time.sleep(3)
        button = self.driver.find_element_by_xpath(self.comment_posn)
        self.driver.execute_script("arguments[0].click();", button)

        button.send_keys(comment)
        button.send_keys(Keys.ENTER)

    # function to add a friend from the current location of the user
    def add_frnd(self):
        time.sleep(2)
        button = self.driver.find_element_by_xpath(self.about_btn)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        button = self.driver.find_element_by_xpath(self.cities_lived)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        button = self.driver.find_element_by_xpath(self.city_link)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        self.driver.get(self.driver.current_url)
        time.sleep(2)
        button = self.driver.find_element_by_xpath(self.person_name_on_city_page)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        self.driver.get(self.driver.current_url)
        time.sleep(2)
        button = self.driver.find_element_by_xpath(self.friend_request_btn)
        self.driver.execute_script("arguments[0].click();", button)


