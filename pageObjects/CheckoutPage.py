from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver


    CardTitle = (By.CSS_SELECTOR, ".card-title a")
    CardFooter = (By.CSS_SELECTOR, ".card-footer button")
    Checkout_Button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")


    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.CardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.CardFooter)

    def getcheckOutbtn(self):
        return self.driver.find_element(*CheckoutPage.Checkout_Button)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page




