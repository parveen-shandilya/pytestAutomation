
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self,driver,*args, **kwargs):
        self.driver = driver
    
    
    def do_waitForElement_PresenceLocated(self,by_locator):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(by_locator))
    
    
    def do_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        element.click()
    
    def do_sendKeys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        element.send_keys(text) 
    
    def do_getText(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return element.text   
    
    def is_elementVisible(self,by_locator):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return element.is_displayed()
       
       
   
          