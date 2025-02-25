import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C://Users//kamal.kumar//PycharmProjects//PythonSelFramework//utilities//logfile.log')
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(Formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger



    def VerifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, text)))

    def selectOptionByText(self,locators,text):
        sel = Select(locators)
        sel.select_by_visible_text(text)
