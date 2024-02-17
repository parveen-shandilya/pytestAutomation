# Test Class for Feature Test
from TestClasses.test_Base import BaseTest
from Config.config import TestData
from Pages.CaseListPage import CaseListPage


class Test_CaseListPage(BaseTest):
    def test_CaseListPage(self):
        self.caseList_page = CaseListPage(self.driver)
        self.caseList_page.test_NavigateToCaseListPage()