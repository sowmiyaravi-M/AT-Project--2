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
   def testvalidateMainMenu(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       admin_link = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
       )
       self.wait = WebDriverWait(self.driver, 10)
       admin_link.click()
       admin_text_found = False
       try:
           admin_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/admin/")]')
           admin_text = admin_element.text
           if admin_text == "Admin":
               admin_text_found = True
               print("Admin text found!")

       except Exception as e:
           print("Admin element not found:", e)

       if not admin_text_found:
           print("Admin text not found!")

       pim_text_found = False
       try:
           PIM_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/pim/")]')
           PIM_text = PIM_element.text
           if PIM_text == "PIM":
               pim_text_found = True
               print("PIM text found!")

       except Exception as e:
           print("PIM element not found:", e)

       if not pim_text_found:
           print("PIM text not found!")

       leave_text_found = False
       try:
           leave_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/leave/")]')
           leave_text = leave_element.text
           if leave_text == "Leave":
               leave_text_found = True
               print("Leave text found!")

       except Exception as e:
           print("Leave element not found:", e)

       if not leave_text_found:
           print("Leave text not found!")

       time_text_found = False
       try:
           time_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/time/")]')
           time_text = time_element.text
           if time_text == "Time":
               time_text_found = True
               print("Time text found!")

       except Exception as e:
           print("Time element not found:", e)

       if not time_text_found:
           print("Time text not found!")

       recruitment_text_found = False
       try:
           recruitment_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/recruitment/")]')
           recruitment_text = recruitment_element.text
           if recruitment_text == "Recruitment":
               recruitment_text_found = True
               print("Recruitment text found!")

       except Exception as e:
           print("Recruitment element not found:", e)

       if not recruitment_text_found:
           print("Recruitment text not found!")

       my_info_text_found = False
       try:
           my_info_element = self.driver.find_element(By.XPATH,
           '//span[contains(@class, "oxd-main-menu-item--name") and text()="My Info"]')
           my_info_text = my_info_element.text
           if my_info_text == "My Info":
               my_info_text_found = True
               print("My Info text found!")

       except Exception as e:
           print("My Info element not found:", e)

       if not my_info_text_found:
           print("My Info text not found!")

       performance_text_found = False
       try:
           performance_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/performance/")]')
           performance_text = performance_element.text
           if performance_text == "Performance":
               performance_text_found = True
               print("Performance text found!")

       except Exception as e:
           print("Performance element not found:", e)

       if not performance_text_found:
           print("Performance text not found!")

       dashboard_text_found = False
       try:
           dashboard_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/dashboard/")]')
           dashboard_text = dashboard_element.text
           if dashboard_text == "Dashboard":
               dashboard_text_found = True
               print("Dashboard text found!")

       except Exception as e:
           print("Dashboard element not found:", e)

       if not dashboard_text_found:
           print("Dashboard text not found!")

       directory_text_found = False
       try:
           directory_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/directory/")]')
           directory_text = directory_element.text
           if directory_text == "Directory":
               directory_text_found = True
               print("Directory text found!")

       except Exception as e:
           print("Directory element not found:", e)

       if not directory_text_found:
           print("Directory text not found!")

       maintenance_text_found = False
       try:
           maintenance_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/maintenance/")]')
           maintenance_text = maintenance_element.text
           if maintenance_text == "Maintenance":
               maintenance_text_found = True
               print("Maintenance text found!")

       except Exception as e:
           print("Maintenance element not found:", e)

       if not maintenance_text_found:
           print("Maintenance text not found!")

       buzz_text_found = False
       try:
           buzz_element = self.driver.find_element(By.XPATH,
            '//a[contains(@class, "oxd-main-menu-item") and contains(@href, "/buzz/")]')
           buzz_text = buzz_element.text
           if buzz_text == "Buzz":
               buzz_text_found = True
               print("Buzz text found!")

       except Exception as e:
           print("Buzz element not found:", e)

       if not buzz_text_found:
           print("Buzz text not found!")




