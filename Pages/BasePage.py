import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities import configReader

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator)).click()

    def type(self,locator,value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator)).send_keys(value)



