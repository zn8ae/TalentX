# from selenium import webdriver
# from django.test import TestCase

# #driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# #driver = webdriver.Chrome('/usr/local/python/lib/python3.5/site-packages/chromedriver')
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# #driver = webdriver.Firefox('/usr/bin/firefox')
# url = "http://localhost:8003"
# webdriver.get(url)

# #driver.get(url)

# # # temp = driver.find_element_by_name("signup")
# # # #print find

# # #SignUp
# # driver.find_element_by_name("signup").click()
# # driver.find_element_by_id("id_username").send_keys("steven8790180")
# # driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
# # driver.find_element_by_id("id_last_name").send_keys("qu")
# # driver.find_element_by_id("id_first_name").send_keys("steven")
# # driver.find_element_by_id("id_password").send_keys("stevenqu")
# # driver.find_element_by_id("id_password2").send_keys("stevenqu")
# # driver.find_element_by_id("submit").click()
# # driver.find_element_by_id("success").click()

# # #LogIn
# # driver.find_element_by_id("id_username").send_keys("steven8790180")
# # driver.find_element_by_id("id_password").send_keys("stevenqu")
# # driver.find_element_by_id("submit").click()

# # #CreateSkill
# # driver.find_element_by_id("id_skill").send_keys("fly")
# # driver.find_element_by_id("id_price").send_keys("100")
# # driver.find_element_by_id("id_desc").send_keys("flyflyfly")
# # driver.find_element_by_id("submit").click()
# # driver.find_element_by_id("success").click()

# # #SignOut
# # driver.find_element_by_name("signout").click()
# # #If find signin, then success. Otherwise, Signout is unsuccessful.
# # driver.find_element_by_name("signin")

# # #Search
# # driver.find_element_by_id("id_search").send_keys("fly")
# # driver.find_element_by_id("submit").click()


# class WebTestCase(TestCase):

# 	def setup(self):
# 		pass

# 	def test_signup(self):
# 		driver.find_element_by_name("signup").click()
# 		driver.find_element_by_id("id_username").send_keys("steven")
# 		driver.find_element_by_id("id_email").send_keys("steven@gmail.com")
# 		driver.find_element_by_id("id_last_name").send_keys("qu")
# 		driver.find_element_by_id("id_first_name").send_keys("steven")
# 		driver.find_element_by_id("id_password").send_keys("stevenqu")
# 		driver.find_element_by_id("id_password2").send_keys("stevenqu")
# 		driver.find_element_by_id("submit").click()
# 		find = driver.find_element_by_id("success")
# 		driver.find_element_by_id("success").click()
# 		self.assertNotEquals(find, None)

# 	def test_login(self):
# 		driver.find_element_by_id("id_username").send_keys("steven")
# 		driver.find_element_by_id("id_password").send_keys("stevenqu")
# 		driver.find_element_by_id("submit").click()
# 		find = driver.find_element_by_name("logout")
# 		self.assertNotEquals(find, None)

# 	def test_create_skill(self):
# 		driver.find_element_by_id("id_skill").send_keys("fly")
# 		driver.find_element_by_id("id_price").send_keys("100")
# 		driver.find_element_by_id("id_desc").send_keys("flyflyfly")
# 		driver.find_element_by_id("submit").click()
# 		find = driver.find_element_by_id("success")
# 		driver.find_element_by_id("success").click()
# 		self.assertNotEquals(find, None)

# 	def test_singout(self):
# 		driver.find_element_by_name("signout").click()
# 		find = driver.find_element_by_name("signin")
# 		self.assertNotEquals(find, None)

# 	def test_search(self):
# 		driver.find_element_by_id("id_search").send_keys("fly")
# 		driver.find_element_by_id("submit").click()
# 		find = driver.find_element_by_name("view")
# 		self.assertNotEquals(find, None)

# 	def tearDown(self):
# 		pass #nothing to tear down



