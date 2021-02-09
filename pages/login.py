# THIS IS THE LOGIN PAGE

from selenium import webdriver
import unittest
class login_class:

    def __init__(self, driver):
        self.driver = driver
        self.user_nametb = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/input'
        self.pass_tb = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/input'
        self.button = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/button'

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.user_nametb).clear()
        self.driver.find_element_by_xpath(self.user_nametb).send_keys(username)

    def enter_pass(self, username):
        self.driver.find_element_by_xpath(self.pass_tb).clear()
        self.driver.find_element_by_xpath(self.pass_tb).send_keys(username)

    def click(self):
        self.driver.find_element_by_xpath(self.button).click()
