from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
class TestLoginUI:
   def test_titel(self):
       driver = webdriver.Chrome()
       driver.maximize_window()
       driver.implicitly_wait(5)
       driver.get("http://demo.openemr.io/b/openemr/")
       actual_tite = driver.title
       #assert  actual_tite=="OpenEMR"
       assert_that("OpenEMR Login").is_equal_to(actual_tite)

   def test_app_description(self):
       driver = webdriver.Chrome()
       driver.maximize_window()
       driver.implicitly_wait(5)
       driver.get("http://demo.openemr.io/b/openemr/")
       actual_tite = driver.title
       # assert  actual_tite=="OpenEMR"
       actual_desc = driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
       assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")
       