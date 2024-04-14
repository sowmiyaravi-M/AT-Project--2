from selenium.webdriver.common.by import By

class WebLocators:

   def __init__(self):
       self.forgotPasswordLocator = "orangehrm-login-forgot-header"
       self.usernameLocator = "username"
       self.resetPasswordLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'

   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.NAME ,value=locator).send_keys(textValue)

   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()

   def click(self, driver, locator):
       driver.find_element(by=By.CLASS_NAME, value=locator).click()
