import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.insert(0, '')

@pytest.mark.usefixtures("selenium_driver")
class BaseTest:
    pass

    def windowhandles(self):
        newwindow = self.driver.window_handles[1]
        self.driver.switch_to_window(newwindow)