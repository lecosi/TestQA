# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re

class TestV5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_v5(self):
        driver = self.driver
        driver.get(self.base_url + "/seguros-para-vehiculos/v5/#/consultar-placa")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("yph79c")
        driver.find_element_by_xpath("//div[@id='step-query-registration']/div/div[2]/form/button").click()
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        driver.find_element_by_css_selector("img.img-responsive").click()
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/div[35]").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("span.text.ng-binding").click()
        driver.find_element_by_css_selector("span.text.ng-binding").click()
        driver.find_element_by_css_selector("i.cmuj-path").click()
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("i.cmuj-identification1").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("1070611554")
        driver.find_element_by_xpath("//div[@id='step-identification']/form/button").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        driver.find_element_by_xpath("//div[@id='step-complete-name']/form/button").click()
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr/td[2]/div[2]/div[53]").click()
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr[3]/td[2]/div[2]/div[11]").click()
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr[5]/td[2]/div[2]/div[26]").click()
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/button").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_xpath("//div[@id='step-email-address']/form/button").click()
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("3131331361")
        driver.find_element_by_xpath("//div[@id='step-phone-numbers']/form/button").click()
        driver.find_element_by_xpath("//div[@id='step-current-situation']/ul/li[5]/span/span").click()
        driver.find_element_by_id("//*[@id='step-promocode']/ul/li[2]/div").click()
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        driver.find_element_by_xpath("//div[@id='step-promocode']/button").click()
        driver.find_element_by_xpath("//div[@id='help-box']/div/div/div[2]/div[2]/p[2]").click()
        driver.find_element_by_css_selector("span.icon-remove").click()


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
