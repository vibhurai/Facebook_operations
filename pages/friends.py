from selenium import webdriver
import unittest
class friends_class:

    def __init__(self, driver):
        self.driver = driver
        self.user_icon = '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/a/span'

    def click(self):
        self.driver.find_element_by_xpath(self.user_icon).click()
