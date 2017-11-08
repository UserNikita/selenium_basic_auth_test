from unittest import main, TestCase
from selenium import webdriver
from browsermobproxy import Server
from variables import *


class BasicAuthTestCase(TestCase):
    def setUp(self):
        self.server = Server(path=BROWSERMOB_PROXY_PATH,
                             options={'port': PROXY_PORT})
        self.server.start()
        proxy = self.server.create_proxy()
        proxy.basic_authentication(domain=DOMAIN, username=USERNAME,
                                   password=PASSWORD)
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--proxy-server=http://%s' % proxy.proxy)
        self.driver = webdriver.Chrome(chrome_options=driver_options)

    def test_basic_auth(self):
        self.driver.get(START_URL)
        standard_auth_button = self.driver.find_element_by_xpath(
            r'//a[contains(text(), "Standard auth")]')
        standard_auth_button.click()
        self.assertIn('Auth Success', self.driver.page_source)

    def tearDown(self):
        self.server.stop()
        self.driver.quit()


if __name__ == '__main__':
    main()
