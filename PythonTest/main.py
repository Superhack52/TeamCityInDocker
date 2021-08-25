import unittest
import os
import time

import allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        self.launch_always_true()

    @allure.step("Always true")
    def launch_always_true(self):
        time.sleep(20)
        assert True == True

if __name__ == '__main__':
    unittest.main()
    print("Тест")