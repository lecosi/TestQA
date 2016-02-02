# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class testExpress(unittest.TestCase):

    def setUp(self):
        #self.driver=webdriver.Firefox()
        url = 'http://lecosi1:Xeq938dyPSnjXaVHKYpK@hub.browserstack.com:80/wd/hub'
        self.driver = webdriver.Remote(command_executor=url,
        desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com/"
        print "Iniciando navegador..."
        self.test_insertPlaca()

    def test_insertPlaca(self):

        driver=self.driver
        driver.get(self.base_url + "seguros-para-vehiculos/express")
        driver.find_element_by_id("vehicle_registration").send_keys("yph79c")
        driver.find_element_by_id("button-quote").click()
        print "ingresó placa..."
        self.typeModel()

    def typeModel(self):

        driver=self.driver
        driver.find_element_by_css_selector("i.cmuj-car").click()
        driver.find_element_by_xpath("//img[contains(@src,'https://segdig1.s3.amazonaws.com/media/uploads/cars/brands/renault.png')]").click()
        print "selecciona tipo y modelo de auto..."
        self.vehicleSpecification()

    def vehicleSpecification(self):

        driver = self.driver
        Select(driver.find_element_by_id("models")).select_by_visible_text("2014")
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/span[2]").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_css_selector("span.text").click()
        driver.find_element_by_css_selector("i.cmuj-path").click()
        driver.find_element_by_css_selector("i.cmuj-car").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        print "selecionó las caracteristicas de vehiculo.... "
        self.personalData()

    def personalData(self):

        driver=self.driver
        driver.find_element_by_css_selector("i.cmuj-identification1").click()
        driver.find_element_by_id("identification").send_keys("1070611554")
        driver.find_element_by_xpath("//div[@id='#identification']/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("name").send_keys("leonardo")
        driver.find_element_by_id("last").send_keys("collazos")
        Select(driver.find_element_by_id("occupation")).select_by_visible_text("Empleado(a)")
        Select(driver.find_element_by_id("year")).select_by_visible_text("1990")
        Select(driver.find_element_by_id("month")).select_by_visible_text("Noviembre")
        Select(driver.find_element_by_id("day")).select_by_visible_text("25")
        Select(driver.find_element_by_id("sex")).select_by_visible_text("Masculino")
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/div[2]/div[2]/button").click()
        driver.find_element_by_id("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_id("mobile_phone").send_keys("3166542572")
        driver.find_element_by_xpath("//div[@id='step-email-address']/div[2]/ul/li[2]/span").click()
        print "Insertó datos Personales..."
        self.FinalishQuote()

    def FinalishQuote(self):

        driver=self.driver
        driver.find_element_by_xpath("//div[@id='step-promocode']/ul/li[2]/div").click()
        driver.find_element_by_xpath("//div[4]/div/div[2]").click()
        print "Terminó Cotización..."
        driver.quit()

if __name__ == "__main__":
    unittest.main()

