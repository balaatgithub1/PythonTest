from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class GoogleSearch(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.browser = webdriver.Chrome('C:/chromedriver_win32/Chromedriver')
        cls.browser.implicitly_wait(10)

    def test_search_jenkins(self):
        self.browser.get('http://google.com')
        self.browser.find_element_by_name("q").send_keys("Jenkins")
        self.browser.find_element_by_name("btnK").click()

    def test_search_title(self):
        assert 'Jenkins' in self.browser.title

    @classmethod

    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("Test Completed")


print("Starting Test")
if __name__ == '__main__':
    unittest.main()

#elem = browser.find_element_by_name('p')  # Find the search box
#elem.send_keys('seleniumhq' + Keys.RETURN)