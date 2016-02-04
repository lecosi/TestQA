# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time

class TestSoat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_soat(self):
        driver = self.driver
        driver.get(self.base_url + "/seguro-obligatorio-soat/v1/#/consultar-placa")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ert345")
        driver.find_element_by_xpath("//div[@id='step-query-registration']/div/div[2]/form/button").click()
        print("ingresó placa....")
        driver.find_element_by_xpath("//div[@id='step-vehicle-body']/ul/li[3]/div").click()
        print("tipo de vehículo....")
        driver.find_element_by_xpath("//img[@alt='AKT']").click()
        print("marca de vehículo....")
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/div[11]").click()
        print("modelo de vehículo....")
        driver.find_element_by_css_selector("span.btnuj").click()
        print("linea de vehículo....")
        driver.find_element_by_xpath("//div[@id='step-vehicle-reference']/ul/li[6]/span").click()
        print("referencia de vehículo....")
        driver.find_element_by_css_selector("span.text.ng-binding").click()
        print("referencia completa....")
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//div[@id='step-price-soat']/div[2]/div[2]/div[2]/button").click()
        print("acepta terminos")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("test")
        driver.find_element_by_xpath("//div[@id='step-complete-name']/form/button").click()
        print("ingresa datos personales de cliente")
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("1070611554")
        driver.find_element_by_xpath("//div[@id='step-identification']/form/button").click()
        print("ingresa Tipo de identificación y Numero ID")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_xpath("//div[@id='step-email-address']/form/button").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("3214566778")
        print("ingresa correo y número telefónico")
        driver.find_element_by_xpath("//div[@id='step-phone-numbers']/form/button").click()
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        print("ingresa sexo (M)")
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        print("tipo de dirección")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("cra 15 #80-90")

        driver.find_element_by_xpath("//div[@id='step-adress']/form/button").click()
        print("digita dirección")
        driver.find_element_by_css_selector("span.btnuj").click()
        print("digita municipio")
        driver.find_element_by_css_selector("span.text").click()
        print("tipo de servicio de vehículo")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(u"kñjhñkjhfdsjdskñhkñs")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"lvñnhvlñdfhdlñdsfhfd")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(u"jksvljfkdjkljnhdñakj")
        driver.find_element_by_xpath("//div[@id='step-vehicle-data']/form/button").click()
        print("digita #chasis,#motor,#serial")
        driver.find_element_by_xpath("//*[@id='step-date-of-birth']/table/tbody/tr[1]/td[2]/div[2]/div[1]").click()
        driver.find_element_by_xpath("//*[@id='step-date-of-birth']/table/tbody/tr[3]/td[2]/div[2]/div[12]").click()
        driver.find_element_by_xpath("//*[@id='step-date-of-birth']/table/tbody/tr[5]/td[2]/div[2]/div[30]").click()
        print("fecha de vigencia")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
