from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    CheckBox = (By.XPATH, "//label[@for='checkbox2']")
    location = (By.ID, "country")
    Select_location = (By.LINK_TEXT, "India")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    purchase = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def Send_location(self):
        return self.driver.find_element(*ConfirmPage.location)

    def Choose_location(self):
        return self.driver.find_element(*ConfirmPage.Select_location)

    def click_submit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def click_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.CheckBox)

