# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, unittest, sys, copy
import wd.parallel

class parallel(unittest.TestCase):
    SAUCE_USERNAME = 'lecosi'
    SAUCE_ACCESS_KEY = '42bf6ac2-da98-4022-9d5a-09eb000ecdd0'

    def setUp(self):

        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['platform'] = 'Linux'
        browser['name'] = 'Python Test Express Firefox'
        browser['tags'] = "Parallel"
        browser['build'] = "9999"
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
        browser['platform'] = 'Windows XP'
        browser['name'] = 'Python Test Express Chrome'
        browser['tags'] = "Parallel"
        browser['build'] = "9999"
        desired_capabilities += [browser]

        self.drivers = wd.parallel.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://" + parallel.SAUCE_USERNAME + ":" + parallel.SAUCE_ACCESS_KEY + "@ondemand.saucelabs.com:80/wd/hub")

    @wd.parallel.multiply
    def test_parallel(self):

        self.driver.get("https://seguros.comparamejor.com/seguros-para-vehiculos/express/#/consultar-placa")
        self.driver.find_element_by_id("vehicle_registration").send_keys("yph79c")

        self.drivers.wait(self,5)
        print self.driver.session_id
        self.drivers.quit()

if __name__ == '__main__':
    unittest.main()

