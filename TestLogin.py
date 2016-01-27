import unittest
from selenium import webdriver


# this is how you set up a test to run on Sauce Labs
desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}
driver = webdriver.Remote(
    command_executor='http://lecosi:42bf6ac2-da98-4022-9d5a-09eb000ecdd0@ondemand.saucelabs.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get('https://wiki.saucelabs.com/display/DOCS/Python+Test+Setup+with+Sauce+Labs+Example')
driver.quit()