# Generated by Selenium IDE
import pytest
import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCatReportList():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_catReportList(self):
    self.driver.get("http://ee/admin/login.php")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "password").send_keys("admin123")
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Report").click()
    self.driver.find_element(By.ID, "dropdownMenuButton1").click()
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  
