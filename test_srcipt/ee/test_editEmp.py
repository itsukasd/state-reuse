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

class TestEditEmp():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editEmp(self):
    self.driver.get("http://ee/admin/login.php")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "password").send_keys("admin123")
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "dropdownMenuButton1").click()#5
    self.driver.find_element(By.LINK_TEXT, "Enrollees").click()
    self.driver.find_element(By.ID,  "btnGroupDrop1").click()
    self.driver.find_element(By.LINK_TEXT, "Edit").click()
    self.driver.find_element(By.ID, "status").click()
    dropdown = self.driver.find_element(By.ID, "status")
    dropdown.find_element(By.XPATH, "//option[. = 'Inactive']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#status > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mid-large .btn-secondary").click()
    self.driver.find_element(By.ID,"dropdownMenuButton1").click()
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  
