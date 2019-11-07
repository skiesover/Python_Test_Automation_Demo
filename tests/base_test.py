import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    # Note: Please specify your chromedriver local path here:
    chromedriver = "/Users/skiesover/WebDriver/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    def tearDown(self):
        self.driver.quit()