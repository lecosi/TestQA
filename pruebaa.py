from pyvirtualdisplay import Display
from selenium import webdriver
import time

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://www.cual-es-mi-ip.net/')
time.sleep(2)
#driver.find_element_by_id("button-copy").click()
data = browser.find_element_by_xpath("//*[@id='ip-col']/span").text
print "la ip publica de la maquina es " +data
browser.quit()

display.stop()
