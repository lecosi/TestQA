# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ejemplo(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        print 'Iniciando navegador....'
    
    def test_express(self):
        driver = self.driver
        driver.get(self.base_url + "seguros-para-vehiculos/express")
        driver.find_element_by_id("vehicle_registration").clear()
        driver.find_element_by_id("vehicle_registration").send_keys("yph79c")
        driver.find_element_by_id("button-quote").click()
        driver.find_element_by_css_selector("i.cmuj-car").click()
        driver.find_element_by_xpath("//img[contains(@src,'https://segdig1.s3.amazonaws.com/media/uploads/cars/brands/renault.png')]").click()
        Select(driver.find_element_by_id("models")).select_by_visible_text("2014")
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/span[2]").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("span.text").click()
        driver.find_element_by_css_selector("i.cmuj-path").click()
        driver.find_element_by_css_selector("i.cmuj-car").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("i.cmuj-identification1").click()
        driver.find_element_by_css_selector("i.cmuj-identification2").click()
        driver.find_element_by_xpath("//div[@id='step-identification-type']/ul/li[3]/div/span").click()
        driver.find_element_by_css_selector("i.cmuj-sheet").click()
        driver.find_element_by_css_selector("i.cmuj-identification1").click()
        driver.find_element_by_id("identification").clear()
        driver.find_element_by_id("identification").send_keys("1070611554")
        driver.find_element_by_xpath("//div[@id='#identification']/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("leonardo")
        driver.find_element_by_id("last").clear()
        driver.find_element_by_id("last").send_keys("collazos")
        Select(driver.find_element_by_id("occupation")).select_by_visible_text("Empleado(a)")
        Select(driver.find_element_by_id("year")).select_by_visible_text("1990")
        Select(driver.find_element_by_id("month")).select_by_visible_text("Noviembre")
        Select(driver.find_element_by_id("day")).select_by_visible_text("25")
        Select(driver.find_element_by_id("sex")).select_by_visible_text("Masculino")
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/div[2]/div[2]/button").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("3166542572")
        driver.find_element_by_xpath("//div[@id='step-email-address']/div[2]/ul/li[2]/span").click()
        driver.find_element_by_xpath("//div[@id='step-promocode']/ul/li[2]/div").click()
        driver.find_element_by_xpath("//div[4]/div/div[2]").click()

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
