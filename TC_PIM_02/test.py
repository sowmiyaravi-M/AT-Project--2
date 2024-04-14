from Locators import locator
from Data import data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
   def testTitle(self, boot):
       self.driver.get(data.WebData().url)
       assert self.driver.title == data.WebData().loginPageTitle
       print("SUCCESS: Web Title Verified")


   @pytest.mark.html
   def testLogin(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       assert self.driver.current_url == data.WebData().dashboardURL
       print(f"SUCCESS : Logged in with {data.WebData().username} and the password is {data.WebData().password}")


   @pytest.mark.html
   def testvalidateTitle(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       self.wait = WebDriverWait(self.driver, 10)
       admin_link = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
       )
       self.wait = WebDriverWait(self.driver, 10)
       admin_link.click()
       self.wait = WebDriverWait(self.driver, 10)
       title = self.driver.title
       expected_title = "OrangeHRM"
       if title == expected_title:
           print("Title validation passed")
       else:
           print(f"Title validation failed. Expected: '{expected_title}', Actual: '{title}'")

   @pytest.mark.html
   def testvalidateHeader(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       self.wait = WebDriverWait(self.driver, 10)
       admin_link = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
       )
       admin_link.click()
       self.wait = WebDriverWait(self.driver, 10)
       options_to_validate = ["User Management", "Job", "Organization", "Qualifications", "Configuration"]
       self.wait = WebDriverWait(self.driver, 10)
       for option in options_to_validate:
           try:
               # Wait for the option to be present
               option_element = WebDriverWait(self.driver, 10).until(
                   EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{option}')]"))
               )
               print(f"Option '{option}' is displayed.")
           except:
               print(f"Option '{option}' is NOT displayed.")

       try:
           nationalities_option = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.XPATH, "//a[text()='Nationalities']"))
           )
           print("Option 'Nationalities' is displayed.")
       except:
           print("Option 'Nationalities' is NOT displayed.")

       try:
           corporate_branding_option = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.XPATH, "//a[text()='Corporate Branding']"))
           )
           print("Option 'Corporate Branding' is displayed.")
       except:
           print("Option 'Corporate Branding' is NOT displayed.")




