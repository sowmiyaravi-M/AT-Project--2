from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait


class PasswordReset:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       
   def quit(self):
       self.driver.quit()

   def resetPassword(self):
       try:
           self.boot()
           locator.WebLocators().click(self.driver, locator.WebLocators().forgotPasswordLocator)
           locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().clickButton(self.driver, locator.WebLocators().resetPasswordLocator)
           print("Reset Password link sent successfully")

       except NoSuchElementException as e:
           print("Error!")


obj = PasswordReset()
obj.resetPassword()

