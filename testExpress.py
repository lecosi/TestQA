# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

desired_cap = {
    'platform': "Windows 7",
    'browserName': "chrome",
    'version': "47",
}
driver = webdriver.Remote(
command_executor='http://lecosi:42bf6ac2-da98-4022-9d5a-09eb000ecdd0@ondemand.saucelabs.com:80/wd/hub',
desired_capabilities=desired_cap)

driver.get("seguros.comparamejor.com/seguros-para-vehiculos/express/#/buscando-polizas")
driver.find_element_by_id("vehicle_registration").clear()
driver.find_element_by_id("vehicle_registration").send_keys("yph79c")
driver.find_element_by_css_selector("#vehicle-ping > span.icon").click()
driver.find_element_by_xpath("//img[contains(@src,'https://segdig1.s3.amazonaws.com/media/uploads/cars/brands/renault.png')]").click()
driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/span[2]").click()
driver.find_element_by_xpath("//div[@id='step-vehicle-line']/ul/li[2]/span").click()
driver.find_element_by_xpath("//div[@id='step-vehicle-reference']/ul/li[2]/span").click()
driver.find_element_by_css_selector("span.btnuj").click()
driver.find_element_by_xpath("//div[@id='step-vehicle-zero-km']/ul/li[2]/div/span").click()
driver.find_element_by_css_selector("i.cmuj-car").click()
driver.find_element_by_css_selector("span.btnuj").click()
driver.find_element_by_css_selector("div.btn-icon-content.active > span.icon").click()
driver.find_element_by_id("identification").clear()
driver.find_element_by_id("identification").send_keys("1070611554")
driver.find_element_by_xpath("//div[@id='#identification']/div/div/div/div/div[2]/button").click()
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys("leonardo")
driver.find_element_by_id("last").clear()
driver.find_element_by_id("last").send_keys("collazos")
Select(driver.find_element_by_id("occupation")).select_by_visible_text("Empleado(a)")
Select(driver.find_element_by_id("year")).select_by_visible_text("1990")
Select(driver.find_element_by_id("month")).select_by_visible_text("Novimbre")
Select(driver.find_element_by_id("day")).select_by_visible_text("26")
Select(driver.find_element_by_id("sex")).select_by_visible_text("Masculino")
driver.find_element_by_xpath("//div[@id='step-date-of-birth']/div[2]/div[2]/button").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("leohcollazos@gmail.com")
driver.find_element_by_id("mobile_phone").clear()
driver.find_element_by_id("mobile_phone").send_keys("3145675653")
driver.find_element_by_xpath("//div[@id='step-email-address']/div[2]/ul/li[2]/span").click()
driver.find_element_by_xpath("//div[@id='step-promocode']/ul/li[2]/div").click()
driver.find_element_by_xpath("//div[4]/div/div[2]").click()
