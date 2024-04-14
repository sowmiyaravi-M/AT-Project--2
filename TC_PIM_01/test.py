from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait

import pytest

class Test:

   @pytest.fixture
   def boot(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       yield
       self.driver.quit()


   @pytest.mark.html
   def testresetPassword(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().click(self.driver, locator.WebLocators().forgotPasswordLocator)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().resetPasswordLocator)
       print("Reset Password link sent successfully")



