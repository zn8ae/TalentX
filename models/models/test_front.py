from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from selenium import webdriver

class HomePageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def test_google(self):
    	self.browser.get("http://google.com")

    def tearDown(self):
        self.browser.quit()