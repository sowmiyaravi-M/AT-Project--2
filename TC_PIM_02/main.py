from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPageValidator:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       
   def quit(self):
       self.driver.quit()

   def login(self):
       try:
           self.boot()
           locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
           locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)

           if self.driver.current_url == data.WebData().dashboardURL:
               print("Successfully LoggedIn")
       except NoSuchElementException as e:
           print("Error!")

   def validateTitle(self):
       admin_link = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
       )
       admin_link.click()
       title = self.driver.title
       expected_title = "OrangeHRM"
       if title == expected_title:
           print("Title validation passed")
       else:
           print(f"Title validation failed. Expected: '{expected_title}', Actual: '{title}'")

   def validateHeader(self):
       """Validate the header options."""
       options_to_validate = ["User Management", "Job", "Organization", "Qualifications", "Configuration"]

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

obj = AdminPageValidator()
obj.login()
obj.validateTitle()
obj.validateHeader()
