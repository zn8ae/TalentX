from selenium import webdriver
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0




class WebTestCase(unittest.TestCase):

	def setup(self):

		pass

	def test_main_page(self): #OK!!!
		driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
		driver.get('http://162.243.207.23:8003/')
		title = driver.title
		self.assertEquals(title, "TalentX")

	# def test_signup(self): #OK!!!
	# 	driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
	# 	driver.get('http://162.243.207.23:8003/home/signup')
	# 	driver.find_element_by_id("id_username").send_keys("steven08")
	# 	driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
	# 	driver.find_element_by_id("id_last_name").send_keys("qu")
	# 	driver.find_element_by_id("id_first_name").send_keys("steven")
	# 	driver.find_element_by_id("id_password").send_keys("stevenqu")
	# 	driver.find_element_by_id("id_password2").send_keys("stevenqu")
	# 	driver.find_element_by_id("submit").click()

	# def test_login(self): #OK!!!
	# 	driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
	# 	driver.get('http://162.243.207.23:8003/home/signin')
	# 	driver.find_element_by_id("id_username").send_keys("steven03")
	# 	driver.find_element_by_id("id_password").send_keys("stevenqu")
	# 	driver.find_element_by_id("submit").click()
	# 	find = driver.find_element_by_id("submit")
	# 	self.assertNotEquals(find, None)


	# def test_create_skill(self):
	# 	driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
	# 	driver.get('http://162.243.207.23:8003/home/signin')
	# 	driver.find_element_by_xpath('//a[@id="submit"]').click()
	# 	# driver.find_element_by_id("id_username").send_keys("steven03")
	# 	# driver.find_element_by_id("id_password").send_keys("stevenqu")
	# 	# driver.find_element_by_id("submit").click()	
	# 	title = driver.title		
	# 		#driver.switch_to_window(driver.window_handles[-1])
		
	# 	self.assertEquals(title, "TalentX")
	# 	# find = driver.find_element_by_id("id_password")
	# 	# self.assertNotEquals(find, None)
	# 	# time.sleep(2) 
	# 	# driver.SwitchTo().Window(driver.WindowHandles.Last());
	# 	# driver.find_element_by_id("id_skill")
	# 	# driver.find_element_by_id("id_skill").send_keys("fly")
	# 	# driver.find_element_by_id("id_price").send_keys("100")
	# 	# driver.find_element_by_id("id_desc").send_keys("flyflyfly")
	# 	# driver.find_element_by_id("submit").click()
	# 	# find = driver.find_element_by_id("success")
	# 	# driver.find_element_by_id("success").click()
	# 	# self.assertNotEquals(find, None)


# 	def test_signout(self):
# 		driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
# 		driver.get('http://162.243.207.23:8003/home/signin')
# 		driver.find_element_by_id("id_username").send_keys("steven03")
# 		driver.find_element_by_id("id_password").send_keys("stevenqu")
# 		#elem1 = driver.find_element_by_css_selector("input[id='submit']")
		
# #		driver.find_element_by_xpath('//input[@id="submit"]').click()
# 		# b.click().perform()

# 		print(driver.current_url)
# 		driver.find_element_by_id("id_username").send_keys("steven08")
# 		driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
# 	#	driver.find_element_by_name("signout").click()
# 		# find = driver.find_element_by_name("signin")
# 		# self.assertNotEquals(find, None)

	# def test_search(self):
	# 	driver = webdriver.Chrome()
	# 	url = 'localhost:8003'
	# 	driver.get(url)
	# 	driver.find_element_by_id("id_search").send_keys("fly")
	# 	driver.find_element_by_id("submit").click()
	# 	find = driver.find_element_by_name("view")
	# 	self.assertNotEquals(find, None)

	def tearDown(self):
		pass #nothing to tear down

if __name__ =='__main__':
	unittest.main()

