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

class TestAddStudent5():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addStudent5(self):
    self.driver.get("http://sqgs/login.php")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("admin123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Students").click()
    self.driver.find_element(By.ID, "create_new").click()#5
    self.driver.find_element(By.ID, "select2-class_id-container").click()
    self.driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
    self.driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
    self.driver.find_element(By.ID, "dropdownMenuButton1").click()
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
