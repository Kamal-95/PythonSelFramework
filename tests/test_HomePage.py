import time

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass






class TestHomePage(BaseClass):

    def test_formSubmission1(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First Name is = "+getData["Name"])
        homepage.getName().send_keys(getData["Name"])
        log.info("Email is = "+getData["Email"])
        homepage.getEmail().send_keys(getData["Email"])
        log.info("Password is = "+getData["Password"])
        homepage.getPassword().send_keys(getData["Password"])
        homepage.clickCheckbox().click()
        log.info("Gender is = "+getData["Gender"])
        self.selectOptionByText(homepage.selectGender(), getData["Gender"])
        homepage.selectEmployment_status().click()
        homepage.clickSubmitButton().click()
        message = homepage.getSuccessMessage().text
        log.info(message)
        assert "Success" in message
        time.sleep(5)
        self.driver.refresh()



    @pytest.fixture(params=HomePageData.get_Test_Data("Testcase2"))
    def getData(self, request):
        return request.param




