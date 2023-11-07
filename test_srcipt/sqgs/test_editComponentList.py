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

class TestEditComponentList():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editComponentList(self):
    self.driver.get("http://sqgs/login.php")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("admin123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Maintenance").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(5) .edit_component").click()
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .edit_component > .svg-inline--fa").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .edit_component > .svg-inline--fa")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "submit").click()
    element = self.driver.find_element(By.ID, "submit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
    self.driver.find_element(By.ID, "dropdownMenuButton1").click()
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  