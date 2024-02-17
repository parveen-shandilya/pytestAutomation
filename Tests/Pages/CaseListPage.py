import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage


class CaseListPage(BasePage):
    cLP = (By.XPATH,"//a[text()='Cases']")
    violationTypeCol = (By.XPATH,"//div[contains(text(),'Violation Type')]")
    locationCol = (By.XPATH,"//div[contains(text(),'Location')]")
    apnCol = (By.XPATH,"//div[contains(text(),'APN')]")
    assigneeCol = (By.XPATH,"//div[contains(text(),'APN')]")
    statusCol = (By.XPATH,"//div[contains(text(),'APN')]")
    createdCol =(By.XPATH, "//div[text()='Created']")
    closedCol = (By.XPATH,"//div[text()='Closed']")
    inspectionAssigneeCol = (By.XPATH,"//div[text()='Inspection Assignee']")
    inspectionAssigneeCol =(By.XPATH, "//div[text()='Inspection Assignee']")
    nextInsepectionAssingeeCol = (By.XPATH,"//div[text()='Next Scheduled Inspection']")
    deleteCol = (By.XPATH,"//div[text()='Next Scheduled Inspection']")
    
    
    def __init__(self,driver,*args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        self.driver.get(TestData.BASE_URL)
    
    
    def test_NavigateToCaseListPage(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_Agency(TestData.USERNAME,TestData.PASSWORD)
        self.do_waitForElement_PresenceLocated(self.cLP)
        self.do_waitForElement_PresenceLocated(self.cLP)
        self.do_waitForElement_PresenceLocated(self.cLP)
        self.driver.implicitly_wait(30)
        self.do_click(self.cLP)
        self.do_waitForElement_PresenceLocated(self.violationTypeCol)
        flag1 = self.is_elementVisible(self.violationTypeCol)
        flag2 = self.is_elementVisible(self.locationCol)
        flag3 = self.is_elementVisible(self.assigneeCol)
        flag4 = self.is_elementVisible(self.closedCol)
        flag5 = self.is_elementVisible(self.nextInsepectionAssingeeCol)
        assert flag1
        assert flag2
        assert flag3
        assert flag4
        assert flag5
            
        
	
    
    
    
    
    
    
    
    
    
