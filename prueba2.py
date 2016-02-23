# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Prueba2(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_prueba2(self):
        driver = self.driver
        driver.get(self.base_url + "/a/")
        driver.find_element_by_name("registration").clear()
        driver.find_element_by_name("registration").send_keys("xcv234")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)
        valor=driver.find_element_by_xpath("/html/body/p[1]").text
        self.assertEqual("CHEVROLET PLATINUM LT - AT 1800CC 4P CT del 2013 motor 1800", valor)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
