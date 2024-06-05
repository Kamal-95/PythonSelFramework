from selenium.webdriver.common.by import By


from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    Name = (By.CSS_SELECTOR, "[name='name']")
    Email = (By.NAME, "email")
    Password = (By.ID, "exampleInputPassword1")
    Checkbox = (By.ID, "exampleCheck1")
    Gender = (By.ID, "exampleFormControlSelect1")
    Employment_status = (By.ID, "inlineRadio2")
    Submit_Button = (By.XPATH, "//input[@value='Submit']")
    message = (By.CLASS_NAME, 'alert-success')


    def __init__(self, driver):
        self.driver = driver



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
         return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.Checkbox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.Gender)


    def selectEmployment_status(self):
        return self.driver.find_element(*HomePage.Employment_status)

    def clickSubmitButton(self):
        return self.driver.find_element(*HomePage.Submit_Button)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.message)


