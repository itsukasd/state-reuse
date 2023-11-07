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

class TestCreateDetails7():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createDetails7(self):
    self.driver.get("http://1addressbook/")
    self.driver.set_window_size(1175, 629)
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.NAME, "searchform").click()
    self.driver.find_element(By.LINK_TEXT, "add new").click()
    self.driver.find_element(By.NAME, "address").send_keys("hadspiashdp")
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) > input:nth-child(1)").click()
    self.driver.find_element(By.NAME, "middlename").click()
    self.driver.find_element(By.NAME, "middlename").send_keys("a")
    self.driver.find_element(By.NAME, "lastname").click()
    self.driver.find_element(By.NAME, "lastname").send_keys("s")
    self.driver.find_element(By.NAME, "nickname").click()
    self.driver.find_element(By.NAME, "nickname").send_keys("d")
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys("aa")
    self.driver.find_element(By.NAME, "company").click()
    self.driver.find_element(By.NAME, "company").send_keys("aaaa")
    self.driver.find_element(By.NAME, "home").click()
    self.driver.find_element(By.NAME, "home").send_keys("a")
    self.driver.find_element(By.NAME, "mobile").click()
    self.driver.find_element(By.NAME, "mobile").send_keys("a")
    self.driver.find_element(By.NAME, "work").click() #7
    self.driver.find_element(By.NAME, "work").send_keys("aaa")
    self.driver.find_element(By.NAME, "theform").click()
    self.driver.find_element(By.NAME, "fax").click()
    self.driver.find_element(By.NAME, "fax").send_keys("aa")
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys("aa")
    self.driver.find_element(By.NAME, "email2").click()
    self.driver.find_element(By.NAME, "email2").send_keys("aa")
    self.driver.find_element(By.NAME, "email3").click()
    self.driver.find_element(By.NAME, "email3").send_keys("a")
    self.driver.find_element(By.NAME, "homepage").click()
    self.driver.find_element(By.NAME, "homepage").send_keys("a")
    element = self.driver.find_element(By.NAME, "bday")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.NAME, "notes").click()
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "bday")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "bday")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "bday").click()
    dropdown = self.driver.find_element(By.NAME, "bday")
    dropdown.find_element(By.XPATH, "//option[. = '7']").click()
    self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
    element = self.driver.find_element(By.NAME, "bmonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "bmonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "bmonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "bmonth").click()
    dropdown = self.driver.find_element(By.NAME, "bmonth")
    dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
    self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
    self.driver.find_element(By.NAME, "byear").click()
    element = self.driver.find_element(By.NAME, "aday")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "aday")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "aday")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "aday").click()
    dropdown = self.driver.find_element(By.NAME, "aday")
    dropdown.find_element(By.XPATH, "//option[. = '7']").click()
    self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
    element = self.driver.find_element(By.NAME, "amonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "amonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "amonth")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "amonth").click()
    dropdown = self.driver.find_element(By.NAME, "amonth")
    dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
    self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
    element = self.driver.find_element(By.NAME, "new_group")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "new_group")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "new_group")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "new_group").click()
    self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
    element = self.driver.find_element(By.NAME, "notes")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "notes")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "notes")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "notes").click()
    self.driver.find_element(By.NAME, "address2").click()
    self.driver.find_element(By.NAME, "address2").send_keys("a")
    self.driver.find_element(By.NAME, "notes").click()
    self.driver.find_element(By.NAME, "notes").send_keys("aa")
    self.driver.find_element(By.NAME, "phone2").click()
    self.driver.find_element(By.NAME, "phone2").send_keys("a")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
    self.driver.find_element(By.NAME, "searchstring").send_keys("aa")
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()