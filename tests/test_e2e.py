from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all the Card titles")
        cards = checkoutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            print(cardText)
            if cardText == "Samsung Note 8":
                checkoutPage.getCardFooter()[i].click()
        time.sleep(3)
        checkoutPage.getcheckOutbtn().click()
        time.sleep(3)
        confirm_page = checkoutPage.checkOutItems()
        confirm_page.Send_location().send_keys("Ind")
        self.VerifyLinkPresence("India")
        confirm_page.Choose_location().click()
        confirm_page.clickCheckbox().click()
        confirm_page.click_submit().click()
        textMatch = confirm_page.click_purchase().text
        log.info("Text received from Application is "+textMatch)

        assert "Success! Thank you!" in textMatch




