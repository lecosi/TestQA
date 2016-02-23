# -*- coding: utf-8 -*-
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ip(unittest.TestCase):
    display = Display(visible=0, size=(800, 600))
    display.start()

    def setUp(self):
        self.driver = webdriver.Firefox()
        """desired_cap = {'browser': 'Chrome', 'browser_version': '47.0', 'os': 'Windows', 'os_version': '7', 'resolution': '800x600'}
        self.driver = webdriver.Remote(
        command_executor='http://lecosi2:qBJHZpaet33yrXqofYFZ@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)"""
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cual-es-mi-ip.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ip(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        #driver.find_element_by_id("button-copy").click()
        data=driver.find_element_by_xpath("//*[@id='ip-col']/span").text
        print "la ip publica de la maquina es " +data

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    display.stop()

if __name__ == "__main__":
    unittest.main()

