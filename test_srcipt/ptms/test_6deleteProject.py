# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test6deleteProject():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_6deleteProject(self):
    self.driver.get("http://ptms/admin/login.php")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.NAME, "username").send_keys("admin")
    self.driver.find_element(By.NAME, "password").send_keys("admin123")
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
    self.driver.execute_script("arguments[0].click();", element)
    self.driver.find_element(By.LINK_TEXT, "Project List").click()
    self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(6) .btn").click()
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
    element = self.driver.find_element(By.ID, "confirm")
    self.driver.execute_script("arguments[0].click();", element)
    element = self.driver.find_element(By.CSS_SELECTOR, ".ml-3")
    self.driver.execute_script("arguments[0].click();", element)
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  
