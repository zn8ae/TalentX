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

	def test_01_signup(self): 
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/home/signup/")
		driver.find_element_by_id("id_username").send_keys("qhw")
		driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
		driver.find_element_by_id("id_last_name").send_keys("qu")
		driver.find_element_by_id("id_first_name").send_keys("steven")
		driver.find_element_by_id("id_password").send_keys("qhw")
		driver.find_element_by_id("id_password2").send_keys("qhw")
		driver.find_element_by_id("submit_signup").click()
		wait = WebDriverWait(driver, 20)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'success')))
		driver.find_element_by_id("success")
		driver.quit()

	def test_02_login(self): 
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/home/signin/")
		driver.find_element_by_id("id_username").send_keys("qhw")
		driver.find_element_by_id("id_password").send_keys("qhw")
		driver.find_element_by_id("submit_login").click()
		wait = WebDriverWait(driver, 20)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'id_skill')))
		self.assertEquals(driver.title, "Create New Listing")
		driver.quit()

	def test_03_create_skill(self):
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/home/signin/")
		driver.find_element_by_id("id_username").send_keys("qhw")
		driver.find_element_by_id("id_password").send_keys("qhw")
		driver.find_element_by_id("submit_login").click()	
		#Create Skill Page
		wait = WebDriverWait(driver, 20)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'id_skill')))
		driver.find_element_by_id("id_skill").send_keys("fly")
		driver.find_element_by_id("id_price").send_keys("200")
		driver.find_element_by_id("id_desc").send_keys("flyflyfly")
		driver.find_element_by_id("submit_create").click()
		#Success Page
		element = wait.until(EC.element_to_be_clickable((By.ID, 'success')))
		driver.find_element_by_id("success")
		driver.quit()


	def test_04_signout(self):
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/home/signin/")
		driver.find_element_by_id("id_username").send_keys("qhw")
		driver.find_element_by_id("id_password").send_keys("qhw")
		driver.find_element_by_id("submit_login").click()	
		wait = WebDriverWait(driver, 20)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'signout')))
		driver.find_element_by_id("signout").click()
		#Back to the main page	
		element = wait.until(EC.element_to_be_clickable((By.ID, 'signin')))
		find = driver.find_element_by_name("signin")
		self.assertNotEquals(find, None)
		driver.quit()

	def test_05_search(self):
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/")
		driver.find_element_by_id("id_search").send_keys("fly")
		driver.find_element_by_id("submit").click()
		time.sleep(2)
		self.assertEquals(driver.title, "Search Detail")
		driver.quit()

	def test_06_detail(self):
		driver = webdriver.Firefox()
		driver.get("http://107.170.71.126:8080/")
		driver.find_element_by_id("id_search").send_keys("fly")
		driver.find_element_by_id("submit").click()
		wait = WebDriverWait(driver, 20)
	 	element = wait.until(EC.element_to_be_clickable((By.NAME, 'view')))
		find = driver.find_element_by_css_selector("a[href*='detail']")
		driver.find_element_by_css_selector("a[href*='detail']").click()
		self.assertNotEquals(find, None)
		driver.quit()

	def tearDown(self):
		pass #nothing to tear down

if __name__ =='__main__':
	unittest.main()


	# def test_signup(self): #OK!!!
	# 	driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
	# 	driver.get('http://162.243.207.23:80/home/signup')
	# 	driver.find_element_by_id("id_username").send_keys("steven08")
	# 	driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
	# 	driver.find_element_by_id("id_last_name").send_keys("qu")
	# 	driver.find_element_by_id("id_first_name").send_keys("steven")
	# 	driver.find_element_by_id("id_password").send_keys("stevenqu")
	# 	driver.find_element_by_id("id_password2").send_keys("stevenqu")
	# 	driver.find_element_by_id("submit").click()

	# def test_login(self): #OK!!!
	# 	driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
	# 	driver.get('http://162.243.207.23:80/home/signin')
	# 	driver.find_element_by_id("id_username").send_keys("steven03")
	# 	driver.find_element_by_id("id_password").send_keys("stevenqu")
	# 	driver.find_element_by_id("submit").click()
	# 	find = driver.find_element_by_id("submit")
	# 	self.assertNotEquals(find, None)

