from selenium import webdriver
import unittest
class homepage_class:

    def __init__(self, driver):
        self.driver = driver
        self.user_icon = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a/span/span'

    def click(self):
        self.driver.find_element_by_xpath(self.user_icon).click()
