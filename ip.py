# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ip(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        desired_cap = {'browser': 'Chrome', 'browser_version': '47.0', 'os': 'Windows', 'os_version': '7', 'resolution': '800x600'}
        self.driver = webdriver.Remote(
        command_executor='http://lecosi2:qBJHZpaet33yrXqofYFZ@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cual-es-mi-ip.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ip(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("button-copy").click()
        data=driver.find_element_by_xpath("//*[@id='ip-col']/span").text
        print "la ip publica de la maquina es " +data
    
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
#282187 -282208 -282212 - 282216