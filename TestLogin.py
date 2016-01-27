import unittest
from selenium import webdriver


SAUCE_USERNAME = 'lecosi'
SAUCE_ACCESS_KEY = '42bf6ac2-da98-4022-9d5a-09eb000ecdd0'


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %
            (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        )

    def test_from_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
        body = self.driver.find_element_by_css_selector('body')
        self.assertIn('This page is a Selenium sandbox', body.text)

    def tearDown(self):
        id = self.driver.session_id
        print 'Link to your job: https://saucelabs.com/jobs/%s' % id
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()