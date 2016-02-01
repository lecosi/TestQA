# -*- coding: utf-8 -*-
from selenium import webdriver
import time, unittest,copy
import wd.parallel
from selenium.webdriver.support.ui import Select

class parallel(unittest.TestCase):
    SAUCE_USERNAME = 'lecosi'
    SAUCE_ACCESS_KEY = '42bf6ac2-da98-4022-9d5a-09eb000ecdd0'

    def setUp(self):

        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['platform'] = 'Windows 8.1'
        browser['name'] = 'Python Test Express Firefox'
        browser['tags'] = "Parallel"
        browser['build'] = "1111"
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
        browser['platform'] = 'Windows 7'
        browser['name'] = 'Python Test Express Chrome'
        browser['tags'] = "Parallel"
        browser['build'] = "1111"
        desired_capabilities += [browser]

        self.drivers = wd.parallel.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://" + parallel.SAUCE_USERNAME + ":" + parallel.SAUCE_ACCESS_KEY + "@ondemand.saucelabs.com:80/wd/hub")
        print 'Conectando a SauceLabs....'

    @wd.parallel.multiply
    def test_parallel(self):
        self.driver.get("https://seguros.comparamejor.com/seguros-para-vehiculos/express/#/consultar-placa")
        self.driver.find_element_by_id("vehicle_registration").send_keys("yph79c")

        self.driver.quit()
        print 'Ejecución terminada!'

if __name__ == '__main__':
    unittest.main()