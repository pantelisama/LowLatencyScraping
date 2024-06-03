from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")



driver.find_element(By.ID, "divpaxinfo").click()

#for id in (0,3):
driver.find_element(By.ID, "hrefIncAdt").click()
#for idx in (0.3):
driver.find_element(By.ID, "hrefIncAdt").click()

driver.find_element(By.ID, "btnclosepaxoption").click()
acceptable_max_ticket = driver.find_element(By.ID, "divpaxinfo").text
print(acceptable_max_ticket)



