# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import unittest, time

class Pruebs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_pruebs(self):
        driver = self.driver
        driver.get(self.base_url + "/usuarios/login/?next=/crm/")
        driver.find_element_by_id("id_username").send_keys("leonardo@comparamejor.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("leonardocollazos1234")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(self,30)
        print "Login Al pelo"
        driver.quit()



if __name__ == "__main__":
    unittest.main()
